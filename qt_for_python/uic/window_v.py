# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_v.ui'
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
        Dialog.resize(505, 384)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout.addWidget(self.commandLinkButton, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u7248\u672c", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"Github", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">OCR\u6587\u672c\u8bc6\u522b</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">V1.0</span></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">---------------\u7248\u672c---------------</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">plan</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1\u3001\u4fee\u590d\u622a\u56fe\u8bc6\u522b\u754c\u9762ESC\u65e0\u6548BUG\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u3001\u589e\u52a0\u6a21\u578b\u9009\u9879\u3001\u81ea\u5b9a\u4e49\u6a21\u578b\u63a5\u53e3\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3\u3001\u589e\u52a0GPU\u52a0\u901f\u9009\u9879\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">V1.0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1\u3001GUI\u4f7f\u7528PySide2\u7f16\u5199</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2\u3001\u4f7f\u7528python3.9.12</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3\u3001OCR\u6a21\u5757\u4e3acnocr2.2\uff0c\u622a\u56fe\u529f\u80fd\u53c2\u8003\u4e86GITHUB\u4e0a\u7684textshot\u6a21\u5757\u4ee3\u7801\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4\u3001\u6587\u4ef6\u8f83\u5927\u4e3b\u8981\u56e0\u4e3a\u5185\u542b\u6587\u5b57\u68c0\u6d4b\u5f15\u64ceCNSTD\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\">5\u3001\u5f88\u591a\u529f\u80fd\u5df2\u7ecf\u6253\u5305\uff0c\u4f46\u7a0b\u5e8f\u5e76\u672a\u8c03\u7528\uff0c\u56e0\u4e3a\u6b64\u7248\u672c\u4e3a\u4e86\u4fbf\u4e8e\u4f7f\u7528\uff0c\u64cd\u4f5c\u754c\u9762\u8f83\u7b80\u5355\u3002\u540e\u7eed\u5c06\u53d1\u5e03\u529f\u80fd\u590d\u6742\u7684\u7248\u672c\u4f9b\u5927\u5bb6\u5b66\u4e60\u53c2\u8003\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6\u3001\u672c\u7a0b\u5e8f\u4e3a\u79bb\u7ebf\u7248\uff0c\u65e0\u9700\u8054\u7f51\uff0c\u65e0\u4f7f\u7528\u6b21\u6570\u9650\u5236\u3002</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">by qhz734</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-size:10pt; font-weight:600;\">2022.07.28</span></p></body></html>", None))
    # retranslateUi

