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

class ExpandAndFill(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Create Label
        self.label = QtWidgets.QLabel("Buttons expand to fill available space", alignment=QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: #2b2b2b; color: #e0e0e0; font-size: 18px; padding: 10px; border-radius: 6px;")
        # Create buttons
        self.button1 = QtWidgets.QPushButton("Button 1")
        self.button1.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
        self.button1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button1.clicked.connect(self.button1_clicked)
        
        self.button2 = QtWidgets.QPushButton("Button 2")
        self.button2.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
        self.button2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button2.clicked.connect(self.button2_clicked)

        self.button3 = QtWidgets.QPushButton("Button 3")
        self.button3.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
        self.button3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button3.clicked.connect(self.button3_clicked)
        
        # Create horizontal layout: 1 button on left, 2 on right
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.button1)
        
        # Create a vertical layout for the right side buttons
        right_layout = QtWidgets.QVBoxLayout()
        right_layout.addWidget(self.button2)
        right_layout.addWidget(self.button3)
        
        layout.addLayout(right_layout)
        
        # Set buttons to expand and fill available space
        layout.setStretch(0, 1)  # Button 1 takes half
        layout.setStretch(1, 1)  # Right side takes half
        
        # Set window background color
        self.setStyleSheet("background-color: #1e1e1e;")
    
    def button1_clicked(self):
        print("Button 1 Pressed")
        # Toggle color on click
        current_style = self.button1.styleSheet()
        if "#3c3c3c" in current_style:
            self.button1.setStyleSheet("background-color: #5a5a5a; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
        else:
            self.button1.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
    
    def button2_clicked(self):
        print("Button 2 Pressed")
        # Toggle color on click
        current_style = self.button2.styleSheet()
        if "#3c3c3c" in current_style:
            self.button2.setStyleSheet("background-color: #5a5a5a; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
        else:
            self.button2.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
    
    def button3_clicked(self):
        print("Button 3 Pressed")
        # Toggle color on click
        current_style = self.button3.styleSheet()
        if "#3c3c3c" in current_style:
            self.button3.setStyleSheet("background-color: #5a5a5a; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")
        else:
            self.button3.setStyleSheet("background-color: #3c3c3c; color: #ffffff; font-size: 16px; padding: 10px; border-radius: 6px;")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = NameAndNumber()
    widget.resize(450, 200)
    widget.show()

    widget2 = ExpandAndFill()
    widget2.resize(450, 100)
    widget2.show()

    sys.exit(app.exec())