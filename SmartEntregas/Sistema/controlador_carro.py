import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                               QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
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

class MapWidget(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.shortest_path = []
        self.current_angle = 0
        self._zoom = 1
        self._scene = QGraphicsScene(self)
        self.setScene(self._scene)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedSize(600, 400)
        
        self.moving_point = None
        
        self.draw_map()

    def set_shortest_path(self, path):
        self.shortest_path = path
        print(self.shortest_path)
        self.draw_map()
        self.move_point_along_path()

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

        # Adicionar ponto móvel amarelo
        x, y = nodos[1]
        self.moving_point = QGraphicsEllipseItem(x-5, y-5, 10, 10)
        self.moving_point.setBrush(QBrush(Qt.yellow))
        self._scene.addItem(self.moving_point)

    def move_point(self, x, y):
        if self.moving_point:
            self.moving_point.setPos(x - 10, y - 40)

    def move_point_along_path(self):
        if not self.shortest_path:
            return

        self.current_step = 0

        def move_step():
            if self.current_step < len(self.shortest_path):
                node_id = self.shortest_path[self.current_step]
                x, y = nodos[node_id]
                self.move_point(x, y)
                self.current_step += 1
                QTimer.singleShot(500, move_step)

        move_step()

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
    

class ThreeFramesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.current_angle = 0
        self.setWindowTitle("Three Frames Layout")
        self.setGeometry(100, 100, 700, 550)
        
        main_layout = QHBoxLayout(self)

        # Frame 1: Title, Map, Button
        frame1 = QFrame()
        frame1.setFrameShape(QFrame.StyledPanel)
        frame1_layout = QVBoxLayout()
        
        title1 = QLabel("Nome do Mapa")
        self.map_widget = MapWidget()
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
        
        up_button = QPushButton("↑")
        left_button = QPushButton("←")
        right_button = QPushButton("→")
        down_button = QPushButton("↓")
        center_button = QPushButton("OK")
        
        directional_layout.addWidget(up_button, 0, 1)
        directional_layout.addWidget(left_button, 1, 0)
        directional_layout.addWidget(center_button, 1, 1)
        directional_layout.addWidget(right_button, 1, 2)
        directional_layout.addWidget(down_button, 2, 1)
        
        button1 = QPushButton("Comp. 1 Fechado")
        button2 = QPushButton("Comp. 2 Aberto")
        
        frame2_layout.addLayout(directional_layout)
        frame2_layout.addWidget(button1)
        frame2_layout.addWidget(button2)
        frame2.setLayout(frame2_layout)

        # Frame 3: Title, Subtitle, Image, Orientation
        frame3 = QFrame()
        frame3.setFrameShape(QFrame.StyledPanel)
        frame3_layout = QVBoxLayout()
        
        self.title3 = QLabel("Posição Atual: Rota R2")
        self.subtitle3 = QLabel("Ação Atual: Standby")
        self.image_label = QLabel()
        pixmap = QPixmap(r"carro.png")  # Carregar a imagem do arquivo
        pixmap = pixmap.scaled(200, 200)  # Ajustar o tamanho da imagem
        
        self.rotate_button = QPushButton("Girar Imagem")
        self.rotate_button.clicked.connect(self.rotate_image)
        
        self.image_label.setPixmap(pixmap)
        self.orientation_label = QLabel("Orientação:")
        self.angle_label = QLabel(f"{self.current_angle}°")
        
        frame3_layout.addWidget(self.title3)
        frame3_layout.addWidget(self.subtitle3)
        frame3_layout.addWidget(self.image_label)
        frame3_layout.addWidget(self.rotate_button)
        frame3_layout.addWidget(self.orientation_label)
        frame3_layout.addWidget(self.angle_label)
        frame3.setLayout(frame3_layout)
        
        # Add frames to main layout
        main_layout.addWidget(frame1)
        main_layout.addWidget(frame2)
        main_layout.addWidget(frame3)
        
        self.setLayout(main_layout)
        
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
    # Inserindo o ponto 1 no início e no final da lista de pontos
    points = [1] + points + [1]

    min_path = None
    min_dist = float('inf')
    for perm in permutations(points):
        perm = list(perm)
        total_dist = 0
        path = []
        for i in range(len(perm) - 1):
            dijkstra_path = dijkstra(perm[i], perm[i + 1])
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ThreeFramesWindow()
    window.show()
    sys.exit(app.exec())


