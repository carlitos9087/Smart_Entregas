import sys
import math
import heapq
import remessa_controller
import gerenciador_mapa
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                               QGridLayout,
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem,
                               QGraphicsLineItem, QGraphicsPixmapItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QWheelEvent, QMouseEvent, QTransform, QPixmap
from PySide6.QtCore import Qt, QTimer

gerenc_mapa = gerenciador_mapa.MapaLogico()
Path_do_arquivo = r"C:\Users\Admin\Desktop\SmartEntregas\SmartEntregas\Sistema\arquivo_mapa.txt"
gerenc_mapa.importar_mapa(Path_do_arquivo)

print(gerenc_mapa.Dados)

nodos = {node["id"]: (node["x"], node["y"]) for node in gerenc_mapa.Dados["Nodos"]}


class MapWidget(QGraphicsView):

    def __init__(self, janela_principal):
        super().__init__()

        self.nodos_prioridade = []
        self.shortest_path = []  # tem uma variavelp/ 1 caminho, interligar isso com a ida e volta de uma remessa
        self.rota_ida = []
        self.rota_volta = []


        self.remessa_carregada = 0


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
        self.janela_remessa = None
        self.janela_gerenc_mapa = None
        self.controlador_remessa = remessa_controller.RemessaController()

        self.draw_map(self.shortest_path)
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover_carro)

    def set_shortest_path(self, path):
        self.shortest_path = path
        print(self.shortest_path)
        self.janela_principal.start_button.setEnabled(True)  # Ativa o botão de iniciar rota
        self.draw_map(self.shortest_path)

    def draw_map(self, rota):

        self._scene.clear()

        pen = QPen(Qt.black)
        pen.setWidth(2)
        x_inicial = nodos[1][0]
        y_inicial = nodos[1][1]

        # Desenhar arestas
        for edge in gerenc_mapa.Dados["Rotas"]:
            x1, y1 = nodos[edge["from"]]
            x2, y2 = nodos[edge["to"]]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(pen)
            self._scene.addItem(line)

        # Desenhar nodos
        for node in gerenc_mapa.Dados["Nodos"]:
            x, y = node["x"], node["y"]
            ellipse = QGraphicsEllipseItem(x - 5, y - 5, 10, 10)
            ellipse.setPen(pen)
            ellipse.setBrush(Qt.black)
            self._scene.addItem(ellipse)

            text = QGraphicsTextItem(f'Casa {node["id"]}')
            text.setFont(QFont("Arial", 10))
            text.setPos(x + 5, y + 5)
            self._scene.addItem(text)

        for obstacle in gerenc_mapa.Dados["Obstaculos"]:
            rota_coordenadas = [nodos[id_] for id_ in obstacle if id_ in nodos]
            x1, y1 = rota_coordenadas[0]
            x2, y2 = rota_coordenadas[1]
            x_obstaculo = (x1 + x2) / 2
            y_obstaculo = (y1 + y2) / 2

            # Carrega a imagem do obstáculo e adiciona na cena
            pixmap = QPixmap(r"C:\Users\Admin\Desktop\SmartEntregas\SmartEntregas\imagem\obstacle.png")
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

        # Adiciona o carro com a coordenada do primeiro ponto da rota calculada
        self.carro = Carro(x_inicial,
                           y_inicial,
                           r"C:\Users\Admin\Desktop\SmartEntregas\SmartEntregas\imagem\carro.png",
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
            #modificar para que quando remessa carregada = True, usar self.rota Ida
            rota_coordenadas = [nodos[id_] for id_ in
                                tsp([int(x) for x in self.janela_principal.points_input.text().split(",")],
                                    gerenc_mapa.Dados["Obstaculos"]) if
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

    def carregar_remessa(self, id_remessa):
        # Fazer um IF para checar se a remessa existe e pa, tratamento de erro
        dados_remessa = self.controlador_remessa.get_dados_remessa(id_remessa)
        nomes_remessa = self.controlador_remessa.get_donos_pacote(dados_remessa)
        self.nodos_prioridade = self.controlador_remessa.relacionar_nomes_nodos(
            self.controlador_remessa.get_donos_pacote(dados_remessa))
        print("nodosss")
        print(self.nodos_prioridade)

        self.janela_principal.label_pacote_1.setText("Pacote 1: Nodo " + str(self.nodos_prioridade[0]))
        self.janela_principal.label_pacote_2.setText("Pacote 2: Nodo " + str(self.nodos_prioridade[1]))
        self.janela_principal.label_nomes.setText(
            "Nomes Moradores: " + str(nomes_remessa[0]) + ", " + str(nomes_remessa[1]))

        rota_ida = tsp(self.nodos_prioridade, gerenc_mapa.Dados["Obstaculos"])
        self.rota_ida = rota_ida
        self.janela_principal.label_rota_ida.setText("Rota Ida: " + str(rota_ida))

        # invertendo manualmente o nodos_prioridade, pq usar .reverse() dá erro por algum motivo
        self.nodos_prioridade.append(self.nodos_prioridade[0])
        self.nodos_prioridade[0] = self.nodos_prioridade[1]
        self.nodos_prioridade[1] = self.nodos_prioridade[2]
        self.nodos_prioridade.pop()

        rota_volta = tsp(self.nodos_prioridade, gerenc_mapa.Dados["Obstaculos"])
        self.rota_volta = rota_volta
        self.janela_principal.label_rota_volta.setText("Rota Volta: " + str(rota_volta))

        # self.janela_remessa.label_rota_volta.setText("ROTA MUDANDO")
        # Set Text das rotas de ia e volta
        # Vai ter que fazer as rotas no controlador carro ler daqui
        self.janela_principal.label_status.setText("Remessa " + str(id_remessa) + " carregada")


    def abrir_janela_gerenc_mapa(self, data):
        if not self.janela_gerenc_mapa or not self.janela_gerenc_mapa.isVisible():
            self.janela_gerenc_mapa = gerenciador_mapa.JanelaGerenciadorMapa(data, self)
            self.janela_gerenc_mapa.show()


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

        title1 = QLabel(Path_do_arquivo)
        self.map_widget = MapWidget(self)


        self.button_gerenc_mapa = QPushButton("Abrir Gerenciador de Mapa")
        self.button_gerenc_mapa.clicked.connect(lambda: self.map_widget.abrir_janela_gerenc_mapa(gerenc_mapa))

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
        frame1_layout.addWidget(self.button_gerenc_mapa)
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
        self.right_button.clicked.connect(
            lambda: self.map_widget.carro.ajustar_rotacao(self.map_widget.carro.angulo + 10))
        self.left_button.clicked.connect(
            lambda: self.map_widget.carro.ajustar_rotacao(self.map_widget.carro.angulo - 10))

        self.start_button.clicked.connect(self.map_widget.iniciar_rota)
        self.stop_button.clicked.connect(self.map_widget.parar_carro)
        self.continuar_button.clicked.connect(self.map_widget.continuar_rota)

        # Frame 3: Title, Subtitle, Image, Orientation
        frame3 = QFrame()
        frame3.setFrameShape(QFrame.StyledPanel)
        frame3_layout = QVBoxLayout()

        frame_dados_remessa = QFrame()
        frame_dados_remessa.setFrameShape(QFrame.StyledPanel)
        frame_dados_remessa_layout = QGridLayout()

        frame_status = QFrame()
        frame_status.setFrameShape(QFrame.StyledPanel)
        frame_status_layout = QGridLayout()

        self.title3 = QLabel("Carrinho")
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

        frame_status_layout.addWidget(self.title3)
        frame_status_layout.addWidget(self.subtitle3)
        frame_status_layout.addWidget(self.angulo_label)
        frame_status_layout.addWidget(self.status_label)
        frame_status_layout.addWidget(self.velocidade_label)
        frame_status_layout.addWidget(self.rota_label)
        frame_status_layout.addWidget(self.ponto_atual_label)
        frame_status_layout.addWidget(self.proximo_ponto_label)
        frame_status_layout.addWidget(self.rotate_button)

        frame_status.setLayout(frame_status_layout)

        #frame para remessas
        frame_inputs_remessa = QFrame()
        frame_inputs_remessa_layout = QHBoxLayout()

        self.input_remessa = QLineEdit()
        self.input_remessa.setPlaceholderText("ID da Remessa a ser carregada")
        self.button_carregar_remessa = QPushButton("Carregar Remessa")

        frame_inputs_remessa_layout.addWidget(self.input_remessa)
        frame_inputs_remessa_layout.addWidget(self.button_carregar_remessa)
        self.button_carregar_remessa.clicked.connect(lambda: self.map_widget.carregar_remessa(self.input_remessa.text()))

        frame_inputs_remessa.setLayout(frame_inputs_remessa_layout)
        frame_dados_remessa_layout.addWidget(frame_inputs_remessa)

        self.label_status = QLabel("Nenhuma remessa Carregada")
        self.label_pacote_1 = QLabel("Pacote 1: ")
        self.label_pacote_2 = QLabel("Pacote 2: ")
        self.label_nomes = QLabel("Nomes Moradores: ")
        self.label_rota_ida = QLabel("Rota Ida: ")
        self.label_rota_volta = QLabel("Rota Volta: ")

        frame_dados_remessa_layout.addWidget(self.label_status)
        frame_dados_remessa_layout.addWidget(self.label_pacote_1)
        frame_dados_remessa_layout.addWidget(self.label_pacote_2)
        frame_dados_remessa_layout.addWidget(self.label_nomes)
        frame_dados_remessa_layout.addWidget(self.label_rota_ida)
        frame_dados_remessa_layout.addWidget(self.label_rota_volta)

        frame_dados_remessa.setLayout(frame_dados_remessa_layout)

        frame3_layout.addWidget(frame_dados_remessa)
        frame3_layout.addWidget(frame_status)

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
        # Checando se colocaram um valor invalido de um nodo, tipo, 99
        for i in points:
            if i not in nodos.keys():
                print("Valores inválidos no input de rotas, parando processo")
                return

        path = tsp(points, gerenc_mapa.Dados["Obstaculos"])
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
        self.scaled_pixmap = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor,
                                           Qt.KeepAspectRatio)
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
        transform.translate(-self.scaled_pixmap.width() / 2,
                            - self.scaled_pixmap.height() / 2)  # Move de volta a origem

        # Aplica a transformação ao carro
        self.setTransform(transform)
        # Atualiza valor de atributo angulo
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


def dijkstra(start, goal, blocked_edges=[]):
    graph = {node["id"]: [] for node in gerenc_mapa.Dados["Nodos"]}

    for edge in gerenc_mapa.Dados["Rotas"]:
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
