import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                               QGridLayout,
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem,
                               QGraphicsLineItem, QGraphicsPixmapItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QWheelEvent, QMouseEvent, QTransform, QPixmap
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


class MapWidget(QGraphicsView):

    def __init__(self, janela_principal):
        super().__init__()

        self.shortest_path = []
        self.rotas_bloqueadas = []

        self.current_angle = 0
        self._zoom = 1
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedSize(600, 400)

        self.carro = None

        self.janela_principal = janela_principal

        self.draw_map([1])
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover_carro)

    def set_shortest_path(self, path):
        self.shortest_path = path
        print(self.shortest_path)
        self.janela_principal.start_button.setEnabled(True)  # Ativa o botão de iniciar rota
        self.draw_map(path)

    def draw_map(self, rota):

        self._scene.clear()

        #pega as informações necessarias para criar os obstaculos e roda o processo de criar
        #obstaculos todas as vezes aqui, vc sabe
        pen = QPen(Qt.black)
        pen.setWidth(2)
        x_inicial = nodos[1][0]
        y_inicial = nodos[1][1]

        # Desenhar arestas
        for edge in data["rotas"]:
            x1, y1 = nodos[edge["from"]]
            x2, y2 = nodos[edge["to"]]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(pen)
            self._scene.addItem(line)

        # Desenhar nodos
        for node in data["nodos"]:
            x, y = node["x"], node["y"]
            ellipse = QGraphicsEllipseItem(x - 5, y - 5, 10, 10)
            ellipse.setPen(pen)
            ellipse.setBrush(Qt.black)
            self._scene.addItem(ellipse)

            text = QGraphicsTextItem(f'Casa {node["id"]}')
            text.setFont(QFont("Arial", 10))
            text.setPos(x + 5, y + 5)
            self._scene.addItem(text)

        for obstacle in self.rotas_bloqueadas:
            rota_coordenadas = [nodos[id_] for id_ in obstacle if id_ in nodos]
            x1, y1 = rota_coordenadas[0]
            x2, y2 = rota_coordenadas[1]
            x_obstaculo = (x1 + x2) / 2
            y_obstaculo = (y1 + y2) / 2

            # Carrega a imagem do obstáculo e adiciona na cena
            pixmap = QPixmap("")
            obstacle_item = QGraphicsPixmapItem(pixmap)
            obstacle_item.setPos(x_obstaculo - pixmap.width() / 2, y_obstaculo - pixmap.height() / 2)
            self._scene.addItem(obstacle_item)

        # Desenhar o caminho mais curto
        if self.shortest_path:
            pen = QPen(Qt.blue)
            pen.setWidth(2)
            x_inicial = nodos[rota[0]][0]
            y_inicial = nodos[rota[0]][1]
            for i in range(len(self.shortest_path) - 1):
                x1, y1 = nodos[self.shortest_path[i]]
                x2, y2 = nodos[self.shortest_path[i + 1]]
                line = QGraphicsLineItem(x1, y1, x2, y2)
                line.setPen(pen)
                self._scene.addItem(line)




        #Adiciona o carro com a coordenada do primeiro ponto da rota calculada
        self.carro = Carro(x_inicial,
                           y_inicial,
                           "C:/Users/pedro/Downloads/1b3aee654bc2b25ec67891c2bea8e313",
                           "rota",
                           5,
                           0,
                           status="ativo")
        self._scene.addItem(self.carro)



    def wheelEvent(self, event: QWheelEvent):
        factor = 1.25 if event.angleDelta().y() > 0 else 0.8
        self._zoom *= factor
        self.scale(factor, factor)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.NoDrag)
        super().mouseReleaseEvent(event)

    def iniciar_rota(self):
        """Inicia o movimento do carro com base na rota inserida."""

        try:
            # Converte o texto da rota para uma lista de IDs

            rota_coordenadas = [nodos[id_] for id_ in
                                tsp([int(x) for x in self.janela_principal.points_input.text().split(",")], self.rotas_bloqueadas) if
                                id_ in nodos]
            print(rota_coordenadas)
            # Atualiza a rota do carro e começa o movimento
            if rota_coordenadas:
                self.carro.rota = rota_coordenadas
                self.carro.ponto_atual = 0
                self.carro.proximo_ponto_rota()
                self.timer.start(100)  # Movimento com intervalo de 100 ms

                self.janela_principal.calculate_button.setEnabled(False)

                self.janela_principal.continuar_button.setEnabled(False)

                self.janela_principal.up_button.setEnabled(False)
                self.janela_principal.down_button.setEnabled(False)
                self.janela_principal.right_button.setEnabled(False)
                self.janela_principal.left_button.setEnabled(False)

                self.janela_principal.start_button.setEnabled(False)
                self.janela_principal.stop_button.setEnabled(True)
            else:
                print("Erro: IDs inválidos na rota.")



        except (SyntaxError, KeyError):
            print("Erro: rota inválida. Use o formato [1, 2, 3] com IDs válidos.")

    def parar_carro(self):
        """Para o movimento do carro e ativa o botão de continuar."""
        self.timer.stop()
        self.janela_principal.calculate_button.setEnabled(True)
        self.janela_principal.continuar_button.setEnabled(True)
        self.janela_principal.start_button.setEnabled(True)
        self.janela_principal.stop_button.setEnabled(False)  # Desativa o botão de parar
        self.janela_principal.up_button.setEnabled(True)

        self.janela_principal.down_button.setEnabled(True)
        self.janela_principal.right_button.setEnabled(True)
        self.janela_principal.left_button.setEnabled(True)
        self.janela_principal.start_button.setEnabled(True)


    def continuar_rota(self):
        """Continua o movimento do carro a partir do ponto onde parou."""
        if self.carro:
            self.timer.start(100)  # Retoma o movimento com intervalo de 100 ms
            self.janela_principal.calculate_button.setEnabled(False)
            self.janela_principal.continuar_button.setEnabled(False)  # Desativa o botão de continuar
            self.janela_principal.up_button.setEnabled(False)
            self.janela_principal.down_button.setEnabled(False)
            self.janela_principal.right_button.setEnabled(False)
            self.janela_principal.left_button.setEnabled(False)

            self.janela_principal.start_button.setEnabled(False)
            self.janela_principal.stop_button.setEnabled(True)

    def mover_carro(self):
        """Move o carro para o próximo ponto da rota e atualiza as informações na interface."""
        if self.carro and self.carro.proximo_ponto:
            self.carro.mover_para_proximo_ponto()
            self.janela_principal.status_label.setText(f"Status: {self.carro.status}")
            self.janela_principal.velocidade_label.setText(f"Velocidade: {self.carro.velocidade}")
            self.janela_principal.rota_label.setText(f"Rota: {self.carro.rota}")
            self.janela_principal.ponto_atual_label.setText(f"Ponto Atual: {self.carro.ponto_atual}")
            self.janela_principal.proximo_ponto_label.setText(f"Próximo Ponto: {self.carro.proximo_ponto}")
        else:
            self.timer.stop()  # Para o movimento quando a rota é concluída
            self.janela_principal.continuar_button.setEnabled(False)  # Desativa o botão de continuar

    def adicionar_obstaculo(self, rota_texto):
        """Permite adicionar um obstáculo em uma rota específica."""

        try:
            # Converte o texto da rota para uma lista de IDs
            rota_ids = eval(rota_texto)
            print (rota_ids)
            for rotas in data["rotas"]:
                if (rota_ids[0] == rotas["from"] or rota_ids[0] == rotas["to"]) and (rota_ids[1] == rotas["from"] or rota_ids[1] == rotas["to"]):


                    print("rotas bloqueadas:",self.rotas_bloqueadas)
                    rota_coordenadas = [nodos[id_] for id_ in rota_ids if id_ in nodos]

                    if len(rota_coordenadas) >= 2:
                        # Adiciona o obstáculo entre os dois primeiros pontos da rota
                        x1, y1 = rota_coordenadas[0]
                        x2, y2 = rota_coordenadas[1]
                        x_obstaculo = (x1 + x2) / 2
                        y_obstaculo = (y1 + y2) / 2

                        # Carrega a imagem do obstáculo e adiciona na cena
                        pixmap = QPixmap("C:/Users/pedro/Downloads/images.png")
                        obstacle_item = QGraphicsPixmapItem(pixmap)
                        obstacle_item.setPos(x_obstaculo - pixmap.width() / 2, y_obstaculo - pixmap.height() / 2)
                        self._scene.addItem(obstacle_item)

                        # Armazena o obstáculo para referência futura

                        self.rotas_bloqueadas.append((rota_ids[0], rota_ids[1]))

                    else:
                        print("Erro: IDs inválidos ou insuficientes na rota para adicionar um obstáculo.")

        except (SyntaxError, KeyError):
            print("Erro: rota inválida. Use o formato [1, 2, 3] com IDs válidos.")

    def remover_obstaculos(self):
        """Remove todos os obstáculos do mapa"""
        # Limpa a lista de obstáculos e de rotas bloqueadas
        self.rotas_bloqueadas = []
        self.draw_map([1])




