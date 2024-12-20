import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                               QGraphicsPixmapItem,QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
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


import sys
import math
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, 
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem)
from PySide6.QtGui import QPen, QBrush, QFont, QPixmap, QPainter, QTransform
from PySide6.QtCore import Qt, QTimer


# Carro
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
                self.ajustar_rotacao(novo_angulo)

                # Verifica se o carro chegou ao ponto
                if distancia <= self.velocidade:
                    self.proximo_ponto_rota()  # Atualiza para o próximo ponto

    def ajustar_rotacao(self, angulo):
        """Ajusta a rotação do carro ao redor de seu centro."""
        transform = QTransform()
        transform.translate(self.scaled_pixmap.width() / 2, self.scaled_pixmap.height() / 2)  # Move o ponto de origem para o centro
        transform.rotate(angulo)  # Aplica a rotação
        transform.translate(-self.scaled_pixmap.width() / 2, -self.scaled_pixmap.height() / 2)  # Move de volta a origem

        self.setTransform(transform)


# Mapa com rotas e nodos à esquerda
class MapaRotas(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mapa de Nodos")
        self.resize(600, 500)

        # Layout principal
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Cena e vista gráfica
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        main_layout.addWidget(self.view)

        # Caixa de texto para inserir a rota
        self.rota_input = QLineEdit(self)
        self.rota_input.setPlaceholderText("Insira a rota de IDs (ex: [1,2,3])")
        main_layout.addWidget(self.rota_input)

        # Botões
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Iniciar Rota", self)
        self.stop_button = QPushButton("Parar Carro", self)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        main_layout.addLayout(button_layout)

        # Conecta os botões às funções
        self.start_button.clicked.connect(self.iniciar_rota)
        self.stop_button.clicked.connect(self.parar_carro)

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

        # Desenha todos os nodos
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

    def iniciar_rota(self):
        """Inicia o movimento do carro com base na rota inserida."""
        rota_texto = self.rota_input.text()
        try:
            # Converte o texto da rota para uma lista de IDs
            rota_ids = eval(rota_texto)

            # Verifica se todos os IDs são válidos
            for id_ in rota_ids:
                if id_ not in nodos:
                    raise KeyError(f"ID {id_} não encontrado no mapa.")

            # Converte os IDs para coordenadas de rota
            rota_coordenadas = [nodos[id_] for id_ in rota_ids]

            # Atualiza a rota do carro e começa o movimento
            self.carro.rota = rota_coordenadas
            self.carro.ponto_atual = 0
            self.carro.proximo_ponto_rota()
            self.timer.start(100)  # Movimento com intervalo de 100 ms

        except (SyntaxError, KeyError) as e:
            print(f"Erro: {e}. Use o formato [1, 2, 3] com IDs válidos.")

    def parar_carro(self):
        """Para o movimento do carro."""
        self.timer.stop()

    def mover_carro(self):
        """Move o carro para o próximo ponto da rota."""
        if self.carro and self.carro.proximo_ponto:
            self.carro.mover_para_proximo_ponto()
        else:
            self.timer.stop()  # Para o movimento quando a rota é concluída



# Mapa com status do carro à direita
class MapaStatus(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout_principal = QVBoxLayout(self)

        # Frame lateral para mostrar os status do carro
        self.status_frame = QFrame()
        self.status_frame.setFrameShape(QFrame.Box)
        self.status_layout = QVBoxLayout(self.status_frame)

        # Labels para mostrar o status do carro
        self.status_label = QLabel("Status do Carro:")
        self.status_label_velocidade = QLabel("Velocidade: N/A")
        self.status_label_angulo = QLabel("Ângulo: N/A")
        self.status_label_proximo_ponto = QLabel("Próximo ponto: N/A")

        # Adiciona os labels ao layout do frame
        self.status_layout.addWidget(self.status_label)
        self.status_layout.addWidget(self.status_label_velocidade)
        self.status_layout.addWidget(self.status_label_angulo)
        self.status_layout.addWidget(self.status_label_proximo_ponto)

        # Adiciona o frame ao layout principal
        self.layout_principal.addWidget(self.status_frame)

        # Exemplo de carro
        self.carro = Carro(10, 40, "SmartEntregas/imagem/carro.png", [(100, 100), (200, 200)], velocidade=5)

        # Atualiza os status do carro regularmente
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_status_carro)
        self.timer.start(100)  # Atualiza a cada 100ms

    def atualizar_status_carro(self):
        """Atualiza as informações de status do carro no frame lateral."""
        self.status_label_velocidade.setText(f"Velocidade: {self.carro.velocidade}")
        self.status_label_angulo.setText(f"Ângulo: {self.carro.angulo:.2f}°")
        self.status_label_proximo_ponto.setText(f"Próximo ponto: {self.carro.proximo_ponto}")


# Interface principal
class InterfacePrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface de Controle do Mapa e Status")

        # Layout principal horizontal
        layout_principal = QHBoxLayout()
        self.setLayout(layout_principal)

        # Adiciona os dois mapas (rotas à esquerda, status à direita)
        self.mapa_rotas = MapaRotas()
        self.mapa_status = MapaStatus()

        layout_principal.addWidget(self.mapa_rotas)
        layout_principal.addWidget(self.mapa_status)


# Simulação dos dados dos nodos e rotas


if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = InterfacePrincipal()
    interface.show()
    sys.exit(app.exec())
