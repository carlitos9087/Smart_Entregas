import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QFrame
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QRect


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circle_x = 100
        self.circle_y = 100
        self.circle_radius = 10
        self.setMinimumSize(500, 200)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor("yellow"))
        painter.drawEllipse(QRect(self.circle_x - self.circle_radius, 
                                  self.circle_y - self.circle_radius, 
                                  self.circle_radius * 2, 
                                  self.circle_radius * 2))

    def move_circle(self, dx, dy):
        self.circle_x += dx
        self.circle_y += dy
        self.update()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Widget que contém o círculo
        self.circle_widget = CircleWidget()

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.circle_widget)

        # Frame lateral com os botões
        button_frame = QFrame(self)
        directional_layout = QGridLayout(button_frame)
        
        # Botões de direção
        up_button = QPushButton("↑")
        left_button = QPushButton("←")
        right_button = QPushButton("→")
        down_button = QPushButton("↓")
        center_button = QPushButton("OK")
        
        # Conectando os botões com as ações de movimento
        up_button.clicked.connect(lambda: self.circle_widget.move_circle(0, -10))
        down_button.clicked.connect(lambda: self.circle_widget.move_circle(0, 10))
        left_button.clicked.connect(lambda: self.circle_widget.move_circle(-10, 0))
        right_button.clicked.connect(lambda: self.circle_widget.move_circle(10, 0))
        
        # Adicionando os botões ao layout de grade
        directional_layout.addWidget(up_button, 0, 1)
        directional_layout.addWidget(left_button, 1, 0)
        directional_layout.addWidget(center_button, 1, 1)
        directional_layout.addWidget(right_button, 1, 2)
        directional_layout.addWidget(down_button, 2, 1)
        
        # Adicionando o frame dos botões ao layout principal
        main_layout.addWidget(button_frame)

        # Configuração da janela principal
        self.setLayout(main_layout)
        self.setWindowTitle("Move o Círculo")

        # Garantir que a janela receba os eventos de teclado
        self.setFocusPolicy(Qt.StrongFocus)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.circle_widget.move_circle(0, -10)
        elif event.key() == Qt.Key_Down:
            self.circle_widget.move_circle(0, 10)
        elif event.key() == Qt.Key_Left:
            self.circle_widget.move_circle(-10, 0)
        elif event.key() == Qt.Key_Right:
            self.circle_widget.move_circle(10, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setFocus()  # Garante que o foco esteja na janela principal
    sys.exit(app.exec())
