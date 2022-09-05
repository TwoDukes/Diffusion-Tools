from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def generateNewPromptBox(self, number):

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.centralwidget.sizePolicy().hasHeightForWidth())

        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ui.imageTabButton.sizePolicy().hasHeightForWidth())



        verticalAnimPromptContainer = QVBoxLayout()
        verticalAnimPromptContainer.setObjectName(f"verticalAnimPromptContainer{number}")
        animLabel1 = QLabel(self.ui.animMainPromptScrollContainer)
        animLabel1.setObjectName(f"animLabel1{number}")
        sizePolicy.setHeightForWidth(animLabel1.sizePolicy().hasHeightForWidth())
        animLabel1.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        animLabel1.setFont(font9)
        animLabel1.setText(f"Prompt #{number}")

        verticalAnimPromptContainer.addWidget(animLabel1)

        animPrompt1 = QLineEdit(self.ui.animMainPromptScrollContainer)
        animPrompt1.setObjectName(f"animPrompt1{number}")
        animPrompt1.setStyleSheet(u"background-color: rgb(218, 218, 218);\n"
"color: rgb(35, 35, 35);")

        verticalAnimPromptContainer.addWidget(animPrompt1)

        animHorizOptionContainter = QHBoxLayout()
        animHorizOptionContainter.setObjectName(f"animHorizOptionContainter{number}")
        animXMotion1 = QDoubleSpinBox(self.ui.animMainPromptScrollContainer)
        animXMotion1.setObjectName(f"animXMotion1{number}")
        sizePolicy2.setHeightForWidth(animXMotion1.sizePolicy().hasHeightForWidth())
        animXMotion1.setSizePolicy(sizePolicy2)
        animXMotion1.setMinimumSize(QSize(120, 0))
        animXMotion1.setMinimum(-99.000000000000000)
        animXMotion1.setSingleStep(0.100000000000000)


        anim2ndOptionLine1 = QFrame(self.ui.animMainPromptScrollContainer)
        anim2ndOptionLine1.setObjectName(f"anim2ndOptionLine1{number}")
        anim2ndOptionLine1.setFrameShape(QFrame.VLine)
        anim2ndOptionLine1.setFrameShadow(QFrame.Sunken)


        animYMotion1 = QDoubleSpinBox(self.ui.animMainPromptScrollContainer)
        animYMotion1.setObjectName(f"animYMotion1{number}")
        sizePolicy2.setHeightForWidth(animYMotion1.sizePolicy().hasHeightForWidth())
        animYMotion1.setSizePolicy(sizePolicy2)
        animYMotion1.setMinimumSize(QSize(120, 0))
        animYMotion1.setMinimum(-99.000000000000000)
        animYMotion1.setSingleStep(0.100000000000000)


        animZoom1 = QDoubleSpinBox(self.ui.animMainPromptScrollContainer)
        animZoom1.setObjectName(f"animZoom1{number}")
        sizePolicy2.setHeightForWidth(animZoom1.sizePolicy().hasHeightForWidth())
        animZoom1.setSizePolicy(sizePolicy2)
        animZoom1.setMinimumSize(QSize(120, 0))
        animZoom1.setMinimum(-99.000000000000000)
        animZoom1.setSingleStep(0.01000000000000)
        animZoom1.setValue(1.000000000000000)


        animRotation1 = QDoubleSpinBox(self.ui.animMainPromptScrollContainer)
        animRotation1.setObjectName(f"animRotation1{number}")
        sizePolicy2.setHeightForWidth(animRotation1.sizePolicy().hasHeightForWidth())
        animRotation1.setSizePolicy(sizePolicy2)
        animRotation1.setMinimumSize(QSize(120, 0))
        animRotation1.setMinimum(-10.000000000000000)
        animRotation1.setMaximum(10.000000000000000)
        animRotation1.setSingleStep(0.100000000000000)


        animFrameCount1 = QSpinBox(self.ui.animMainPromptScrollContainer)
        animFrameCount1.setObjectName(f"animFrameCount1{number}")
        sizePolicy2.setHeightForWidth(animFrameCount1.sizePolicy().hasHeightForWidth())
        animFrameCount1.setSizePolicy(sizePolicy2)
        animFrameCount1.setMinimumSize(QSize(120, 0))
        animFrameCount1.setMaximum(100000)
        animFrameCount1.setSingleStep(5)
        animFrameCount1.setValue(50)


        animStength1 = QDoubleSpinBox(self.ui.animMainPromptScrollContainer)
        animStength1.setObjectName(f"animStength1{number}")
        sizePolicy2.setHeightForWidth(animStength1.sizePolicy().hasHeightForWidth())
        animStength1.setSizePolicy(sizePolicy2)
        animStength1.setMinimumSize(QSize(120, 0))
        font10 = QFont()
        font10.setPointSize(8)
        font10.setBold(False)
        font10.setWeight(50)
        animStength1.setFont(font10)
        animStength1.setMaximum(1.000000000000000)
        animStength1.setSingleStep(0.010000000000000)
        animStength1.setValue(0.400000000000000)


        animOptionHorizSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)


        animOptionLine1 = QFrame(self.ui.animMainPromptScrollContainer)
        animOptionLine1.setObjectName(f"animOptionLine1{number}")
        animOptionLine1.setFrameShape(QFrame.VLine)
        animOptionLine1.setFrameShadow(QFrame.Sunken)

        animStength1.setPrefix(u"Strength: ")
        animFrameCount1.setPrefix(u"Frames: ")
        animZoom1.setPrefix(u"Zoom: ")
        animRotation1.setPrefix(u"Rotation: ")
        animXMotion1.setPrefix(u"X Motion: ")
        animYMotion1.setPrefix(u"Y Motion: ")

        animHorizOptionContainter.addWidget(animStength1)
        animHorizOptionContainter.addWidget(animFrameCount1)
        animHorizOptionContainter.addWidget(animOptionLine1)
        animHorizOptionContainter.addWidget(anim2ndOptionLine1)
        animHorizOptionContainter.addWidget(animZoom1)
        animHorizOptionContainter.addWidget(animRotation1)
        animHorizOptionContainter.addWidget(animXMotion1)
        animHorizOptionContainter.addWidget(animYMotion1)
        animHorizOptionContainter.addItem(animOptionHorizSpacer1)


        verticalAnimPromptContainer.addLayout(animHorizOptionContainter)


        self.ui.AnimatorMainVertLayoutGroup.addLayout(verticalAnimPromptContainer)
