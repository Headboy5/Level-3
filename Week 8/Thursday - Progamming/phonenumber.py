import sys
import webbrowser

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextBrowser,
    QMessageBox,
)
from PySide6.QtCore import Qt

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
        self.setWindowTitle("Phone Number Lookup — Prototype")
        self.resize(560, 420)

        main = QVBoxLayout(self)

        # Input row
        row = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter phone number (e.g. +447700900123 or 07700900123)")
        self.input.returnPressed.connect(self.on_lookup)
        row.addWidget(self.input)

        self.lookup_btn = QPushButton("Lookup")
        self.lookup_btn.clicked.connect(self.on_lookup)
        row.addWidget(self.lookup_btn)

        main.addLayout(row)

        # Quick action row
        action_row = QHBoxLayout()
        self.open_map_btn = QPushButton("Open location in web maps")
        self.open_map_btn.clicked.connect(self.open_maps)
        self.open_map_btn.setEnabled(False)
        action_row.addWidget(self.open_map_btn)

        self.copy_btn = QPushButton("Copy result")
        self.copy_btn.clicked.connect(self.copy_result)
        self.copy_btn.setEnabled(False)
        action_row.addWidget(self.copy_btn)

        main.addLayout(action_row)

        # Output area
        self.out = QTextBrowser()
        self.out.setOpenExternalLinks(True)
        main.addWidget(self.out)

        # Footer
        footer = QLabel("Backend: phonenumbers (if installed) — UI prototype only")
        footer.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        main.addWidget(footer)

        if phonenumbers is None:
            QMessageBox.warning(
                self,
                "Missing dependency",
                "The `phonenumbers` package is not available.\nInstall with: pip install phonenumbers",
            )

        self._last_location_text = None

    def on_lookup(self):
        text = self.input.text().strip()
        if not text:
            return

        if phonenumbers is None:
            self.out.setPlainText("ERROR: phonenumbers module is not installed. Run `pip install phonenumbers`.")
            return

        # Try to parse. Let phonenumbers infer region if a leading + not provided.
        try:
            # If user provides no plus and no region we still attempt parse with None; it may raise.
            num = phonenumbers.parse(text, None)
        except NumberParseException as exc:
            self.out.setPlainText(f"Parse error: {exc}")
            self.open_map_btn.setEnabled(False)
            self.copy_btn.setEnabled(False)
            return

        # Gather information
        is_valid = phonenumbers.is_valid_number(num)
        e164 = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
        intl = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        national = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.NATIONAL)
        country_code = num.country_code
        region = phonenumbers.region_code_for_number(num)
        carrier_name = carrier.name_for_number(num, "en") or "(unknown)"
        location = geocoder.description_for_number(num, "en") or "(unknown)"
        tzs = timezone.time_zones_for_number(num) or []

        # Build result text
        lines = []
        lines.append(f"Input: {text}")
        lines.append(f"E.164: {e164}")
        lines.append(f"International: {intl}")
        lines.append(f"National: {national}")
        lines.append(f"Valid number: {is_valid}")
        lines.append(f"Country code: +{country_code}")
        lines.append(f"Region code: {region}")
        lines.append(f"Carrier: {carrier_name}")
        lines.append(f"Geocoded location: {location}")
        lines.append(f"Timezones: {', '.join(tzs) if tzs else '(unknown)'}")

        # Link to a simple Google Maps search for the geocoded location string (if available)
        if location and location != "(unknown)":
            maps_url = f"https://www.google.com/maps/search/{location.replace(' ', '+')}"
            lines.append(f"Map search: <a href=\"{maps_url}\">Open maps</a>")
            self._last_location_text = location
            self.open_map_btn.setEnabled(True)
        else:
            self._last_location_text = None
            self.open_map_btn.setEnabled(False)

        out_text = "\n".join(lines)
        self.out.setHtml(out_text.replace('\n', '<br/>'))
        self.copy_btn.setEnabled(True)

    def open_maps(self):
        if not self._last_location_text:
            return
        url = f"https://www.google.com/maps/search/{self._last_location_text.replace(' ', '+')}"
        webbrowser.open(url)

    def copy_result(self):
        QApplication.clipboard().setText(self.out.toPlainText())


def main():
    app = QApplication(sys.argv)
    w = PhoneLookupApp()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
