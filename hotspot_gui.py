import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QFont, QColor
import random

class AutoAttendanceSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Attendance System")
        self.setGeometry(100, 100, 600, 500)
        self.setFont(QFont("Times-New-Roman", 12))

        # Create the main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Add the "Start Scanning" button
        self.start_scanning_button = QPushButton("Start Scanning")
        self.start_scanning_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 8px 16px;")
        self.main_layout.addWidget(self.start_scanning_button)

        self.table = QTableWidget()
        self.table.setColumnCount(10)  # number of columns in the table
        self.table.setRowCount(8)  # number of rows in the table
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        # self.table.horizontalHeader().setFont(QFont("Times-New-Roman", 14))
        # self.table.horizontalHeader().setStyleSheet("padding: 16px;")
        # self.table.verticalHeader().setFont(QFont("Times-New-Roman", 14))
        # self.table.verticalHeader().setStyleSheet("padding: 8px;")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setStyleSheet("background-color: white; color: #555; font-size: 14px; padding: 8px;")
        self.main_layout.addWidget(self.table)

        # Add the present and absent lists
        self.lists_layout = QHBoxLayout()
        self.present_label = QLabel("Present:")
        self.present_label.setStyleSheet("font-size: 16px;")
        self.present_list = QTextEdit()
        self.present_list.setStyleSheet("background-color: #f2f2f2; color: #555; font-size: 14px; padding: 8px;")
        self.present_list.setReadOnly(True)
        self.absent_label = QLabel("Absent:")
        self.absent_label.setStyleSheet("font-size: 16px;")
        self.absent_list = QTextEdit()
        self.absent_list.setStyleSheet("background-color: #f2f2f2; color: #555; font-size: 14px; padding: 8px;")
        self.absent_list.setReadOnly(True)
        self.lists_layout.addWidget(self.present_label)
        self.lists_layout.addWidget(self.present_list)
        self.lists_layout.addWidget(self.absent_label)
        self.lists_layout.addWidget(self.absent_list)
        self.main_layout.addLayout(self.lists_layout)

        # # Add a QLabel to indicate the orientation of the table
        # self.table_orientation_label = QLabel()
        # self.table_orientation_label.setFixedSize(50, 50)
        # self.table_orientation_label.setStyleSheet("background-color: black;")
        # self.main_layout.addWidget(self.table_orientation_label)

        # Connect the "Start Scanning" button to the function that scans and updates the UI
        self.start_scanning_button.clicked.connect(self.scan_and_update_ui)

    def scan_and_update_ui(self):
        # Update the table with the matrix of seats
      for row in range(8):
        for col in range(10):
            item = QTableWidgetItem("X" if (row+col)%3==0 else "?" if (row+col)%3==1 else "✓")  # set X, ?, or ✓ in the cell
            item.setTextAlignment(4)  # center-align the text in the cell
            item.setFlags(item.flags() ^ 0x0001)  # make the cell non-editable
            self.table.setItem(row, col, item)

            # Sample list of register numbers
            register_numbers = list(range(133, 200))

            # Generate random lists for present and absent
            present_list = random.sample(register_numbers, k=30)
            absent_list = [num for num in register_numbers if num not in present_list]

            # Set the text for the present and absent lists
            self.present_list.setPlainText("\n".join(str(num) for num in present_list))
            self.absent_list.setPlainText("\n".join(str(num) for num in absent_list))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutoAttendanceSystem()
    window.show()
    sys.exit(app.exec_())










