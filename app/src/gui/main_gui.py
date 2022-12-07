# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_interfaceIEdsgH.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import gui.res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 610)
        MainWindow.setStyleSheet(u"*{\n"
                                 "  border: none;\n"
                                 "  background-color: transparent;\n"
                                 "  background: transparent;\n"
                                 "  padding: 0;\n"
                                 "  margin: 0;\n"
                                 "  color: #fff;\n"
                                 " }\n"
                                 "#centralwidget{\n"
                                 "  background-color: #aedbf0;\n"
                                 "}\n"
                                 "#leftMenuSubCont{\n"
                                 "  background-color: #2859A6;\n"
                                 "}\n"
                                 "#leftMenuSubCont QPushButton{\n"
                                 "  text-align: left;\n"
                                 "  padding: 4px 9px;\n"
                                 "}\n"
                                 "#leftPopMenuSubCont{\n"
                                 "  background-color: #567AC5;\n"
                                 "   padding: 0;\n"
                                 "  margin: 0;\n"
                                 "}\n"
                                 "#frame_4{\n"
                                 "  background-color: #567AC5;\n"
                                 "  border-top-right-radius: 8px;\n"
                                 "  border-bottom-right-radius: 8px;\n"
                                 "}\n"
                                 "#frame_7{\n"
                                 "  background-color: #16191d;\n"
                                 "  border-radius: 4px;\n"
                                 "  color: #fff;\n"
                                 "}\n"
                                 "#headerCont{\n"
                                 "  background-color: #2859A6;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuCont = QCustomSlideMenu(self.centralwidget)
        self.leftMenuCont.setObjectName(u"leftMenuCont")
        self.leftMenuCont.setMaximumSize(QSize(48, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuCont)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubCont = QWidget(self.leftMenuCont)
        self.leftMenuSubCont.setObjectName(u"leftMenuSubCont")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubCont)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.frame = QFrame(self.leftMenuSubCont)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame)
        self.menuButton.setObjectName(u"menuButton")
        icon = QIcon()
        icon.addFile(u":/icons/align-justify.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.menuButton)

        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubCont)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeButton = QPushButton(self.frame_2)
        self.homeButton.setObjectName(u"homeButton")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.homeButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.homeButton)

        self.trainButton = QPushButton(self.frame_2)
        self.trainButton.setObjectName(u"trainButton")
        font1 = QFont()
        font1.setPointSize(11)
        self.trainButton.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.trainButton.setIcon(icon2)
        self.trainButton.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.trainButton)

        self.systemTempButton = QPushButton(self.frame_2)
        self.systemTempButton.setObjectName(u"systemTempButton")
        self.systemTempButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/thermometer.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.systemTempButton.setIcon(icon3)
        self.systemTempButton.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.systemTempButton)

        self.resultsButton = QPushButton(self.frame_2)
        self.resultsButton.setObjectName(u"resultsButton")
        self.resultsButton.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/monitor.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.resultsButton.setIcon(icon4)
        self.resultsButton.setIconSize(QSize(28, 28))

        self.verticalLayout_3.addWidget(self.resultsButton)

        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubCont)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsButton = QPushButton(self.frame_3)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon5)
        self.settingsButton.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.logoutButton = QPushButton(self.frame_3)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutButton.setIcon(icon6)
        self.logoutButton.setIconSize(QSize(28, 28))

        self.verticalLayout_4.addWidget(self.logoutButton)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.verticalLayout.addWidget(self.leftMenuSubCont)

        self.horizontalLayout.addWidget(self.leftMenuCont, 0, Qt.AlignLeft)

        self.leftPopMenuCont = QCustomSlideMenu(self.centralwidget)
        self.leftPopMenuCont.setObjectName(u"leftPopMenuCont")
        self.leftPopMenuCont.setMinimumSize(QSize(170, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.leftPopMenuCont)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.leftPopMenuSubCont = QWidget(self.leftPopMenuCont)
        self.leftPopMenuSubCont.setObjectName(u"leftPopMenuSubCont")
        sizePolicy.setHeightForWidth(
            self.leftPopMenuSubCont.sizePolicy().hasHeightForWidth())
        self.leftPopMenuSubCont.setSizePolicy(sizePolicy)
        self.leftPopMenuSubCont.setMinimumSize(QSize(170, 0))
        self.verticalLayout_6 = QVBoxLayout(self.leftPopMenuSubCont)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.leftPopMenuSubCont)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.hidePopMenuButton = QPushButton(self.frame_4)
        self.hidePopMenuButton.setObjectName(u"hidePopMenuButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/arrow-left-circle.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.hidePopMenuButton.setIcon(icon7)
        self.hidePopMenuButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(
            self.hidePopMenuButton, 0, Qt.AlignRight)

        self.verticalLayout_6.addWidget(self.frame_4)

        self.popMenuPages = QCustomStackedWidget(self.leftPopMenuSubCont)
        self.popMenuPages.setObjectName(u"popMenuPages")
        self.popSettingsPage = QWidget()
        self.popSettingsPage.setObjectName(u"popSettingsPage")
        self.verticalLayout_8 = QVBoxLayout(self.popSettingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.popSettingsPage)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.popMenuPages.addWidget(self.popSettingsPage)
        self.popTrainPage = QWidget()
        self.popTrainPage.setObjectName(u"popTrainPage")
        self.verticalLayout_10 = QVBoxLayout(self.popTrainPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.popTrainPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.popMenuPages.addWidget(self.popTrainPage)
        self.popSystemPage = QWidget()
        self.popSystemPage.setObjectName(u"popSystemPage")
        self.verticalLayout_9 = QVBoxLayout(self.popSystemPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.popSystemPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.popMenuPages.addWidget(self.popSystemPage)
        self.popResultsPage = QWidget()
        self.popResultsPage.setObjectName(u"popResultsPage")
        self.verticalLayout_7 = QVBoxLayout(self.popResultsPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.popResultsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.popMenuPages.addWidget(self.popResultsPage)

        self.verticalLayout_6.addWidget(self.popMenuPages)

        self.horizontalLayout_4.addWidget(self.leftPopMenuSubCont)

        self.horizontalLayout.addWidget(self.leftPopMenuCont, 0, Qt.AlignLeft)

        self.mainBodyCont = QWidget(self.centralwidget)
        self.mainBodyCont.setObjectName(u"mainBodyCont")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.mainBodyCont.sizePolicy().hasHeightForWidth())
        self.mainBodyCont.setSizePolicy(sizePolicy1)
        self.mainBodyCont.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyCont)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.headerCont = QWidget(self.mainBodyCont)
        self.headerCont.setObjectName(u"headerCont")
        self.horizontalLayout_5 = QHBoxLayout(self.headerCont)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.headerCont)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.alertButton = QPushButton(self.frame_5)
        self.alertButton.setObjectName(u"alertButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.alertButton.sizePolicy().hasHeightForWidth())
        self.alertButton.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alertButton.setIcon(icon8)
        self.alertButton.setIconSize(QSize(28, 28))

        self.horizontalLayout_7.addWidget(self.alertButton)

        self.horizontalLayout_5.addWidget(
            self.frame_5, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.frame_6 = QFrame(self.headerCont)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.minBtn = QPushButton(self.frame_6)
        self.minBtn.setObjectName(u"minBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon9)
        self.minBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.minBtn)

        self.restoreBtn = QPushButton(self.frame_6)
        self.restoreBtn.setObjectName(u"restoreBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon10)
        self.restoreBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_6)
        self.closeBtn.setObjectName(u"closeBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon11)
        self.closeBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout_6.addWidget(self.closeBtn)

        self.horizontalLayout_5.addWidget(
            self.frame_6, 0, Qt.AlignRight | Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.headerCont, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyCont)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy3)
        self.verticalLayout_11 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.mainContentsCont = QWidget(self.mainBodyContent)
        self.mainContentsCont.setObjectName(u"mainContentsCont")
        self.verticalLayout_12 = QVBoxLayout(self.mainContentsCont)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainContentsCont)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_14 = QVBoxLayout(self.homePage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.label_6 = QLabel(self.homePage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_14.addWidget(self.label_6)

        self.mainPages.addWidget(self.homePage)
        self.trainPage = QWidget()
        self.trainPage.setObjectName(u"trainPage")
        self.verticalLayout_16 = QVBoxLayout(self.trainPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_7 = QLabel(self.trainPage)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_16.addWidget(self.label_7)

        self.mainPages.addWidget(self.trainPage)
        self.systemPage = QWidget()
        self.systemPage.setObjectName(u"systemPage")
        self.verticalLayout_17 = QVBoxLayout(self.systemPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_8 = QLabel(self.systemPage)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_17.addWidget(self.label_8)

        self.mainPages.addWidget(self.systemPage)
        self.resultsPage = QWidget()
        self.resultsPage.setObjectName(u"resultsPage")
        self.verticalLayout_18 = QVBoxLayout(self.resultsPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_9 = QLabel(self.resultsPage)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_18.addWidget(self.label_9)

        self.mainPages.addWidget(self.resultsPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_15 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_10 = QLabel(self.settingsPage)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_15.addWidget(self.label_10)

        self.mainPages.addWidget(self.settingsPage)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_13 = QVBoxLayout(self.page_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.page_10)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.mainPages.addWidget(self.page_10)

        self.verticalLayout_12.addWidget(self.mainPages)

        self.verticalLayout_11.addWidget(self.mainContentsCont)

        self.popupCont = QCustomSlideMenu(self.mainBodyContent)
        self.popupCont.setObjectName(u"popupCont")
        self.verticalLayout_20 = QVBoxLayout(self.popupCont)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.popupSubCont = QWidget(self.popupCont)
        self.popupSubCont.setObjectName(u"popupSubCont")
        self.verticalLayout_19 = QVBoxLayout(self.popupSubCont)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.frame_7 = QFrame(self.popupSubCont)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(
            self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(16777215, 500))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(
            self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(
            self.label_12, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.closeAlertButton = QPushButton(self.frame_7)
        self.closeAlertButton.setObjectName(u"closeAlertButton")
        icon12 = QIcon()
        icon12.addFile(u":/icons/x-square.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.closeAlertButton.setIcon(icon12)
        self.closeAlertButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(
            self.closeAlertButton, 0, Qt.AlignRight | Qt.AlignTop)

        self.verticalLayout_19.addWidget(self.frame_7)

        self.verticalLayout_20.addWidget(self.popupSubCont)

        self.verticalLayout_11.addWidget(self.popupCont)

        self.verticalLayout_5.addWidget(self.mainBodyContent)

        self.footerCont = QWidget(self.mainBodyCont)
        self.footerCont.setObjectName(u"footerCont")
        self.footerCont.setMinimumSize(QSize(0, 25))
        self.footerCont.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_9 = QHBoxLayout(self.footerCont)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.sizeGrip = QFrame(self.footerCont)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(25, 25))
        self.sizeGrip.setMaximumSize(QSize(25, 25))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.sizeGrip)

        self.verticalLayout_5.addWidget(
            self.footerCont, 0, Qt.AlignRight | Qt.AlignBottom)

        self.horizontalLayout.addWidget(self.mainBodyCont)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
# if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuButton.setText("")
# if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText(
            QCoreApplication.translate("MainWindow", u"Home", None))
# if QT_CONFIG(tooltip)
        self.trainButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Train", None))
#endif // QT_CONFIG(tooltip)
        self.trainButton.setText(
            QCoreApplication.translate("MainWindow", u"Train", None))
# if QT_CONFIG(tooltip)
        self.systemTempButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"System status", None))
#endif // QT_CONFIG(tooltip)
        self.systemTempButton.setText(
            QCoreApplication.translate("MainWindow", u"Loads", None))
# if QT_CONFIG(tooltip)
        self.resultsButton.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Monitor results", None))
#endif // QT_CONFIG(tooltip)
        self.resultsButton.setText(
            QCoreApplication.translate("MainWindow", u"Results", None))
# if QT_CONFIG(tooltip)
        self.settingsButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsButton.setText(
            QCoreApplication.translate("MainWindow", u"Settings", None))
# if QT_CONFIG(tooltip)
        self.logoutButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Logout", None))
#endif // QT_CONFIG(tooltip)
        self.logoutButton.setText(
            QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Menu", None))
# if QT_CONFIG(tooltip)
        self.hidePopMenuButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close menu", None))
#endif // QT_CONFIG(tooltip)
        self.hidePopMenuButton.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Train", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Loads", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Results", None))
        self.alertButton.setText("")
# if QT_CONFIG(tooltip)
        self.minBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Minimize window", None))
#endif // QT_CONFIG(tooltip)
        self.minBtn.setText("")
# if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Full screen", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
# if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close app", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Home", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Train", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Loads", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Results", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Logout", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Notification", None))
# if QT_CONFIG(tooltip)
        self.closeAlertButton.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAlertButton.setText("")
    # retranslateUi
