# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clienteFOdGDj.ui'
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

        self.cliTable = QTableWidget(self.frame_27)
        if (self.cliTable.columnCount() < 11):
            self.cliTable.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.cliTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cliTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cliTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.cliTable.rowCount() < 3):
            self.cliTable.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cliTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cliTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cliTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cliTable.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.cliTable.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.cliTable.setItem(0, 2, __qtablewidgetitem8)
        self.cliTable.setObjectName(u"cliTable")
        self.cliTable.setMinimumSize(QSize(0, 0))
        self.cliTable.setMaximumSize(QSize(16777215, 16777215))
        self.cliTable.setFrameShape(QFrame.NoFrame)
        self.cliTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.cliTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.cliTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cliTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cliTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cliTable.setShowGrid(True)
        self.cliTable.setGridStyle(Qt.SolidLine)
        self.cliTable.setSortingEnabled(False)
        self.cliTable.setRowCount(3)
        self.cliTable.setColumnCount(11)
        self.cliTable.horizontalHeader().setVisible(True)
        self.cliTable.horizontalHeader().setCascadingSectionResizes(False)
        self.cliTable.horizontalHeader().setDefaultSectionSize(120)
        self.cliTable.horizontalHeader().setStretchLastSection(True)
        self.cliTable.verticalHeader().setVisible(False)
        self.cliTable.verticalHeader().setCascadingSectionResizes(False)
        self.cliTable.verticalHeader().setHighlightSections(False)
        self.cliTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_28.addWidget(self.cliTable)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer)

        self.usuAddButton = QPushButton(self.frame_26)
        self.usuAddButton.setObjectName(u"usuAddButton")
        self.usuAddButton.setMinimumSize(QSize(120, 30))
        self.usuAddButton.setFont(font)
        self.usuAddButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuAddButton.setIcon(icon)

        self.horizontalLayout_14.addWidget(self.usuAddButton)

        self.usuEditButton = QPushButton(self.frame_26)
        self.usuEditButton.setObjectName(u"usuEditButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usuEditButton.sizePolicy().hasHeightForWidth())
        self.usuEditButton.setSizePolicy(sizePolicy)
        self.usuEditButton.setMinimumSize(QSize(120, 30))
        self.usuEditButton.setFont(font)
        self.usuEditButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuEditButton.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.usuEditButton)

        self.usuDelButton = QPushButton(self.frame_26)
        self.usuDelButton.setObjectName(u"usuDelButton")
        self.usuDelButton.setMinimumSize(QSize(120, 30))
        self.usuDelButton.setFont(font)
        self.usuDelButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuDelButton.setIcon(icon2)

        self.horizontalLayout_14.addWidget(self.usuDelButton)

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
        self.formLayout_7 = QFormLayout(self.frame_23)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.labelVersion_12 = QLabel(self.frame_23)
        self.labelVersion_12.setObjectName(u"labelVersion_12")
        self.labelVersion_12.setLineWidth(1)
        self.labelVersion_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.labelVersion_12)

        self.cliNom1Text = QLineEdit(self.frame_23)
        self.cliNom1Text.setObjectName(u"cliNom1Text")
        self.cliNom1Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.cliNom1Text)

        self.labelVersion_20 = QLabel(self.frame_23)
        self.labelVersion_20.setObjectName(u"labelVersion_20")
        self.labelVersion_20.setLineWidth(1)
        self.labelVersion_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.labelVersion_20)

        self.cliNom2Text = QLineEdit(self.frame_23)
        self.cliNom2Text.setObjectName(u"cliNom2Text")
        self.cliNom2Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.cliNom2Text)

        self.labelVersion_21 = QLabel(self.frame_23)
        self.labelVersion_21.setObjectName(u"labelVersion_21")
        self.labelVersion_21.setLineWidth(1)
        self.labelVersion_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.labelVersion_21)

        self.cliApe1Text = QLineEdit(self.frame_23)
        self.cliApe1Text.setObjectName(u"cliApe1Text")
        self.cliApe1Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.cliApe1Text)

        self.labelVersion_22 = QLabel(self.frame_23)
        self.labelVersion_22.setObjectName(u"labelVersion_22")
        self.labelVersion_22.setLineWidth(1)
        self.labelVersion_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.labelVersion_22)

        self.cliApe2Text = QLineEdit(self.frame_23)
        self.cliApe2Text.setObjectName(u"cliApe2Text")
        self.cliApe2Text.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.cliApe2Text)

        self.labelVersion_14 = QLabel(self.frame_23)
        self.labelVersion_14.setObjectName(u"labelVersion_14")
        self.labelVersion_14.setLineWidth(1)
        self.labelVersion_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.labelVersion_14)

        self.cliCedText = QLineEdit(self.frame_23)
        self.cliCedText.setObjectName(u"cliCedText")
        self.cliCedText.setMinimumSize(QSize(0, 30))
        self.cliCedText.setFrame(True)
        self.cliCedText.setEchoMode(QLineEdit.Normal)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.cliCedText)

        self.labelVersion_16 = QLabel(self.frame_23)
        self.labelVersion_16.setObjectName(u"labelVersion_16")
        self.labelVersion_16.setLineWidth(1)
        self.labelVersion_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.labelVersion_16)

        self.cliUbiText = QLineEdit(self.frame_23)
        self.cliUbiText.setObjectName(u"cliUbiText")
        self.cliUbiText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.cliUbiText)

        self.labelVersion_18 = QLabel(self.frame_23)
        self.labelVersion_18.setObjectName(u"labelVersion_18")
        self.labelVersion_18.setLineWidth(1)
        self.labelVersion_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.labelVersion_18)

        self.cliCorrText = QLineEdit(self.frame_23)
        self.cliCorrText.setObjectName(u"cliCorrText")
        self.cliCorrText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.cliCorrText)

        self.labelVersion_13 = QLabel(self.frame_23)
        self.labelVersion_13.setObjectName(u"labelVersion_13")
        self.labelVersion_13.setLineWidth(1)
        self.labelVersion_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.labelVersion_13)

        self.cliDirText = QLineEdit(self.frame_23)
        self.cliDirText.setObjectName(u"cliDirText")
        self.cliDirText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.cliDirText)

        self.labelVersion_15 = QLabel(self.frame_23)
        self.labelVersion_15.setObjectName(u"labelVersion_15")
        self.labelVersion_15.setLineWidth(1)
        self.labelVersion_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.labelVersion_15)

        self.cliTelText = QLineEdit(self.frame_23)
        self.cliTelText.setObjectName(u"cliTelText")
        self.cliTelText.setMinimumSize(QSize(0, 30))

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.cliTelText)


        self.verticalLayout_27.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_25)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.usuSaveButton = QPushButton(self.frame_24)
        self.usuSaveButton.setObjectName(u"usuSaveButton")
        self.usuSaveButton.setMinimumSize(QSize(120, 30))
        self.usuSaveButton.setFont(font)
        self.usuSaveButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.usuSaveButton.setIcon(icon)

        self.horizontalLayout_13.addWidget(self.usuSaveButton)

        self.usuCancelButton = QPushButton(self.frame_24)
        self.usuCancelButton.setObjectName(u"usuCancelButton")
        self.usuCancelButton.setMinimumSize(QSize(120, 30))
        self.usuCancelButton.setFont(font)
        self.usuCancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.usuCancelButton.setIcon(icon2)

        self.horizontalLayout_13.addWidget(self.usuCancelButton)

        self.usuClearButton = QPushButton(self.frame_24)
        self.usuClearButton.setObjectName(u"usuClearButton")
        self.usuClearButton.setMinimumSize(QSize(120, 30))
        self.usuClearButton.setFont(font)
        self.usuClearButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usuClearButton.setIcon(icon3)

        self.horizontalLayout_13.addWidget(self.usuClearButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_27.addWidget(self.frame_24)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_10)


        self.horizontalLayout_15.addWidget(self.frame_25)


        self.verticalLayout_2.addWidget(self.frame_28)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(usuarios)

        QMetaObject.connectSlotsByName(usuarios)
    # setupUi

    def retranslateUi(self, usuarios):
        usuarios.setWindowTitle(QCoreApplication.translate("usuarios", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Clientes</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Lista de Clientes</span></p></body></html>", None))
        ___qtablewidgetitem = self.cliTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("usuarios", u"0", None));
        ___qtablewidgetitem1 = self.cliTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("usuarios", u"Nueva columna", None));
        ___qtablewidgetitem2 = self.cliTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("usuarios", u"1", None));
        ___qtablewidgetitem3 = self.cliTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("usuarios", u"New Row", None));
        ___qtablewidgetitem4 = self.cliTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("usuarios", u"New Row", None));
        ___qtablewidgetitem5 = self.cliTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("usuarios", u"New Row", None));

        __sortingEnabled = self.cliTable.isSortingEnabled()
        self.cliTable.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.cliTable.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("usuarios", u"Nombre ", None));
        ___qtablewidgetitem7 = self.cliTable.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("usuarios", u"C\u00e9dula", None));
        ___qtablewidgetitem8 = self.cliTable.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("usuarios", u"Rol", None));
        self.cliTable.setSortingEnabled(__sortingEnabled)

        self.usuAddButton.setText(QCoreApplication.translate("usuarios", u"Agregar", None))
        self.usuEditButton.setText(QCoreApplication.translate("usuarios", u"Editar", None))
        self.usuDelButton.setText(QCoreApplication.translate("usuarios", u"Eliminar", None))
        self.label_15.setText(QCoreApplication.translate("usuarios", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Cliente Seleccionado</span></p></body></html>", None))
        self.labelVersion_12.setText(QCoreApplication.translate("usuarios", u"Nombre1", None))
        self.cliNom1Text.setText("")
        self.cliNom1Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el primer nombre", None))
        self.labelVersion_20.setText(QCoreApplication.translate("usuarios", u"Nombre2", None))
        self.cliNom2Text.setText("")
        self.cliNom2Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el segundo nombre", None))
        self.labelVersion_21.setText(QCoreApplication.translate("usuarios", u"Apellido1", None))
        self.cliApe1Text.setText("")
        self.cliApe1Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el primer apellido", None))
        self.labelVersion_22.setText(QCoreApplication.translate("usuarios", u"Apellido2", None))
        self.cliApe2Text.setText("")
        self.cliApe2Text.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el segundo apellido", None))
        self.labelVersion_14.setText(QCoreApplication.translate("usuarios", u"C\u00e9dula", None))
        self.cliCedText.setText("")
        self.cliCedText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el numero de c\u00e9dula", None))
        self.labelVersion_16.setText(QCoreApplication.translate("usuarios", u"Ubicaci\u00f3n", None))
        self.cliUbiText.setText("")
        self.cliUbiText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el alias", None))
        self.labelVersion_18.setText(QCoreApplication.translate("usuarios", u"Correo", None))
        self.cliCorrText.setText("")
        self.cliCorrText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese la contrase\u00f1a", None))
        self.labelVersion_13.setText(QCoreApplication.translate("usuarios", u"Direcci\u00f3n", None))
        self.cliDirText.setText("")
        self.cliDirText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese la direcci\u00f3n", None))
        self.labelVersion_15.setText(QCoreApplication.translate("usuarios", u"Tel\u00e9fono", None))
        self.cliTelText.setText("")
        self.cliTelText.setPlaceholderText(QCoreApplication.translate("usuarios", u"Ingrese el numero de tel\u00e9fono", None))
        self.usuSaveButton.setText(QCoreApplication.translate("usuarios", u"Confirmar", None))
        self.usuCancelButton.setText(QCoreApplication.translate("usuarios", u"Cancelar", None))
        self.usuClearButton.setText(QCoreApplication.translate("usuarios", u"Limpiar", None))
    # retranslateUi

