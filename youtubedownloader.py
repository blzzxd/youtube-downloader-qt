# Form implementation generated from reading ui file 'C:\Users\artur\PycharmProjects\youtube-downloader-qt\youtubedownloader.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 271)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\artur\\PycharmProjects\\youtube-downloader-qt\\icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pasteBox = QtWidgets.QLineEdit(self.centralwidget)
        self.pasteBox.setGeometry(QtCore.QRect(20, 50, 511, 21))
        self.pasteBox.setObjectName("pasteBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setEnabled(True)
        self.convertButton.setGeometry(QtCore.QRect(20, 80, 511, 61))
        self.convertButton.setObjectName("convertButton")
        self.videostate = QtWidgets.QLabel(self.centralwidget)
        self.videostate.setGeometry(QtCore.QRect(80, 200, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.videostate.setFont(font)
        self.videostate.setObjectName("videostate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 200, 311, 16))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 170, 511, 23))
        self.progressBar.setMouseTracking(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.ytname = QtWidgets.QLabel(self.centralwidget)
        self.ytname.setGeometry(QtCore.QRect(130, 150, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(10)
        font.setItalic(True)
        self.ytname.setFont(font)
        self.ytname.setObjectName("ytname")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen_Folder = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        self.actionOpen_Folder.setFont(font)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "youtube-downloader-qt"))
        self.label.setText(_translate("MainWindow", "Paste youtube link here"))
        self.convertButton.setText(_translate("MainWindow", "Convert and download the video"))
        self.videostate.setText(_translate("MainWindow", "( waiting ... )"))
        self.label_2.setText(_translate("MainWindow", "Go to \'File -> Open Folder\' to see your downloaded videos"))
        self.ytname.setText(_translate("MainWindow", "( waiting... )"))
        self.label_3.setText(_translate("MainWindow", "Video title: "))
        self.label_4.setText(_translate("MainWindow", "State: "))
        self.label_5.setText(_translate("MainWindow", "YouTube Downloader"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Close the program"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
