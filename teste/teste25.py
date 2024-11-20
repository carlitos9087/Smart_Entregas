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
    def __init__(self, x, y, image_path, rota, velocidade=5, angulo=0, status="Disponível"):
        super().__init__()

        # Atributos do carro
        self.status = status
        self.angulo = angulo
        self.velocidade = velocidade
        self.rota = rota
        self.ponto_atual = 0
        self.proximo_ponto = rota[self.ponto_atual] if rota else None
        self.id_atual = 1
        self.coordenada_atual = [x, y]

        # Caixas no carro (máximo de 2)
        self.caixas = []
        # self.box_image_path = "SmartEntregas/imagem/box.png"

        # Carrega a imagem do carro
        pixmap = QPixmap(image_path)
        scale_factor = 1 / 40  # Escala para reduzir a imagem para 1/3
        self.scaled_pixmap = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor, Qt.KeepAspectRatio)
        self.setPixmap(self.scaled_pixmap)

        # Centraliza a imagem do carro no ponto inicial
        self.setPos(x - self.scaled_pixmap.width() / 2, y - self.scaled_pixmap.height() / 2)

    def adicionar_caixa(self):
        """Adiciona uma caixa ao carro, se houver espaço."""
        if len(self.caixas) < 2:
            pixmap = QPixmap(self.box_image_path)
            scale_factor = 1 / 1000  # Escala para ajustar a caixa no carro
            scaled_box_pixmap = pixmap.scaled(pixmap.width() * scale_factor, pixmap.height() * scale_factor, Qt.KeepAspectRatio)
            self.caixas.append(scaled_box_pixmap)
            self.atualizar_posicao_caixas()
        else:
            print("Capacidade máxima de caixas atingida (2).")

    def remover_caixa(self):
        """Remove uma caixa que o carro está carregando."""
        if self.caixas:
            # Remove a última caixa adicionada
            caixa = self.caixas.pop()
            self.scene.removeItem(caixa)
        else:
            print("Erro: O carro não possui caixas para remover.")



    def atualizar_posicao_caixas(self):
        """Atualiza a posição das caixas para que fiquem sobre o carro."""
        for i, box in enumerate(self.caixas):
            box_item = QGraphicsPixmapItem(box, self)
            # Define a posição das caixas no carro
            offset_x = 10 if i == 0 else -10  # Ajuste horizontal para caixas 1 e 2
            offset_y = -self.scaled_pixmap.height() / 2 - 5  # Ajuste vertical acima do carro
            box_item.setPos(offset_x, offset_y)

    def proximo_ponto_rota(self):
        """Atualiza o próximo ponto da rota."""
        if self.rota and self.ponto_atual < len(self.rota) - 1:
            self.ponto_atual += 1
            self.proximo_ponto = self.rota[self.ponto_atual]
            self.id_atual = encontrar_nodo_por_coordenadas(self.rota[self.ponto_atual-1][0], self.rota[self.ponto_atual-1][1], nodos)
        else:
            self.proximo_ponto = None
            self.id_atual = encontrar_nodo_por_coordenadas(self.rota[self.ponto_atual][0], self.rota[self.ponto_atual][1], nodos)
            print(self.rota, "proximo_ponto_rota")

    def calcular_angulo(self, x_atual, y_atual, x_proximo, y_proximo):
        """Calcula o ângulo entre dois pontos (atual e próximo)."""
        dx = x_proximo - x_atual
        dy = y_proximo - y_atual
        angulo_radianos = math.atan2(dy, dx)
        angulo_graus = math.degrees(angulo_radianos)
        angulo_graus = angulo_graus + 270
        return angulo_graus

    def mover_para_proximo_ponto(self):
        """Move o carro para o próximo ponto da rota com base na velocidade e ajusta o ângulo."""
        if self.proximo_ponto:
            x_atual, y_atual = self.pos().x() + self.scaled_pixmap.width() / 2, self.pos().y() + self.scaled_pixmap.height() / 2
            self.coordenada_atual = [x_atual, y_atual]

            x_proximo, y_proximo = self.proximo_ponto
            print(x_atual, y_atual, "atual")
            print(x_proximo, y_proximo, "proximo")

            if x_atual == x_proximo and y_proximo == y_atual:
                self.rota[0], self.rota[1] = self.rota[1], self.rota[0]
                self.ponto_atual = 0
                self.rota.insert(2, self.rota[0])
                self.proximo_ponto_rota()
            
            dx, dy = x_proximo - x_atual, y_proximo - y_atual
            distancia = math.hypot(dx, dy)

            if distancia > 0:
                dx /= distancia
                dy /= distancia
                x_atual += dx * self.velocidade
                y_atual += dy * self.velocidade

                self.setPos(x_atual - self.scaled_pixmap.width() / 2, y_atual - self.scaled_pixmap.height() / 2)

                novo_angulo = self.calcular_angulo(x_atual, y_atual, x_proximo, y_proximo)
                self.angulo = novo_angulo
                if distancia >= self.velocidade:
                    self.ajustar_rotacao(novo_angulo)

                if distancia <= self.velocidade:
                    self.proximo_ponto_rota()

    def ajustar_rotacao(self, angulo):
        """Ajusta a rotação do carro ao redor de seu centro."""
        transform = QTransform()
        transform.translate(self.scaled_pixmap.width() / 2, self.scaled_pixmap.height() / 2)
        transform.rotate(angulo)
        transform.translate(-self.scaled_pixmap.width() / 2, -self.scaled_pixmap.height() / 2)
        self.angulo = angulo
        self.setTransform(transform)

    def set_shortest_path(self, path):
        self.rota = path
        print(path)


