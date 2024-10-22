import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                               QGraphicsPixmapItem,QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QWheelEvent, QMouseEvent, QTransform, QBrush, QPixmap
from PySide6.QtCore import Qt, QTimer
import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                               QGraphicsPixmapItem, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QWheelEvent, QMouseEvent, QTransform, QBrush, QPixmap
from PySide6.QtCore import Qt, QTimer

data = {
    "nodos": [
        {"id": 1, "x": 10, "y": 40},
        {"id": 2, "x": 100, "y": 20},
        {"id": 3, "x": 200, "y": 20},
        {"id": 4, "x": 10, "y": 100},
        {"id": 5, "x": 200, "y": 100},
        {"id": 6, "x": 400, "y": 100},
        {"id": 7, "x": 10, "y": 300},
        {"id": 8, "x": 300, "y": 300},
        {"id": 9, "x": 400, "y": 300},
    ],
    "rotas": [
        {"from": 1, "to": 2}, {"from": 1, "to": 4},
        {"from": 2, "to": 3},
        {"from": 3, "to": 6}, {"from": 3, "to": 5},
        {"from": 4, "to": 5}, {"from": 4, "to": 7},
        {"from": 5, "to": 6}, {"from": 5, "to": 8},
        {"from": 6, "to": 9},
        {"from": 7, "to": 8},
        {"from": 8, "to": 9},
    ]
}

nodos = {node["id"]: (node["x"], node["y"]) for node in data["nodos"]}

class Carro(QGraphicsPixmapItem):
    def __init__(self, x, y, image_path, rota, velocidade=5, angulo=0, status="inativo"):
        super().__init__()

        # Atributos do carro
        self.status = status
        self.angulo = angulo
        self.velocidade = velocidade
        self.rota = rota
        self.ponto_atual = 0
        self.proximo_ponto = rota[self.ponto_atual] if rota else None

        # Carrega a imagem do carro
        pixmap = QPixmap(image_path)
        scale_factor = 1 / 40  # Escala para reduzir a imagem para 1/3
        self.scaled_pixmap = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor, Qt.KeepAspectRatio)
        self.setPixmap(self.scaled_pixmap)

        # Centraliza a imagem do carro no ponto inicial
        self.setPos(x - self.scaled_pixmap.width() / 2, y - self.scaled_pixmap.height() / 2)

    def proximo_ponto_rota(self):
        """Atualiza o próximo ponto da rota."""
        if self.rota and self.ponto_atual < len(self.rota) - 1:
            self.ponto_atual += 1
            self.proximo_ponto = self.rota[self.ponto_atual]
        else:
            self.proximo_ponto = None  # Chegou ao final da rota

    def calcular_angulo(self, x_atual, y_atual, x_proximo, y_proximo):
        """Calcula o ângulo entre dois pontos (atual e próximo)."""
        dx = x_proximo - x_atual
        dy = y_proximo - y_atual
        angulo_radianos = math.atan2(dy, dx)  # Calcula o ângulo em radianos
        angulo_graus = math.degrees(angulo_radianos)  # Converte para graus
        angulo_graus = angulo_graus + 270
        return angulo_graus

    def mover_para_proximo_ponto(self):
        """Move o carro para o próximo ponto da rota com base na velocidade e ajusta o ângulo."""
        if self.proximo_ponto:
            # Pega as coordenadas atuais do carro
            x_atual, y_atual = self.pos().x() + self.scaled_pixmap.width() / 2, self.pos().y() + self.scaled_pixmap.height() / 2
            x_proximo, y_proximo = self.proximo_ponto

            # Calcular a direção do movimento
            dx, dy = x_proximo - x_atual, y_proximo - y_atual
            distancia = math.hypot(dx, dy)

            if distancia > 0:
                # Normaliza o vetor de direção e move o carro
                dx /= distancia
                dy /= distancia
                x_atual += dx * self.velocidade
                y_atual += dy * self.velocidade

                # Ajusta a posição do carro, centralizando a imagem
                self.setPos(x_atual - self.scaled_pixmap.width() / 2, y_atual - self.scaled_pixmap.height() / 2)

                # Calcula o novo ângulo e ajusta a rotação do carro
                novo_angulo = self.calcular_angulo(x_atual, y_atual, x_proximo, y_proximo)
                self.angulo = novo_angulo
                
                if distancia >= self.velocidade:
                    self.ajustar_rotacao(novo_angulo)

                # Verifica se o carro chegou ao ponto
                if distancia <= self.velocidade:
                    self.proximo_ponto_rota()  # Atualiza para o próximo ponto

    def ajustar_rotacao(self, angulo):
        """Ajusta a rotação do carro ao redor de seu centro."""
        # Cria a transformação para ajustar o centro de rotação
        transform = QTransform()
        transform.translate(self.scaled_pixmap.width() / 2, self.scaled_pixmap.height() / 2)  # Move o ponto de origem para o centro
        transform.rotate(angulo)  # Aplica a rotação
        transform.translate(-self.scaled_pixmap.width() / 2, -self.scaled_pixmap.height() / 2)  # Move de volta a origem

        # Aplica a transformação ao carro
        self.setTransform(transform)


