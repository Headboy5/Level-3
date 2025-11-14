from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtSvg import QSvgRenderer
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

        # Password row with a visibility toggle button on the right
        pwd_row = QtWidgets.QHBoxLayout()
        pwd_row.setSpacing(6)
        pwd_row.addWidget(self.password_input)

        pwd_toggle = QtWidgets.QToolButton()
        pwd_toggle.setCheckable(True)
        pwd_toggle.setCursor(QtCore.Qt.PointingHandCursor)
        pwd_toggle.setToolTip("Show / hide password")
        # Small flat style so it visually sits beside the input; reduce horizontal padding
        pwd_toggle.setStyleSheet("QToolButton { background: transparent; color: #7fb7ff; border: none; padding: 2px 6px; }")

        # Simple inline SVGs for eye open / closed
        eye_open_svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
            '<path fill="none" stroke="#7fb7ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7S1 12 1 12z"/>'
            '<circle cx="12" cy="12" r="3" fill="#7fb7ff"/>'
            '</svg>'
        )
        eye_closed_svg = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
            '<path fill="none" stroke="#7fb7ff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7S1 12 1 12z"/>'
            '<path fill="none" stroke="#7fb7ff" stroke-width="1.8" stroke-linecap="round" d="M2 2 L22 22"/>'
            '</svg>'
        )

        def svg_icon(svg_text, size_px):
            # Render SVG string into QIcon
            renderer = QSvgRenderer(bytearray(svg_text, encoding='utf-8'))
            pix = QtGui.QPixmap(size_px, size_px)
            pix.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pix)
            renderer.render(painter)
            painter.end()
            return QtGui.QIcon(pix)

        # Make the toggle roughly match the line edit height and set appropriate icon size
        try:
            h = max(20, self.password_input.sizeHint().height())
            size = max(16, h - 8)
            pwd_toggle.setFixedSize(h + 4, h)
            pwd_toggle.setIconSize(QtCore.QSize(size, size))
            pwd_toggle.setIcon(svg_icon(eye_open_svg, size))
        except Exception:
            pwd_toggle.setFixedSize(36, 28)

        def _on_toggle(checked: bool):
            if checked:
                self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
                pwd_toggle.setIcon(svg_icon(eye_closed_svg, size))
                pwd_toggle.setAccessibleName("Hide password")
            else:
                self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
                pwd_toggle.setIcon(svg_icon(eye_open_svg, size))
                pwd_toggle.setAccessibleName("Show password")

        pwd_toggle.toggled.connect(_on_toggle)
        pwd_row.addWidget(pwd_toggle)

        # Accent button for login
        login_button = QtWidgets.QPushButton("Login")
        login_button.setStyleSheet(
            "QPushButton { background-color: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #0a84ff, stop:1 #0a7be6); "
            "color: white; padding: 6px 10px; border-radius: 6px; border: none; font-weight: 600;}"
            "QPushButton:hover { background-color: #0c8dff; }"
            "QPushButton:pressed { background-color: #076ed1; }"
        )
        login_button.setCursor(QtCore.Qt.PointingHandCursor)
        # Replace the link with a grey box-style signup button and place it immediately left of Login
        signup_button = QtWidgets.QPushButton("Don't have an account? Sign up")
        signup_button.setStyleSheet(
            "QPushButton { background-color: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #6f7377, stop:1 #5a5d60); "
            "color: white; padding: 6px 10px; border-radius: 6px; border: none; font-weight: 600;}"
            "QPushButton:hover { background-color: #7a7d80; }"
            "QPushButton:pressed { background-color: #4d5053; }"
        )
        signup_button.setCursor(QtCore.Qt.PointingHandCursor)

        # Put the two buttons side-by-side (signup on the left, login on the right)
        button_row = QtWidgets.QHBoxLayout()
        button_row.setSpacing(8)
        # Make them a little bigger: use fixed width and a sensible base height
        self._btn_height = 40
        self._btn_width = 160
        signup_button.setObjectName("signup_button")
        login_button.setObjectName("login_button")
        signup_button.setFixedWidth(self._btn_width)
        login_button.setFixedWidth(self._btn_width)
        signup_button.setFixedHeight(self._btn_height)
        login_button.setFixedHeight(self._btn_height)
        # Use Preferred policy so they don't stretch to fill the whole row
        signup_button.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        login_button.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        button_row.addWidget(signup_button)
        button_row.addWidget(login_button)

        # Apply initial shrink/wrap to both buttons using their fixed widths
        self._shrink_and_wrap(signup_button)
        self._shrink_and_wrap(login_button)

        layout.addWidget(self.username_input)
        layout.addLayout(pwd_row)
        layout.addLayout(button_row)

        self.setStyleSheet("QWidget { background-color: #0b0f12; color: #e6eef6; }")

    def _shrink_and_wrap(self, button, min_pt=8, padding=16):
        """Reduce the button font until the text fits its current width, and
        if it still doesn't fit try a simple two-line wrap.

        This measures button.width() so it works on live resize.
        """
        text = button.text()
        font = button.font()
        # Ensure we start with a usable point size
        pt = font.pointSize()
        if pt <= 0:
            px = font.pixelSize()
            if px > 0:
                pt = max(8, int(px * 0.75))
            else:
                pt = 12
        font.setPointSize(pt)

        available = max(8, button.width() - padding)
        fm = QtGui.QFontMetrics(font)

        # Reduce font size until it fits or reaches min_pt
        while pt > min_pt and fm.horizontalAdvance(text) > available:
            pt -= 1
            font.setPointSize(pt)
            fm = QtGui.QFontMetrics(font)

        # If it still doesn't fit, try a simple two-line wrap (split between words)
        if fm.horizontalAdvance(text) > available:
            words = text.split()
            for i in range(1, len(words)):
                first = " ".join(words[:i])
                second = " ".join(words[i:])
                fm_first = QtGui.QFontMetrics(font).horizontalAdvance(first)
                fm_second = QtGui.QFontMetrics(font).horizontalAdvance(second)
                if fm_first <= available and fm_second <= available:
                    button.setText(first + "\n" + second)
                    break

        # Apply the font and ensure the button height fits the (possibly) wrapped text
        button.setFont(font)
        # compute required height based on lines and font metrics
        lines = button.text().count("\n") + 1
        line_h = fm.lineSpacing()
        padding_v = 12  # approximate vertical padding from stylesheet
        required_h = int(line_h * lines + padding_v)
        try:
            button.setFixedHeight(max(self._btn_height, required_h))
        except Exception:
            # if called before attributes exist, ignore
            pass

    def resizeEvent(self, event):
        # Re-apply shrink/wrap when the window changes size (handles DPI or layout changes)
        super().resizeEvent(event)
        try:
            # buttons are local variables in __init__, so find them by object type in the layout
            # We assume the last layout row contains the buttons as the last layout item
            # Simpler: iterate children and find QPushButton instances used here
            for w in self.findChildren(QtWidgets.QPushButton):
                # Only adjust our signup/login buttons (ignore other buttons if present)
                if w.text():
                    self._shrink_and_wrap(w)
        except Exception:
            pass


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