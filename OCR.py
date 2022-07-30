import io
import sys
import time

from PySide2.QtCore import QBuffer, Signal, QPoint, QRect, QUrl, QCoreApplication
from PySide2.QtWidgets import QSystemTrayIcon, QMainWindow, QWidget, QApplication, QDialog
from PySide2.QtGui import QIcon, QPixmap, QImage, Qt, QCursor, QPalette, QBrush, QPainter, QPen, QColor, QDesktopServices
from cnocr import CnOcr
from PIL import Image

try:
    from pynotifier import Notification
except ImportError:
    pass

from qt_for_python.uic import main, window_h, window_v
tmp_res = []
# 函数-CNOCR
def processImage(img):
    global tmp_res
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    img.save(buffer, "PNG")
    pil_img = Image.open(io.BytesIO(buffer.data()))
    img_name_str = 'test_img.png'
    pil_img.save(img_name_str)
    buffer.close()
    
    try:
        ocr = CnOcr()
        tmp_res1 = ocr.ocr(img_name_str)
        for i in range(len(tmp_res1)):
            tmp_res.append(tmp_res1[i]['text'])
            
        print(f'INFO: 已识别')
        notify(f'已识别')
    except (IndexError, RuntimeError):
        print(f"INFO: 无法识别,请确定框选截图局域有文本！")
        notify(f"无法识别,请确定框选截图局域有文本！")
        pass
# 函数-notify
def notify(msg):
    try:
        Notification(title="OCR文本识别", description=msg).send()
    except (SystemError, NameError):
        trayicon = QSystemTrayIcon(
            QIcon(
                QPixmap.fromImage(QImage(1, 1, QImage.Format_Mono))
                )
            )
        trayicon.show()
        trayicon.showMessage("OCR文本识别", msg, QSystemTrayIcon.NoIcon)
        trayicon.hide()
# 类-主窗口
class Creat_root(QMainWindow):
    def __init__(self, Ui_file):
        super().__init__()
        # 创建主窗口
        self.root = QMainWindow()
        # 创建Ui_MainWindow的实例
        self.root_ui = Ui_file.Ui_MainWindow()
        # 调用setupUi在指定窗口(主窗口)中添加控件
        self.root_ui.setupUi(self.root)
        self.root_ui.action.triggered.connect(lambda: self.open_win_a(dialog_v))
        self.root_ui.actionhelp.triggered.connect(lambda: self.open_win_a(dialog_h))
        self.root_ui.pushButton.clicked.connect(self.open_win_s)

    def open_win_a(self, widget_o):
        # 新窗口
        widget_o.win.show()
        
    def open_win_s(self):
        self.root.showMinimized()
        time.sleep(0.3)
        # 新窗口
        self.snipper = Snipper()
        self.snipper.show()
        self.snipper.send_str_signal.connect(self.printResult)
        self.snipper.close_snipper_signal.connect(self.close_snipper_widget)
        self.root.showNormal()

    def printResult(self):
        self.root_ui.textBrowser.clear()
        for i in range(len(tmp_res)):
            self.root_ui.textBrowser.append(tmp_res[i])
        
    def close_snipper_widget(self):
        self.snipper.close()
        
# 类-截图窗口
class Snipper(QWidget):
    # 自定义信号
    send_str_signal = Signal()  # 将结果传给主界面
    close_snipper_signal = Signal()
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("OCR文本识别")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setWindowState(self.windowState() | Qt.WindowFullScreen)
        self.screen = QApplication.screenAt(QCursor.pos()).grabWindow(0)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(self.screen))
        self.setPalette(palette)
        self.setCursor(QCursor(Qt.CrossCursor))
        self.start, self.end = QPoint(), QPoint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:  # esc键退出
            self.close()
        return super().keyPressEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 100))
        painter.drawRect(0, 0, self.width(), self.height())
        if self.start == self.end:
            return super().paintEvent(event)
        painter.setPen(QPen(QColor(255, 0, 255), 3))
        painter.setBrush(painter.background())
        painter.drawRect(QRect(self.start, self.end))
        return super().paintEvent(event)

    def mousePressEvent(self, event):
        self.start = self.end = event.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.start == self.end:
            return super().mouseReleaseEvent(event)
        shot = self.screen.copy(
            min(self.start.x(), self.end.x()),
            min(self.start.y(), self.end.y()),
            abs(self.start.x() - self.end.x()),
            abs(self.start.y() - self.end.y()),
        )
        processImage(shot)
        self.send_str_signal.emit()
        self.close_snipper_signal.emit()
# 类-菜单窗口
class Creat_win1(QDialog):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QDialog()
        self.win_ui = Ui_file.Ui_Dialog()
        self.win_ui.setupUi(self.win)
        self.win_ui.commandLinkButton.clicked.connect(self.open_git)
    
    def open_git(self):
        QDesktopServices.openUrl(QUrl("https://github.com/qhzgit734/OCR.git"))
# 主程序运行
if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app = QApplication(sys.argv)
    mainwindow = Creat_root(main)
    dialog_v = Creat_win1(window_v)
    dialog_h = Creat_win1(window_h)
    # 窗口显示
    mainwindow.root.show()
    app.setWindowIcon(QIcon('Development tools.ico'))
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
# 使用QPT脚本打包exe
