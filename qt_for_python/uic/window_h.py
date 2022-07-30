# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_h.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(592, 389)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout.addWidget(self.commandLinkButton, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(388, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"HELP", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"Github", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">OCR\u6587\u672c\u8bc6\u522b</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">V1.0</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">---------------\u5e2e\u52a9---------------</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">1\u3001\u70b9\u51fb'\u5f00\u59cb\u8bc6\u522b'\u6309\u94ae\uff0c\u622a\u5b8c\u56fe\u540e\u81ea\u52a8\u8bc6\u522b\u6587\u672c\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">2\u3001\u82e5\u8bc6\u522b\u622a\u56fe\u754c\u9762\u6309ESC\u9000\u51fa\u65e0\u6548\uff0c\u968f\u4fbf\u62c9\u4e2a\u7ea2\u6846\uff0c\u81ea\u52a8\u8fdb\u5165\u4e3b\u754c\u9762\u518d\u9000\u51fa\u5373\u53ef\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';"
                        "\">3\u3001</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u9996\u6b21\u4f7f\u7528</span><span style=\" font-family:'Cambria','serif'; color:#000000; background-color:#ffffff;\">\u00a0</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u65f6\uff0c\u7cfb\u7edf\u9700\u914d\u7f6e\uff0c\u6253\u5f00\u8f83\u6162\u3002\u518d\u6b21\u6253\u5f00\u5c31\u5f88\u5feb\u4e86\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u539f\u56e0\uff1a</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; color:#000000; background-color:#ffffff;\">1)</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u3001\u7cfb"
                        "\u7edf\u4f1a\u81ea\u52a8\u4e0b\u8f7d</span><span style=\" font-family:'Cambria','serif'; color:#000000; background-color:#ffffff;\">\u00a0</span><span style=\" font-family:'Roboto'; color:#000000; background-color:#ffffff;\">zip </span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u683c\u5f0f\u7684\u6a21\u578b\u538b\u7f29\u6587\u4ef6\uff0c\u5e76\u5b58\u4e8e</span><span style=\" font-family:'Cambria','serif'; color:#000000; background-color:#ffffff;\">\u00a0</span><span style=\" font-family:'Courier New'; color:#000000;\">~/.cnocr</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u76ee\u5f55\uff08</span><span style=\" font-family:'Roboto'; color:#000000; background-color:#ffffff;\">Windows</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u4e0b\u9ed8\u8ba4\u8def\u5f84\u4e3a</span><span style=\" font-family:'Cambria','serif'; color:#000000; background-color:#ffffff;\">\u00a0</span><span "
                        "style=\" font-family:'Courier New'; color:#000000;\">C:\\Users\\&lt;username&gt;\\AppData\\Roaming\\cnocr</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\uff09\u3002</span><span style=\" font-family:'Roboto'; color:#000000; background-color:#ffffff;\"> </span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u4e0b\u8f7d\u540e\u7684</span><span style=\" font-family:'Roboto'; color:#000000; background-color:#ffffff;\">zip</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u6587\u4ef6\u4ee3\u7801\u4f1a\u81ea\u52a8\u5bf9\u5176\u89e3\u538b\uff0c\u7136\u540e\u628a\u89e3\u538b\u540e\u7684\u6a21\u578b\u76f8\u5173\u76ee\u5f55\u653e\u4e8e</span><span style=\" font-family:'Courier New'; color:#000000;\">~/.cnocr/2.2</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u76ee\u5f55\u4e2d\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; marg"
                        "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; color:#000000; background-color:#ffffff;\">2)</span><span style=\" font-family:'\u5b8b\u4f53'; color:#000000; background-color:#ffffff;\">\u3001\u7cfb\u7edf\u5176\u4ed6\u914d\u7f6e\u3002</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-weight:600; color:#000000; background-color:#ffffff;\">4</span><span style=\" font-family:'\u5b8b\u4f53'; font-weight:600; color:#000000; background-color:#ffffff;\">\u3001\u7a0b\u5e8f\u8def\u5f84\u4e0d\u80fd\u6709\u4e2d\u6587\u3001\u7a7a\u683c\u7b49\uff01</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u5b8b\u4f53';\">5\u3001OCR \uff08Optical Character Recognition\uff0c\u5149\u5b66\u5b57\u7b26\u8bc6\u522b\uff09\u662f\u6307\u7535"
                        "\u5b50\u8bbe\u5907\uff08\u4f8b\u5982\u626b\u63cf\u4eea\u6216\u6570\u7801\u76f8\u673a\uff09\u68c0\u67e5\u7eb8\u4e0a\u6253\u5370\u7684\u5b57\u7b26\uff0c\u901a\u8fc7\u68c0\u6d4b\u6697\u3001\u4eae\u7684\u6a21\u5f0f\u786e\u5b9a\u5176\u5f62\u72b6\uff0c\u7136\u540e\u7528\u5b57\u7b26\u8bc6\u522b\u65b9\u6cd5\u5c06\u5f62\u72b6\u7ffb\u8bd1\u6210\u8ba1\u7b97\u673a\u6587\u5b57\u7684\u8fc7\u7a0b\uff1b\u5373\uff0c\u9488\u5bf9\u5370\u5237\u4f53\u5b57\u7b26\uff0c\u91c7\u7528\u5149\u5b66\u7684\u65b9\u5f0f\u5c06\u7eb8\u8d28\u6587\u6863\u4e2d\u7684\u6587\u5b57\u8f6c\u6362\u6210\u4e3a\u9ed1\u767d\u70b9\u9635\u7684\u56fe\u50cf\u6587\u4ef6\uff0c\u5e76\u901a\u8fc7\u8bc6\u522b\u8f6f\u4ef6\u5c06\u56fe\u50cf\u4e2d\u7684\u6587\u5b57\u8f6c\u6362\u6210\u6587\u672c\u683c\u5f0f\uff0c\u4f9b\u6587\u5b57\u5904\u7406\u8f6f\u4ef6\u8fdb\u4e00\u6b65\u7f16\u8f91\u52a0\u5de5\u7684\u6280\u672f\u3002\u5982\u4f55\u9664\u9519\u6216\u5229\u7528\u8f85\u52a9\u4fe1\u606f\u63d0\u9ad8\u8bc6\u522b\u6b63\u786e\u7387\uff0c\u662fOCR\u6700\u91cd\u8981\u7684\u8bfe\u9898"
                        "\uff0cICR\uff08Intelligent Character Recognition\uff09\u7684\u540d\u8bcd\u4e5f\u56e0\u6b64\u800c\u4ea7\u751f\u3002\u8861\u91cf\u4e00\u4e2aOCR\u7cfb\u7edf\u6027\u80fd\u597d\u574f\u7684\u4e3b\u8981\u6307\u6807\u6709\uff1a\u62d2\u8bc6\u7387\u3001\u8bef\u8bc6\u7387\u3001\u8bc6\u522b\u901f\u5ea6\u3001\u7528\u6237\u754c\u9762\u7684\u53cb\u597d\u6027\uff0c\u4ea7\u54c1\u7684\u7a33\u5b9a\u6027\uff0c\u6613\u7528\u6027\u53ca\u53ef\u884c\u6027\u7b49\u3002</span> </p></body></html>", None))
    # retranslateUi

