# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ordenHQTrBQ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_usuarios(object):
    def setupUi(self, usuarios):
        if not usuarios.objectName():
            usuarios.setObjectName(u"usuarios")
        usuarios.resize(1182, 608)
        usuarios.setStyleSheet(u"/*---- QLineEdit  ----*/\n"
"QLineEdit, QDateEdit {\n"
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
"QLineEdit:disabled, QDateEdit:disabled {\n"
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
"    border: 2px solid"
                        " #808080;\n"
"    background-color: #4d4d4d;\n"
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
"    "
                        "color: #f8f8f2;\n"
"    border-radius: 0px;\n"
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
"QScrollBar::up-arrow:hor"
                        "izontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
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
""
                        "}\n"
"\n"
"QScrollBar::up-arrow:vertical,\n"
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
"    color:"
                        " #FFF59D;\n"
"    background-color: #6AAB6D;\n"
"    padding: 10px;\n"
"    selection-background-color: #6AAB6D;\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    color: #dbdbdb;\n"
"    border: 2px solid #808080;\n"
"    background-color: #4d4d4d;\n"
"}")
        self.verticalLayout = QVBoxLayout(usuarios)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(usuarios)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_28)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_27)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_16 = QLabel(self.frame_27)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_28.addWidget(self.label_16)

        self.ordTable = QTableWidget(self.frame_27)
        if (self.ordTable.columnCount() < 11):
            self.ordTable.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.ordTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ordTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ordTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.ordTable.rowCount() < 3):
            self.ordTable.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ordTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ordTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ordTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ordTable.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ordTable.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ordTable.setItem(0, 2, __qtablewidgetitem8)
        self.ordTable.setObjectName(u"ordTable")
        self.ordTable.setMinimumSize(QSize(0, 0))
        self.ordTable.setMaximumSize(QSize(16777215, 16777215))
        self.ordTable.setFrameShape(QFrame.NoFrame)
        self.ordTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ordTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.ordTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ordTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ordTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ordTable.setShowGrid(True)
        self.ordTable.setGridStyle(Qt.SolidLine)
        self.ordTable.setSortingEnabled(False)
        self.ordTable.setRowCount(3)
        self.ordTable.setColumnCount(11)
        self.ordTable.horizontalHeader().setVisible(True)
        self.ordTable.horizontalHeader().setCascadingSectionResizes(False)
        self.ordTable.horizontalHeader().setDefaultSectionSize(120)
        self.ordTable.horizontalHeader().setStretchLastSection(True)
        self.ordTable.verticalHeader().setVisible(False)
        self.ordTable.verticalHeader().setCascadingSectionResizes(False)
        self.ordTable.verticalHeader().setHighlightSections(False)
        self.ordTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_28.addWidget(self.ordTable)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.ordAddButton = QPushButton(self.frame_26)
        self.ordAddButton.setObjectName(u"ordAddButton")
        self.ordAddButton.setMinimumSize(QSize(120, 30))
        self.ordAddButton.setFont(font)
        self.ordAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ordAddButton.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.ordAddButton)

        self.ordEditButton = QPushButton(self.frame_26)
        self.ordEditButton.setObjectName(u"ordEditButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ordEditButton.sizePolicy().hasHeightForWidth())
        self.ordEditButton.setSizePolicy(sizePolicy)
        self.ordEditButton.setMinimumSize(QSize(120, 30))
        self.ordEditButton.setFont(font)
        self.ordEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ordEditButton.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.ordEditButton)

        self.ordDelButton = QPushButton(self.frame_26)
        self.ordDelButton.setObjectName(u"ordDelButton")
        self.ordDelButton.setMinimumSize(QSize(120, 30))
        self.ordDelButton.setFont(font)
        self.ordDelButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ordDelButton.setIcon(icon2)

        self.horizontalLayout_14.addWidget(self.ordDelButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)


        self.verticalLayout_28.addWidget(self.frame_26)


        self.horizontalLayout_15.addWidget(self.frame_27)

        self.frame_25 = QFrame(self.frame_28)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(450, 0))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_9)

        self.label_15 = QLabel(self.frame_25)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_27.addWidget(self.label_15)

        self.frame_23 = QFrame(self.frame_25)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_23)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelVersion_22 = QLabel(self.frame_23)
        self.labelVersion_22.setObjectName(u"labelVersion_22")
        self.labelVersion_22.setLineWidth(1)
        self.labelVersion_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_22, 4, 0, 1, 1)

        self.labelVersion_20 = QLabel(self.frame_23)
        self.labelVersion_20.setObjectName(u"labelVersion_20")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_20, 3, 0, 1, 1)

        self.labelVersion_17 = QLabel(self.frame_23)
        self.labelVersion_17.setObjectName(u"labelVersion_17")
        self.labelVersion_17.setLineWidth(1)
        self.labelVersion_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_17, 2, 0, 1, 1)

        self.labelVersion_16 = QLabel(self.frame_23)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_16, 8, 0, 1, 1)

        self.frame_29 = QFrame(self.frame_23)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_29)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ordCliText = QLineEdit(self.frame_29)
        self.ordCliText.setObjectName(u"ordCliText")
        self.ordCliText.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.ordCliText)

        self.ordCliButton = QPushButton(self.frame_29)
        self.ordCliButton.setObjectName(u"ordCliButton")
        self.ordCliButton.setMinimumSize(QSize(120, 30))
        self.ordCliButton.setFont(font)
        self.ordCliButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ordCliButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.ordCliButton)


        self.gridLayout.addWidget(self.frame_29, 1, 2, 1, 1)

        self.labelVersion_21 = QLabel(self.frame_23)
        self.labelVersion_21.setObjectName(u"labelVersion_21")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_21, 6, 0, 1, 1)

        self.ordDesText = QTextEdit(self.frame_23)
        self.ordDesText.setObjectName(u"ordDesText")

        self.gridLayout.addWidget(self.ordDesText, 8, 2, 1, 1)

        self.ordResCombo = QComboBox(self.frame_23)
        self.ordResCombo.addItem("")
        self.ordResCombo.addItem("")
        self.ordResCombo.addItem("")
        self.ordResCombo.setObjectName(u"ordResCombo")
        self.ordResCombo.setFont(font)
        self.ordResCombo.setAutoFillBackground(False)
        self.ordResCombo.setIconSize(QSize(16, 16))
        self.ordResCombo.setFrame(True)

        self.gridLayout.addWidget(self.ordResCombo, 2, 2, 1, 1)

        self.labelVersion_14 = QLabel(self.frame_23)
        self.labelVersion_14.setObjectName(u"labelVersion_14")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_14, 5, 0, 1, 1)

        self.labelVersion_12 = QLabel(self.frame_23)
        self.labelVersion_12.setObjectName(u"labelVersion_12")
        self.labelVersion_12.setLineWidth(1)
        self.labelVersion_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_12, 1, 0, 1, 1)

        self.frame_30 = QFrame(self.frame_23)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ordRecDate = QDateEdit(self.frame_30)
        self.ordRecDate.setObjectName(u"ordRecDate")
        self.ordRecDate.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"  	height: 60px;\n"
