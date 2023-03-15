# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ZhihuSpider.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 493)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_Run = QPushButton(self.centralwidget)
        self.btn_Run.setObjectName(u"btn_Run")

        self.verticalLayout_3.addWidget(self.btn_Run)

        self.btn_Paste = QPushButton(self.centralwidget)
        self.btn_Paste.setObjectName(u"btn_Paste")

        self.verticalLayout_3.addWidget(self.btn_Paste)

        self.btn_Get_MarkDowm = QPushButton(self.centralwidget)
        self.btn_Get_MarkDowm.setObjectName(u"btn_Get_MarkDowm")

        self.verticalLayout_3.addWidget(self.btn_Get_MarkDowm)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 7)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit_Input = QTextEdit(self.centralwidget)
        self.textEdit_Input.setObjectName(u"textEdit_Input")

        self.verticalLayout.addWidget(self.textEdit_Input)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textBrowser_Output = QTextBrowser(self.centralwidget)
        self.textBrowser_Output.setObjectName(u"textBrowser_Output")
        self.textBrowser_Output.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.textBrowser_Output)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btn_Paste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.btn_Get_MarkDowm.setText(QCoreApplication.translate("MainWindow", u"Get_MarkDowm", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output", None))
    # retranslateUi

