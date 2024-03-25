# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManagerKMEVja.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush1 = QBrush(QColor(0, 120, 215, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(240, 240, 240, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #333;\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"    color: #333;\n"
"    background-color: #f8f8f2;\n"
"    border: 1px solid #CCC;\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid #FFF59D;\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {\n"
"    background-color: #f8f8f2;\n"
"    border: 1px solid #CCC;\n"
"    color: #3A7D43;\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#leftMenuBg {\n"
"    background-color: #6AAB6D;\n"
"}\n"
"\n"
"#topLogo {\n"
"    background-color: #6AAB6D;\n"
"\n"
"}\n"
"\n"
"#titleLeftApp {\n"
"    font: 63 12pt \"Segoe UI Semibold\";\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#titleLeftDescription {\n"
"    font: 8pt \"Segoe UI\";\n"
"    color: #8BC34A;\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"    background-position: left center;\n"
"   "
                        " background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: #8BC34A;\n"
"}\n"
"\n"
"#topMenu .QPushButton:pressed {\n"
"    background-color: #FFF59D;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#bottomMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: #8BC34A;\n"
"}\n"
"\n"
"#bottomMenu .QPushButton:pressed {\n"
"    background-color: #FFF59D;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftMenuFrame {\n"
"    border-top: 3px solid #77B27A;\n"
"}\n"
"\n"
"/* Toggle Button *"
                        "/\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: #519D55;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#toggleButton:hover {\n"
"    background-color: #8BC34A;\n"
"}\n"
"\n"
"#toggleButton:pressed {\n"
"    background-color: #FFF59D;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo {\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"/* Extra Tab */\n"
"#extraLeftBox {\n"
"    background-color: #3B7447;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#extraTopBg {\n"
"    background-color: #A9D277\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Btn Close */\n"
""
                        "#extraCloseColumnBtn {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#extraCloseColumnBtn:hover {\n"
"    background-color: #FFF59D;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#extraCloseColumnBtn:pressed {\n"
"    background-color: #FFF59D;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Extra Content */\n"
"#extraContent {\n"
"    border-top: 3px solid #6AAB6D;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: #5EA461;\n"
"}\n"
"\n"
"#extraTopMenu .QPushButton:pressed {\n"
"    background-color: #8BC34A;\n"
"    color: rgb(255, 255,"
                        " 255);\n"
"}\n"
"\n"
"/* Content App */\n"
"#contentTopBg {\n"
"    background-color: #6AAB6D;\n"
"}\n"
"\n"
"#contentBottom {\n"
"    border-top: 3px solid #8BC34A;\n"
"}\n"
"\n"
"#titleRightInfo {\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#rightButtons .QPushButton:hover {\n"
"    background-color: #8BC34A;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"#rightButtons .QPushButton:pressed {\n"
"    background-color: #FFF59D;\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox {\n"
"    background-color: #3B7447;\n"
"}\n"
"\n"
"#themeSettingsTopDetail {\n"
"    background-color: #6AAB6D;\n"
"}\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar {\n"
"    background-color: #3B7447\n"
"}\n"
"\n"
"#bottomBar QLabel {\n"
"    font-size: 11px;\n"
"    color: #f8f8f2;\n"
"    padding"
                        "-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: #5EA461;\n"
