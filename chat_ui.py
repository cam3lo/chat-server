# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys, socket
from _thread import *

#host = self.textEdit.text()
port = 9009
name = ''
send = False
rmessage = ''
rmsg = ''

def msg_box(title, data):
    w = QtGui.QWidget()
    QtGui.QMessageBox.information(w, title, data)

def update_list(self, data):
    self.listWidget.addItem(data)
    print("\a")
"""
def setSendFalse():
    send = False
    name = ""
    rmessage = ""
    rmsg = ""
"""
class Client_Socket(QThread):

    def __init__(self, ip_addr):
        QThread.__init__(self)
        self.ip_addr = ip_addr

    def __del__(self):
        self.wait()

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((self.ip_addr, port))
            s.listen(1) #doesn't work after including this
        except:
            #msg_box("Socket Error!", "Unable to connect... you should fix that")
            print("damn son")
            return

        while True:
            conn, addr = s.accept()

            data = conn.recv(4096)
            data_string = data.decode()
            self.emit(SIGNAL("display_message(QString)"), data_string)

            if send:
                try:
                    self.emit(SIGNAL("display_message(QString)"), rmsg)
                    conn.send(rmsg.encode)
                    send = False
                    name = ""
                    rmessage = ""
                    rmsg = ""
                except:
                    print("damn playa")
                    return

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 41))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(90, 10, 151, 21))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 10, 91, 21))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_3.clicked.connect(self.start_connect)

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 80, 751, 321))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.listWidget = QtGui.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 721, 301))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 420, 421, 91))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.textEdit_2 = QtGui.QTextEdit(self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 401, 51))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton = QtGui.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 66, 101, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.setSend)

        self.pushButton_2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 66, 91, 21))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(470, 420, 301, 121))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.listWidget_2 = QtGui.QListWidget(self.frame_4)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 10, 281, 101))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu_Actions = QtGui.QMenu(self.menubar)
        self.menuMenu_Actions.setObjectName(_fromUtf8("menuMenu_Actions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName(_fromUtf8("actionVersion"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuMenu_Actions.addAction(self.actionVersion)
        self.menuMenu_Actions.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu_Actions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "IP Address:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Connect", None))
        self.pushButton.setText(_translate("MainWindow", "Send Message", None))
        self.pushButton_2.setText(_translate("MainWindow", "Clear", None))
        self.menuMenu_Actions.setTitle(_translate("MainWindow", "Menu Actions", None))
        self.actionVersion.setText(_translate("MainWindow", "Version", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
    
    def start_connect(self):
        ip_addr = self.textEdit.toPlainText()
        self.clientThread = Client_Socket(ip_addr)
        self.clientThread.start()
        #msg_box("Success", "Now connected to server")
        #self.pushButton_3.setEnabled(False)
        QtCore.QObject.connect(self.clientThread, SIGNAL("display_message(QString)"), self.display_message)
        
    def setSend(self):
        send = True
        name = "[Me]"
        rmessage = self.textEdit_2.toPlainText()
        rmsg = name + ">: " + rmessage

    def display_message(self, message):
        self.listWidget.addItem(message)
        print("\a")
"""
    def client_send_message(self):
        ip = self.textEdit.toPlainText()

        name = "[Me]"
        rmessage = self.textEdit_2.toPlainText()
        rmsg = name + ">: " + rmessage
        
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            c.connect(ip, port)
        except:
            msg_box("Connection Refused", "Unable to send message.")
            return

        try:
            c.send(rmsg.encode)
            self.listWidget.addItem(rmsg)
            self.textEdit_2.setText("")
        except:
            msg_box("Connection Refused", "Address is currently unavailable")

        c.close()
"""

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