class JanelaPrincipal(QWidget):

    def __init__(self):
        super().__init__()
        self.current_angle = 0
        self.setWindowTitle("Controlador Carro")
        self.setGeometry(100, 100, 700, 550)

        self.main_layout = QHBoxLayout(self)

        # Frame 1: Title, Map, Button
        frame1 = QFrame()
        frame1.setFrameShape(QFrame.StyledPanel)
        frame1_layout = QVBoxLayout()

        title1 = QLabel("Nome do Mapa")
        self.map_widget = MapWidget(self)
        button1 = QPushButton("Carregar Mapa")

        # Input fields and button for calculating shortest path
        input_layout = QHBoxLayout()
        self.points_input = QLineEdit()
        self.points_input.setPlaceholderText("IDs das Casas (separados por vírgula)")
        input_layout.addWidget(self.points_input)

        self.calculate_button = QPushButton("Calcular Rota Mais Curta")
        self.calculate_button.clicked.connect(self.calculate_shortest_path)
        input_layout.addWidget(self.calculate_button)

        frame1_layout.addWidget(title1)
        frame1_layout.addWidget(self.map_widget)
        frame1_layout.addWidget(button1)
        frame1_layout.addWidget(self.points_input)
        frame1_layout.addWidget(self.calculate_button)
        frame1_layout.addWidget(self.calculate_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Directional Buttons and Additional Buttons
        frame2 = QFrame()
        frame2.setFrameShape(QFrame.StyledPanel)
        frame2_layout = QVBoxLayout()

        directional_layout = QGridLayout()

        self.up_button = QPushButton("↑")
        self.up_button.setEnabled(True)
        self.left_button = QPushButton("←")
        self.left_button.setEnabled(True)
        self.right_button = QPushButton("→")
        self.right_button.setEnabled(True)
        self.down_button = QPushButton("↓")
        self.down_button.setEnabled(True)
        self.center_button = QPushButton("SCAN")

        directional_layout.addWidget(self.up_button, 0, 1)
        directional_layout.addWidget(self.left_button, 1, 0)
        directional_layout.addWidget(self.center_button, 1, 1)
        directional_layout.addWidget(self.right_button, 1, 2)
        directional_layout.addWidget(self.down_button, 2, 1)

        comp_1_button = QPushButton("Comp. 1 Fechado")
        comp_2_button = QPushButton("Comp. 2 Aberto")

        self.start_button = QPushButton("Iniciar Rota", self)
        self.start_button.setEnabled(False)
        self.stop_button = QPushButton("Parar Carro", self)
        self.stop_button.setEnabled(False)
        self.continuar_button = QPushButton("Continuar Rota", self)
        self.continuar_button.setEnabled(False)

        frame2_layout.addLayout(directional_layout)
        frame2_layout.addWidget(comp_1_button)
        frame2_layout.addWidget(comp_2_button)
        frame2_layout.addWidget(self.start_button)
        frame2_layout.addWidget(self.stop_button)
        frame2_layout.addWidget(self.continuar_button)
        frame2.setLayout(frame2_layout)

        self.up_button.clicked.connect(lambda: self.map_widget.carro.movimento_manual(True))
        self.down_button.clicked.connect(lambda: self.map_widget.carro.movimento_manual(False))
        self.right_button.clicked.connect(lambda: self.map_widget.carro.ajustar_rotacao(self.map_widget.carro.angulo + 10))
        self.left_button.clicked.connect(lambda: self.map_widget.carro.ajustar_rotacao(self.map_widget.carro.angulo - 10))
        self.center_button.clicked.connect(self.map_widget.carro.scan)

        self.start_button.clicked.connect(self.map_widget.iniciar_rota)
        self.stop_button.clicked.connect(self.map_widget.parar_carro)
        self.continuar_button.clicked.connect(self.map_widget.continuar_rota)

        # Botão para adicionar obstáculo
        self.add_obstacle_button = QPushButton("Adicionar Obstáculo", self)
        frame2_layout.addWidget(self.add_obstacle_button)
        self.add_obstacle_button.clicked.connect(lambda:self.map_widget.adicionar_obstaculo(self.points_input.text()))

        # Botão para remover obstáculos
        self.remove_obstacle_button = QPushButton("Remover todos Obstáculos", self)
        frame2_layout.addWidget(self.remove_obstacle_button)
        self.remove_obstacle_button.clicked.connect(self.map_widget.remover_obstaculos)

        # Frame 3: Title, Subtitle, Image, Orientation
        frame3 = QFrame()
        frame3.setFrameShape(QFrame.StyledPanel)
        frame3_layout = QVBoxLayout()

        self.title3 = QLabel("Posição Atual: Rota R2")
        self.subtitle3 = QLabel("Ação Atual: Standby")

        self.rotate_button = QPushButton("Girar Imagem")
        self.rotate_button.clicked.connect(self.rotate_image)

        # Labels para status, velocidade, rota, ponto atual e próximo ponto
        self.status_label = QLabel("Status: inativo", self)
        self.velocidade_label = QLabel("Velocidade: 0", self)
        self.rota_label = QLabel("Rota: []", self)
        self.ponto_atual_label = QLabel("Ponto Atual: 0", self)
        self.proximo_ponto_label = QLabel("Próximo Ponto: None", self)
        self.angulo_label = QLabel(f"Ângulo: {0}", self)

        frame3_layout.addWidget(self.title3)
        frame3_layout.addWidget(self.subtitle3)
        frame3_layout.addWidget(self.angulo_label)
        frame3_layout.addWidget(self.status_label)
        frame3_layout.addWidget(self.velocidade_label)
        frame3_layout.addWidget(self.rota_label)
        frame3_layout.addWidget(self.ponto_atual_label)
        frame3_layout.addWidget(self.proximo_ponto_label)
        frame3_layout.addWidget(self.rotate_button)

        frame3.setLayout(frame3_layout)

        # Add frames to main layout
        self.main_layout.addWidget(frame1)
        self.main_layout.addWidget(frame2)
        self.main_layout.addWidget(frame3)

        self.setLayout(self.main_layout)

    def rotate_image(self):
        # Rotate the image by 90 degrees
        self.current_angle = (self.current_angle + 90) % 360
        pixmap = self.image_label.pixmap()
        if pixmap:
            transform = QTransform().rotate(90)
            rotated_pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)
            self.image_label.setPixmap(rotated_pixmap)
        self.angle_label.setText(f"{self.current_angle}°")

    def calculate_shortest_path(self):
        points = [int(x) for x in self.points_input.text().split(",")]
        #Checando se colocaram um valor invalido de um nodo, tipo, 99
        for i in points:
            if i not in nodos.keys():
                print("Valores inválidos no input de rotas, parando processo")
                return

        path = tsp(points, self.map_widget.rotas_bloqueadas)
        self.map_widget.set_shortest_path(path)


