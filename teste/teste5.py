from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QWheelEvent, QMouseEvent, QTransform, QBrush, QPixmap
import sys
import math

class Carro:
    def __init__(self, velocidade=0, angulo=0, posicao=(0, 0), status='parado'):
        self.velocidade = velocidade
        self.angulo = angulo
        self.posicao = list(posicao)
        self.status = status
        self.proximo_passo = None


    def mover(self, distancia):
        if self.status == 'ativo':
            dx = distancia * math.cos(math.radians(self.angulo))
            dy = distancia * math.sin(math.radians(self.angulo))
            print(f"dx={dx}\tdy{dy}")
            self.posicao[0] += dx
            self.posicao[1] += dy

    def mudar_status(self, novo_status):
        if novo_status in ['ativo', 'parado', 'sem sinal']:
            self.status = novo_status



class CarroWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.carro = Carro(velocidade=0, angulo=0, posicao=[0, 0], status='ativo')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Controle de Carro')

        # Layout principal
        main_layout = QGridLayout()
        self.setLayout(main_layout)

        # Adiciona imagem do carro
        self.carro_label = QLabel(self)
        self.pixmap = QPixmap("SmartEntregas/imagem/carro.png").scaled(200, 200, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.carro_label.setPixmap(self.pixmap)
        main_layout.addWidget(self.carro_label, 0, 0, 1, 3)


        # Layout para os botões de controle
        directional_layout = QGridLayout()

        self.up_button = QPushButton("↑")
        self.left_button = QPushButton("←")
        self.right_button = QPushButton("→")
        self.down_button = QPushButton("↓")
        self.center_button = QPushButton("pause/continue")

        directional_layout.addWidget(self.up_button, 0, 1)
        directional_layout.addWidget(self.left_button, 1, 0)
        directional_layout.addWidget(self.center_button, 1, 1)
        directional_layout.addWidget(self.right_button, 1, 2)
        directional_layout.addWidget(self.down_button, 2, 1)

        main_layout.addLayout(directional_layout, 1, 0, 1, 3)

        # Conectando os botões aos métodos
        self.up_button.clicked.connect(self.move_up)
        self.left_button.clicked.connect(self.move_left)
        self.right_button.clicked.connect(self.move_right)
        self.down_button.clicked.connect(self.move_down)
        self.center_button.clicked.connect(self.pause_continue)

        self.setMinimumSize(600, 700)
        self.show()

    def update_car_position(self):
        self.carro_label.move(int(self.carro.posicao[0]), int(self.carro.posicao[1]))
        print(self.carro.posicao)
        

    def move_up(self):
        self.carro.angulo = 270
        self.carro.mover(10)
        self.update_car_position()

    def move_down(self):
        self.carro.angulo = 90
        self.carro.mover(10)
        self.update_car_position()

    def move_left(self):
        self.carro.angulo = 180
        self.carro.mover(10)
        self.update_car_position()

    def move_right(self):
        self.carro.angulo = 0
        self.carro.mover(10)
        self.update_car_position()
        # self.rotate_image()

    def pause_continue(self):
        if self.carro.status == 'ativo':
            self.carro.mudar_status('parado')
            self.center_button.setText('continue')
        elif self.carro.status == 'parado':
            self.carro.mudar_status('ativo')
            self.center_button.setText('pause')


    def rotate_image(self):
        transform = QTransform().rotate(90)
        rotated_pixmap = self.pixmap.transformed(transform)
        self.carro_label.setPixmap(rotated_pixmap)
        # self.pixmap = rotated_pixmap
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Controle de Carro")
        self.setCentralWidget(CarroWidget())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
