# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homerzVSJX.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc
class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(1182, 608)
        home.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(home)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_17.setFont(font)

        self.verticalLayout_6.addWidget(self.label_17)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.RightToLeft)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.proTable = QTableWidget(self.frame_3)
        if (self.proTable.columnCount() < 3):
            self.proTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.proTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.proTable.rowCount() < 20):
            self.proTable.setRowCount(20)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(8, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(9, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.proTable.setVerticalHeaderItem(10, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.proTable.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.proTable.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.proTable.setItem(0, 2, __qtablewidgetitem16)
        self.proTable.setObjectName(u"proTable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proTable.sizePolicy().hasHeightForWidth())
        self.proTable.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.proTable.setPalette(palette)
        self.proTable.setStyleSheet(u"/*---- QLineEdit  ----*/\n"
"QLineEdit {\n"
"    background-color: #6AAB6D;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6AAB6D;\n"
"    padding-left: 10px;\n"
"    selection-color: #ffffff;\n"
"    selection-background-color: #343b48;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3C6B4A;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #FFF59D;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color: #dbdbdb;\n"
"    border: 2px solid #808080;\n"
"    background-color: #4d4d4d;\n"
"}\n"
"\n"
"/*---- QPushButton ----*/\n"
"QPushButton {\n"
"    border: 2px solid #6AAB6D;\n"
"    border-radius: 5px;\n"
"    color: #6AAB6D;\n"
"    background-color: #343b48;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #83B986;\n"
"    border: 2px solid #83B986;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #388E3C;\n"
"    border: 2px solid #FFF59D;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #dbdbdb;\n"
"    border: 2px solid #808080;\n"
"    background-co"
                        "lor: #4d4d4d;\n"
"}\n"
"\n"
"/*---- QTableWidget ----*/\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: #CEE3CF;\n"
"    outline: none;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border-color: #CEE3CF;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: #CEE3CF;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #8BC34A;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: trasparent;\n"
"    max-width: 30px;\n"
"    border: none;\n"
"    border-style: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: #6AAB6D;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid #6AAB6D;\n"
"    background-color: #6AAB6D;\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"    border-"
                        "radius: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid #6AAB6D;\n"
"}\n"
"\n"
"/* ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6AAB6D;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #8BC34A;\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6AAB6D;\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6AAB6D;\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-a"
                        "rrow:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: #6AAB6D;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #8BC34A;\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: #6AAB6D;\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #6AAB6D;\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-ar"
                        "row:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: #6AAB6D;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #6AAB6D;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #9CC79E;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 3px;\n"
"    border-left-color: #6AAB6D;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: #FFF59D;\n"
"    background"
                        "-color: #6AAB6D;\n"
"    padding: 10px;\n"
"    selection-background-color: #6AAB6D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    color: #dbdbdb;\n"
"    border: 2px solid #808080;\n"
"    background-color: #4d4d4d;\n"
"}")
        self.proTable.setFrameShape(QFrame.NoFrame)
        self.proTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.proTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.proTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.proTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.proTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.proTable.setShowGrid(True)
        self.proTable.setGridStyle(Qt.SolidLine)
        self.proTable.setSortingEnabled(False)
        self.proTable.setRowCount(20)
        self.proTable.horizontalHeader().setVisible(False)
        self.proTable.horizontalHeader().setCascadingSectionResizes(True)
        self.proTable.horizontalHeader().setDefaultSectionSize(200)
        self.proTable.horizontalHeader().setStretchLastSection(True)
        self.proTable.verticalHeader().setVisible(False)
        self.proTable.verticalHeader().setCascadingSectionResizes(False)
        self.proTable.verticalHeader().setHighlightSections(False)
        self.proTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.proTable)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.proFotLabel = QLabel(self.frame_8)
        self.proFotLabel.setObjectName(u"proFotLabel")
        self.proFotLabel.setMinimumSize(QSize(50, 50))
        self.proFotLabel.setMaximumSize(QSize(100, 100))
        self.proFotLabel.setPixmap(QPixmap(u":/images/images/images/Icon.png"))
        self.proFotLabel.setScaledContents(True)
        self.proFotLabel.setAlignment(Qt.AlignCenter)
        self.proFotLabel.setMargin(10)

        self.horizontalLayout_4.addWidget(self.proFotLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.textWelcome = QLabel(self.frame_8)
        self.textWelcome.setObjectName(u"textWelcome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textWelcome.sizePolicy().hasHeightForWidth())
        self.textWelcome.setSizePolicy(sizePolicy1)
        self.textWelcome.setStyleSheet(u"color: #8BC34A;\n"
"font: 20pt;")
        self.textWelcome.setTextFormat(Qt.PlainText)
        self.textWelcome.setAlignment(Qt.AlignCenter)
        self.textWelcome.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.textWelcome)

        self.tags_2 = QFrame(self.frame_8)
        self.tags_2.setObjectName(u"tags_2")
        self.tags_2.setMaximumSize(QSize(16777215, 16777215))
        self.tags_2.setFrameShape(QFrame.StyledPanel)
        self.tags_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.tags_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.label_7 = QLabel(self.tags_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 25))
        self.label_7.setStyleSheet(u"color: #3B7447;\n"
"font: 16pt;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.textDate = QLabel(self.tags_2)
        self.textDate.setObjectName(u"textDate")
        self.textDate.setMinimumSize(QSize(0, 25))
        self.textDate.setStyleSheet(u"color: #6AAB6D;\n"
"font: 25pt;")
        self.textDate.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.textDate)


        self.horizontalLayout_4.addWidget(self.tags_2)

        self.fills_2 = QFrame(self.frame_8)
        self.fills_2.setObjectName(u"fills_2")
        self.fills_2.setFrameShape(QFrame.StyledPanel)
        self.fills_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.fills_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.label_8 = QLabel(self.fills_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 25))
        self.label_8.setStyleSheet(u"color: #3B7447;\n"
"font: 16pt;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.textTime = QLabel(self.fills_2)
        self.textTime.setObjectName(u"textTime")
        self.textTime.setMinimumSize(QSize(0, 25))
        self.textTime.setStyleSheet(u"color: #6AAB6D;\n"
"font: 25pt;")
        self.textTime.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.textTime)


        self.horizontalLayout_4.addWidget(self.fills_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(home)

        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"Form", None))
        self.label_17.setText(QCoreApplication.translate("home", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">Sistema de Informaci\u00f3n Miscelanea Iv\u00e1n</span></p></body></html>", None))
        ___qtablewidgetitem = self.proTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("home", u"0", None));
        ___qtablewidgetitem1 = self.proTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("home", u"1", None));
        ___qtablewidgetitem2 = self.proTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("home", u"2", None));
        ___qtablewidgetitem3 = self.proTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem4 = self.proTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem5 = self.proTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem6 = self.proTable.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem7 = self.proTable.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem8 = self.proTable.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem9 = self.proTable.verticalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem10 = self.proTable.verticalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem11 = self.proTable.verticalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem12 = self.proTable.verticalHeaderItem(9)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("home", u"New Row", None));
        ___qtablewidgetitem13 = self.proTable.verticalHeaderItem(10)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("home", u"New Row", None));

        __sortingEnabled = self.proTable.isSortingEnabled()
        self.proTable.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.proTable.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("home", u"Producto", None));
        ___qtablewidgetitem15 = self.proTable.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("home", u"Cantidad", None));
        ___qtablewidgetitem16 = self.proTable.item(0, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("home", u"Costo Compra", None));
        self.proTable.setSortingEnabled(__sortingEnabled)

        self.textWelcome.setText(QCoreApplication.translate("home", u"Bienvenido, Wilmar Alexander Rodriguez Bueno", None))
        self.label_7.setText(QCoreApplication.translate("home", u"Fecha:", None))
        self.textDate.setText(QCoreApplication.translate("home", u"Fecha", None))
        self.label_8.setText(QCoreApplication.translate("home", u"Hora:", None))
        self.textTime.setText(QCoreApplication.translate("home", u"Hora", None))
    # retranslateUi

