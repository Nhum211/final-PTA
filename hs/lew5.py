from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("signin.ui", self)
        self.btnforgot.clicked.connect(self.show_resister)
        self.btnmaa.clicked.connect(self.show_signup)
        self.btnsignin.clicked.connect(self.check_login)
        self.msg_box = QMessageBox()

    def check_login(self):
        email = self.txtemail.text()
        password = self.txtpassword.text()

        if email == "admin" and password == "admin":
              main.show()
              self.close()
        else:
            self.msg_box.setText("loi") 
            self.msg_box.exec()
    def show_resister(self):
         resister_window.show()
         self.close
    def show_signup(self):
         signup_window.show()
         self.close()
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.btnwc.clicked.connect(self.show_giaodien)
    def show_giaodien(self):
         giaodien_window.show()
         self.close()
class Giaodien(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("giaodien.ui", self)
        self.btnsk.clicked.connect(self.show_sukien)
        self.btngt.clicked.connect(self.show_gioithieu)
        self.btnlydo.clicked.connect(self.show_noinfo)
        self.btncn.clicked.connect(self.show_no)
        self.btngc.clicked.connect(self.show_noinfo)
    def show_noinfo(self):
         noinfo_window.show()
         self.close()
    def show_no(self):
         no_window.show()
         self.close()
    def show_gioithieu(self):
         gioithieu_window.show()
         self.close()
    def show_sukien(self):
         sukien_window.show()
         self.close()
class Gioithieu(QMainWindow):
     def __init__(self):
          super().__init__()
          uic.loadUi("gioithieu.ui", self)
          self.btnsk.clicked.connect(self.show_sukien)
          self.btntt.clicked.connect(self.show_giaodien)
     def show_giaodien(self):
         giaodien_window.show()
         self.close()
     def show_sukien(self):
         sukien_window.show()
         self.close()
class Noinfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("noinfo.ui", self)
        self.btninfo.clicked.connect(self.show_giaodien)
    def show_giaodien(self):
         giaodien_window.show()
         self.close()
class No(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("no.ui", self)
        self.btnno.clicked.connect(self.show_giaodien)
    def show_giaodien(self):
         giaodien_window.show()
         self.close()
class Sukien(QMainWindow):
     def __init__(self):
          super().__init__()
          uic.loadUi("sukien.ui", self)
          self.btngt.clicked.connect(self.show_gioithieu)
          self.btntt.clicked.connect(self.show_giaodien)
          self.xacnhan.clicked.connect(self.check_xacnhan)
          self.msg_box = QMessageBox()
     def show_gioithieu(self):
         gioithieu_window.show()
         self.close()
     def show_giaodien(self):
         giaodien_window.show()
         self.close()
     def check_xacnhan(self):
        sdt = self.txtsdt.text()
        skgt = self.txtsktg.text()

        if sdt == "admin" and skgt == "admin":
              self.msg_box.setText("dang ki thanh cong") 
              self.msg_box.exec()
        else:
            self.msg_box.setText("loi") 
            self.msg_box.exec()
class Signup(QMainWindow):
     def __init__(self):
          super().__init__()
          uic.loadUi("signup.ui", self)
          self.btnahaa.clicked.connect(self.show_login)
          self.btnsignup.clicked.connect(self.check_login)
     def check_login(self):
        email = self.txtemail.text()
        password = self.txtpassword.text()

        if email == "admin" and password == "admin":
              main.show()
              self.close()
        else:
            self.msg_box.setText("loi") 
            self.msg_box.exec()
     def show_login(self):
         login_window.show()
         self.close

class Resister(QMainWindow):
     def __init__(self):
          super().__init__()
          uic.loadUi("resister.ui", self)
          self.btnresister.clicked.connect(self.check_resister)
          self.msg_box = QMessageBox()
     def check_resister(self):
        email = self.txtemail.text()
        if email == "admin":
            self.msg_box.setText("Thông báo đã được gửi đến email.") 
            self.msg_box.exec()
        else:
            self.msg_box.setText("loi") 
            self.msg_box.exec()
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Login()
        window.show()
        login_window = Login()
        sukien_window = Sukien()
        noinfo_window = Noinfo()
        no_window = No()
        gioithieu_window = Gioithieu()
        signup_window = Signup()
        trangchu_window = Gioithieu()
        resister_window = Resister()
        giaodien_window = Giaodien()
        main_window = Main()
        main = Main()
        app.exec()