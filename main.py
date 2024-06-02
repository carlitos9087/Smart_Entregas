import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Simple PySide6 App')

        self.layout = QVBoxLayout()

        self.input = QLineEdit(self)
        self.add_button = QPushButton('Add Item', self)
        self.list_widget = QListWidget(self)

        self.layout.addWidget(self.input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.list_widget)

        self.setLayout(self.layout)

        self.add_button.clicked.connect(self.add_item)

    def add_item(self):
        item = self.input.text()
        if item:
            self.list_widget.addItem(item)
            self.input.clear()
        else:
            self.show_message("Please enter an item.")

    def show_message(self, message):
        QMessageBox.information(self, "Info", message)

def main():
    app = QApplication(sys.argv)

    main_app = MainApp()
    main_app.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
