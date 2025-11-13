from PySide6 import QtCore, QtWidgets, QtGui
import sys

class NameAndNumber(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Create labels
        self.name_label = QtWidgets.QLabel("Name")
        self.name_label.setStyleSheet("background-color: #2b2b2b; color: #e0e0e0; font-size: 18px; padding: 10px; border-radius: 6px;")
        
        self.number_label = QtWidgets.QLabel("Number")
        self.number_label.setStyleSheet("background-color: #2b2b2b; color: #e0e0e0; font-size: 18px; padding: 10px; border-radius: 6px;")
        
        # Create line edits for displaying values
        self.name_input = QtWidgets.QLineEdit()
        self.name_input.setText("Your Name Here")
        self.name_input.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border: 1px solid #555555; border-radius: 6px;")
        
        self.number_input = QtWidgets.QLineEdit()
        self.number_input.setText("Your Number Here")
        self.number_input.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border: 1px solid #555555; border-radius: 6px;")
        
        # Create grid layout
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(self.number_label, 1, 0)
        layout.addWidget(self.number_input, 1, 1)
        
        # Set window background color
        self.setStyleSheet("background-color: #1e1e1e;")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = NameAndNumber()
    widget.resize(450, 200)
    widget.show()

    sys.exit(app.exec())