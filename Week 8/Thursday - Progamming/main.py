from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtSvg import QSvgRenderer
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton
class UsernameAndAddress(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Info")

        # Create layout
        layout = QVBoxLayout()

        # Username label and entry
        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)

        # Address label and entry
        self.address_label = QLabel("Address:")
        self.address_entry = QLineEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_entry)

        # Button to retrieve input
        self.retrieve_button = QPushButton("Retrieve Info")
        self.retrieve_button.clicked.connect(self.retrieve_info)
        layout.addWidget(self.retrieve_button)
        self.setLayout(layout)

    def retrieve_info(self):
        username = self.username_entry.text()
        address = self.address_entry.text()
        print(f"Username: {username}, Address: {address}")
    

class UsernameAndPassword(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        # Create layout
        layout = QVBoxLayout()

        # Username label and entry
        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)

        # Password label and entry
        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)

        # Button to retrieve input
        self.retrieve_button = QPushButton("Retrieve Credentials")
        self.retrieve_button.clicked.connect(self.retrieve_credentials)
        layout.addWidget(self.retrieve_button)
        self.setLayout(layout)

    def retrieve_credentials(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        print(f"Username: {username}, Password: {password}")

def choose_app():
    app = QApplication(sys.argv)

    match input("Choose app (1: User Info, 2: Login): "):
        case "1":
            user_info_window = UsernameAndAddress()
            user_info_window.show()
        case "2":
            login_window = UsernameAndPassword()
            login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    choose_app()