class Carro(QGraphicsPixmapItem):
    def __init__(self, x, y, image_path, rota, velocidade=5, angulo=0, status="inativo"):
        super().__init__()

        self.status = status
        self.angulo = angulo
        self.velocidade = velocidade
        self.rota = rota
        self.ponto_atual = 0
        self.proximo_ponto = rota[self.ponto_atual] if rota else None


        pixmap = QPixmap(image_path)
        scale_factor = 1 / 40  # Escala para reduzir a imagem para 1/3
        self.scaled_pixmap = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor,Qt.KeepAspectRatio)
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

            # Calcular a distância do movimento
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
        transform.translate(self.scaled_pixmap.width() / 2,
                            self.scaled_pixmap.height() / 2)  # Move o ponto de origem para o centro
        transform.rotate(angulo)  # Aplica a rotação
        transform.translate(-self.scaled_pixmap.width() / 2, - self.scaled_pixmap.height() / 2)  # Move de volta a origem

        # Aplica a transformação ao carro
        self.setTransform(transform)
        #Atualiza valor de atributo angulo
        self.angulo = angulo

    def movimento_manual(self, acelerar):

        x_atual = self.pos().x()
        y_atual = self.pos().y()

        desloc_x = self.velocidade * math.cos(math.radians(self.angulo))
        desloc_y = self.velocidade * math.sin(math.radians(self.angulo))

        if acelerar:
            x_atual += desloc_x
            y_atual += desloc_y
            self.setPos(x_atual, y_atual)

        if not acelerar:
            x_atual -= desloc_x
            y_atual -= desloc_y
            self.setPos(x_atual, y_atual)


    def scan(self):
        #Checa posição atual, se coincidir com um nodo, le todas as conexões dom outros nodos e lista
        #o angulo das rotas para cada nodo conectado

        #depreciado por enquanto
        print("-------------------")
        nodo_atual = 0
        lista_rotas = {}
        print(self.x())
        print(self.y())

        print("----")

        print(self.pos().x())
        print(self.pos().y())

        for i in nodos:
            if (self.pos().x() - nodos[i][0] >= 10 and self.pos().y()) - nodos[i][1] >= 10:
                print(self.pos().x() - nodos[i][0])
                print(self.pos().y() - nodos[i][1])
                nodo_atual = i

        if nodo_atual == 0:
            print("O carro não se encontra em nenhum nodo")
        else:
            print("O carro se encontra no nodo " + str(nodo_atual))

            for i in data["rotas"]:

                nodo_origem = i["from"]
                nodo_destino = i["to"]

                x1 = nodos[i["from"]][0]
                y1 = nodos[i["from"]][1]

                x2 = nodos[i["to"]][0]
                y2 = nodos[i["to"]][1]

                if nodo_destino == nodo_atual:
                    #invertendo YX para XY
                    nodo_destino = i["from"]
                    nodo_origem = i["to"]

                    x1 = nodos[i["to"]][0]
                    y1 = nodos[i["to"]][1]

                    x2 = nodos[i["from"]][0]
                    y2 = nodos[i["from"]][1]

                if nodo_origem == nodo_atual:

                    m1 = float(y1 - y2) / float(x1 - x2 + 0.00001)
                    m2 = float((y1 + 50) - y1) / float(x1 - x1 + 0.00001)

                    angulo = round(math.degrees(math.atan(math.tan((m2 - m1) / (1 + m1 * m2)))), 2)

                    if x2 > x1 and y2 > y1:
                        print("X maior, Y maior, quadrante 2")
                        if angulo < 0:
                            lista_rotas[nodo_destino] = float(abs(angulo - 90))
                        if angulo > 0:
                            lista_rotas[nodo_destino] = float(abs(angulo - 180))

                    if x2 > x1 and y2 < y1:
                        print("X maior, Y menor, quadrante 1")
                        lista_rotas[nodo_destino] = float(abs(angulo))

                    if x2 < x1 and y2 > y1:
                        print("X menor, Y maior, quadrante 3,")
                        lista_rotas[nodo_destino] = float(abs(angulo) + 180)

                    if x2 < x1 and y2 < y1:
                        print("X menor, Y menor, quadrante 4")
                        lista_rotas[nodo_destino] = float(angulo + 270)

                    if x2 == x1 and y1 > y2:
                        print("X igual, Y menor, reta para cima")
                        lista_rotas[nodo_destino] = float(abs(angulo))

                    if x2 == x1 and y1 < y2:
                        print("X igual, Y maior, reta para baixo")
                        lista_rotas[nodo_destino] = float(180)

                    if x2 < x1 and y2 == y1:
                        print("X menor, Y igual, reta para esquerda")
                        lista_rotas[nodo_destino] = float(270)

                    if x2 > x1 and y2 == y1:
                        print("X maior, Y igual, reta para direita")
                        lista_rotas[nodo_destino] = float(90)

        print(lista_rotas)
        return lista_rotas


