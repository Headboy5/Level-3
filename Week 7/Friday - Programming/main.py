from PySide6 import QtCore, QtWidgets, QtGui
import sys


class PackAttributes(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pack Attributes — Dark Mode")
        self.resize(480, 280)

        layout = QtWidgets.QVBoxLayout(self)

        # Title / header
        label = QtWidgets.QLabel(
            "This is a test of pack attributes",
            alignment=QtCore.Qt.AlignCenter,
        )
        label.setStyleSheet(
            "QLabel { background-color: #0f1720; color: #e6eef6; font-size: 18px; padding: 12px; "
            "border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; }"
        )

        # Buttons use a consistent dark style with subtle hover
        btn_style = (
            "QPushButton { background-color: #15202b; color: #e6eef6; font-size: 15px; "
            "padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.03); }"
            "QPushButton:hover { background-color: #1b2a36; }"
            "QPushButton:pressed { background-color: #12202a; }"
        )

        button1 = QtWidgets.QPushButton("Primary Action")
        button1.setStyleSheet(btn_style)
        button1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        button2 = QtWidgets.QPushButton("Secondary Action")
        button2.setStyleSheet(btn_style)
        button2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        # Use spacing and subtle separators to show layout behaviour
        layout.addWidget(label)
        layout.addSpacing(12)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addStretch()

        # Global widget stylesheet for this window to ensure good contrast
        self.setStyleSheet(
            "QWidget { background-color: #0b0f12; color: #e6eef6; font-family: Segoe UI, Arial, sans-serif;}"
        )


def TestPackAttributes():
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    window = PackAttributes()
    window.show()
    app.exec()


class LoginForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login — Dark Mode")
        self.resize(360, 200)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(10)

        # Dark input fields
        field_style = (
            "QLineEdit { background-color: #0f1417; color: #e6eef6; padding: 8px; "
            "border: 1px solid rgba(255,255,255,0.04); border-radius: 6px; }"
            "QLineEdit:focus { border: 1px solid #2a9df4; }"
        )

        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(field_style)

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setStyleSheet(field_style)

        # Accent button for login
        login_button = QtWidgets.QPushButton("Login")
        login_button.setStyleSheet(
            "QPushButton { background-color: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #0a84ff, stop:1 #0a7be6); "
            "color: white; padding: 10px; border-radius: 8px; border: none; font-weight: 600;}"
            "QPushButton:hover { background-color: #0c8dff; }"
            "QPushButton:pressed { background-color: #076ed1; }"
        )

        # Link-style secondary action
        no_account_button = QtWidgets.QPushButton("Don't have an account? Sign up")
        no_account_button.setStyleSheet(
            "QPushButton { background: transparent; color: #7fb7ff; padding: 6px; border: none; text-align: left; }"
            "QPushButton:hover { color: #a6d3ff; }"
        )
        no_account_button.setCursor(QtCore.Qt.PointingHandCursor)

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        layout.addWidget(no_account_button)

        self.setStyleSheet("QWidget { background-color: #0b0f12; color: #e6eef6; }")


def TestLoginForm():
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication(sys.argv)
    window = LoginForm()
    window.show()
    app.exec()


def main():
    choice = input(
        "Which program would you like to run? (Choose 1 for pack_attributes, 2 for login_form): "
    )
    match choice:
        case "1":
            TestPackAttributes()
        case "2":
            TestLoginForm()
        case _:
            print("Invalid choice. Please choose one of the valid choices.")


if __name__ == "__main__":
    main()