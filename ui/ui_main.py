# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1275, 720)
        MainWindow.setMinimumSize(QSize(1275, 720))
        MainWindow.setStyleSheet(u"background-color: rgb(68, 68, 68);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionopen_output_folder = QAction(MainWindow)
        self.actionopen_output_folder.setObjectName(u"actionopen_output_folder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.MainName = QLabel(self.centralwidget)
        self.MainName.setObjectName(u"MainName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainName.sizePolicy().hasHeightForWidth())
        self.MainName.setSizePolicy(sizePolicy1)
        self.MainName.setMinimumSize(QSize(800, 0))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.MainName.setFont(font)
        self.MainName.setLayoutDirection(Qt.LeftToRight)
        self.MainName.setAutoFillBackground(False)
        self.MainName.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.MainName)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.imageTabButton = QPushButton(self.centralwidget)
        self.imageTabButton.setObjectName(u"imageTabButton")
        self.imageTabButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.imageTabButton.sizePolicy().hasHeightForWidth())
        self.imageTabButton.setSizePolicy(sizePolicy2)
        self.imageTabButton.setMinimumSize(QSize(100, 84))
        self.imageTabButton.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setKerning(True)
        self.imageTabButton.setFont(font1)
        self.imageTabButton.setCheckable(True)
        self.imageTabButton.setChecked(True)
        self.imageTabButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.imageTabButton)

        self.AnimatorTabButton = QPushButton(self.centralwidget)
        self.AnimatorTabButton.setObjectName(u"AnimatorTabButton")
        sizePolicy2.setHeightForWidth(self.AnimatorTabButton.sizePolicy().hasHeightForWidth())
        self.AnimatorTabButton.setSizePolicy(sizePolicy2)
        self.AnimatorTabButton.setMinimumSize(QSize(100, 84))
        self.AnimatorTabButton.setMaximumSize(QSize(100, 16777215))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.AnimatorTabButton.setFont(font2)
        self.AnimatorTabButton.setCheckable(True)
        self.AnimatorTabButton.setChecked(False)
        self.AnimatorTabButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.AnimatorTabButton)

        self.vid2vidTabButton = QPushButton(self.centralwidget)
        self.vid2vidTabButton.setObjectName(u"vid2vidTabButton")
        self.vid2vidTabButton.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.vid2vidTabButton.sizePolicy().hasHeightForWidth())
        self.vid2vidTabButton.setSizePolicy(sizePolicy2)
        self.vid2vidTabButton.setMinimumSize(QSize(100, 84))
        self.vid2vidTabButton.setMaximumSize(QSize(100, 16777215))
        self.vid2vidTabButton.setFont(font2)
        self.vid2vidTabButton.setStyleSheet(u"")
        self.vid2vidTabButton.setCheckable(True)
        self.vid2vidTabButton.setChecked(False)
        self.vid2vidTabButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.vid2vidTabButton)

        self.inpaintingButton = QPushButton(self.centralwidget)
        self.inpaintingButton.setObjectName(u"inpaintingButton")
        self.inpaintingButton.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.inpaintingButton.sizePolicy().hasHeightForWidth())
        self.inpaintingButton.setSizePolicy(sizePolicy2)
        self.inpaintingButton.setMinimumSize(QSize(100, 84))
        self.inpaintingButton.setMaximumSize(QSize(100, 16777215))
        self.inpaintingButton.setFont(font2)
        self.inpaintingButton.setCheckable(True)
        self.inpaintingButton.setChecked(False)
        self.inpaintingButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.inpaintingButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_15.addLayout(self.verticalLayout_5)

        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.SingleImagePage = QWidget()
        self.SingleImagePage.setObjectName(u"SingleImagePage")
        self.verticalLayout_9 = QVBoxLayout(self.SingleImagePage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.line_2 = QFrame(self.SingleImagePage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 15, 30, -1)
        self.label_2 = QLabel(self.SingleImagePage)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(18)
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.promptLabel = QLabel(self.SingleImagePage)
        self.promptLabel.setObjectName(u"promptLabel")
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setMinimumSize(QSize(600, 0))
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.promptLabel.setFont(font4)

        self.verticalLayout.addWidget(self.promptLabel)

        self.promptInput = QLineEdit(self.SingleImagePage)
        self.promptInput.setObjectName(u"promptInput")
        sizePolicy.setHeightForWidth(self.promptInput.sizePolicy().hasHeightForWidth())
        self.promptInput.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(12)
        self.promptInput.setFont(font5)
        self.promptInput.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.verticalLayout.addWidget(self.promptInput)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.seedLable = QLabel(self.SingleImagePage)
        self.seedLable.setObjectName(u"seedLable")
        sizePolicy2.setHeightForWidth(self.seedLable.sizePolicy().hasHeightForWidth())
        self.seedLable.setSizePolicy(sizePolicy2)
        self.seedLable.setMaximumSize(QSize(16777215, 20))
        self.seedLable.setFont(font4)

        self.horizontalLayout_2.addWidget(self.seedLable)

        self.seedInputBox = QLineEdit(self.SingleImagePage)
        self.seedInputBox.setObjectName(u"seedInputBox")
        sizePolicy2.setHeightForWidth(self.seedInputBox.sizePolicy().hasHeightForWidth())
        self.seedInputBox.setSizePolicy(sizePolicy2)
        self.seedInputBox.setMaximumSize(QSize(16777215, 20))
        font6 = QFont()
        font6.setPointSize(10)
        self.seedInputBox.setFont(font6)
        self.seedInputBox.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")
        self.seedInputBox.setInputMethodHints(Qt.ImhDigitsOnly)

        self.horizontalLayout_2.addWidget(self.seedInputBox)

        self.seedRandomized = QCheckBox(self.SingleImagePage)
        self.seedRandomized.setObjectName(u"seedRandomized")
        sizePolicy2.setHeightForWidth(self.seedRandomized.sizePolicy().hasHeightForWidth())
        self.seedRandomized.setSizePolicy(sizePolicy2)
        self.seedRandomized.setMaximumSize(QSize(16777215, 20))
        self.seedRandomized.setFont(font4)
        self.seedRandomized.setChecked(True)

        self.horizontalLayout_2.addWidget(self.seedRandomized)

        self.horizontalSpacer = QSpacerItem(270, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_3 = QLabel(self.SingleImagePage)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.widthInput = QSpinBox(self.SingleImagePage)
        self.widthInput.setObjectName(u"widthInput")
        self.widthInput.setMinimum(64)
        self.widthInput.setMaximum(1024)
        self.widthInput.setSingleStep(64)
        self.widthInput.setValue(512)

        self.horizontalLayout_3.addWidget(self.widthInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.SingleImagePage)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.heightInput = QSpinBox(self.SingleImagePage)
        self.heightInput.setObjectName(u"heightInput")
        self.heightInput.setMinimum(64)
        self.heightInput.setMaximum(1024)
        self.heightInput.setValue(512)

        self.horizontalLayout_3.addWidget(self.heightInput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stepCountLabel = QLabel(self.SingleImagePage)
        self.stepCountLabel.setObjectName(u"stepCountLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stepCountLabel.sizePolicy().hasHeightForWidth())
        self.stepCountLabel.setSizePolicy(sizePolicy5)
        self.stepCountLabel.setMinimumSize(QSize(0, 20))
        self.stepCountLabel.setMaximumSize(QSize(75, 16777215))
        self.stepCountLabel.setFont(font4)

        self.horizontalLayout_4.addWidget(self.stepCountLabel)

        self.stepSlider = QSlider(self.SingleImagePage)
        self.stepSlider.setObjectName(u"stepSlider")
        sizePolicy.setHeightForWidth(self.stepSlider.sizePolicy().hasHeightForWidth())
        self.stepSlider.setSizePolicy(sizePolicy)
        self.stepSlider.setMaximum(25)
        self.stepSlider.setPageStep(1)
        self.stepSlider.setValue(4)
        self.stepSlider.setSliderPosition(4)
        self.stepSlider.setOrientation(Qt.Horizontal)
        self.stepSlider.setTickPosition(QSlider.TicksAbove)
        self.stepSlider.setTickInterval(1)

        self.horizontalLayout_4.addWidget(self.stepSlider)

        self.stepsValueBox = QLineEdit(self.SingleImagePage)
        self.stepsValueBox.setObjectName(u"stepsValueBox")
        sizePolicy2.setHeightForWidth(self.stepsValueBox.sizePolicy().hasHeightForWidth())
        self.stepsValueBox.setSizePolicy(sizePolicy2)
        self.stepsValueBox.setMaximumSize(QSize(30, 16777215))
        self.stepsValueBox.setFont(font6)
        self.stepsValueBox.setInputMethodHints(Qt.ImhDigitsOnly)
        self.stepsValueBox.setFrame(False)
        self.stepsValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.stepsValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scaleCountLabel = QLabel(self.SingleImagePage)
        self.scaleCountLabel.setObjectName(u"scaleCountLabel")
        sizePolicy5.setHeightForWidth(self.scaleCountLabel.sizePolicy().hasHeightForWidth())
        self.scaleCountLabel.setSizePolicy(sizePolicy5)
        self.scaleCountLabel.setMinimumSize(QSize(0, 20))
        self.scaleCountLabel.setMaximumSize(QSize(75, 16777215))
        self.scaleCountLabel.setBaseSize(QSize(0, 0))
        font7 = QFont()
        font7.setBold(True)
        font7.setUnderline(False)
        font7.setWeight(75)
        self.scaleCountLabel.setFont(font7)

        self.horizontalLayout_5.addWidget(self.scaleCountLabel)

        self.scaleSlider = QSlider(self.SingleImagePage)
        self.scaleSlider.setObjectName(u"scaleSlider")
        sizePolicy.setHeightForWidth(self.scaleSlider.sizePolicy().hasHeightForWidth())
        self.scaleSlider.setSizePolicy(sizePolicy)
        self.scaleSlider.setMaximum(20)
        self.scaleSlider.setPageStep(1)
        self.scaleSlider.setValue(7)
        self.scaleSlider.setSliderPosition(7)
        self.scaleSlider.setOrientation(Qt.Horizontal)
        self.scaleSlider.setTickPosition(QSlider.TicksAbove)
        self.scaleSlider.setTickInterval(0)

        self.horizontalLayout_5.addWidget(self.scaleSlider)

        self.scaleValueBox = QLineEdit(self.SingleImagePage)
        self.scaleValueBox.setObjectName(u"scaleValueBox")
        sizePolicy3.setHeightForWidth(self.scaleValueBox.sizePolicy().hasHeightForWidth())
        self.scaleValueBox.setSizePolicy(sizePolicy3)
        self.scaleValueBox.setMaximumSize(QSize(30, 16777215))
        self.scaleValueBox.setFont(font6)
        self.scaleValueBox.setInputMethodHints(Qt.ImhDigitsOnly)
        self.scaleValueBox.setFrame(False)
        self.scaleValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.scaleValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imageAmountLabel = QLabel(self.SingleImagePage)
        self.imageAmountLabel.setObjectName(u"imageAmountLabel")
        sizePolicy5.setHeightForWidth(self.imageAmountLabel.sizePolicy().hasHeightForWidth())
        self.imageAmountLabel.setSizePolicy(sizePolicy5)
        self.imageAmountLabel.setMinimumSize(QSize(0, 20))
        self.imageAmountLabel.setMaximumSize(QSize(75, 16777215))
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setWeight(75)
        self.imageAmountLabel.setFont(font8)

        self.horizontalLayout_6.addWidget(self.imageAmountLabel)

        self.imageCountSlider = QSlider(self.SingleImagePage)
        self.imageCountSlider.setObjectName(u"imageCountSlider")
        sizePolicy.setHeightForWidth(self.imageCountSlider.sizePolicy().hasHeightForWidth())
        self.imageCountSlider.setSizePolicy(sizePolicy)
        self.imageCountSlider.setMinimum(1)
        self.imageCountSlider.setMaximum(9)
        self.imageCountSlider.setPageStep(1)
        self.imageCountSlider.setOrientation(Qt.Horizontal)
        self.imageCountSlider.setTickPosition(QSlider.TicksAbove)
        self.imageCountSlider.setTickInterval(1)

        self.horizontalLayout_6.addWidget(self.imageCountSlider)

        self.imageCountValueBox = QLineEdit(self.SingleImagePage)
        self.imageCountValueBox.setObjectName(u"imageCountValueBox")
        sizePolicy2.setHeightForWidth(self.imageCountValueBox.sizePolicy().hasHeightForWidth())
        self.imageCountValueBox.setSizePolicy(sizePolicy2)
        self.imageCountValueBox.setMaximumSize(QSize(30, 16777215))
        self.imageCountValueBox.setFont(font6)
        self.imageCountValueBox.setInputMethodHints(Qt.ImhDigitsOnly)
        self.imageCountValueBox.setFrame(False)
        self.imageCountValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.imageCountValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.img2imgGroup = QGroupBox(self.SingleImagePage)
        self.img2imgGroup.setObjectName(u"img2imgGroup")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.img2imgGroup.sizePolicy().hasHeightForWidth())
        self.img2imgGroup.setSizePolicy(sizePolicy6)
        self.img2imgGroup.setMinimumSize(QSize(0, 120))
        self.img2imgGroup.setAlignment(Qt.AlignCenter)
        self.img2imgGroup.setFlat(False)
        self.img2imgGroup.setCheckable(False)
        self.verticalLayout_7 = QVBoxLayout(self.img2imgGroup)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.img2imgCheckbox = QCheckBox(self.img2imgGroup)
        self.img2imgCheckbox.setObjectName(u"img2imgCheckbox")
        sizePolicy5.setHeightForWidth(self.img2imgCheckbox.sizePolicy().hasHeightForWidth())
        self.img2imgCheckbox.setSizePolicy(sizePolicy5)
        self.img2imgCheckbox.setFont(font4)
        self.img2imgCheckbox.setTristate(False)

        self.horizontalLayout_10.addWidget(self.img2imgCheckbox)

        self.img2imgInitPathLineEdit = QLineEdit(self.img2imgGroup)
        self.img2imgInitPathLineEdit.setObjectName(u"img2imgInitPathLineEdit")
        sizePolicy.setHeightForWidth(self.img2imgInitPathLineEdit.sizePolicy().hasHeightForWidth())
        self.img2imgInitPathLineEdit.setSizePolicy(sizePolicy)
        self.img2imgInitPathLineEdit.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.horizontalLayout_10.addWidget(self.img2imgInitPathLineEdit)

        self.img2imgChoosefolder = QPushButton(self.img2imgGroup)
        self.img2imgChoosefolder.setObjectName(u"img2imgChoosefolder")
        sizePolicy5.setHeightForWidth(self.img2imgChoosefolder.sizePolicy().hasHeightForWidth())
        self.img2imgChoosefolder.setSizePolicy(sizePolicy5)

        self.horizontalLayout_10.addWidget(self.img2imgChoosefolder)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.strengthLabel = QLabel(self.img2imgGroup)
        self.strengthLabel.setObjectName(u"strengthLabel")
        sizePolicy4.setHeightForWidth(self.strengthLabel.sizePolicy().hasHeightForWidth())
        self.strengthLabel.setSizePolicy(sizePolicy4)
        self.strengthLabel.setFont(font4)

        self.horizontalLayout_13.addWidget(self.strengthLabel)

        self.strengthSlider = QSlider(self.img2imgGroup)
        self.strengthSlider.setObjectName(u"strengthSlider")
        sizePolicy3.setHeightForWidth(self.strengthSlider.sizePolicy().hasHeightForWidth())
        self.strengthSlider.setSizePolicy(sizePolicy3)
        self.strengthSlider.setMaximum(100)
        self.strengthSlider.setSingleStep(1)
        self.strengthSlider.setValue(70)
        self.strengthSlider.setOrientation(Qt.Horizontal)
        self.strengthSlider.setTickPosition(QSlider.TicksAbove)
        self.strengthSlider.setTickInterval(10)

        self.horizontalLayout_13.addWidget(self.strengthSlider)

        self.strengthValueBox = QLineEdit(self.img2imgGroup)
        self.strengthValueBox.setObjectName(u"strengthValueBox")
        sizePolicy.setHeightForWidth(self.strengthValueBox.sizePolicy().hasHeightForWidth())
        self.strengthValueBox.setSizePolicy(sizePolicy)
        self.strengthValueBox.setMinimumSize(QSize(50, 0))
        self.strengthValueBox.setMaximumSize(QSize(30, 16777215))
        self.strengthValueBox.setSizeIncrement(QSize(0, 0))
        self.strengthValueBox.setFont(font6)
        self.strengthValueBox.setFrame(False)
        self.strengthValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.strengthValueBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.img2imgGroup)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.generateButton = QPushButton(self.SingleImagePage)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy3.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy3)
        self.generateButton.setAcceptDrops(False)
        self.generateButton.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"color: rgb(16, 16, 16);")

        self.verticalLayout.addWidget(self.generateButton)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.mainStackedWidget.addWidget(self.SingleImagePage)
        self.AnimatorPage = QWidget()
        self.AnimatorPage.setObjectName(u"AnimatorPage")
        self.verticalLayout_8 = QVBoxLayout(self.AnimatorPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.AnimatorPage)
        self.label.setObjectName(u"label")
        font9 = QFont()
        font9.setPointSize(30)
        self.label.setFont(font9)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.mainStackedWidget.addWidget(self.AnimatorPage)
        self.vid2vidPage = QWidget()
        self.vid2vidPage.setObjectName(u"vid2vidPage")
        self.verticalLayout_10 = QVBoxLayout(self.vid2vidPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tempLabel = QLabel(self.vid2vidPage)
        self.tempLabel.setObjectName(u"tempLabel")
        font10 = QFont()
        font10.setPointSize(30)
        font10.setBold(False)
        font10.setWeight(50)
        self.tempLabel.setFont(font10)
        self.tempLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.tempLabel)

        self.mainStackedWidget.addWidget(self.vid2vidPage)
        self.InpaintingPage = QWidget()
        self.InpaintingPage.setObjectName(u"InpaintingPage")
        self.mainStackedWidget.addWidget(self.InpaintingPage)

        self.horizontalLayout_15.addWidget(self.mainStackedWidget)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.imagePreview = QLabel(self.centralwidget)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy7)
        self.imagePreview.setMinimumSize(QSize(512, 512))
        self.imagePreview.setMaximumSize(QSize(512, 512))
        self.imagePreview.setPixmap(QPixmap(u"../outputs/txt2img-samples/grid-0018.png"))
        self.imagePreview.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.imagePreview)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.outputFolderLabel = QLabel(self.centralwidget)
        self.outputFolderLabel.setObjectName(u"outputFolderLabel")
        self.outputFolderLabel.setFont(font4)

        self.horizontalLayout_9.addWidget(self.outputFolderLabel)

        self.imageOutputFolderLineEdit = QLineEdit(self.centralwidget)
        self.imageOutputFolderLineEdit.setObjectName(u"imageOutputFolderLineEdit")
        self.imageOutputFolderLineEdit.setMinimumSize(QSize(318, 0))
        self.imageOutputFolderLineEdit.setMaximumSize(QSize(318, 16777215))
        self.imageOutputFolderLineEdit.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.horizontalLayout_9.addWidget(self.imageOutputFolderLineEdit)

        self.imageOutputFolderButton = QPushButton(self.centralwidget)
        self.imageOutputFolderButton.setObjectName(u"imageOutputFolderButton")

        self.horizontalLayout_9.addWidget(self.imageOutputFolderButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1275, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)

        self.imageTabButton.setDefault(False)
        self.AnimatorTabButton.setDefault(False)
        self.vid2vidTabButton.setDefault(False)
        self.inpaintingButton.setDefault(False)
        self.mainStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Diffusion Tools", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(statustip)
        self.action_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Create a new file", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.action_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(statustip)
        self.actionCopy.setStatusTip(QCoreApplication.translate("MainWindow", u"copy a file", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(statustip)
        self.actionPaste.setStatusTip(QCoreApplication.translate("MainWindow", u"paste a file", None))
#endif // QT_CONFIG(statustip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(statustip)
        self.actionSave.setStatusTip(QCoreApplication.translate("MainWindow", u"Save a new file", None))
#endif // QT_CONFIG(statustip)
        self.actionopen_output_folder.setText(QCoreApplication.translate("MainWindow", u"open output folder", None))
#if QT_CONFIG(statustip)
        self.actionopen_output_folder.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.MainName.setText(QCoreApplication.translate("MainWindow", u"DIFFUSION TOOLS", None))
        self.imageTabButton.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.AnimatorTabButton.setText(QCoreApplication.translate("MainWindow", u"Animator", None))
        self.vid2vidTabButton.setText(QCoreApplication.translate("MainWindow", u"vid2vid", None))
        self.inpaintingButton.setText(QCoreApplication.translate("MainWindow", u"Inpainting", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SINGLE IMAGE DIFFUSION", None))
        self.promptLabel.setText(QCoreApplication.translate("MainWindow", u"PROMPT", None))
        self.promptInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Anything you can imagine...", None))
        self.seedLable.setText(QCoreApplication.translate("MainWindow", u"SEED", None))
        self.seedRandomized.setText(QCoreApplication.translate("MainWindow", u"randomize", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WIDTH", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HEIGHT", None))
        self.stepCountLabel.setText(QCoreApplication.translate("MainWindow", u"STEPS", None))
        self.stepsValueBox.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.scaleCountLabel.setText(QCoreApplication.translate("MainWindow", u"CFG SCALE", None))
        self.scaleValueBox.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.imageAmountLabel.setText(QCoreApplication.translate("MainWindow", u"IMAGES", None))
        self.imageCountValueBox.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.img2imgGroup.setTitle(QCoreApplication.translate("MainWindow", u"IMG2IMG", None))
        self.img2imgCheckbox.setText(QCoreApplication.translate("MainWindow", u"ENABLED", None))
        self.img2imgInitPathLineEdit.setText(QCoreApplication.translate("MainWindow", u"ui/preview.png", None))
        self.img2imgChoosefolder.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.strengthLabel.setText(QCoreApplication.translate("MainWindow", u"STRENGTH", None))
        self.strengthValueBox.setText(QCoreApplication.translate("MainWindow", u"70%", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.imagePreview.setText("")
        self.outputFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.imageOutputFolderLineEdit.setText(QCoreApplication.translate("MainWindow", u"Outputs/SingleImage", None))
        self.imageOutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