"  	width: 150px;\n"
"  	color: white;\n"
"  	font-size: 24px;\n"
"  	icon-size: 56px, 56px;\n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"  	width: 150px;\n"
"  	left: 20px;\n"
"  	color: white;\n"
"  	font-size: 18px;\n"
"  	background-color: rgb(100, 100, 100);\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"  	width: 150px; \n"
"  	font-size:24px; \n"
"  	color: white; \n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"  	selection-background-color: rgb(136, 136, 136);\n"
"  	selection-color: rgb(255, 255, 255);\n"
"  }\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"  QCalendarWidget QSpinBox::up-arrow { width:56p"
                        "x;  height:56px; }\n"
"  QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; }\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size:24px;  \n"
"  	color: rgb(180, 180, 180);  \n"
"  	background-color: #35322f;  \n"
"  	selection-background-color: rgb(64, 64, 64); \n"
"  	selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.ordRecDate.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.ordRecDate)


        self.gridLayout.addWidget(self.frame_30, 4, 2, 1, 1)

        self.frame_31 = QFrame(self.frame_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ordEntDate = QDateEdit(self.frame_31)
        self.ordEntDate.setObjectName(u"ordEntDate")
        self.ordEntDate.setStyleSheet(u"QCalendarWidget QToolButton {\n"
"  	height: 60px;\n"
"  	width: 150px;\n"
"  	color: white;\n"
"  	font-size: 24px;\n"
"  	icon-size: 56px, 56px;\n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"  	width: 150px;\n"
"  	left: 20px;\n"
"  	color: white;\n"
"  	font-size: 18px;\n"
"  	background-color: rgb(100, 100, 100);\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"  	width: 150px; \n"
"  	font-size:24px; \n"
"  	color: white; \n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"  	selection-background-color: rgb(136, 136, 136);\n"
"  	selection-color: rgb(255, 255, 255);\n"
"  }\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"  QCalendarWidget QSpinBox::up-arrow { width:56p"
                        "x;  height:56px; }\n"
"  QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; }\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size:24px;  \n"
"  	color: rgb(180, 180, 180);  \n"
"  	background-color: #35322f;  \n"
"  	selection-background-color: rgb(64, 64, 64); \n"
"  	selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.ordEntDate.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.ordEntDate)


        self.gridLayout.addWidget(self.frame_31, 5, 2, 1, 1)

        self.ordValText = QLineEdit(self.frame_23)
        self.ordValText.setObjectName(u"ordValText")
        self.ordValText.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.ordValText, 3, 2, 1, 1)

        self.ordEstText = QLineEdit(self.frame_23)
        self.ordEstText.setObjectName(u"ordEstText")
        self.ordEstText.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.ordEstText, 6, 2, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_25)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.ordSaveButton = QPushButton(self.frame_24)
        self.ordSaveButton.setObjectName(u"ordSaveButton")
        self.ordSaveButton.setMinimumSize(QSize(120, 30))
        self.ordSaveButton.setFont(font)
        self.ordSaveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ordSaveButton.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.ordSaveButton)

        self.ordCancelButton = QPushButton(self.frame_24)
        self.ordCancelButton.setObjectName(u"ordCancelButton")
        self.ordCancelButton.setMinimumSize(QSize(120, 30))
        self.ordCancelButton.setFont(font)
        self.ordCancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ordCancelButton.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.ordCancelButton)

        self.ordClearButton = QPushButton(self.frame_24)
        self.ordClearButton.setObjectName(u"ordClearButton")
        self.ordClearButton.setMinimumSize(QSize(120, 30))
        self.ordClearButton.setFont(font)
        self.ordClearButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ordClearButton.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.ordClearButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_27.addWidget(self.frame_24)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)


        self.horizontalLayout_15.addWidget(self.frame_25)


        self.verticalLayout_2.addWidget(self.frame_28)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(usuarios)

        self.ordResCombo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(usuarios)
    # setupUi

    def retranslateUi(self, usuarios):
        usuarios.setWindowTitle(QCoreApplication.translate("usuarios", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Ordenes de Trabajo</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Ordenes</span></p></body></html>", None))
        ___qtablewidgetitem = self.ordTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("usuarios", u"0", None));
        ___qtablewidgetitem1 = self.ordTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("usuarios", u"Nueva columna", None));
        ___qtablewidgetitem2 = self.ordTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("usuarios", u"1", None));
        ___qtablewidgetitem3 = self.ordTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("usuarios", u"New Row", None));
        ___qtablewidgetitem4 = self.ordTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("usuarios", u"New Row", None));
        ___qtablewidgetitem5 = self.ordTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("usuarios", u"New Row", None));

        __sortingEnabled = self.ordTable.isSortingEnabled()
        self.ordTable.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.ordTable.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("usuarios", u"Nombre ", None));
        ___qtablewidgetitem7 = self.ordTable.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("usuarios", u"C\u00e9dula", None));
        ___qtablewidgetitem8 = self.ordTable.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("usuarios", u"Rol", None));
        self.ordTable.setSortingEnabled(__sortingEnabled)

        self.ordAddButton.setText(QCoreApplication.translate("usuarios", u"Agregar", None))
        self.ordEditButton.setText(QCoreApplication.translate("usuarios", u"Editar", None))
        self.ordDelButton.setText(QCoreApplication.translate("usuarios", u"Eliminar", None))
        self.label_15.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Orden Seleccionada</span></p></body></html>", None))
        self.labelVersion_22.setText(QCoreApplication.translate("usuarios", u"Fecha Recepcion", None))
        self.labelVersion_20.setText(QCoreApplication.translate("usuarios", u"Valor", None))
        self.labelVersion_17.setText(QCoreApplication.translate("usuarios", u"Responsable", None))
        self.labelVersion_16.setText(QCoreApplication.translate("usuarios", u"Descripcion", None))
        self.ordCliText.setText("")
        self.ordCliText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el primer nombre", None))
        self.ordCliButton.setText(QCoreApplication.translate("usuarios", u"Cambiar", None))
        self.labelVersion_21.setText(QCoreApplication.translate("usuarios", u"Estado", None))
        self.ordDesText.setHtml(QCoreApplication.translate("usuarios", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.ordResCombo.setItemText(0, QCoreApplication.translate("usuarios", u"Fotocopiado", None))
        self.ordResCombo.setItemText(1, QCoreApplication.translate("usuarios", u"Impresi\u00f3n", None))
        self.ordResCombo.setItemText(2, QCoreApplication.translate("usuarios", u"Laminado", None))

        self.ordResCombo.setPlaceholderText(QCoreApplication.translate("usuarios", u"Seleccione una opci\u00f3n", None))
        self.labelVersion_14.setText(QCoreApplication.translate("usuarios", u"Fecha Entrega", None))
        self.labelVersion_12.setText(QCoreApplication.translate("usuarios", u"Cliente", None))
        self.ordValText.setText("")
        self.ordValText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el segundo nombre", None))
        self.ordEstText.setText("")
        self.ordEstText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el primer nombre", None))
        self.ordSaveButton.setText(QCoreApplication.translate("usuarios", u"Confirmar", None))
        self.ordCancelButton.setText(QCoreApplication.translate("usuarios", u"Cancelar", None))
        self.ordClearButton.setText(QCoreApplication.translate("usuarios", u"Limpiar", None))
    # retranslateUi

