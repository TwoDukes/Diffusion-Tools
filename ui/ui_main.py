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
        MainWindow.resize(1670, 900)
        MainWindow.setMinimumSize(QSize(1670, 900))
        icon = QIcon()
        icon.addFile(u"../outputs/SingleImage/samples/00123.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.actionMenuStandard = QAction(MainWindow)
        self.actionMenuStandard.setObjectName(u"actionMenuStandard")
        self.actionMenuStandard.setCheckable(True)
        self.actionMenuStandard.setChecked(True)
        self.actionMenuOptimized = QAction(MainWindow)
        self.actionMenuOptimized.setObjectName(u"actionMenuOptimized")
        self.actionMenuOptimized.setCheckable(True)
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

        self.horizontalSpacer = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.heightInput.setSingleStep(64)
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
        self.animPromptScrollArea = QScrollArea(self.AnimatorPage)
        self.animPromptScrollArea.setObjectName(u"animPromptScrollArea")
        self.animPromptScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.animPromptScrollArea.setWidgetResizable(True)
        self.animMainPromptScrollContainer = QWidget()
        self.animMainPromptScrollContainer.setObjectName(u"animMainPromptScrollContainer")
        self.animMainPromptScrollContainer.setGeometry(QRect(0, 0, 943, 736))
        self.animPromptContainterLayoutGroup = QVBoxLayout(self.animMainPromptScrollContainer)
        self.animPromptContainterLayoutGroup.setObjectName(u"animPromptContainterLayoutGroup")
        self.label = QLabel(self.animMainPromptScrollContainer)
        self.label.setObjectName(u"label")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy7)
        self.label.setFont(font3)

        self.animPromptContainterLayoutGroup.addWidget(self.label)

        self.AnimatorMainVertLayoutGroup = QVBoxLayout()
        self.AnimatorMainVertLayoutGroup.setObjectName(u"AnimatorMainVertLayoutGroup")
        self.verticalAnimPromptContainer = QVBoxLayout()
        self.verticalAnimPromptContainer.setObjectName(u"verticalAnimPromptContainer")
        self.animLabel1 = QLabel(self.animMainPromptScrollContainer)
        self.animLabel1.setObjectName(u"animLabel1")
        sizePolicy.setHeightForWidth(self.animLabel1.sizePolicy().hasHeightForWidth())
        self.animLabel1.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.animLabel1.setFont(font9)

        self.verticalAnimPromptContainer.addWidget(self.animLabel1)

        self.animPrompt1 = QLineEdit(self.animMainPromptScrollContainer)
        self.animPrompt1.setObjectName(u"animPrompt1")
        self.animPrompt1.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.verticalAnimPromptContainer.addWidget(self.animPrompt1)

        self.animHorizOptionContainter = QHBoxLayout()
        self.animHorizOptionContainter.setObjectName(u"animHorizOptionContainter")
        self.animStength1 = QDoubleSpinBox(self.animMainPromptScrollContainer)
        self.animStength1.setObjectName(u"animStength1")
        sizePolicy2.setHeightForWidth(self.animStength1.sizePolicy().hasHeightForWidth())
        self.animStength1.setSizePolicy(sizePolicy2)
        self.animStength1.setMinimumSize(QSize(120, 0))
        font10 = QFont()
        font10.setPointSize(8)
        font10.setBold(False)
        font10.setWeight(50)
        self.animStength1.setFont(font10)
        self.animStength1.setMaximum(1.000000000000000)
        self.animStength1.setSingleStep(0.010000000000000)
        self.animStength1.setValue(0.400000000000000)

        self.animHorizOptionContainter.addWidget(self.animStength1)

        self.animFrameCount1 = QSpinBox(self.animMainPromptScrollContainer)
        self.animFrameCount1.setObjectName(u"animFrameCount1")
        sizePolicy2.setHeightForWidth(self.animFrameCount1.sizePolicy().hasHeightForWidth())
        self.animFrameCount1.setSizePolicy(sizePolicy2)
        self.animFrameCount1.setMinimumSize(QSize(120, 0))
        self.animFrameCount1.setMaximum(100000)
        self.animFrameCount1.setSingleStep(5)
        self.animFrameCount1.setValue(50)

        self.animHorizOptionContainter.addWidget(self.animFrameCount1)

        self.anim2ndOptionLine1 = QFrame(self.animMainPromptScrollContainer)
        self.anim2ndOptionLine1.setObjectName(u"anim2ndOptionLine1")
        self.anim2ndOptionLine1.setFrameShape(QFrame.VLine)
        self.anim2ndOptionLine1.setFrameShadow(QFrame.Sunken)

        self.animHorizOptionContainter.addWidget(self.anim2ndOptionLine1)

        self.animOptionLine1 = QFrame(self.animMainPromptScrollContainer)
        self.animOptionLine1.setObjectName(u"animOptionLine1")
        self.animOptionLine1.setFrameShape(QFrame.VLine)
        self.animOptionLine1.setFrameShadow(QFrame.Sunken)

        self.animHorizOptionContainter.addWidget(self.animOptionLine1)

        self.animZoom1 = QDoubleSpinBox(self.animMainPromptScrollContainer)
        self.animZoom1.setObjectName(u"animZoom1")
        sizePolicy2.setHeightForWidth(self.animZoom1.sizePolicy().hasHeightForWidth())
        self.animZoom1.setSizePolicy(sizePolicy2)
        self.animZoom1.setMinimumSize(QSize(120, 0))
        self.animZoom1.setMinimum(-99.000000000000000)
        self.animZoom1.setSingleStep(0.010000000000000)
        self.animZoom1.setValue(1.000000000000000)

        self.animHorizOptionContainter.addWidget(self.animZoom1)

        self.animRotation1 = QDoubleSpinBox(self.animMainPromptScrollContainer)
        self.animRotation1.setObjectName(u"animRotation1")
        sizePolicy2.setHeightForWidth(self.animRotation1.sizePolicy().hasHeightForWidth())
        self.animRotation1.setSizePolicy(sizePolicy2)
        self.animRotation1.setMinimumSize(QSize(120, 0))
        self.animRotation1.setMinimum(-10.000000000000000)
        self.animRotation1.setMaximum(10.000000000000000)
        self.animRotation1.setSingleStep(0.100000000000000)

        self.animHorizOptionContainter.addWidget(self.animRotation1)

        self.animXMotion1 = QDoubleSpinBox(self.animMainPromptScrollContainer)
        self.animXMotion1.setObjectName(u"animXMotion1")
        sizePolicy2.setHeightForWidth(self.animXMotion1.sizePolicy().hasHeightForWidth())
        self.animXMotion1.setSizePolicy(sizePolicy2)
        self.animXMotion1.setMinimumSize(QSize(120, 0))
        self.animXMotion1.setMinimum(-99.000000000000000)
        self.animXMotion1.setSingleStep(0.100000000000000)

        self.animHorizOptionContainter.addWidget(self.animXMotion1)

        self.animYMotion1 = QDoubleSpinBox(self.animMainPromptScrollContainer)
        self.animYMotion1.setObjectName(u"animYMotion1")
        sizePolicy2.setHeightForWidth(self.animYMotion1.sizePolicy().hasHeightForWidth())
        self.animYMotion1.setSizePolicy(sizePolicy2)
        self.animYMotion1.setMinimumSize(QSize(120, 0))
        self.animYMotion1.setMinimum(-99.000000000000000)
        self.animYMotion1.setSingleStep(0.100000000000000)

        self.animHorizOptionContainter.addWidget(self.animYMotion1)

        self.animOptionHorizSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.animHorizOptionContainter.addItem(self.animOptionHorizSpacer1)


        self.verticalAnimPromptContainer.addLayout(self.animHorizOptionContainter)


        self.AnimatorMainVertLayoutGroup.addLayout(self.verticalAnimPromptContainer)


        self.animPromptContainterLayoutGroup.addLayout(self.AnimatorMainVertLayoutGroup)

        self.animRemovePromptButton = QPushButton(self.animMainPromptScrollContainer)
        self.animRemovePromptButton.setObjectName(u"animRemovePromptButton")
        self.animRemovePromptButton.setFont(font9)

        self.animPromptContainterLayoutGroup.addWidget(self.animRemovePromptButton)

        self.animNewPromptButton = QPushButton(self.animMainPromptScrollContainer)
        self.animNewPromptButton.setObjectName(u"animNewPromptButton")
        self.animNewPromptButton.setFont(font9)

        self.animPromptContainterLayoutGroup.addWidget(self.animNewPromptButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.animPromptContainterLayoutGroup.addItem(self.verticalSpacer_4)

        self.animPromptScrollArea.setWidget(self.animMainPromptScrollContainer)

        self.verticalLayout_8.addWidget(self.animPromptScrollArea)

        self.mainStackedWidget.addWidget(self.AnimatorPage)
        self.vid2vidPage = QWidget()
        self.vid2vidPage.setObjectName(u"vid2vidPage")
        self.verticalLayout_10 = QVBoxLayout(self.vid2vidPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tempLabel = QLabel(self.vid2vidPage)
        self.tempLabel.setObjectName(u"tempLabel")
        font11 = QFont()
        font11.setPointSize(30)
        font11.setBold(False)
        font11.setWeight(50)
        self.tempLabel.setFont(font11)
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
        sizePolicy4.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy4)
        self.imagePreview.setMinimumSize(QSize(512, 512))
        self.imagePreview.setMaximumSize(QSize(512, 512))
        self.imagePreview.setPixmap(QPixmap(u"../../../../.designer/outputs/txt2img-samples/grid-0018.png"))
        self.imagePreview.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.imagePreview)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.outputFolderLabel = QLabel(self.centralwidget)
        self.outputFolderLabel.setObjectName(u"outputFolderLabel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.outputFolderLabel.sizePolicy().hasHeightForWidth())
        self.outputFolderLabel.setSizePolicy(sizePolicy8)
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
        sizePolicy5.setHeightForWidth(self.imageOutputFolderButton.sizePolicy().hasHeightForWidth())
        self.imageOutputFolderButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_9.addWidget(self.imageOutputFolderButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.SecondaryStackedWidget = QStackedWidget(self.centralwidget)
        self.SecondaryStackedWidget.setObjectName(u"SecondaryStackedWidget")
        sizePolicy1.setHeightForWidth(self.SecondaryStackedWidget.sizePolicy().hasHeightForWidth())
        self.SecondaryStackedWidget.setSizePolicy(sizePolicy1)
        self.SingleImage = QWidget()
        self.SingleImage.setObjectName(u"SingleImage")
        self.SecondaryStackedWidget.addWidget(self.SingleImage)
        self.Animator = QWidget()
        self.Animator.setObjectName(u"Animator")
        self.verticalLayout_12 = QVBoxLayout(self.Animator)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.animInitPathLineEdit = QLineEdit(self.Animator)
        self.animInitPathLineEdit.setObjectName(u"animInitPathLineEdit")
        self.animInitPathLineEdit.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.horizontalLayout_19.addWidget(self.animInitPathLineEdit)

        self.animInitChooseFileButton = QPushButton(self.Animator)
        self.animInitChooseFileButton.setObjectName(u"animInitChooseFileButton")

        self.horizontalLayout_19.addWidget(self.animInitChooseFileButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.animStepsSpinBox = QDoubleSpinBox(self.Animator)
        self.animStepsSpinBox.setObjectName(u"animStepsSpinBox")
        self.animStepsSpinBox.setMaximum(200.000000000000000)
        self.animStepsSpinBox.setSingleStep(5.000000000000000)
        self.animStepsSpinBox.setValue(50.000000000000000)

        self.horizontalLayout_11.addWidget(self.animStepsSpinBox)

        self.animScaleSpinBox = QDoubleSpinBox(self.Animator)
        self.animScaleSpinBox.setObjectName(u"animScaleSpinBox")
        self.animScaleSpinBox.setMinimum(-99.000000000000000)
        self.animScaleSpinBox.setValue(7.000000000000000)

        self.horizontalLayout_11.addWidget(self.animScaleSpinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.startAnimationButton = QPushButton(self.Animator)
        self.startAnimationButton.setObjectName(u"startAnimationButton")
        self.startAnimationButton.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"color: rgb(16, 16, 16);")

        self.horizontalLayout_7.addWidget(self.startAnimationButton)

        self.stopAnimationButton = QPushButton(self.Animator)
        self.stopAnimationButton.setObjectName(u"stopAnimationButton")
        self.stopAnimationButton.setStyleSheet(u"background-color: rgb(255, 42, 42);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.stopAnimationButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.animCompletionProgressBar = QProgressBar(self.Animator)
        self.animCompletionProgressBar.setObjectName(u"animCompletionProgressBar")
        self.animCompletionProgressBar.setEnabled(True)
        self.animCompletionProgressBar.setValue(0)
        self.animCompletionProgressBar.setTextVisible(False)
        self.animCompletionProgressBar.setOrientation(Qt.Horizontal)
        self.animCompletionProgressBar.setInvertedAppearance(False)
        self.animCompletionProgressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_12.addWidget(self.animCompletionProgressBar)

        self.SecondaryStackedWidget.addWidget(self.Animator)

        self.verticalLayout_6.addWidget(self.SecondaryStackedWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1670, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuperformance = QMenu(self.menuMenu)
        self.menuperformance.setObjectName(u"menuperformance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.menuperformance.menuAction())
        self.menuperformance.addAction(self.actionMenuStandard)
        self.menuperformance.addAction(self.actionMenuOptimized)

        self.retranslateUi(MainWindow)

        self.imageTabButton.setDefault(False)
        self.AnimatorTabButton.setDefault(False)
        self.vid2vidTabButton.setDefault(False)
        self.inpaintingButton.setDefault(False)
        self.mainStackedWidget.setCurrentIndex(1)
        self.SecondaryStackedWidget.setCurrentIndex(1)


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
        self.actionMenuStandard.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.actionMenuOptimized.setText(QCoreApplication.translate("MainWindow", u"Optimized", None))
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
        self.img2imgChoosefolder.setText(QCoreApplication.translate("MainWindow", u"Choose Image", None))
        self.strengthLabel.setText(QCoreApplication.translate("MainWindow", u"STRENGTH", None))
        self.strengthValueBox.setText(QCoreApplication.translate("MainWindow", u"70%", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"ANIMATOR", None))
        self.animLabel1.setText(QCoreApplication.translate("MainWindow", u"Prompt #1", None))
        self.animStength1.setSpecialValueText("")
        self.animStength1.setPrefix(QCoreApplication.translate("MainWindow", u"Strength: ", None))
        self.animFrameCount1.setSuffix("")
        self.animFrameCount1.setPrefix(QCoreApplication.translate("MainWindow", u"Frames: ", None))
        self.animZoom1.setPrefix(QCoreApplication.translate("MainWindow", u"Zoom: ", None))
        self.animZoom1.setSuffix("")
        self.animRotation1.setPrefix(QCoreApplication.translate("MainWindow", u"Rotation: ", None))
        self.animXMotion1.setPrefix(QCoreApplication.translate("MainWindow", u"X Motion:", None))
        self.animYMotion1.setPrefix(QCoreApplication.translate("MainWindow", u"Y Motion: ", None))
        self.animRemovePromptButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.animNewPromptButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"COMING SOON", None))
        self.imagePreview.setText("")
        self.outputFolderLabel.setText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.imageOutputFolderLineEdit.setText(QCoreApplication.translate("MainWindow", u"Outputs/SingleImage", None))
        self.imageOutputFolderButton.setText(QCoreApplication.translate("MainWindow", u"Choose Folder", None))
        self.animInitPathLineEdit.setText(QCoreApplication.translate("MainWindow", u"ui/preview.png", None))
        self.animInitChooseFileButton.setText(QCoreApplication.translate("MainWindow", u"Choose Image", None))
        self.animStepsSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"STEPS: ", None))
        self.animScaleSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"CFG SCALE: ", None))
        self.startAnimationButton.setText(QCoreApplication.translate("MainWindow", u"START ANIMATION", None))
        self.stopAnimationButton.setText(QCoreApplication.translate("MainWindow", u"STOP ANIMATION", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(statustip)
        self.menuperformance.setStatusTip(QCoreApplication.translate("MainWindow", u"Choose setting for your hardware", None))
#endif // QT_CONFIG(statustip)
        self.menuperformance.setTitle(QCoreApplication.translate("MainWindow", u"Performance", None))
    # retranslateUi