print(nodos)
print("-------------------")


def dijkstra(start, goal, blocked_edges=[]):
    graph = {node["id"]: [] for node in data["nodos"]}

    for edge in data["rotas"]:
        frm, to = edge["from"], edge["to"]
        if (frm, to) in blocked_edges or (to, frm) in blocked_edges:
            continue  # Pula esta rota se estiver bloqueada
        x1, y1 = nodos[frm]
        x2, y2 = nodos[to]
        dist = math.hypot(x2 - x1, y2 - y1)
        graph[frm].append((dist, to))
        graph[to].append((dist, frm))

    queue = [(0, start, [])]
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        seen.add(node)
        if node == goal:
            return path
        for next_cost, next_node in graph[node]:
            if next_node not in seen:
                heapq.heappush(queue, (cost + next_cost, next_node, path))

    return []


def tsp(points, blocked_edges=[]):

    min_path = None
    min_dist = float('inf')
    for perm in permutations(points):
        perm = list(perm)
        total_dist = 0
        path = []
        for i in range(len(perm) - 1):
            dijkstra_path = dijkstra(perm[i], perm[i + 1], blocked_edges)
            if not dijkstra_path:
                break

            path.extend(dijkstra_path if not path else dijkstra_path[1:])

            for j in range(len(dijkstra_path) - 1):
                x1, y1 = nodos[dijkstra_path[j]]
                x2, y2 = nodos[dijkstra_path[j + 1]]
                total_dist += math.hypot(x2 - x1, y2 - y1)
        else:
            if total_dist < min_dist:
                min_dist = total_dist
                min_path = path

    if min_path == None:
        print("Não existe nenhum caminho até os IDs informados")

    return min_path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JanelaPrincipal()

    window.show()
    sys.exit(app.exec())