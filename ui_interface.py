# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceRzlfJH.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 600)
        MainWindow.setStyleSheet(u"\n"
"*{\n"
"	font: \"Rockwell\";\n"
"	border:none\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background: rgb(195, 195, 201);\n"
"	font: \"Rockwell\";\n"
"	border: 1px solid;\n"
"	\n"
"	border-color: rgb(156, 156, 161);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(208, 208, 214);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.header_left_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/2757271291543238854.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menu_btn, 0, Qt.AlignLeft)

        self.label_3 = QLabel(self.header_left_frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icons/10511101761543238864.svg"))

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame)

        self.header_left_frame_2 = QFrame(self.header_frame)
        self.header_left_frame_2.setObjectName(u"header_left_frame_2")
        self.header_left_frame_2.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_left_frame_2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.header_left_frame_2)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setStyleSheet(u"background-color: rgb(208, 208, 214);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/17474714781543238905.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.restor_btn = QPushButton(self.header_left_frame_2)
        self.restor_btn.setObjectName(u"restor_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/12627537101543238871.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restor_btn.setIcon(icon2)
        self.restor_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.restor_btn)

        self.close_btn = QPushButton(self.header_left_frame_2)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/5299154331543238955.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.header_left_frame_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame = QFrame(self.main_frame)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(39, 0))
        self.left_menu_frame.setMaximumSize(QSize(39, 16777215))
        self.left_menu_frame.setStyleSheet(u"background-color: rgb(208, 208, 214);")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(100, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cpu_btn = QPushButton(self.menu_frame)
        self.cpu_btn.setObjectName(u"cpu_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/15601232391543238881.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_btn.setIcon(icon4)
        self.cpu_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.cpu_btn, 0, 0, 1, 1)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(3)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.battery_btn = QPushButton(self.menu_frame)
        self.battery_btn.setObjectName(u"battery_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/16964359561543238861.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_btn.setIcon(icon5)
        self.battery_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.battery_btn, 1, 0, 1, 1)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(3)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.system_btn = QPushButton(self.menu_frame)
        self.system_btn.setObjectName(u"system_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/10010006041543238906.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_btn.setIcon(icon6)
        self.system_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.system_btn, 2, 0, 1, 1)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(3)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)

        self.activities_btn = QPushButton(self.menu_frame)
        self.activities_btn.setObjectName(u"activities_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/2475893221543238851.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activities_btn.setIcon(icon7)
        self.activities_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.activities_btn, 3, 0, 1, 1)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(3)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)

        self.storage_btn = QPushButton(self.menu_frame)
        self.storage_btn.setObjectName(u"storage_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/11931009711543238875.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_btn.setIcon(icon8)
        self.storage_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.storage_btn, 4, 0, 1, 1)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(3)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.sensors_btn = QPushButton(self.menu_frame)
        self.sensors_btn.setObjectName(u"sensors_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/3850855891543238935.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensors_btn.setIcon(icon9)
        self.sensors_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.sensors_btn, 5, 0, 1, 1)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(3)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.networks_btn = QPushButton(self.menu_frame)
        self.networks_btn.setObjectName(u"networks_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/wifi_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.networks_btn.setIcon(icon10)
        self.networks_btn.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.networks_btn, 6, 0, 1, 1)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(3)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.left_menu_frame)

        self.right_main_frame = QFrame(self.main_frame)
        self.right_main_frame.setObjectName(u"right_main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_main_frame.sizePolicy().hasHeightForWidth())
        self.right_main_frame.setSizePolicy(sizePolicy2)
        self.right_main_frame.setStyleSheet(u"background-color: rgb(195, 195, 201);\n"
"\n"
"")
        self.right_main_frame.setFrameShape(QFrame.StyledPanel)
        self.right_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.right_main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid rgb(195, 195, 201);\n"
"	border-bottom-color: rgb(182, 182, 188);\n"
"	\n"
"	background-color: rgb(208, 208, 214);\n"
"}\n"
"\n"
"QLineEdit::edit-focus{\n"
"	border: 1px solid rgb(195, 195, 201);\n"
"	border-bottom-color: rgb(182, 182, 188);\n"
"	\n"
"	\n"
"	background-color: rgb(156, 156, 161);\n"
"}\n"
"\n"
"")
        self.cpu_page = QWidget()
        self.cpu_page.setObjectName(u"cpu_page")
        self.verticalLayout_4 = QVBoxLayout(self.cpu_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.cpu_page)
        self.label_52.setObjectName(u"label_52")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_52.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_52, 0, Qt.AlignBottom)

        self.frame_10 = QFrame(self.cpu_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cpu_info_frame = QFrame(self.frame_10)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cpu_info_frame.sizePolicy().hasHeightForWidth())
        self.cpu_info_frame.setSizePolicy(sizePolicy3)
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.cpu_info_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_5.addWidget(self.label_41, 2, 0, 1, 1)

        self.cpu_usage = QLabel(self.cpu_info_frame)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setFont(font)

        self.gridLayout_5.addWidget(self.cpu_usage, 3, 1, 1, 1)

        self.cpu_core = QLabel(self.cpu_info_frame)
        self.cpu_core.setObjectName(u"cpu_core")
        self.cpu_core.setFont(font)

        self.gridLayout_5.addWidget(self.cpu_core, 2, 1, 1, 1)

        self.label_17 = QLabel(self.cpu_info_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_39 = QLabel(self.cpu_info_frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)

        self.gridLayout_5.addWidget(self.label_39, 3, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setFont(font)

        self.gridLayout_5.addWidget(self.cpu_count, 0, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.cpu_info_frame)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 200))
        self.verticalLayout_17 = QVBoxLayout(self.frame_11)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.cpu_usage_layout = QVBoxLayout()
        self.cpu_usage_layout.setSpacing(0)
        self.cpu_usage_layout.setObjectName(u"cpu_usage_layout")

        self.verticalLayout_17.addLayout(self.cpu_usage_layout)


        self.horizontalLayout_10.addWidget(self.frame_11)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.label_53 = QLabel(self.cpu_page)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_53, 0, Qt.AlignBottom)

        self.frame_12 = QFrame(self.cpu_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 40))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.ram_info_frame = QFrame(self.frame_12)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ram_info_frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ram_avibile = QLabel(self.ram_info_frame)
        self.ram_avibile.setObjectName(u"ram_avibile")
        self.ram_avibile.setFont(font)

        self.gridLayout_4.addWidget(self.ram_avibile, 1, 1, 1, 1)

        self.ram_used = QLabel(self.ram_info_frame)
        self.ram_used.setObjectName(u"ram_used")
        self.ram_used.setFont(font)

        self.gridLayout_4.addWidget(self.ram_used, 4, 1, 1, 1)

        self.ram_free = QLabel(self.ram_info_frame)
        self.ram_free.setObjectName(u"ram_free")
        self.ram_free.setFont(font)

        self.gridLayout_4.addWidget(self.ram_free, 5, 1, 1, 1)

        self.ram_usage = QLabel(self.ram_info_frame)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setFont(font)

        self.gridLayout_4.addWidget(self.ram_usage, 6, 1, 1, 1)

        self.label_33 = QLabel(self.ram_info_frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.gridLayout_4.addWidget(self.label_33, 6, 0, 1, 1)

        self.label_31 = QLabel(self.ram_info_frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_4.addWidget(self.label_31, 1, 0, 1, 1)

        self.ram_total = QLabel(self.ram_info_frame)
        self.ram_total.setObjectName(u"ram_total")
        self.ram_total.setFont(font)

        self.gridLayout_4.addWidget(self.ram_total, 0, 1, 1, 1)

        self.label_30 = QLabel(self.ram_info_frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)

        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_32 = QLabel(self.ram_info_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_4.addWidget(self.label_32, 5, 0, 1, 1)

        self.label_28 = QLabel(self.ram_info_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.gridLayout_4.addWidget(self.label_28, 4, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.ram_info_frame)

        self.ram_usage_frame = QFrame(self.frame_12)
        self.ram_usage_frame.setObjectName(u"ram_usage_frame")
        self.ram_usage_frame.setMinimumSize(QSize(300, 200))
        self.ram_usage_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_usage_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.ram_usage_frame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.ram_usage_layout = QVBoxLayout()
        self.ram_usage_layout.setObjectName(u"ram_usage_layout")

        self.verticalLayout_19.addLayout(self.ram_usage_layout)


        self.horizontalLayout_11.addWidget(self.ram_usage_frame)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.cpu_page)
        self.battery_page = QWidget()
        self.battery_page.setObjectName(u"battery_page")
        self.verticalLayout_5 = QVBoxLayout(self.battery_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.label_43 = QLabel(self.battery_page)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_43, 0, Qt.AlignBottom)

        self.frame = QFrame(self.battery_page)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)

        self.gridLayout_6.addWidget(self.label_44, 0, 0, 1, 1)

        self.label_45 = QLabel(self.frame)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)

        self.gridLayout_6.addWidget(self.label_45, 1, 0, 1, 1)

        self.battery_status = QLabel(self.frame)
        self.battery_status.setObjectName(u"battery_status")
        self.battery_status.setFont(font)

        self.gridLayout_6.addWidget(self.battery_status, 0, 1, 1, 1)

        self.battery_plugged = QLabel(self.frame)
        self.battery_plugged.setObjectName(u"battery_plugged")
        self.battery_plugged.setFont(font)

        self.gridLayout_6.addWidget(self.battery_plugged, 3, 1, 1, 1)

        self.label_46 = QLabel(self.frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.gridLayout_6.addWidget(self.label_46, 2, 0, 1, 1)

        self.battery_charge = QLabel(self.frame)
        self.battery_charge.setObjectName(u"battery_charge")
        self.battery_charge.setFont(font)

        self.gridLayout_6.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.label_47 = QLabel(self.frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font)

        self.gridLayout_6.addWidget(self.label_47, 3, 0, 1, 1)

        self.battery_time = QLabel(self.frame)
        self.battery_time.setObjectName(u"battery_time")
        self.battery_time.setFont(font)

        self.gridLayout_6.addWidget(self.battery_time, 2, 1, 1, 1)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setMinimumSize(QSize(200, 200))
        self.frame_13.setLayoutDirection(Qt.LeftToRight)
        self.frame_13.setAutoFillBackground(False)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.battery_charge_percentage = QVBoxLayout()
        self.battery_charge_percentage.setObjectName(u"battery_charge_percentage")
        self.battery_charge_percentage.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_16.addLayout(self.battery_charge_percentage)


        self.gridLayout_6.addWidget(self.frame_13, 0, 2, 4, 1)


        self.verticalLayout_5.addWidget(self.frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.battery_page)
        self.system_page = QWidget()
        self.system_page.setObjectName(u"system_page")
        self.verticalLayout_6 = QVBoxLayout(self.system_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.system_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_63 = QLabel(self.frame_2)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font)

        self.gridLayout_7.addWidget(self.label_63, 4, 2, 1, 1)

        self.system_platform = QLabel(self.frame_2)
        self.system_platform.setObjectName(u"system_platform")
        self.system_platform.setFont(font)

        self.gridLayout_7.addWidget(self.system_platform, 2, 1, 1, 1)

        self.label_56 = QLabel(self.frame_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.gridLayout_7.addWidget(self.label_56, 2, 0, 1, 1)

        self.label_57 = QLabel(self.frame_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)

        self.gridLayout_7.addWidget(self.label_57, 4, 0, 1, 1)

        self.label_58 = QLabel(self.frame_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)

        self.gridLayout_7.addWidget(self.label_58, 5, 0, 1, 1)

        self.system_version = QLabel(self.frame_2)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setFont(font)

        self.gridLayout_7.addWidget(self.system_version, 4, 1, 1, 1)

        self.label_62 = QLabel(self.frame_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font)

        self.gridLayout_7.addWidget(self.label_62, 2, 2, 1, 1)

        self.label_54 = QLabel(self.frame_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)

        self.gridLayout_7.addWidget(self.label_54, 0, 0, 1, 1)

        self.system_date = QLabel(self.frame_2)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setFont(font)

        self.gridLayout_7.addWidget(self.system_date, 5, 1, 1, 1)

        self.system_name = QLabel(self.frame_2)
        self.system_name.setObjectName(u"system_name")
        self.system_name.setFont(font1)

        self.gridLayout_7.addWidget(self.system_name, 1, 0, 1, 1)

        self.system_machine = QLabel(self.frame_2)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setFont(font)

        self.gridLayout_7.addWidget(self.system_machine, 2, 3, 1, 1)

        self.system_time = QLabel(self.frame_2)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font)

        self.gridLayout_7.addWidget(self.system_time, 4, 3, 1, 1)

        self.label_64 = QLabel(self.frame_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font)

        self.gridLayout_7.addWidget(self.label_64, 5, 2, 1, 1)

        self.system_processor = QLabel(self.frame_2)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setFont(font)

        self.gridLayout_7.addWidget(self.system_processor, 5, 3, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.system_page)
        self.activities_page = QWidget()
        self.activities_page.setObjectName(u"activities_page")
        self.verticalLayout_7 = QVBoxLayout(self.activities_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.activities_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 10, 0, 0)
        self.label_68 = QLabel(self.frame_3)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_68)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(60, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(3, 5, 5, 5)
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_8.addWidget(self.frame_6, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.activities_page)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectColumns)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)

        self.verticalLayout_8.addWidget(self.tableWidget)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.activities_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	font: 10pt \"Rockwell\";\n"
