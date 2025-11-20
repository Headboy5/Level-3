import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
    from phonenumbers.phonenumberutil import NumberParseException
except Exception as e:
    phonenumbers = None
    geocoder = carrier = timezone = None
    NumberParseException = Exception


class PhoneLookupApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NHS Track and Trace - Phone Number Lookup")
        self.resize(560, 420)

        main = QVBoxLayout(self)

        # INPUT ROW
        row = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter phone number (e.g. +447700900123 or 07700900123)")
        self.input.returnPressed.connect(self.on_lookup)
        row.addWidget(self.input)

        self.lookup_btn = QPushButton("Lookup")
        self.lookup_btn.clicked.connect(self.on_lookup)
        row.addWidget(self.lookup_btn)

        main.addLayout(row)

        # OUTPUT AREA
        output_font = QFont()
        output_font.setPointSize(10)

        self.location_label = QLabel("Location:")
        self.location_label.setFont(output_font)
        main.addWidget(self.location_label)

        self.country_label = QLabel("Country code:")
        self.country_label.setFont(output_font)
        main.addWidget(self.country_label)

        self.timezone_label = QLabel("Time zone:")
        self.timezone_label.setFont(output_font)
        main.addWidget(self.timezone_label)

        self.carrier_label = QLabel("Carrier:")
        self.carrier_label.setFont(output_font)
        main.addWidget(self.carrier_label)

        self.valid_label = QLabel("Valid Number:")
        self.valid_label.setFont(output_font)
        main.addWidget(self.valid_label)

        main.addStretch()

        # DARK MODE STYLING
        self.setStyleSheet("""
            QWidget {
                background-color: #0b0f12;
                color: #e6eef6;
                font-family: Segoe UI, Arial, sans-serif;
            }
            QLineEdit {
                background-color: #0f1417;
                color: #e6eef6;
                padding: 8px;
                border: 1px solid rgba(255,255,255,0.04);
                border-radius: 6px;
            }
            QLineEdit:focus {
                border: 1px solid #2a9df4;
            }
            QPushButton {
                background-color: #15202b;
                color: #e6eef6;
                font-size: 15px;
                padding: 8px 12px;
                border-radius: 8px;
                border: 1px solid rgba(255,255,255,0.03);
            }
            QPushButton:hover {
                background-color: #1b2a36;
            }
            QPushButton:pressed {
                background-color: #12202a;
            }
            QLabel {
                color: #e6eef6;
                padding: 4px;
            }
        """)

        if phonenumbers is None:
            QMessageBox.warning(
                self,
                "Missing dependency",
                "The `phonenumbers` package is not available.\nInstall with: pip install phonenumbers",
            )

    def on_lookup(self):
        text = self.input.text().strip()
        if not text:
            return

        if phonenumbers is None:
            QMessageBox.critical(self, "Error", "phonenumbers module is not installed.\nRun: pip install phonenumbers")
            return

        # TRY TO PARSE - DEFAULT TO GB (UK) FOR NUMBERS WITHOUT COUNTRY CODE
        try:
            # FIRST TRY WITH GB REGION (FOR UK NUMBERS LIKE 07xxx)
            num = phonenumbers.parse(text, "GB")
        except NumberParseException:
            try:
                # IF THAT FAILS, TRY WITH NO REGION (FOR INTERNATIONAL NUMBERS WITH +)
                num = phonenumbers.parse(text, None)
            except NumberParseException as exc:
                QMessageBox.warning(self, "Parse Error", f"Could not parse number:\n{exc}")
                self.location_label.setText("Location:")
                self.country_label.setText("Country code:")
                self.timezone_label.setText("Time zone:")
                self.carrier_label.setText("Carrier:")
                self.valid_label.setText("Valid Number:")
                return

        # GATHER INFORMATION
        is_valid = phonenumbers.is_valid_number(num)
        country_code = f"+{num.country_code}"
        region = phonenumbers.region_code_for_number(num)
        carrier_name = carrier.name_for_number(num, "en") or "Unknown"
        location = geocoder.description_for_number(num, "en") or "Unknown"
        tzs = timezone.time_zones_for_number(num) or []
        tz_str = ", ".join(tzs) if tzs else "Unknown"

        # UPDATE LABELS
        self.location_label.setText(f"Location: {location}")
        self.country_label.setText(f"Country code: {country_code} ({region})")
        self.timezone_label.setText(f"Time zone: {tz_str}")
        self.carrier_label.setText(f"Carrier: {carrier_name}")
        self.valid_label.setText(f"Valid Number: {'Yes' if is_valid else 'No'}")


def main():
    app = QApplication(sys.argv)
    w = PhoneLookupApp()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
