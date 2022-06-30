# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'st_edit.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Editor(object):
    def setupUi(self, Editor):
        if not Editor.objectName():
            Editor.setObjectName(u"Editor")
        Editor.setWindowModality(Qt.WindowModal)
        Editor.resize(517, 610)
        self.grid = QWidget(Editor)
        self.grid.setObjectName(u"grid")
        self.gridLayout = QGridLayout(self.grid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.input = QPlainTextEdit(self.grid)
        self.input.setObjectName(u"input")

        self.gridLayout.addWidget(self.input, 0, 0, 1, 3)

        self.b_build = QPushButton(self.grid)
        self.b_build.setObjectName(u"b_build")
        self.b_build.setMinimumSize(QSize(0, 40))
        self.b_build.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.b_build, 1, 0, 1, 1)

        self.b_save = QPushButton(self.grid)
        self.b_save.setObjectName(u"b_save")
        self.b_save.setMinimumSize(QSize(0, 40))
        self.b_save.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.b_save, 1, 1, 1, 1)

        self.b_import = QPushButton(self.grid)
        self.b_import.setObjectName(u"b_import")
        self.b_import.setMinimumSize(QSize(0, 40))
        self.b_import.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.b_import, 1, 2, 1, 1)

        Editor.setCentralWidget(self.grid)

        self.retranslateUi(Editor)

        QMetaObject.connectSlotsByName(Editor)
    # setupUi

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(QCoreApplication.translate("Editor", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        Editor.setToolTip(QCoreApplication.translate("Editor", u"QMainWindow", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.grid.setToolTip(QCoreApplication.translate("Editor", u"QWidget", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input.setToolTip(QCoreApplication.translate("Editor", u"QPlainTextEdit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.b_build.setToolTip(QCoreApplication.translate("Editor", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.b_build.setText(QCoreApplication.translate("Editor", u"BUILD", None))
#if QT_CONFIG(shortcut)
        self.b_build.setShortcut(QCoreApplication.translate("Editor", u"F9", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.b_save.setToolTip(QCoreApplication.translate("Editor", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.b_save.setText(QCoreApplication.translate("Editor", u"SAVE", None))
#if QT_CONFIG(shortcut)
        self.b_save.setShortcut(QCoreApplication.translate("Editor", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.b_import.setToolTip(QCoreApplication.translate("Editor", u"QPushButton", None))
#endif // QT_CONFIG(tooltip)
        self.b_import.setText(QCoreApplication.translate("Editor", u"IMPORT", None))
#if QT_CONFIG(shortcut)
        self.b_import.setShortcut(QCoreApplication.translate("Editor", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