"	background-color: rgb(208, 208, 214);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_9.addWidget(self.pushButton_6)


        self.verticalLayout_7.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activities_page)
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.storage_page.setStyleSheet(u"\n"
"*{\n"
"	font: \"Rockwell\";\n"
"	border:none\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.storage_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.storage_page)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_69)

        self.tableWidget_2 = QTableWidget(self.storage_page)
        if (self.tableWidget_2.columnCount() < 6):
            self.tableWidget_2.setColumnCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_9.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.storage_page)
        self.sensors_page = QWidget()
        self.sensors_page.setObjectName(u"sensors_page")
        self.verticalLayout_10 = QVBoxLayout(self.sensors_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.sensors_page)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_70)

        self.tableWidget_3 = QTableWidget(self.sensors_page)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(152)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.sensors_page)
        self.networks_page = QWidget()
        self.networks_page.setObjectName(u"networks_page")
        self.verticalLayout_11 = QVBoxLayout(self.networks_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.networks_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 135, 606))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 100)
        self.label_71 = QLabel(self.frame_7)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_13.addWidget(self.label_71)

        self.tableWidget_4 = QTableWidget(self.frame_7)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(145)
        self.tableWidget_4.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_13.addWidget(self.tableWidget_4)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 100)
        self.label_73 = QLabel(self.frame_9)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_15.addWidget(self.label_73)

        self.tableWidget_6 = QTableWidget(self.frame_9)
        if (self.tableWidget_6.columnCount() < 6):
            self.tableWidget_6.setColumnCount(6)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.tableWidget_6)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, -1, -1, 100)
        self.label_72 = QLabel(self.frame_8)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_14.addWidget(self.label_72)

        self.tableWidget_5 = QTableWidget(self.frame_8)
        if (self.tableWidget_5.columnCount() < 8):
            self.tableWidget_5.setColumnCount(8)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.verticalLayout_14.addWidget(self.tableWidget_5)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.networks_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.right_main_frame)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(208, 208, 214);")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.footer_frame)
        self.pushButton.setObjectName(u"pushButton")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/21286857451543238864.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.size_grip.setFont(font3)
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PC Info", None))
        self.minimize_btn.setText("")
        self.restor_btn.setText("")
        self.close_btn.setText("")
        self.cpu_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.battery_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.system_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.activities_btn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.storage_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.sensors_btn.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.networks_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Networks", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"CPU Information", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"CPU Core", None))
        self.cpu_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"CPU Usage", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"RAM Information", None))
        self.ram_avibile.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_used.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_free.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Avibile RAM", None))
        self.ram_total.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Total RAM", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Free RAM", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Used RAM", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.battery_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Sysytem Information", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.pushButton_2.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Device", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total Storage", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Used Storage", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Free Space", None));
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nowa kolumna", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Critical", None));
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"DUPLEX", None));
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"SPEED", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem17 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem18 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ADDRESS", None));
        ___qtablewidgetitem19 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"NETMASK", None));
        ___qtablewidgetitem20 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"BROADCAST", None));
        ___qtablewidgetitem21 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Network I/O Counters", None))
        ___qtablewidgetitem22 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"BYTES SENT", None));
        ___qtablewidgetitem23 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"BYTES RECEIVED", None));
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"PACKED SENT", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"ERR In", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ERR Out", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(7)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.pushButton.setText("")
    # retranslateUi