class Mapa(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mapa de Nodos")
        self.resize(800, 500)

        # Layout principal
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Layout do mapa
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        main_layout.addWidget(self.view)

        # Layout do frame 2
        right_frame = QFrame(self)
        right_frame.setFrameShape(QFrame.StyledPanel)
        right_frame.setFixedWidth(200)
        right_frame.setMaximumWidth(300)
        right_layout = QVBoxLayout()
        right_frame.setLayout(right_layout)
        main_layout.addWidget(right_frame)

        # Título do frame
        title_label = QLabel("Frame 2", self)
        title_label.setFont(QFont("Arial", 12, QFont.Bold))
        right_layout.addWidget(title_label)

        # Labels para status, velocidade, rota, ponto atual e próximo ponto
        self.status_label = QLabel("Status: inativo", self)
        self.velocidade_label = QLabel("Velocidade: 0", self)
        self.rota_label = QLabel("Rota: []", self)
        self.ponto_atual_label = QLabel("Ponto Atual: 0", self)
        self.proximo_ponto_label = QLabel("Próximo Ponto: None", self)
        self.angulo_label = QLabel(f"Ângulo: {0}", self)
        
        right_layout.addWidget(self.angulo_label)
        right_layout.addWidget(self.status_label)
        right_layout.addWidget(self.velocidade_label)
        right_layout.addWidget(self.rota_label)
        right_layout.addWidget(self.ponto_atual_label)
        right_layout.addWidget(self.proximo_ponto_label)

        # Caixa de texto para inserir a rota
        self.rota_input = QLineEdit(self)
        self.rota_input.setPlaceholderText("Insira a rota de IDs (ex: [1,2,3])")
        right_layout.addWidget(self.rota_input)

        # Botão para iniciar e parar/continuar a rota
        self.toggle_button = QPushButton("Iniciar Rota", self)
        right_layout.addWidget(self.toggle_button)
        self.toggle_button.clicked.connect(self.toggle_rota)

        # Cria o carro
        self.carro = None
        self.desenhar_nodos_e_rotas()

        # Timer para mover o carro
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover_carro)

    def desenhar_nodos_e_rotas(self):
        # Desenha as rotas (linhas entre os nodos)
        for rota in data["rotas"]:
            x1, y1 = nodos[rota["from"]]
            x2, y2 = nodos[rota["to"]]
            linha = QGraphicsLineItem(x1, y1, x2, y2)
            linha.setPen(QPen(Qt.black, 2))
            self.scene.addItem(linha)

        # Desenha os nodos (círculos ou carro)
        for node in data["nodos"]:
            x, y = node["x"], node["y"]
            id_ = node["id"]

            # Verifica se é o nodo de id 1 para desenhar o carro
            if id_ == 1:
                rota = []  # Rota vazia inicialmente
                self.carro = Carro(x, y, "SmartEntregas/imagem/carro.png", rota=rota)
                self.scene.addItem(self.carro)
            else:
                circulo = QGraphicsEllipseItem(x - 10, y - 10, 20, 20)
                circulo.setBrush(QBrush(Qt.gray))
                self.scene.addItem(circulo)

            # Adiciona um texto no centro do nodo com o ID
            texto = QGraphicsTextItem(str(id_))
            texto.setFont(QFont("Arial", 10))
            texto.setPos(x - 5, y - 10)
            self.scene.addItem(texto)

    def toggle_rota(self):
        """Alterna entre iniciar, parar e continuar a rota do carro."""
        if self.toggle_button.text() == "Iniciar Rota":
            self.iniciar_rota()
        elif self.toggle_button.text() == "Parar Carro":
            self.parar_carro()
        elif self.toggle_button.text() == "Continuar Rota":
            self.continuar_rota()

    def iniciar_rota(self):
        """Inicia o movimento do carro com base na rota inserida."""
        rota_texto = self.rota_input.text()
        try:
            # Converte o texto da rota para uma lista de IDs
            rota_ids = eval(rota_texto)
            rota_coordenadas = [nodos[id_] for id_ in rota_ids if id_ in nodos]

            # Atualiza a rota do carro e começa o movimento
            if rota_coordenadas:
                self.carro.rota = rota_coordenadas
                self.carro.ponto_atual = 0
                self.carro.proximo_ponto_rota()
                self.timer.start(100)  # Movimento com intervalo de 100 ms
                self.toggle_button.setText("Parar Carro")
            else:
                print("Erro: IDs inválidos na rota.")

        except (SyntaxError, KeyError):
            print("Erro: rota inválida. Use o formato [1, 2, 3] com IDs válidos.")

    def parar_carro(self):
        """Para o movimento do carro e atualiza o botão para continuar a rota."""
        self.timer.stop()
        self.toggle_button.setText("Continuar Rota")

    def continuar_rota(self):
        """Continua o movimento do carro a partir do ponto onde parou."""
        if self.carro:
            self.timer.start(100)  # Retoma o movimento com intervalo de 100 ms
            self.toggle_button.setText("Parar Carro")

    def mover_carro(self):
        """Move o carro para o próximo ponto da rota e atualiza as informações na interface."""
        if self.carro and self.carro.proximo_ponto:
            self.carro.mover_para_proximo_ponto()
            self.status_label.setText(f"Status: {self.carro.status}")
            self.velocidade_label.setText(f"Velocidade: {self.carro.velocidade}")
            self.rota_label.setText(f"Rota: {self.carro.rota}")
            self.ponto_atual_label.setText(f"Ponto Atual: {self.carro.ponto_atual}")
            self.proximo_ponto_label.setText(f"Próximo Ponto: {self.carro.proximo_ponto}")
            self.angulo_label.setText(f"Ângulo: {self.carro.angulo}")
        else:
            self.timer.stop()  # Para o movimento quando a rota é concluída
            self.toggle_button.setText("Iniciar Rota")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapa = Mapa()
    mapa.show()
    sys.exit(app.exec())
