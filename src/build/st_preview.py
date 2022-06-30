# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'st_preview.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCalendarWidget,
    QCheckBox, QColumnView, QComboBox, QCommandLinkButton,
    QDateEdit, QDateTimeEdit, QDial, QDialogButtonBox,
    QFontComboBox, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHeaderView, QLCDNumber, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QTextEdit, QTimeEdit,
    QToolBox, QToolButton, QTreeView, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_Preview(object):
    def setupUi(self, Preview):
        if not Preview.objectName():
            Preview.setObjectName(u"Preview")
        Preview.resize(601, 636)
        Preview.setMinimumSize(QSize(601, 623))
        self.actionOpen = QAction(Preview)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionClose = QAction(Preview)
        self.actionClose.setObjectName(u"actionClose")
        self.actionExit = QAction(Preview)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSave = QAction(Preview)
        self.actionSave.setObjectName(u"actionSave")
        self.actionBuild = QAction(Preview)
        self.actionBuild.setObjectName(u"actionBuild")
        self.actionDocs = QAction(Preview)
        self.actionDocs.setObjectName(u"actionDocs")
        self.actionHelp = QAction(Preview)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionInfo = QAction(Preview)
        self.actionInfo.setObjectName(u"actionInfo")
        self.centralwidget = QWidget(Preview)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setMinimumSize(QSize(298, 195))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 195))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton = QRadioButton(self.tab_3)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.tab_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoRepeat(True)

        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton_3 = QRadioButton(self.tab_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setCheckable(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setAutoRepeat(True)
        self.radioButton_3.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_3, 2, 0, 1, 1)

        self.checkBox = QCheckBox(self.tab_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(True)

        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.tab_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 4, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_3 = QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textEdit = QTextEdit(self.tab_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_3.addWidget(self.plainTextEdit, 2, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_10 = QGridLayout(self.tab_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lineEdit_2 = QLineEdit(self.tab_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout_10.addWidget(self.lineEdit_2, 0, 0, 1, 2)

        self.progressBar = QProgressBar(self.tab_8)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 30))
        self.progressBar.setValue(24)

        self.gridLayout_10.addWidget(self.progressBar, 1, 0, 1, 1)

        self.dial = QDial(self.tab_8)
        self.dial.setObjectName(u"dial")

        self.gridLayout_10.addWidget(self.dial, 1, 1, 2, 1)

        self.horizontalScrollBar = QScrollBar(self.tab_8)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setMinimumSize(QSize(0, 30))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.horizontalScrollBar, 2, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.gridLayout_7.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.tab)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.Tex = QWidget()
        self.Tex.setObjectName(u"Tex")
        self.gridLayout_2 = QGridLayout(self.Tex)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.toolButton = QToolButton(self.Tex)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QSize(262, 40))

        self.gridLayout_2.addWidget(self.toolButton, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.Tex)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(240, 40))
        self.pushButton_2.setFlat(True)

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.Tex)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(240, 40))

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(self.Tex)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(240, 60))
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Discard|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.Tex)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setMinimumSize(QSize(240, 40))

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.Tex)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(240, 40))

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.Tex)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setMinimumSize(QSize(240, 41))
        self.commandLinkButton.setAutoDefault(False)
        self.commandLinkButton.setDefault(False)

        self.gridLayout_2.addWidget(self.commandLinkButton, 6, 0, 1, 1)

        self.tabWidget_3.addTab(self.Tex, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_11 = QGridLayout(self.tab_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget = QTableWidget(self.tab_5)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem18)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 400))
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnCount(10)

        self.gridLayout_11.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_5, "")

        self.gridLayout_7.addWidget(self.tabWidget_3, 1, 0, 1, 1)

        self.tabWidget_4 = QTabWidget(self.tab)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_8 = QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.listWidget = QListWidget(self.tab_6)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_8.addWidget(self.listWidget, 0, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.tab_6)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout_8.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(self.tab_6)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        if (self.tableWidget_2.rowCount() < 6):
            self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setColumnCount(8)

        self.gridLayout_8.addWidget(self.tableWidget_2, 2, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_9 = QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.listView = QListView(self.tab_7)
        self.listView.setObjectName(u"listView")

        self.gridLayout_9.addWidget(self.listView, 0, 0, 1, 1)

        self.treeView = QTreeView(self.tab_7)
        self.treeView.setObjectName(u"treeView")

        self.gridLayout_9.addWidget(self.treeView, 1, 0, 1, 1)

        self.tableView = QTableView(self.tab_7)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_9.addWidget(self.tableView, 2, 0, 1, 1)

        self.columnView = QColumnView(self.tab_7)
        self.columnView.setObjectName(u"columnView")

        self.gridLayout_9.addWidget(self.columnView, 3, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_7, "")

        self.gridLayout_7.addWidget(self.tabWidget_4, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_16 = QGridLayout(self.tab_2)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(561, 251))
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(541, 218))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 573, 295))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(140, 190))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 158, 155))
        self.gridLayout_12 = QGridLayout(self.page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.progressBar_2 = QProgressBar(self.page)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMinimumSize(QSize(140, 30))
        self.progressBar_2.setValue(24)

        self.gridLayout_12.addWidget(self.progressBar_2, 0, 0, 1, 1)

        self.progressBar_3 = QProgressBar(self.page)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setMinimumSize(QSize(140, 101))
        self.progressBar_3.setValue(63)
        self.progressBar_3.setAlignment(Qt.AlignCenter)
        self.progressBar_3.setOrientation(Qt.Vertical)
        self.progressBar_3.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_12.addWidget(self.progressBar_3, 1, 0, 1, 1)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 140, 223))
        self.toolBox.addItem(self.page_2, u"Page 2")

        self.gridLayout_6.addWidget(self.toolBox, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(120, 190))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_17 = QGridLayout(self.page_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lcdNumber = QLCDNumber(self.page_3)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_17.addWidget(self.lcdNumber, 0, 0, 1, 1)

        self.progressBar_4 = QProgressBar(self.page_3)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setMinimumSize(QSize(0, 40))
        self.progressBar_4.setValue(61)
        self.progressBar_4.setTextVisible(False)

        self.gridLayout_17.addWidget(self.progressBar_4, 1, 0, 1, 1)

        self.line = QFrame(self.page_3)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(0, 20))
        self.line.setLineWidth(6)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_17.addWidget(self.line, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_6.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(110, 190))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.graphicsView = QGraphicsView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_13.addWidget(self.graphicsView, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 2, 1, 1)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(110, 190))
        self.gridLayout_14 = QGridLayout(self.widget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.openGLWidget = QOpenGLWidget(self.widget)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.gridLayout_14.addWidget(self.openGLWidget, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.widget, 0, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(560, 260))
        self.gridLayout_15 = QGridLayout(self.groupBox_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(9, 9, -1, -1)
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(260, 30))

        self.gridLayout_15.addWidget(self.comboBox, 0, 0, 1, 1)

        self.calendarWidget = QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_15.addWidget(self.calendarWidget, 0, 1, 6, 1)

        self.fontComboBox = QFontComboBox(self.groupBox_2)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMinimumSize(QSize(260, 30))

        self.gridLayout_15.addWidget(self.fontComboBox, 1, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.groupBox_2)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(260, 30))

        self.gridLayout_15.addWidget(self.timeEdit, 2, 0, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(260, 30))

        self.gridLayout_15.addWidget(self.dateEdit, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(260, 30))

        self.gridLayout_15.addWidget(self.spinBox, 4, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setMinimumSize(QSize(260, 30))

        self.gridLayout_15.addWidget(self.dateTimeEdit, 5, 0, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        Preview.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Preview)
        self.statusbar.setObjectName(u"statusbar")
        Preview.setStatusBar(self.statusbar)

        self.retranslateUi(Preview)
        self.dial.valueChanged.connect(self.progressBar.setValue)
        self.dial.valueChanged.connect(self.horizontalScrollBar.setValue)
        self.progressBar_2.valueChanged.connect(self.timeEdit.selectAll)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        self.pushButton_3.setDefault(True)
        self.tabWidget_4.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Preview)
    # setupUi

    def retranslateUi(self, Preview):
        Preview.setWindowTitle(QCoreApplication.translate("Preview", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        Preview.setToolTip(QCoreApplication.translate("Preview", u"QMainWindow", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen.setText(QCoreApplication.translate("Preview", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("Preview", u"Close", None))
        self.actionExit.setText(QCoreApplication.translate("Preview", u"Exit", None))
        self.actionSave.setText(QCoreApplication.translate("Preview", u"Save", None))
        self.actionBuild.setText(QCoreApplication.translate("Preview", u"Build", None))
        self.actionDocs.setText(QCoreApplication.translate("Preview", u"Docs", None))
        self.actionHelp.setText(QCoreApplication.translate("Preview", u"Help", None))
        self.actionInfo.setText(QCoreApplication.translate("Preview", u"Info", None))
#if QT_CONFIG(tooltip)
        self.centralwidget.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("Preview", u"QTabWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tabWidget_2.setToolTip(QCoreApplication.translate("Preview", u"QTabWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tab_3.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Preview", u"QRadioButton", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Preview", u"RadioButton", None))
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("Preview", u"QRadioButton", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("Preview", u"RadioButton", None))
#if QT_CONFIG(tooltip)
        self.radioButton_3.setToolTip(QCoreApplication.translate("Preview", u"QRadioButton", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_3.setText(QCoreApplication.translate("Preview", u"RadioButton", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("Preview", u"QCheckBox", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("Preview", u"CheckBox", None))
#if QT_CONFIG(tooltip)
        self.checkBox_2.setToolTip(QCoreApplication.translate("Preview", u"QCheckBox", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_2.setText(QCoreApplication.translate("Preview", u"CheckBox", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Preview", u"GroupBox", None))
#if QT_CONFIG(tooltip)
        self.tab_4.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("Preview", u"QTextEdit", None))
#endif // QT_CONFIG(tooltip)
        self.textEdit.setHtml(QCoreApplication.translate("Preview", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QTextEdit</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("Preview", u"QLineEdit", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit.setText(QCoreApplication.translate("Preview", u"QLineEdit", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit.setToolTip(QCoreApplication.translate("Preview", u"QPlainTextEdit", None))
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Preview", u"QPlainTextEdit", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Preview", u"Text Edit", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("Preview", u"QLineEdit", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setText(QCoreApplication.translate("Preview", u"123456", None))
#if QT_CONFIG(tooltip)
        self.progressBar.setToolTip(QCoreApplication.translate("Preview", u"QProgressBar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dial.setToolTip(QCoreApplication.translate("Preview", u"<html><head/><body><p>QDial</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.horizontalScrollBar.setToolTip(QCoreApplication.translate("Preview", u"<html><head/><body><p>QScrollBar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("Preview", u"Misc", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_3.setToolTip(QCoreApplication.translate("Preview", u"QTabWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Tex.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.toolButton.setToolTip(QCoreApplication.translate("Preview", u"QToolButton", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton.setText(QCoreApplication.translate("Preview", u"... Tool ...", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Preview", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("Preview", u"PushButton Flat", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("Preview", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("Preview", u"PushButton Default", None))
#if QT_CONFIG(tooltip)
        self.buttonBox.setToolTip(QCoreApplication.translate("Preview", u"QDiaogButtonBox", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("Preview", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("Preview", u"PushButton Disabled", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Preview", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("Preview", u"PushButton Normal", None))
#if QT_CONFIG(tooltip)
        self.commandLinkButton.setToolTip(QCoreApplication.translate("Preview", u"QCommandLinkButton", None))
#endif // QT_CONFIG(tooltip)
        self.commandLinkButton.setText(QCoreApplication.translate("Preview", u"Command Link Button", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Tex), QCoreApplication.translate("Preview", u"Buttons", None))
#if QT_CONFIG(tooltip)
        self.tab_5.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Preview", u"New Column", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Preview", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Preview", u"New Row", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip(QCoreApplication.translate("Preview", u"QTableWidget", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("Preview", u"Tab Edit", None))
#if QT_CONFIG(tooltip)
        self.tabWidget_4.setToolTip(QCoreApplication.translate("Preview", u"QTabWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tab_6.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Preview", u"QListView", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Preview", u"QListWidget", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Preview", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Preview", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Preview", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Preview", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Preview", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Preview", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("Preview", u"QListWidget", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Preview", u"QTreeWidget", None));

        __sortingEnabled1 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem6 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(6)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem8 = self.treeWidget.topLevelItem(7)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem9 = self.treeWidget.topLevelItem(8)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(9)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        ___qtreewidgetitem11 = self.treeWidget.topLevelItem(10)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("Preview", u"New Item", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.treeWidget.setToolTip(QCoreApplication.translate("Preview", u"QTreeWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tableWidget_2.setToolTip(QCoreApplication.translate("Preview", u"QTableWidget", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QCoreApplication.translate("Preview", u"Items", None))
#if QT_CONFIG(tooltip)
        self.tab_7.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.listView.setToolTip(QCoreApplication.translate("Preview", u"QListView", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.treeView.setToolTip(QCoreApplication.translate("Preview", u"QTreeView", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tableView.setToolTip(QCoreApplication.translate("Preview", u"QTableView", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.columnView.setToolTip(QCoreApplication.translate("Preview", u"QColumnView", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), QCoreApplication.translate("Preview", u"Views", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Preview", u"Main Widgets", None))
#if QT_CONFIG(tooltip)
        self.tab_2.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("Preview", u"QGroupBox", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("Preview", u"Containers", None))
#if QT_CONFIG(tooltip)
        self.scrollArea.setToolTip(QCoreApplication.translate("Preview", u"QScrollArea", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.toolBox.setToolTip(QCoreApplication.translate("Preview", u"QToolBox", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.page.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.progressBar_2.setToolTip(QCoreApplication.translate("Preview", u"QProgressBar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.progressBar_3.setToolTip(QCoreApplication.translate("Preview", u"QProgressBar", None))
#endif // QT_CONFIG(tooltip)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Preview", u"Page 1", None))
#if QT_CONFIG(tooltip)
        self.page_2.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Preview", u"Page 2", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip(QCoreApplication.translate("Preview", u"QStackedWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.page_3.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lcdNumber.setToolTip(QCoreApplication.translate("Preview", u"QLCDNumber", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.progressBar_4.setToolTip(QCoreApplication.translate("Preview", u"QProgressBar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.line.setToolTip(QCoreApplication.translate("Preview", u"Line", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.page_4.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.frame.setToolTip(QCoreApplication.translate("Preview", u"QFrame", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.graphicsView.setToolTip(QCoreApplication.translate("Preview", u"QGraphicsView", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(QCoreApplication.translate("Preview", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.openGLWidget.setToolTip(QCoreApplication.translate("Preview", u"QOpenGLWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip(QCoreApplication.translate("Preview", u"QGroupBox", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Preview", u"Inputs box", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Preview", u"New Item", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Preview", u"New Item", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("Preview", u"QComboBox", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.calendarWidget.setToolTip(QCoreApplication.translate("Preview", u"QCalendarWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fontComboBox.setToolTip(QCoreApplication.translate("Preview", u"QFontComboBox", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.timeEdit.setToolTip(QCoreApplication.translate("Preview", u"QTimeEdit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("Preview", u"QSpinBox", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Preview", u"Misc Widgets", None))
#if QT_CONFIG(tooltip)
        self.statusbar.setToolTip(QCoreApplication.translate("Preview", u"QStatusBar", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

