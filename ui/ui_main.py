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
        MainWindow.resize(1205, 740)
        MainWindow.setMinimumSize(QSize(1200, 680))
        MainWindow.setStyleSheet(u"background-color: rgb(68, 68, 68);\n"
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 15, -1, -1)
        self.txt2imgButton = QPushButton(self.centralwidget)
        self.txt2imgButton.setObjectName(u"txt2imgButton")
        self.txt2imgButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt2imgButton.sizePolicy().hasHeightForWidth())
        self.txt2imgButton.setSizePolicy(sizePolicy2)
        self.txt2imgButton.setMinimumSize(QSize(100, 84))
        self.txt2imgButton.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setKerning(True)
        self.txt2imgButton.setFont(font1)

        self.verticalLayout_5.addWidget(self.txt2imgButton)

        self.img2imgButton = QPushButton(self.centralwidget)
        self.img2imgButton.setObjectName(u"img2imgButton")
        sizePolicy2.setHeightForWidth(self.img2imgButton.sizePolicy().hasHeightForWidth())
        self.img2imgButton.setSizePolicy(sizePolicy2)
        self.img2imgButton.setMinimumSize(QSize(100, 84))
        self.img2imgButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_5.addWidget(self.img2imgButton)

        self.vid2vidButton = QPushButton(self.centralwidget)
        self.vid2vidButton.setObjectName(u"vid2vidButton")
        sizePolicy2.setHeightForWidth(self.vid2vidButton.sizePolicy().hasHeightForWidth())
        self.vid2vidButton.setSizePolicy(sizePolicy2)
        self.vid2vidButton.setMinimumSize(QSize(100, 84))
        self.vid2vidButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_5.addWidget(self.vid2vidButton)

        self.txt2animButton = QPushButton(self.centralwidget)
        self.txt2animButton.setObjectName(u"txt2animButton")
        sizePolicy2.setHeightForWidth(self.txt2animButton.sizePolicy().hasHeightForWidth())
        self.txt2animButton.setSizePolicy(sizePolicy2)
        self.txt2animButton.setMinimumSize(QSize(100, 84))
        self.txt2animButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_5.addWidget(self.txt2animButton)

        self.inpaintingButton = QPushButton(self.centralwidget)
        self.inpaintingButton.setObjectName(u"inpaintingButton")
        sizePolicy2.setHeightForWidth(self.inpaintingButton.sizePolicy().hasHeightForWidth())
        self.inpaintingButton.setSizePolicy(sizePolicy2)
        self.inpaintingButton.setMinimumSize(QSize(100, 84))
        self.inpaintingButton.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_5.addWidget(self.inpaintingButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 15, 30, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(18)
        self.label_2.setFont(font2)

        self.verticalLayout.addWidget(self.label_2)

        self.promptLabel = QLabel(self.centralwidget)
        self.promptLabel.setObjectName(u"promptLabel")
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setMinimumSize(QSize(600, 0))
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.promptLabel.setFont(font3)

        self.verticalLayout.addWidget(self.promptLabel)

        self.promptInput = QTextEdit(self.centralwidget)
        self.promptInput.setObjectName(u"promptInput")
        sizePolicy.setHeightForWidth(self.promptInput.sizePolicy().hasHeightForWidth())
        self.promptInput.setSizePolicy(sizePolicy)
        self.promptInput.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(12)
        self.promptInput.setFont(font4)
        self.promptInput.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")
        self.promptInput.setFrameShape(QFrame.StyledPanel)
        self.promptInput.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.promptInput)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.seedLable = QLabel(self.centralwidget)
        self.seedLable.setObjectName(u"seedLable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.seedLable.sizePolicy().hasHeightForWidth())
        self.seedLable.setSizePolicy(sizePolicy3)
        self.seedLable.setMaximumSize(QSize(16777215, 20))
        self.seedLable.setFont(font3)

        self.horizontalLayout_2.addWidget(self.seedLable)

        self.seedInputBox = QLineEdit(self.centralwidget)
        self.seedInputBox.setObjectName(u"seedInputBox")
        sizePolicy3.setHeightForWidth(self.seedInputBox.sizePolicy().hasHeightForWidth())
        self.seedInputBox.setSizePolicy(sizePolicy3)
        self.seedInputBox.setMaximumSize(QSize(16777215, 20))
        font5 = QFont()
        font5.setPointSize(10)
        self.seedInputBox.setFont(font5)
        self.seedInputBox.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.horizontalLayout_2.addWidget(self.seedInputBox)

        self.seedRandomized = QCheckBox(self.centralwidget)
        self.seedRandomized.setObjectName(u"seedRandomized")
        sizePolicy3.setHeightForWidth(self.seedRandomized.sizePolicy().hasHeightForWidth())
        self.seedRandomized.setSizePolicy(sizePolicy3)
        self.seedRandomized.setMaximumSize(QSize(16777215, 20))
        self.seedRandomized.setFont(font3)
        self.seedRandomized.setChecked(True)

        self.horizontalLayout_2.addWidget(self.seedRandomized)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.widthInput = QSpinBox(self.centralwidget)
        self.widthInput.setObjectName(u"widthInput")
        self.widthInput.setMinimum(64)
        self.widthInput.setMaximum(1024)
        self.widthInput.setSingleStep(64)
        self.widthInput.setValue(512)

        self.horizontalLayout_3.addWidget(self.widthInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.heightInput = QSpinBox(self.centralwidget)
        self.heightInput.setObjectName(u"heightInput")
        self.heightInput.setMinimum(64)
        self.heightInput.setMaximum(1024)
        self.heightInput.setValue(512)

        self.horizontalLayout_3.addWidget(self.heightInput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stepCountLabel = QLabel(self.centralwidget)
        self.stepCountLabel.setObjectName(u"stepCountLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stepCountLabel.sizePolicy().hasHeightForWidth())
        self.stepCountLabel.setSizePolicy(sizePolicy5)
        self.stepCountLabel.setMinimumSize(QSize(0, 20))
        self.stepCountLabel.setMaximumSize(QSize(75, 16777215))
        self.stepCountLabel.setFont(font3)

        self.horizontalLayout_4.addWidget(self.stepCountLabel)

        self.stepSlider = QSlider(self.centralwidget)
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

        self.stepsValueBox = QLineEdit(self.centralwidget)
        self.stepsValueBox.setObjectName(u"stepsValueBox")
        sizePolicy3.setHeightForWidth(self.stepsValueBox.sizePolicy().hasHeightForWidth())
        self.stepsValueBox.setSizePolicy(sizePolicy3)
        self.stepsValueBox.setMaximumSize(QSize(30, 16777215))
        self.stepsValueBox.setFont(font5)
        self.stepsValueBox.setFrame(False)
        self.stepsValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.stepsValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scaleCountLabel = QLabel(self.centralwidget)
        self.scaleCountLabel.setObjectName(u"scaleCountLabel")
        sizePolicy5.setHeightForWidth(self.scaleCountLabel.sizePolicy().hasHeightForWidth())
        self.scaleCountLabel.setSizePolicy(sizePolicy5)
        self.scaleCountLabel.setMinimumSize(QSize(0, 20))
        self.scaleCountLabel.setMaximumSize(QSize(75, 16777215))
        self.scaleCountLabel.setBaseSize(QSize(0, 0))
        font6 = QFont()
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setWeight(75)
        self.scaleCountLabel.setFont(font6)

        self.horizontalLayout_5.addWidget(self.scaleCountLabel)

        self.scaleSlider = QSlider(self.centralwidget)
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

        self.scaleValueBox = QLineEdit(self.centralwidget)
        self.scaleValueBox.setObjectName(u"scaleValueBox")
        self.scaleValueBox.setMaximumSize(QSize(30, 16777215))
        self.scaleValueBox.setFont(font5)
        self.scaleValueBox.setFrame(False)
        self.scaleValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.scaleValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.imageAmountLabel = QLabel(self.centralwidget)
        self.imageAmountLabel.setObjectName(u"imageAmountLabel")
        sizePolicy5.setHeightForWidth(self.imageAmountLabel.sizePolicy().hasHeightForWidth())
        self.imageAmountLabel.setSizePolicy(sizePolicy5)
        self.imageAmountLabel.setMinimumSize(QSize(0, 20))
        self.imageAmountLabel.setMaximumSize(QSize(75, 16777215))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setWeight(75)
        self.imageAmountLabel.setFont(font7)

        self.horizontalLayout_6.addWidget(self.imageAmountLabel)

        self.imageCountSlider = QSlider(self.centralwidget)
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

        self.imageCountValueBox = QLineEdit(self.centralwidget)
        self.imageCountValueBox.setObjectName(u"imageCountValueBox")
        self.imageCountValueBox.setMaximumSize(QSize(30, 16777215))
        self.imageCountValueBox.setFont(font5)
        self.imageCountValueBox.setFrame(False)
        self.imageCountValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.imageCountValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.iterationLabel = QLabel(self.centralwidget)
        self.iterationLabel.setObjectName(u"iterationLabel")
        self.iterationLabel.setMaximumSize(QSize(75, 16777215))
        self.iterationLabel.setFont(font3)

        self.horizontalLayout_8.addWidget(self.iterationLabel)

        self.iterationsSlider = QSlider(self.centralwidget)
        self.iterationsSlider.setObjectName(u"iterationsSlider")
        self.iterationsSlider.setMinimum(1)
        self.iterationsSlider.setMaximum(10)
        self.iterationsSlider.setPageStep(1)
        self.iterationsSlider.setValue(2)
        self.iterationsSlider.setOrientation(Qt.Horizontal)
        self.iterationsSlider.setTickPosition(QSlider.TicksAbove)
        self.iterationsSlider.setTickInterval(1)

        self.horizontalLayout_8.addWidget(self.iterationsSlider)

        self.iterationsValueBox = QLineEdit(self.centralwidget)
        self.iterationsValueBox.setObjectName(u"iterationsValueBox")
        self.iterationsValueBox.setMaximumSize(QSize(30, 16777215))
        self.iterationsValueBox.setFont(font5)
        self.iterationsValueBox.setFrame(False)
        self.iterationsValueBox.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.iterationsValueBox)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy6)
        self.generateButton.setAcceptDrops(False)
        self.generateButton.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"color: rgb(16, 16, 16);")

        self.verticalLayout.addWidget(self.generateButton)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.imagePreview = QLabel(self.centralwidget)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy7)
        self.imagePreview.setMinimumSize(QSize(512, 512))
        self.imagePreview.setMaximumSize(QSize(512, 512))
        self.imagePreview.setPixmap(QPixmap(u"preview.png"))
        self.imagePreview.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.imagePreview)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1205, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionopen_output_folder)

        self.retranslateUi(MainWindow)

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
        self.txt2imgButton.setText(QCoreApplication.translate("MainWindow", u"txt2img", None))
        self.img2imgButton.setText(QCoreApplication.translate("MainWindow", u"img2img", None))
        self.vid2vidButton.setText(QCoreApplication.translate("MainWindow", u"vid2vid", None))
        self.txt2animButton.setText(QCoreApplication.translate("MainWindow", u"txt2anim", None))
        self.inpaintingButton.setText(QCoreApplication.translate("MainWindow", u"Inpainting", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TXT2IMG", None))
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
        self.iterationLabel.setText(QCoreApplication.translate("MainWindow", u"ITERATIONS", None))
        self.iterationsValueBox.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.imagePreview.setText("")
        self.label.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

