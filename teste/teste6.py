from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QTransform
import sys
import math

class CarroWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.carro = Carro(velocidade=0, angulo=0, posicao=[0, 0], status='ativo')  # Posição inicial centralizada
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Controle de Carro')

        # Layout principal
        main_layout = QGridLayout()
        self.setLayout(main_layout)

        # Adiciona imagem do carro
        self.carro_label = QLabel(self)
        self.original_pixmap = QPixmap("SmartEntregas/imagem/carro.png").scaled(50, 50, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.carro_label.setPixmap(self.original_pixmap)
        self.carro_label.setGeometry(0, 0, 50, 50)  # Define a posição inicial da label do carro

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


        # main_layout.addLayout(directional_layout, 1, 0, 1, 3)
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
        """Atualiza a posição e a rotação da imagem do carro."""
        # Mover a label do carro para a nova posição
        self.carro_label.setGeometry(int(self.carro.posicao[0]), int(self.carro.posicao[1]), 50, 50)

        # Atualizar a rotação da imagem
        self.rotate_image()
        print(f"Posição: {self.carro.posicao}, Ângulo: {self.carro.angulo}")

    def move_left(self):
        self.carro.angulo = 180
        self.carro.mover(10)
        self.update_car_position()

    def move_right(self):
        self.carro.angulo = 0
        self.carro.mover(10)
        self.update_car_position()

    def move_up(self):
        self.carro.angulo = 90
        self.carro.mover(10)
        self.update_car_position()

    def move_down(self):
        self.carro.angulo = 270
        self.carro.mover(10)
        self.update_car_position()

    def rotate_image(self):
        """Gira a imagem do carro com base no ângulo atual."""
        transform = QTransform().rotate(self.carro.angulo-90)
        if self.carro.angulo == 90 or self.carro.angulo == 270:
            transform = QTransform().rotate(self.carro.angulo+90)
        rotated_pixmap = self.original_pixmap.transformed(transform)
        self.carro_label.setPixmap(rotated_pixmap)

    def pause_continue(self):
        """Função de pause/continue - implementação a ser definida."""
        pass

# Classe Carro com método de movimento
class Carro:
    def __init__(self, velocidade, angulo, posicao, status):
        self.velocidade = velocidade
        self.angulo = angulo
        self.posicao = posicao
        self.status = status

    def mover(self, distancia):
        """Move o carro na direção do ângulo atual."""
        radiano = math.radians(self.angulo)
        self.posicao[0] += distancia * math.cos(radiano)
        self.posicao[1] -= distancia * math.sin(radiano)  # Subtração para ajustar o sistema de coordenadas da tela

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarroWidget()
    window.show()
    sys.exit(app.exec())
