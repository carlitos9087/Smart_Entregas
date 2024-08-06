import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QFrame, QWidget, QLabel
from PySide6.QtGui import QPainter, QPen, QFont, QWheelEvent, QMouseEvent, QTransform
from PySide6.QtCore import Qt, QPointF, QRectF


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
        {"id": 9, "x": 600, "y": 300},
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
    def __init__(self):
        super().__init__()
        self.shortest_path = []
        self._zoom = 1
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedSize(600, 400)

        self.draw_map()

    def set_shortest_path(self, path):
        self.shortest_path = path
        self.draw_map()
        print("Caminho mais curto:", self.shortest_path)

    def draw_map(self):
        self._scene.clear()

        pen = QPen(Qt.black)
        pen.setWidth(2)

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
        
        # Desenhar o caminho mais curto
        if self.shortest_path:
            pen = QPen(Qt.red)
            pen.setWidth(2)
            for i in range(len(self.shortest_path) - 1):
                x1, y1 = nodos[self.shortest_path[i]]
                x2, y2 = nodos[self.shortest_path[i + 1]]
                line = QGraphicsLineItem(x1, y1, x2, y2)
                line.setPen(pen)
                self._scene.addItem(line)

    def wheelEvent(self, event: QWheelEvent):
        factor = 1.25 if event.angleDelta().y() > 0 else 0.8
        self._zoom *= factor
        self.scale(factor, factor)
        print("factor", factor)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.setDragMode(QGraphicsView.NoDrag)
        super().mouseReleaseEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mapa de Casas e Caminhos")
        self.setGeometry(50, 50, 1000, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout(central_widget)


        self.map_frame = QFrame()
        self.map_frame.setFrameShape(QFrame.Box)
        self.map_frame.setFrameShadow(QFrame.Raised)
        self.map_frame.setLineWidth(2)
        self.map_frame.setFixedSize(620, 420)

        self.map_widget = MapWidget()

        layout_mapa = QVBoxLayout()

        frame_layout = QVBoxLayout(self.map_frame)
        frame_layout.addWidget(self.map_widget, 0, Qt.AlignCenter)

        layout_mapa.addWidget(self.map_frame, 0, Qt.AlignCenter)

        # Input fields and button for calculating shortest path
        input_layout = QHBoxLayout()
        
        self.points_input = QLineEdit()
        self.points_input.setPlaceholderText("IDs das Casas (separados por vírgula)")
        input_layout.addWidget(self.points_input)
        
        self.calculate_button = QPushButton("Calcular Rota Mais Curta")
        self.calculate_button.clicked.connect(self.calculate_shortest_path)
        input_layout.addWidget(self.calculate_button)
        
        layout_mapa.addLayout(input_layout)


        layout.addLayout(layout_mapa)

        #Frame Botões de controle do carro

        BotaoFrente = QPushButton("^", self)
        BotaoDireita = QPushButton(">", self)
        BotaoEsquerda = QPushButton("<", self)
        BotaoTras = QPushButton("V", self)
        BotaoComp1 = QPushButton("Comp. 1", self)
        BotaoComp2 = QPushButton("Comp. 2", self)

        self.botoes_frame_1 = QFrame()
        self.botoes_frame_1.setFrameShape(QFrame.Box)
        self.botoes_frame_1.setFrameShadow(QFrame.Raised)
        self.botoes_frame_1.setLineWidth(2)
        self.botoes_frame_1.setFixedSize(150,50)

        self.botoes_frame_2 = QFrame()
        self.botoes_frame_2.setFrameShape(QFrame.Box)
        self.botoes_frame_2.setFrameShadow(QFrame.Raised)
        self.botoes_frame_2.setLineWidth(2)
        self.botoes_frame_2.setFixedSize(150, 50)

        self.botoes_frame_3 = QFrame()
        self.botoes_frame_3.setFrameShape(QFrame.Box)
        self.botoes_frame_3.setFrameShadow(QFrame.Raised)
        self.botoes_frame_3.setLineWidth(2)
        self.botoes_frame_3.setFixedSize(150, 50)

        self.botoes_frame_4 = QFrame()
        self.botoes_frame_4.setFrameShape(QFrame.Box)
        self.botoes_frame_4.setFrameShadow(QFrame.Raised)
        self.botoes_frame_4.setLineWidth(2)
        self.botoes_frame_4.setFixedSize(150, 50)

        layout_botoes_linha_1 = QHBoxLayout(self.botoes_frame_1)
        layout_botoes_linha_1.addWidget(BotaoFrente, 0, )

        layout_botoes_linha_2 = QHBoxLayout(self.botoes_frame_2)
        layout_botoes_linha_2.addWidget(BotaoEsquerda, 0, )
        layout_botoes_linha_2.addWidget(BotaoDireita, 0, )

        layout_botoes_linha_3 = QHBoxLayout(self.botoes_frame_3)
        layout_botoes_linha_3.addWidget(BotaoTras, 0, )

        layout_botoes_linha_4 = QHBoxLayout(self.botoes_frame_4)
        layout_botoes_linha_4.addWidget(BotaoComp1, 0, )
        layout_botoes_linha_4.addWidget(BotaoComp2, 0, )


        layout_botoes = QVBoxLayout()
        layout_botoes.setSpacing(-1)
        layout_botoes.addWidget(self.botoes_frame_1)
        layout_botoes.addWidget(self.botoes_frame_2)
        layout_botoes.addWidget(self.botoes_frame_3)
        layout_botoes.addWidget(self.botoes_frame_4)
        layout.addLayout(layout_botoes)


        #Frame de Status do carro

        labelPosic = QLabel("Posição Atual do Carro: ")
        labelAcao = QLabel("Ação Atual: ")
        labelOrientacao = QLabel("Orientaçao: ")
        labelAlgumaCoisa = QLabel("0-0")

        self.status_frame_1 = QFrame()
        self.status_frame_1.setFrameShape(QFrame.Box)
        self.status_frame_1.setFrameShadow(QFrame.Raised)
        self.status_frame_1.setLineWidth(2)
        self.status_frame_1.setFixedSize(150, 400)

        self.status_frame_2 = QFrame()
        self.status_frame_2.setFrameShape(QFrame.Box)
        self.status_frame_2.setFrameShadow(QFrame.Raised)
        self.status_frame_2.setLineWidth(2)
        self.status_frame_2.setFixedSize(150, 50)


        frame_status_linha_1 = QVBoxLayout(self.status_frame_1)

        frame_status_linha_1.addWidget(labelPosic, 0, Qt.AlignCenter)
        frame_status_linha_1.addWidget(labelAcao, 0, Qt.AlignCenter)
        frame_status_linha_1.addWidget(labelOrientacao, 0, Qt.AlignCenter)

        frame_status_linha_2 = QHBoxLayout(self.status_frame_2)


        frame_status_linha_2.addWidget(labelAlgumaCoisa, 0, Qt.AlignCenter)

        layout_status = QVBoxLayout()
        layout_status.setSpacing(0)

        layout_status.addWidget(self.status_frame_1)
        layout_status.addWidget(self.status_frame_2)


        layout.addLayout(layout_status)

    def calculate_shortest_path(self):
        points = list(map(int, self.points_input.text().split(',')))
        path = tsp(points)
        self.map_widget.set_shortest_path(path)
        

def dijkstra(start, goal):
    graph = {node["id"]: [] for node in data["nodos"]}
    for edge in data["rotas"]:
        frm, to = edge["from"], edge["to"]
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

def tsp(points):
    print('tsp rodou')
    min_path = None
    min_dist = float('inf')
    for perm in permutations(points):
        perm = list(perm)
        total_dist = 0
        path = []
        for i in range(len(perm) - 1):
            segment_path = dijkstra(perm[i], perm[i + 1])
            if not segment_path:
                break
            total_dist += path_distance(segment_path)
            path.extend(segment_path[:-1])
        path.append(perm[-1])
        if total_dist < min_dist:
            min_dist = total_dist
            min_path = path
    return min_path

def path_distance(path):
    dist = 0
    for i in range(len(path) - 1):
        x1, y1 = nodos[path[i]]
        x2, y2 = nodos[path[i + 1]]
        dist += math.hypot(x2 - x1, y2 - y1)
    
    return dist

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
