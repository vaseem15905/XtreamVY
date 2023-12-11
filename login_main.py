#<<<<<<<<<<__GOTSTACK_DEVELOPERS__>>>>>>>>>>#

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

app = QApplication(sys.argv)
mw=QMainWindow()
mw.setGeometry(700,400,410,170)
mw.setStyleSheet("background-color: #27374D;")
mw.setWindowTitle("System Login")



myfont=QFont()
myfont.setBold(True)
myfont.setPointSize(10)


username_label=QLabel("Username   : ",mw)
username_label.setGeometry(20,20,200,30)
username_label.setStyleSheet("color: white;")
username_label.setFont(myfont)


username_input=QLineEdit(mw)
username_input.setGeometry(155,20,235,30)
username_input.setFont(myfont)
username_input.setPlaceholderText("Enter here!")
username_input.setStyleSheet("""
                             border: 1px solid white;
                             border-radius: 7px;
                             color: white;
                             background-color: #212A3E;
                             selection-background-color: white;
                             selection-color: #212A3E;
                             """)



password_label=QLabel("Password    : ",mw)
password_label.setGeometry(20,60,200,30)
password_label.setStyleSheet("""
                             color: white;
                             """)
password_label.setFont(myfont)


password_input=QLineEdit(mw)
password_input.setGeometry(155,60,235,30)
password_input.setEchoMode(QLineEdit.Password)
password_input.setFont(myfont)
password_input.setPlaceholderText("Enter here!")
password_input.setStyleSheet("""
                             border:1px solid white;
                             color: white;
                             border-radius: 7px;
                             background-color: #212A3E;
                             selection-background-color: white;
                             selection-color: #212A3E;
                             """)



ok_button=QPushButton("Ok",mw)
ok_button.setGeometry(243,110,60,40)
ok_button.setFont(myfont)
ok_button.setStyleSheet("""
                        QPushButton 
                        {
                            color: white;
                            background-color: #27374D;
                            border-radius: 6px;
                            border: 1px solid white;
                        }
                        QPushButton:Pressed 
                        {
                            background-color: #16213E;
                            color: white;
                        }
                        QPushButton:hover
                        {
                            background-color: #212A3E;
                            color: white;
                        }
                        """)
def success_info():
    info=QMessageBox()
    info.setIcon(QMessageBox.Information)
    info.setWindowTitle("Info")
    info.setText("Login Successful!")
    info.setGeometry(810,450 ,100,100)
    
    info.setStyleSheet("background-color: white;")     
    info.exec_()
    
def username_invalid_info():
    info=QMessageBox()
    info.setIcon(QMessageBox.Warning)
    info.setWindowTitle("Ouch!")
    info.setText("Your Username is not entered!.")
    info.setGeometry(760,445,100,100)
    info.setStyleSheet("background-color: white;")
    info.exec_()

def invalid_info():
    info=QMessageBox()
    info.setIcon(QMessageBox.Warning)
    info.setWindowTitle("Ouch!")
    info.setText("Please enter all the credentials.")
    info.setGeometry(760,445,100,100)
    info.setStyleSheet("background-color: white;")
    info.exec_()
    
def password_invalid_info():
    info=QMessageBox()
    info.setIcon(QMessageBox.Warning)
    info.setWindowTitle("Ouch!")
    info.setText("Your Password is not entered!")
    info.setGeometry(760,445,100,100)
    info.setStyleSheet("background-color: white;")
    info.exec_()
    
    
    
def info():
    if(username_input.text()=="" and password_input.text()==""):
        invalid_info()
    elif(username_input.text()==""):
        username_invalid_info()
    elif(password_input.text()==""):
        password_invalid_info()
    else:
        success_info()

ok_button.clicked.connect(info)



cancel_button=QPushButton("Cancel",mw)
cancel_button.setGeometry(314,110,75,40)
cancel_button.setFont(myfont)
cancel_button.setStyleSheet("""
                            QPushButton
                            {
                                color: white;
                                background-color: #27374D;
                                border-radius: 6px;
                                border: 1px solid white;
                            }
                            QPushButton:Pressed 
                            {
                                background-color: #16213E;
                                color: white;
                            }
                            QPushButton:hover 
                            {
                                background-color: #212A3E;
                                color: white;
                            } 
                            """)
def exit():
    mw.destroy()

cancel_button.clicked.connect(exit)


clear_button=QPushButton("Clear",mw)
clear_button.setGeometry(20,110,75,40)
clear_button.setFont(myfont)
clear_button.setStyleSheet("""
                            QPushButton
                            {
                                color: white;
                                background-color: #27374D;
                                border-radius: 6px;
                                border: 1px solid white;
                            }
                            QPushButton:Pressed 
                            {
                                background-color: #16213E;
                                color: white;
                            }
                            QPushButton:hover 
                            {
                                background-color: #212A3E;
                                color: white;
                            } 
                            """)

def clear():
    username_input.clear()
    password_input.clear()

clear_button.clicked.connect(clear)

mw.show()
sys.exit(app.exec_())