class Mapa(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mapa de Nodos")
        self.resize(800, 500)

        self.pacotes = []  # Lista para armazenar os pacotes
        self.rotas_bloqueadas = []

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
        self.status_label = QLabel(f"Status: Disponível", self)
        self.velocidade_label = QLabel("Velocidade: 0", self)
        self.rota_label = QLabel("Rota: []", self)
        self.ponto_atual_label = QLabel("Ponto Atual: 0", self)
        self.proximo_ponto_label = QLabel("Próximo Ponto: None", self)
        self.angulo_label = QLabel(f"Ângulo: {0}", self)
        self.x_y = QLabel(f"Coordenadas: x= y=", self)
        
        right_layout.addWidget(self.angulo_label)
        right_layout.addWidget(self.status_label)
        right_layout.addWidget(self.velocidade_label)
        right_layout.addWidget(self.rota_label)
        right_layout.addWidget(self.ponto_atual_label)
        right_layout.addWidget(self.proximo_ponto_label)
        right_layout.addWidget(self.x_y)

        # Caixa de texto para inserir a rota
        self.rota_input = QLineEdit(self)
        self.rota_input.setPlaceholderText("Insira a rota de IDs (ex: 1,2,3)")
        right_layout.addWidget(self.rota_input)

        # Botões
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Iniciar Rota", self)
        self.stop_button = QPushButton("Parar Carro", self)
        self.continuar_button = QPushButton("Continuar Rota", self)
        self.continuar_button.setEnabled(False)  # Inicialmente desativado
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.continuar_button)
        right_layout.addLayout(button_layout)

        # Conecta os botões às funções
        self.start_button.clicked.connect(self.iniciar_rota)
        self.stop_button.clicked.connect(self.parar_carro)
        self.continuar_button.clicked.connect(self.continuar_rota)

        # Botão para adicionar obstáculo
        self.add_obstacle_button = QPushButton("Adicionar Obstáculo", self)
        right_layout.addWidget(self.add_obstacle_button)
        self.add_obstacle_button.clicked.connect(self.adicionar_obstaculo)

        # Botão para remover obstáculos
        self.remove_obstacle_button = QPushButton("Remover Obstáculo", self)
        right_layout.addWidget(self.remove_obstacle_button)
        self.remove_obstacle_button.clicked.connect(self.remover_obstaculos)
 
        # Botões para adicionar e remover caixas
        self.add_box_button = QPushButton("Adicionar Caixa", self)
        self.remove_box_button = QPushButton("Remover Caixa", self)
        right_layout.addWidget(self.add_box_button)
        right_layout.addWidget(self.remove_box_button)
        self.add_box_button.clicked.connect(self.adicionar_caixa)
        self.remove_box_button.clicked.connect(self.remover_caixa)



       # Cria o carro
        self.carro = None
        self.obstaculos = []  # Lista para armazenar os obstáculos
        self.linhas_rotas = {}  # Dicionário para armazenar as linhas das rotas
        self.rotas_com_obstaculos = []  # Lista para armazenar rotas bloqueadas por obstáculos
        self.caixas = []
        self.desenhar_nodos_e_rotas()

        # Timer para mover o carro
        self.timer = QTimer()
        self.timer.timeout.connect(self.mover_carro)

     # Funções para adicionar e remover caixas
    def adicionar_caixa(self):
        """Adiciona uma caixa ao carro, se o limite de 2 caixas não for excedido."""
        if len(self.carro.caixas) < 2:
            # Carrega a imagem da caixa e reduz o tamanho
            pixmap = QPixmap("SmartEntregas/imagem/box1.png").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            caixa_item = QGraphicsPixmapItem(pixmap)
            
            # Calcula a posição para a caixa, para que não fiquem no mesmo local
            if len(self.carro.caixas) == 0:
                # Primeira caixa à esquerda
                caixa_item.setPos(self.carro.x() - 30, self.carro.y() - 10)
            else:
                # Segunda caixa à direita
                caixa_item.setPos(self.carro.x() + 30, self.carro.y() - 10)

            self.carro.caixas.append(caixa_item)
            self.scene.addItem(caixa_item)
        else:
            print("Erro: O carro já está carregando o número máximo de caixas.")


    def remover_caixa(self):
        """Remove uma caixa que o carro está carregando."""
        if self.carro.caixas:
            # Remove a última caixa adicionada
            caixa = self.carro.caixas.pop()
            self.scene.removeItem(caixa)
        else:
            print("Erro: O carro não possui caixas para remover.")



    def desenhar_nodos_e_rotas(self):
        # Desenha as rotas (linhas entre os nodos)
        for rota in data["rotas"]:
            x1, y1 = nodos[rota["from"]]
            x2, y2 = nodos[rota["to"]]
            linha = QGraphicsLineItem(x1, y1, x2, y2)
            linha.setPen(QPen(Qt.black, 2))
            self.scene.addItem(linha)

            # Armazena a linha da rota no dicionário com a chave sendo o par de nodos
            self.linhas_rotas[(rota["from"], rota["to"])] = linha

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

    def adicionar_obstaculo(self):
        """Permite adicionar um obstáculo em uma rota específica."""
        rota_texto = self.rota_input.text()
        print("rota_texto", rota_texto, type(rota_texto))
        try:
            # Converte o texto da rota para uma lista de IDs
            rota_ids = eval(rota_texto)
            print("rota_ids ", rota_ids)


            rota_coordenadas = [nodos[id_] for id_ in rota_ids if id_ in nodos]
            print("rota_coordenadas ", rota_coordenadas)

            if len(rota_coordenadas) >= 2:
                # Verifica se existe uma rota entre os dois primeiros IDs
                if (rota_ids[0], rota_ids[1]) in self.linhas_rotas or (rota_ids[1], rota_ids[0]) in self.linhas_rotas:
                    print("self.linhas_rotas", self.linhas_rotas)
                    # Adiciona o obstáculo entre os dois primeiros pontos da rota
                    x1, y1 = rota_coordenadas[0]
                    x2, y2 = rota_coordenadas[1]
                    print("x1, y1", x1, y1)
                    print("x2, y2", x2, y2)
                    x_obstaculo = (x1 + x2) / 2
                    y_obstaculo = (y1 + y2) / 2

                    # Carrega a imagem do obstáculo e adiciona na cena
                    pixmap = QPixmap("SmartEntregas/imagem/obstacle.png")
                    obstacle_item = QGraphicsPixmapItem(pixmap)
                    obstacle_item.setPos(x_obstaculo - pixmap.width() / 2, y_obstaculo - pixmap.height() / 2)
                    self.scene.addItem(obstacle_item)

                    # Armazena o obstáculo para referência futura
                    self.obstaculos.append(obstacle_item)

                    # Muda a cor da linha entre os dois primeiros pontos da rota para vermelho, sem removê-la do dicionário
                    if (rota_ids[0], rota_ids[1]) in self.linhas_rotas:
                        linha = self.linhas_rotas[(rota_ids[0], rota_ids[1])]
                        linha.setPen(QPen(Qt.red, 2))
                        # Armazena a rota como contendo um obstáculo
                        self.rotas_com_obstaculos.append((rota_ids[0], rota_ids[1]))
                    elif (rota_ids[1], rota_ids[0]) in self.linhas_rotas:
                        linha = self.linhas_rotas[(rota_ids[1], rota_ids[0])]
                        linha.setPen(QPen(Qt.red, 2))
                        # Armazena a rota como contendo um obstáculo
                        self.rotas_com_obstaculos.append((rota_ids[1], rota_ids[0]))
                    if rota_ids not in self.rotas_bloqueadas: 
                        self.rotas_bloqueadas.append(rota_ids)
                    
                    print("rotas bloqueadas:", self.rotas_bloqueadas)

                else:
                    print("Erro: Não existe uma rota entre os IDs especificados.")

            else:
                print("Erro: IDs inválidos ou insuficientes na rota para adicionar um obstáculo.")

        except (SyntaxError, KeyError):
            print("Erro: rota inválida. Use o formato [1, 2, 3] com IDs válidos.")


    def remover_obstaculos(self):
        """Remove todos os obstáculos do mapa e restaura a cor original das rotas."""
        for obstaculo in self.obstaculos:
            self.scene.removeItem(obstaculo)

        # Restaura a cor das rotas para preto
        for id1, id2 in self.rotas_com_obstaculos:
            if (id1, id2) in self.linhas_rotas:
                linha = self.linhas_rotas[(id1, id2)]
                linha.setPen(QPen(Qt.black, 2))
            elif (id2, id1) in self.linhas_rotas:
                linha = self.linhas_rotas[(id2, id1)]
                linha.setPen(QPen(Qt.black, 2))

        # Limpa a lista de obstáculos e de rotas bloqueadas
        self.obstaculos.clear()
        self.rotas_com_obstaculos.clear()
        self.rotas_bloqueadas = []

    
    def iniciar_rota(self):
        """Inicia o movimento do carro com base na rota inserida."""
        rota_texto = self.rota_input.text()
        
        try:
            
            # Converte o texto da rota para uma lista de IDs
            rota_ids = eval(rota_texto)
       
            #a =self.carro.rota
            #rota_ids = a     ###############mudei isso aqui
            self.calculate_shortest_path()
            a = self.carro.rota
            rota_ids = a

            rota_coordenadas = [nodos[id_] for id_ in rota_ids if id_ in nodos]
 

            # Atualiza a rota do carro e começa o movimento
            if rota_coordenadas:
                self.carro.rota = rota_coordenadas
                self.carro.ponto_atual = 0
                self.carro.proximo_ponto_rota()
                self.timer.start(100)  # Movimento com intervalo de 100 ms
                self.continuar_button.setEnabled(False)  # Desativa o botão de continuar
                self.stop_button.setEnabled(True)  # Ativa o botão de parar
            else:
                print("Erro: IDs inválidos na rota.")

        except (SyntaxError, KeyError):
            print("Erro: rota inválida. Use o formato [1, 2, 3] com IDs válidos.")

    def parar_carro(self):
        """Para o movimento do carro e ativa o botão de continuar."""
        self.timer.stop()
        self.continuar_button.setEnabled(True)  # Ativa o botão de continuar
        self.stop_button.setEnabled(False)  # Desativa o botão de parar
        self.carro.status = "Parado"
            # Atualiza as labels com as informações do carro
        self.status_label.setText(f"Status: {self.carro.status}")  # Atualiza o status

    def continuar_rota(self):
        """Continua o movimento do carro a partir do ponto onde parou."""
        if self.carro:
            self.timer.start(100)  # Retoma o movimento com intervalo de 100 ms
            self.continuar_button.setEnabled(False)  # Desativa o botão de continuar
            self.stop_button.setEnabled(True)  # Ativa o botão de parar


    def mover_carro(self):
        """Move o carro para o próximo ponto da rota e atualiza as informações na interface."""
        if self.carro and self.carro.proximo_ponto:
            self.carro.mover_para_proximo_ponto()
            self.carro.status = "Ativo"
            
            # Atualiza as posições das caixas para acompanhar o carro
            for idx, caixa in enumerate(self.carro.caixas):
                if idx == 0:
                    # Primeira caixa à esquerda do carro
                    caixa.setPos(self.carro.x() - 10, self.carro.y() - 10)
                else:
                    # Segunda caixa à direita do carro
                    caixa.setPos(self.carro.x() + 10, self.carro.y() - 10)
            
            # Atualiza as labels com as informações do carro
            self.status_label.setText(f"Status: {self.carro.status}")
            self.velocidade_label.setText(f"Velocidade: {self.carro.velocidade}")
            self.rota_label.setText(f"Rota: {self.carro.rota}")
            self.ponto_atual_label.setText(f"Ponto Atual: {self.carro.ponto_atual}")
            self.proximo_ponto_label.setText(f"Próximo Ponto: {self.carro.proximo_ponto}")
            self.angulo_label.setText(f"Ângulo: {self.carro.angulo:.1f}")
            self.x_y.setText(f"Coordenadas: x={self.carro.coordenada_atual[0]:.1f} y={self.carro.coordenada_atual[1]:.1f}")
        else:
            self.carro.status = "Aguardando coleta"
            self.status_label.setText(f"Status: {self.carro.status}")
            self.timer.stop()

    def descarregar_caixas(self):
        """Descarrega todas as caixas do carro no ponto atual."""
        self.remover_caixas_do_carro()
        print("Caixas descarregadas no ponto atual.")



    def calculate_shortest_path(self):
        points = [int(x) for x in self.rota_input.text().split(",")]
        points = [self.carro.id_atual]+points
        path = tsp(points, self.rotas_bloqueadas)
        # print(path)
        self.carro.set_shortest_path(path)


    def remover_segmento_rota(self, rota_ids):
        """Remove o segmento da rota que foi bloqueado."""
        # Filtra a rota removendo os segmentos bloqueados
        nova_rota = []
        for id1, id2 in zip(rota_ids[:-1], rota_ids[1:]):
            if (id1, id2) not in self.rotas_com_obstaculos and (id2, id1) not in self.rotas_com_obstaculos:
                nova_rota.append(id1)
        if rota_ids[-1] not in [par for segmento in self.rotas_com_obstaculos for par in segmento]:
            nova_rota.append(rota_ids[-1])  # Adiciona o último ponto se ele não for bloqueado

        return nova_rota
    
def remover_rota(data, ponto1, ponto2):
    # Cria uma cópia da lista de rotas para não modificar a original
    data_atual = {"nodos": data["nodos"], "rotas": []}

    for rota in data["rotas"]:
        # Verifica se a rota não é entre os pontos fornecidos
        if not ((rota["from"] == ponto1 and rota["to"] == ponto2) or 
                (rota["from"] == ponto2 and rota["to"] == ponto1)):
            data_atual["rotas"].append(rota)

    return data_atual


# Função Dijkstra modificada para evitar caminhos bloqueados
def dijkstra(start, goal, blocked_edges=[]):
    # Criando o grafo de adjacência
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

# Função TSP modificada para passar rotas bloqueadas para o Dijkstra
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

    return min_path

def encontrar_nodo_por_coordenadas(x, y, nodos):
    for id_nodo, coordenadas in nodos.items():
        if coordenadas == (x, y):
            return id_nodo
    return None  # Caso não encontre correspondência


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapa = Mapa()
    mapa.show()
    sys.exit(app.exec())
