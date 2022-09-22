# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#Created by Hafiz Zulkepli 21-09-2022

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1647, 808)
        MainWindow.setMaximumSize(QtCore.QSize(1647, 808))
        MainWindow.setStyleSheet("background-color:rgba(44, 51, 51,255);\n"
"border-radius:10px;")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgba(44, 51, 51,255)")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, -10, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.dir_text = QtWidgets.QLabel(self.centralwidget)
        self.dir_text.setGeometry(QtCore.QRect(410, 80, 801, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.dir_text.setFont(font)
        self.dir_text.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.dir_text.setText("")
        self.dir_text.setObjectName("dir_text")
        self.month_text = QtWidgets.QLabel(self.centralwidget)
        self.month_text.setGeometry(QtCore.QRect(480, 140, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.month_text.setFont(font)
        self.month_text.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.month_text.setText("")
        self.month_text.setObjectName("month_text")
        self.ic_text = QtWidgets.QLabel(self.centralwidget)
        self.ic_text.setGeometry(QtCore.QRect(480, 190, 721, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.ic_text.setFont(font)
        self.ic_text.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.ic_text.setText("")
        self.ic_text.setObjectName("ic_text")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(20, 670, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.update_button.setFont(font)
        self.update_button.setMouseTracking(False)
        self.update_button.setStyleSheet("QPushButton {background-color : transparent; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}"
"QPushButton::hover {background-color : lightgreen; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}")

        self.update_button.setObjectName("update_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(182, 667, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.clear_button.setFont(font)
        self.clear_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.clear_button.setStyleSheet("QPushButton {background-color : transparent; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}"
"QPushButton::hover {background-color : lightgreen; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}")

        self.clear_button.setObjectName("clear_button")
        self.ic_table = QtWidgets.QLabel(self.centralwidget)
        self.ic_table.setGeometry(QtCore.QRect(20, 710, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ic_table.setFont(font)
        self.ic_table.setStyleSheet("color:rgb(255, 255, 255)")
        self.ic_table.setText("")
        self.ic_table.setObjectName("ic_table")
        self.scrape_data = QtWidgets.QListWidget(self.centralwidget)
        self.scrape_data.setGeometry(QtCore.QRect(1270, 70, 351, 481))
        self.scrape_data.setStyleSheet("color: rgb(255,255,255)")
        self.scrape_data.setObjectName("scrape_data")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(340, 300, 861, 411))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(44, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.listWidget.setPalette(palette)
        self.listWidget.setStyleSheet("color: rgb(255,255,255)")
        self.listWidget.setObjectName("listWidget")
        self.actionBorder_5 = QtWidgets.QLabel(self.centralwidget)
        self.actionBorder_5.setGeometry(QtCore.QRect(10, 60, 1211, 191))
        self.actionBorder_5.setStyleSheet("border:1px solid rgb(120, 139, 139);\n"
"border-radius:15px;")
        self.actionBorder_5.setText("")
        self.actionBorder_5.setObjectName("actionBorder_5")
        self.actionBorder_6 = QtWidgets.QLabel(self.centralwidget)
        self.actionBorder_6.setGeometry(QtCore.QRect(10, 290, 281, 451))
        self.actionBorder_6.setStyleSheet("border:1px solid rgb(120, 139, 139);\n"
"background-color:rgba(44, 51, 51,255);\n"
"border-radius:15px;")
        self.actionBorder_6.setText("")
        self.actionBorder_6.setObjectName("actionBorder_6")
        self.actionBorder_7 = QtWidgets.QLabel(self.centralwidget)
        self.actionBorder_7.setGeometry(QtCore.QRect(1260, 60, 371, 521))
        self.actionBorder_7.setStyleSheet("border:1px solid rgb(120, 139, 139);\n"
"border-radius:15px;")
        self.actionBorder_7.setText("")
        self.actionBorder_7.setObjectName("actionBorder_7")
        self.actionBorder_8 = QtWidgets.QLabel(self.centralwidget)
        self.actionBorder_8.setGeometry(QtCore.QRect(330, 290, 891, 451))
        self.actionBorder_8.setStyleSheet("border:1px solid rgb(120, 139, 139);\n"
"border-radius:15px;")
        self.actionBorder_8.setText("")
        self.actionBorder_8.setObjectName("actionBorder_8")
        self.actionBorder_9 = QtWidgets.QLabel(self.centralwidget)
        self.actionBorder_9.setGeometry(QtCore.QRect(1260, 620, 371, 121))
        self.actionBorder_9.setStyleSheet("border:1px solid rgb(120, 139, 139);\n"
"border-radius:15px;")
        self.actionBorder_9.setText("")
        self.actionBorder_9.setObjectName("actionBorder_9")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(1270, 640, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton {background-color : transparent; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}"
"QPushButton::hover {background-color : lightgreen; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}")

        self.start_button.setObjectName("start_button")
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(1270, 680, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("QPushButton {background-color : transparent; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}"
"QPushButton::hover {background-color : lightgreen; border:1px solid rgb(120, 139, 139); border-radius:15px; color: rgb(255,255,255);}")

        self.finish_button.setObjectName("finish_button")
        self.create_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.create_dir.setGeometry(QtCore.QRect(160, 80, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.create_dir.setFont(font)
        self.create_dir.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgb(120, 139, 139);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.create_dir.setText("")
        self.create_dir.setPlaceholderText("")
        self.create_dir.setObjectName("create_dir")
        self.month_dur = QtWidgets.QLineEdit(self.centralwidget)
        self.month_dur.setGeometry(QtCore.QRect(380, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.month_dur.setFont(font)
        self.month_dur.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgb(120, 139, 139);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.month_dur.setText("")
        self.month_dur.setPlaceholderText("")
        self.month_dur.setObjectName("month_dur")
        self.ic = QtWidgets.QLineEdit(self.centralwidget)
        self.ic.setGeometry(QtCore.QRect(290, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ic.setFont(font)
        self.ic.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgb(120, 139, 139);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.ic.setText("")
        self.ic.setPlaceholderText("")
        self.ic.setObjectName("ic")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255,0)")
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1380, 640, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("border:1px solid rgb(120, 139, 139);\n"
"border-radius:15px;\n"
"color: rgb(255,255,255)")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(590, 240, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 730, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(710, 730, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1430, 570, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1450, 730, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet('QWidget { background-color: #aa8888; } QHeaderView::section { background-color: #88aa88; } QTableWidget QTableCornerButton::section {background-color: #8888aa; }')

        self.tableWidget.setGeometry(QtCore.QRect(20, 310, 256, 341))
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setForeground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)


        self.current_scrape = QtWidgets.QLabel(self.centralwidget)
        self.current_scrape.setGeometry(QtCore.QRect(1390, 680, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.current_scrape.setFont(font)
        self.current_scrape.setStyleSheet("color:rgb(255, 255, 255)")
        self.current_scrape.setObjectName("current_scrape")
        self.actionBorder_9.raise_()
        self.actionBorder_5.raise_()
        self.actionBorder_8.raise_()
        self.actionBorder_6.raise_()
        self.actionBorder_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.dir_text.raise_()
        self.ic_text.raise_()
        self.update_button.raise_()
        self.clear_button.raise_()
        self.ic_table.raise_()
        self.scrape_data.raise_()
        self.start_button.raise_()
        self.finish_button.raise_()
        self.month_text.raise_()
        self.create_dir.raise_()
        self.month_dur.raise_()
        self.ic.raise_()
        self.label_5.raise_()
        self.progressBar.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.listWidget.raise_()
        self.tableWidget.raise_()
        self.current_scrape.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1647, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">CIDB &amp; NTSP SCRAPER</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Month duration before CIDB/NTSP expired in digit :"))
        self.label_3.setText(_translate("MainWindow", "Create a directory :"))
        self.label_4.setText(_translate("MainWindow", "Please enter Mykad Identity                :"))
        self.update_button.setText(_translate("MainWindow", "Update all IC"))
        self.clear_button.setText(_translate("MainWindow", "Clear all IC"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.finish_button.setText(_translate("MainWindow", "Quit"))
        self.label_5.setText(_translate("MainWindow", "Passport / IMMP13 without SPACE"))
        self.label_6.setText(_translate("MainWindow", "Input Section"))
        self.label_7.setText(_translate("MainWindow", "IC List"))
        self.label_8.setText(_translate("MainWindow", "Scraping Report"))
        self.label_9.setText(_translate("MainWindow", "Status"))
        self.label_10.setText(_translate("MainWindow", "Action"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IC/ Passport/ IMMP13"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())