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
        MainWindow.resize(1100, 600)
        MainWindow.setMinimumSize(QSize(1100, 600))
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(60, -1, 60, -1)
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
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.MainName.setFont(font)
        self.MainName.setLayoutDirection(Qt.LeftToRight)
        self.MainName.setAutoFillBackground(False)
        self.MainName.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.MainName)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.promptLabel = QLabel(self.centralwidget)
        self.promptLabel.setObjectName(u"promptLabel")
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.promptLabel)

        self.promptInput = QLineEdit(self.centralwidget)
        self.promptInput.setObjectName(u"promptInput")
        font1 = QFont()
        font1.setPointSize(12)
        self.promptInput.setFont(font1)
        self.promptInput.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")
        self.promptInput.setFrame(True)

        self.verticalLayout.addWidget(self.promptInput)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.seedLable = QLabel(self.centralwidget)
        self.seedLable.setObjectName(u"seedLable")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.seedLable.sizePolicy().hasHeightForWidth())
        self.seedLable.setSizePolicy(sizePolicy2)
        self.seedLable.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.seedLable.setFont(font2)

        self.horizontalLayout_2.addWidget(self.seedLable)

        self.seedInputBox = QLineEdit(self.centralwidget)
        self.seedInputBox.setObjectName(u"seedInputBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.seedInputBox.sizePolicy().hasHeightForWidth())
        self.seedInputBox.setSizePolicy(sizePolicy3)
        self.seedInputBox.setMaximumSize(QSize(16777215, 20))
        self.seedInputBox.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        self.horizontalLayout_2.addWidget(self.seedInputBox)

        self.seedRandomized = QCheckBox(self.centralwidget)
        self.seedRandomized.setObjectName(u"seedRandomized")
        sizePolicy2.setHeightForWidth(self.seedRandomized.sizePolicy().hasHeightForWidth())
        self.seedRandomized.setSizePolicy(sizePolicy2)
        self.seedRandomized.setMaximumSize(QSize(16777215, 20))
        self.seedRandomized.setFont(font2)
        self.seedRandomized.setChecked(True)

        self.horizontalLayout_2.addWidget(self.seedRandomized)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stepCountLabel = QLabel(self.centralwidget)
        self.stepCountLabel.setObjectName(u"stepCountLabel")
        sizePolicy.setHeightForWidth(self.stepCountLabel.sizePolicy().hasHeightForWidth())
        self.stepCountLabel.setSizePolicy(sizePolicy)
        self.stepCountLabel.setMinimumSize(QSize(0, 20))
        self.stepCountLabel.setFont(font2)

        self.verticalLayout.addWidget(self.stepCountLabel)

        self.stepSlider = QSlider(self.centralwidget)
        self.stepSlider.setObjectName(u"stepSlider")
        self.stepSlider.setMaximum(150)
        self.stepSlider.setValue(50)
        self.stepSlider.setOrientation(Qt.Horizontal)
        self.stepSlider.setTickPosition(QSlider.TicksAbove)
        self.stepSlider.setTickInterval(10)

        self.verticalLayout.addWidget(self.stepSlider)

        self.scaleCountLabel = QLabel(self.centralwidget)
        self.scaleCountLabel.setObjectName(u"scaleCountLabel")
        sizePolicy.setHeightForWidth(self.scaleCountLabel.sizePolicy().hasHeightForWidth())
        self.scaleCountLabel.setSizePolicy(sizePolicy)
        self.scaleCountLabel.setMinimumSize(QSize(0, 20))
        self.scaleCountLabel.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.scaleCountLabel.setFont(font3)

        self.verticalLayout.addWidget(self.scaleCountLabel)

        self.scaleSlider = QSlider(self.centralwidget)
        self.scaleSlider.setObjectName(u"scaleSlider")
        self.scaleSlider.setMaximum(20)
        self.scaleSlider.setValue(5)
        self.scaleSlider.setOrientation(Qt.Horizontal)
        self.scaleSlider.setTickPosition(QSlider.TicksAbove)
        self.scaleSlider.setTickInterval(5)

        self.verticalLayout.addWidget(self.scaleSlider)

        self.imageAmountLabel = QLabel(self.centralwidget)
        self.imageAmountLabel.setObjectName(u"imageAmountLabel")
        sizePolicy.setHeightForWidth(self.imageAmountLabel.sizePolicy().hasHeightForWidth())
        self.imageAmountLabel.setSizePolicy(sizePolicy)
        self.imageAmountLabel.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.imageAmountLabel.setFont(font4)

        self.verticalLayout.addWidget(self.imageAmountLabel)

        self.imageCountSlider = QSlider(self.centralwidget)
        self.imageCountSlider.setObjectName(u"imageCountSlider")
        self.imageCountSlider.setMinimum(1)
        self.imageCountSlider.setMaximum(9)
        self.imageCountSlider.setOrientation(Qt.Horizontal)
        self.imageCountSlider.setTickPosition(QSlider.TicksAbove)
        self.imageCountSlider.setTickInterval(1)

        self.verticalLayout.addWidget(self.imageCountSlider)

        self.generateButton = QPushButton(self.centralwidget)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy4)
        self.generateButton.setAcceptDrops(False)
        self.generateButton.setStyleSheet(u"background-color: rgb(216, 216, 216);\n"
"color: rgb(16, 16, 16);")

        self.verticalLayout.addWidget(self.generateButton)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.imagePreview = QLabel(self.centralwidget)
        self.imagePreview.setObjectName(u"imagePreview")
        self.imagePreview.setMaximumSize(QSize(16777215, 16777215))
        self.imagePreview.setPixmap(QPixmap(u"../outputs/txt2img-samples/grid-0049.png"))
        self.imagePreview.setScaledContents(True)

        self.horizontalLayout.addWidget(self.imagePreview)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 26))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.MainName.setText(QCoreApplication.translate("MainWindow", u"SD TOOLS", None))
        self.promptLabel.setText(QCoreApplication.translate("MainWindow", u"PROMPT", None))
        self.seedLable.setText(QCoreApplication.translate("MainWindow", u"SEED", None))
        self.seedRandomized.setText(QCoreApplication.translate("MainWindow", u"randomize", None))
        self.stepCountLabel.setText(QCoreApplication.translate("MainWindow", u"STEP COUNT: 50", None))
        self.scaleCountLabel.setText(QCoreApplication.translate("MainWindow", u"SCALE: 5", None))
        self.imageAmountLabel.setText(QCoreApplication.translate("MainWindow", u"IMAGES: 1", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.generateButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.imagePreview.setText("")
        self.label.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