"}\n"
"\n"
"#contentSettings .QPushButton:pressed {\n"
"    background-color: #8BC34A;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        palette1 = QPalette()
        brush3 = QBrush(QColor(58, 125, 67, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush4 = QBrush(QColor(248, 248, 242, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.bgApp.setPalette(palette1)
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.bgApp)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(106, 171, 109, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.leftMenuBg.setPalette(palette2)
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.topLogoInfo.setPalette(palette3)
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.topLogo.setPalette(palette4)
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.topLogo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 42, 42))
        self.label.setMaximumSize(QSize(42, 42))
        self.label.setPixmap(QPixmap(u":/images/images/images/Icon.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.titleLeftApp.setPalette(palette5)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        palette6 = QPalette()
        brush6 = QBrush(QColor(139, 195, 74, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.titleLeftDescription.setPalette(palette6)
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.leftMenuFrame.setPalette(palette7)
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.toggleBox.setPalette(palette8)
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        brush7 = QBrush(QColor(81, 157, 85, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.toggleButton.setPalette(palette9)
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Highlight, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.topMenu.setPalette(palette10)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        brush8 = QBrush(QColor(0, 0, 0, 0))
        brush8.setStyle(Qt.SolidPattern)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_home.setPalette(palette11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_usuario = QPushButton(self.topMenu)
        self.btn_usuario.setObjectName(u"btn_usuario")
        sizePolicy.setHeightForWidth(self.btn_usuario.sizePolicy().hasHeightForWidth())
        self.btn_usuario.setSizePolicy(sizePolicy)
        self.btn_usuario.setMinimumSize(QSize(0, 45))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_usuario.setPalette(palette12)
        self.btn_usuario.setFont(font)
        self.btn_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_usuario.setLayoutDirection(Qt.LeftToRight)
        self.btn_usuario.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user-follow.png);")

        self.verticalLayout_8.addWidget(self.btn_usuario)

        self.btn_cliente = QPushButton(self.topMenu)
        self.btn_cliente.setObjectName(u"btn_cliente")
        sizePolicy.setHeightForWidth(self.btn_cliente.sizePolicy().hasHeightForWidth())
        self.btn_cliente.setSizePolicy(sizePolicy)
        self.btn_cliente.setMinimumSize(QSize(0, 45))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_cliente.setPalette(palette13)
        self.btn_cliente.setFont(font)
        self.btn_cliente.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente.setLayoutDirection(Qt.LeftToRight)
        self.btn_cliente.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_cliente)

        self.btn_orden = QPushButton(self.topMenu)
        self.btn_orden.setObjectName(u"btn_orden")
        sizePolicy.setHeightForWidth(self.btn_orden.sizePolicy().hasHeightForWidth())
        self.btn_orden.setSizePolicy(sizePolicy)
        self.btn_orden.setMinimumSize(QSize(0, 45))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_orden.setPalette(palette14)
        self.btn_orden.setFont(font)
        self.btn_orden.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_orden.setLayoutDirection(Qt.LeftToRight)
        self.btn_orden.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-cart.png);")

        self.verticalLayout_8.addWidget(self.btn_orden)

        self.btn_reporte = QPushButton(self.topMenu)
        self.btn_reporte.setObjectName(u"btn_reporte")
        sizePolicy.setHeightForWidth(self.btn_reporte.sizePolicy().hasHeightForWidth())
        self.btn_reporte.setSizePolicy(sizePolicy)
        self.btn_reporte.setMinimumSize(QSize(0, 45))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_reporte.setPalette(palette15)
        self.btn_reporte.setFont(font)
        self.btn_reporte.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reporte.setLayoutDirection(Qt.LeftToRight)
        self.btn_reporte.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_8.addWidget(self.btn_reporte)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.bottomMenu.setPalette(palette16)
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.toggleLeftBox.setPalette(palette17)
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-star.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.horizontalLayout_16.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        brush9 = QBrush(QColor(59, 116, 71, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.extraLeftBox.setPalette(palette18)
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush10 = QBrush(QColor(169, 210, 119, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush10)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraTopBg.setPalette(palette19)
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(255, 255, 255, 0))
        brush11.setStyle(Qt.SolidPattern)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraCloseColumnBtn.setPalette(palette20)
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        palette21 = QPalette()
        brush12 = QBrush(QColor(255, 255, 255, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush12)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush12)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush12)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush12)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.extraLabel.setPalette(palette21)

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-star.png);\n"
"background-position: centered;\n"
"background-repeat: no-repeat;")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraContent.setPalette(palette22)
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraTopMenu.setPalette(palette23)
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraCenter.setPalette(palette24)
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.textEdit.setPalette(palette25)
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraBottom.setPalette(palette26)
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.horizontalLayout_16.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.contentBox.setPalette(palette27)
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.contentTopBg.setPalette(palette28)
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.leftBox.setPalette(palette29)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.titleRightInfo.setPalette(palette30)
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.rightButtons.setPalette(palette31)
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.settingsTopBtn.setPalette(palette32)
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.minimizeAppBtn.setPalette(palette33)
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette34.setBrush(QPalette.Active, QPalette.Highlight, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette34.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette34.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.maximizeRestoreAppBtn.setPalette(palette34)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush11)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.closeAppBtn.setPalette(palette35)
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.contentBottom.setPalette(palette36)
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.content.setPalette(palette37)
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.pagesContainer.setPalette(palette38)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.stackedWidget.setPalette(palette39)
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.extraRightBox.setPalette(palette40)
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush5)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.themeSettingsTopDetail.setPalette(palette41)
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.contentSettings.setPalette(palette42)
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.topMenus.setPalette(palette43)
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_message.setPalette(palette44)
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_print.setPalette(palette45)
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush8)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush8)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.btn_logout.setPalette(palette46)
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.bottomBar.setPalette(palette47)
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.creditsLabel.setPalette(palette48)
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.version.setPalette(palette49)
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush)
        palette50.setBrush(QPalette.Active, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.frame_size_grip.setPalette(palette50)
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.horizontalLayout_16.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Miscelanea Iv\u00e1n", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Sistema de Informaci\u00f3n", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.btn_cliente.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.btn_orden.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.btn_reporte.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Desarrollador", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**Miscel\u00e1nea Iv\u00e1n**\n"
"\n"
"Sistema de Informaci\u00f3n para el control y evaluaci\u00f3n de los procesos llevados a\n"
"cabo en la Miscel\u00e1nea Iv\u00e1n ubicada en el municipio de Cantrataci\u00f3n, Santander.\n"
"\n"
"Universidad de Investigaci\u00f3n y Desarrollo UDI\n"
"\n"
"*Desarrollado por: *\n"
"Wilmar Alex\u00e1nder Rodr\u00edguez Bueno\n"
"Miguel Angel Chac\u00f3n Garc\u00eda\n"
"\n"
"**Herramientas**\n"
"\n"
"PyDracula, PyQt6, PySide6, FPDF, MySQL\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffff7f;\">Miscel\u00e1nea Iv\u00e1n</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Sistema de Informaci\u00f3n para el control y evaluaci\u00f3n de los procesos llevados a cabo en la Miscel\u00e1nea Iv\u00e1n ubicada en el municipio de Cantrataci\u00f3n, Santander.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; mar"
                        "gin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Universidad de Investigaci\u00f3n y Desarrollo UDI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#aaff7f;\">Desarrollado por: </span><span style=\" color:#aaff7f;\"><br />Wilmar Alex\u00e1nder Rodr\u00edguez Bueno<br />Miguel Angel Chac\u00f3n Garc\u00eda</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffff7f;\">Herramientas</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">PyDracula, PyQt6, PySide6, FPDF, MySQL</span></p></body></html"
                        ">", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Conectado al servidor correctamente", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v 0.0.3", None))
    # retranslateUi

