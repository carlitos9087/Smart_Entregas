import sys
from PySide6.QtWidgets import (QFrame, QVBoxLayout, QLabel,
                               QGraphicsPixmapItem, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QBrush, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton, QFileDialog
class MapaLogico(dict):
    def __init__(self):
      super().__init__()
      self.Dados = {"Nodos": [],
               "Rotas": [],
               "Obstaculos": []
              }
      
      self.Nodos ={}

    
    def importar_mapa(self, path):
      with open(path, 'r') as arquivo:
            loop_nodos = False
            loop_rotas = False
            loop_obstacs = False
            content = arquivo.readlines()
            self.limpar_mapa()
            for line in content: 
                line_checked = False
                #Checando qual bloco específico estamos lendo
                if "BEGIN NODOS" in line:
                    loop_nodos = True
                    loop_rotas = False
                    loop_obstacs = False

                    line_checked = True
                    print("\nIniciando Nodos\n---\n")
                    pass
                
                if "BEGIN ROTAS" in line:
                    loop_nodos = False
                    loop_rotas = True
                    loop_obstacs = False

                    line_checked = True

                    print("\nIniciando Rotas\n---\n")
                    pass
                
                if "BEGIN OBSTACULOS" in line:
                    loop_nodos = False
                    loop_rotas = False
                    loop_obstacs = True

                    line_checked = True
                    print("\nIniciando Obstáculos\n---\n")
                    pass


                #Lendo linha e alimentando para função apropriada
                if loop_nodos and  not line_checked:               
                    self.criar_nodo(
                        line.split(", ")[0], 
                        line.split(", ")[1], 
                        line.split(", ")[2].rstrip("\n"))
                    pass
                if loop_rotas and not line_checked:                
                    self.criar_rota(
                        line.split(", ")[0], 
                        line.split(", ")[1].rstrip("\n"))
                    pass
                if loop_obstacs and not line_checked:
                    self.criar_obstac(
                        line.split(", ")[0], 
                        line.split(", ")[1].rstrip("\n"))
                    pass           
                pass
             
            arquivo.close()
            pass
    def exportar_mapa(self, path):
        #Exportando Nodos
        with open(path, 'w') as arquivo:
            arquivo.write("BEGIN NODOS\n")
            for nodo in self.Dados["Nodos"]:
                id = nodo["id"]
                x = nodo["x"]
                y = nodo["y"]
                arquivo.write(f"{id}, {x}, {y}\n")
            pass
            arquivo.write("BEGIN ROTAS\n")
            for rota in self.Dados["Rotas"]:
                id_origem = rota["from"]
                id_destino = rota["to"]
                arquivo.write(f"{id_origem}, {id_destino}\n")
            pass
            arquivo.write("BEGIN OBSTACULOS\n")
            for obstac in self.Dados["Obstaculos"]:
                id_1 = obstac[0]
                id_2 = obstac[1]
                arquivo.write(f"{id_1}, {id_2}\n")
        pass
    
    #funções de inserção de dados
    def criar_nodo(self, id, x, y):  
        
        for nodo in self.Dados['Nodos']:
            if (x == nodo["x"] and y == nodo["y"]) or id == nodo["id"] :
                print("Nodo já existe, pulando Criação")
                return
                    
        self.Dados['Nodos'].append({"id": int(id), "x": int(x), "y": int(y)})
        print("Nodo Criado")
        self.atualiza_Nodos()
        pass
        
    def criar_rota(self, id_nodo_origem, id_nodo_destino):
        nodos_existentes = self.nodos_existentes()
        
        if int(id_nodo_origem) not in nodos_existentes or int(id_nodo_destino) not in nodos_existentes:
            print("Nodos informados não existem, rota não criada")
            return
        
        for rota in self.Dados['Rotas']:
            if (rota["from"], rota["to"]) in rota:
                print("Rota já existe, pulando Criação")
                return

            
        self.Dados['Rotas'].append({"from": int(id_nodo_origem), "to": int(id_nodo_destino)})
        print("Rota Criada")     
        self.atualiza_Nodos()
        pass

    def criar_obstac(self, id_nodo_1, id_nodo_2):
        ids = [(int(id_nodo_1), int(id_nodo_2)), (int(id_nodo_2), int(id_nodo_1))]
        for obstaculo in self.Dados['Obstaculos']:
            if obstaculo in ids:
                print("Obstaculo já existe, pulando Criação")
                return
                
        for rota in self.Dados['Rotas']:
            if (rota["from"], rota["to"]) in ids:
                self.Dados['Obstaculos'].append((int(id_nodo_1), int(id_nodo_2)))
                print("Obstaculo Criado")
                return
                   
        print("Rota não existe, impossível criar obstáculo")
        self.atualiza_Nodos()
        pass

    #Funções de Deleção de dados

    def deletar_nodo(self, id):
        
        for i, nodo in enumerate(self.Dados["Nodos"]):
            if nodo["id"]== str(id):
                del self.Dados["Nodos"][i]
                print("Nodo Deletada")
                return
        print("Nodo não encontrado para deleção")
        self.atualiza_Nodos()
        pass

    def deletar_rota(self, id_nodo_origem, id_nodo_destino):
        
        
        for i, rota in enumerate(self.Dados["Rotas"]):
           
            if (rota["from"], rota["to"]) == (str(id_nodo_origem),str(id_nodo_destino)) or \
                (rota["from"], rota["to"]) == (str(id_nodo_destino), str(id_nodo_origem)):
                del self.Dados["Rotas"][i]
                print("Rota Deletada")
                return
        print("Rota não encontrada para deleção")
        self.atualiza_Nodos()
        
    def deletar_obstac(self, id_nodo_1, id_nodo_2):
        
        for i, obstac in enumerate(self.Dados["Obstaculos"]):

            if  obstac == (str(id_nodo_1),str(id_nodo_2)) or \
                obstac == (str(id_nodo_2),str(id_nodo_1)):
                del self.Dados["Obstaculos"][i]
                print("Obstaculo Deletado")
                return
        print("Obstaculo não encontrado para deleção")
        self.atualiza_Nodos()

    #Funções de Modificação de dados, nodos, no caso
    def alterar_nodo(self, id, x, y):
        
        for i, nodo in enumerate(self.Dados["Nodos"]):
            if nodo["id"]== str(id):
                self.Dados["Nodos"][i] = {"id": id, "x": x, "y": y}
                print("Nodo " + str(id) +  " Atualizado")
                return
        print("Nodo não encontrado para Alteração")
        self.atualiza_Nodos()
        pass

    #Funções Gerais
    def print_mapa(self):
        print("\nNodos: ")
        for nodos in self.Dados['Nodos']:
            print(nodos)
        
        print("\nRotas: ")
        for rotas in self.Dados['Rotas']:
            print(rotas)
 
        print("\nObstáculos: ")
        for obstac in self.Dados['Obstaculos']:
            print(obstac)
        pass
        
    def nodos_existentes(self):
        nodos_existentes = []
        for nodo in self.Dados['Nodos']:
            nodos_existentes.append(nodo["id"])
            # print(nodos_existentes)
        self.atualiza_Nodos()
        return nodos_existentes
    
    
    def limpar_mapa(self):
        self.Dados['Nodos'] = []
        self.Dados['Rotas'] = []
        self.Dados['Obstaculos'] = []
        self.atualiza_Nodos()

    def limpar_obstaculos(self):
         self.Dados['Obstaculos'] = []
         self.atualiza_Nodos()

    def get_pos_Nodo(self, id):

        coordenadas_nodo = []
        for nodo in self.Dados["Nodos"]:           
            if str(nodo["id"]) == str(id):
                coordenadas_nodo.insert(0, (nodo["x"], nodo["y"]))
        print(coordenadas_nodo)
        return coordenadas_nodo

    
    def atualiza_Nodos(self):
        self.Nodos = {node["id"]: (node["x"], node["y"]) for node in self.Dados["Nodos"]}




class JanelaGerenciadorMapa(QWidget):
    def __init__(self, data,MapWidget):
        super().__init__()

        self.data = data
        self.MapWidget = MapWidget

        self.setWindowTitle("Mapa de Nodos")
        self.resize(900, 600)

        # Layout principal
        main_layout = QHBoxLayout()  # Alterado para QHBoxLayout
        self.setLayout(main_layout)

        # Layout para mapa e busca (vertical)
        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        # Layout do mapa
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        left_layout.addWidget(self.view)  # O mapa ficará na parte superior

        # Layout da busca
        search_layout = QHBoxLayout()
        self.input_pasta = QLineEdit(self)
        self.input_pasta.setPlaceholderText("Selecione uma pasta")
        search_layout.addWidget(self.input_pasta)

        botao_procurar = QPushButton("Importar Arquivo de Mapa", self)
        search_layout.addWidget(botao_procurar)
        botao_procurar.clicked.connect(self.abrir_seletor_de_arquivo)

        botao_Exportar = QPushButton("Exportar Arquivo de Mapa", self)
        search_layout.addWidget(botao_Exportar)
        botao_Exportar.clicked.connect(self.exportar_mapa)

        left_layout.addLayout(search_layout)  # A busca ficará abaixo do mapa

        # Frame 2 na direita
        right_frame = QFrame(self)
        right_frame.setFrameShape(QFrame.StyledPanel)
        right_frame.setFixedWidth(200)
        right_frame.setMaximumWidth(400)
        right_layout = QVBoxLayout()
        right_frame.setLayout(right_layout)
        main_layout.addWidget(right_frame)  # Adicionado à direita

        # Título do frame
        title_label = QLabel("Gerenciador Mapa", self)
        title_label.setFont(QFont("Arial", 12, QFont.Bold))
        right_layout.addWidget(title_label)

        button_layout = QHBoxLayout()
        self.button_limpar_obstaculo = QPushButton("limpar_obstaculos", self)
        self.button_limpar_mapa = QPushButton("limpar_mapa", self)
        self.button_aplicar_mudancas = QPushButton("Aplicar Mudanças", self)

        button_layout.addWidget(self.button_aplicar_mudancas)
        button_layout.addWidget(self.button_limpar_obstaculo)
        button_layout.addWidget(self.button_limpar_mapa)
        right_layout.addLayout(button_layout)

        self.button_aplicar_mudancas.clicked.connect(self.aplicar_mudancas)
        self.button_limpar_mapa.clicked.connect(self.limpar_mapa)
        self.button_limpar_obstaculo.clicked.connect(self.limpar_obstaculos)

        self.rotas = QLabel(f"rotas", self)
        right_layout.addWidget(self.rotas)

        input_layout_rotas = QHBoxLayout()
        self.rota_input1 = QLineEdit(self)
        self.rota_input1.setPlaceholderText("ID_1")

        self.rota_input2 = QLineEdit(self)
        self.rota_input2.setPlaceholderText("ID_2")

        input_layout_rotas.addWidget(self.rota_input1)
        input_layout_rotas.addWidget(self.rota_input2)
        right_layout.addLayout(input_layout_rotas)

        button_layout_rotas = QHBoxLayout()
        self.button_cria_rotas = QPushButton("Criar_rota", self)
        self.button_deleta_rotas = QPushButton("Deletar_rota", self)


        self.button_cria_rotas.clicked.connect(self.criar_rota_e_atualizar)
        self.button_deleta_rotas.clicked.connect(self.deletar_rota_e_atualizar)

        button_layout_rotas.addWidget(self.button_cria_rotas)
        button_layout_rotas.addWidget(self.button_deleta_rotas)
        right_layout.addLayout(button_layout_rotas)

        self.x_y = QLabel(f"Obstaculo", self)
        right_layout.addWidget(self.x_y)

        input_layout = QHBoxLayout()
        self.obstaculos_input1 = QLineEdit(self)
        self.obstaculos_input1.setPlaceholderText("ID_1")

        self.obstaculos_input2 = QLineEdit(self)
        self.obstaculos_input2.setPlaceholderText("ID_2")


        button_layout_obstaculo = QHBoxLayout()
        self.criar_obstaculo = QPushButton("Criar_obstaculo", self)
        self.Deletar_obstaculo = QPushButton("Deletar_obstaculo", self)

        self.criar_obstaculo.clicked.connect(self.cria_obstaculos)
        self.Deletar_obstaculo.clicked.connect(self.deleta_obstaculo)


        input_layout.addWidget(self.obstaculos_input1)
        input_layout.addWidget(self.obstaculos_input2)
        right_layout.addLayout(input_layout)


        button_layout_obstaculo.addWidget(self.criar_obstaculo)
        button_layout_obstaculo.addWidget(self.Deletar_obstaculo)
        right_layout.addLayout(button_layout_obstaculo)


        self.x_y = QLabel(f"Nodo", self)
        right_layout.addWidget(self.x_y)

        input_layout = QHBoxLayout()
        self.nodo_input1 = QLineEdit(self)
        self.nodo_input1.setPlaceholderText("ID")

        self.nodo_input2 = QLineEdit(self)
        self.nodo_input2.setPlaceholderText("x")

        self.nodo_input3 = QLineEdit(self)
        self.nodo_input3.setPlaceholderText("y")

        input_layout.addWidget(self.nodo_input1)
        input_layout.addWidget(self.nodo_input2)
        input_layout.addWidget(self.nodo_input3)
        right_layout.addLayout(input_layout)

        button_layout_nodo = QHBoxLayout()
        self.criar_nodos = QPushButton("Criar_nodo", self)
        self.Deletar_nodo = QPushButton("Deletar_nodo", self)
        self.Alterar_nodo = QPushButton("alterar_nodo", self)

        self.criar_nodos.clicked.connect(self.criar_nodo)
        self.Deletar_nodo.clicked.connect(self.deletar_nodo)
        self.Alterar_nodo.clicked.connect(self.alterar_nodo)



        button_layout_nodo.addWidget(self.criar_nodos)
        button_layout_nodo.addWidget(self.Deletar_nodo)
        button_layout_nodo.addWidget(self.Alterar_nodo)
        right_layout.addLayout(button_layout_nodo)

        self.obstaculos = []  # Lista para armazenar os obstáculos
        self.linhas_rotas = {}  # Dicionário para armazenar as linhas das rotas
        self.rotas_com_obstaculos = []  # Lista para armazenar rotas bloqueadas por obstáculos

        (self.atualizar_mapa
         ())


    def criar_nodo(self):
        # print("nodo1",self.nodo_input1.text())
        self.data.criar_nodo(self.nodo_input1.text(),self.nodo_input2.text(), self.nodo_input3.text())
        self.atualizar_mapa()

    def deletar_nodo(self):
        self.data.deletar_nodo(self.nodo_input1.text(), )
        self.atualizar_mapa()

    def alterar_nodo(self):
        self.data.alterar_nodo(self.nodo_input1.text(),self.nodo_input2.text(), self.nodo_input3.text())
        self.atualizar_mapa()

    def aplicar_mudancas(self):
        self.MapWidget.draw_map([])

        print("Mudanças aplicadas! Fechando Janela")
        self.window().close()


    def limpar_mapa(self):
        self.data.limpar_mapa()
        self.data.Nodos = {}
        self.atualizar_mapa()
        
    def limpar_obstaculos(self):
        self.data.limpar_obstaculos()
        self.atualizar_mapa()
        
    def cria_obstaculos(self):
        self.data.criar_obstac(self.obstaculos_input1.text(), self.obstaculos_input2.text())
        self.atualizar_mapa()

    def deleta_obstaculo(self):
        self.data.deletar_obstac(self.obstaculos_input1.text(), self.obstaculos_input2.text())
        self.atualizar_mapa()
        
    def abrir_seletor_de_arquivo(self):
        arquivo, _ = QFileDialog.getOpenFileName(self, "Selecione um arquivo", "", "Arquivos de Texto (*.txt)")
        if arquivo:
            self.input_pasta.setText(arquivo)
            self.data.importar_mapa(arquivo)
            # print(self.data.Dados)
            (self.atualizar_mapa
             ())

    def exportar_mapa(self):
        arquivo, _ = QFileDialog.getSaveFileName(self, "Exportar Mapa", "", "Arquivos de Texto (*.txt)")
        if arquivo:
            if not arquivo.endswith(".txt"):
                arquivo += ".txt"  # Adiciona a extensão .txt se não estiver presente
            self.input_pasta.setText(arquivo)
            self.data.exportar_mapa(arquivo)
            self.atualizar_mapa()


    def criar_rota_e_atualizar(self):
        self.data.criar_rota(self.rota_input1.text(), self.rota_input2.text())
        self.atualizar_mapa()

    def deletar_rota_e_atualizar(self):
        self.data.deletar_rota(self.rota_input1.text(), self.rota_input2.text())
        self.atualizar_mapa()
        print("deletar_rota_e_atualizar")

    def atualizar_mapa(self):
        self.scene.clear()
        for rota in self.data.Dados["Rotas"]:
            x1, y1 = self.data.Nodos[rota["from"]]
            x1, y1 =float(x1), float(y1)
            x2, y2 = self.data.Nodos[rota["to"]]
            x2, y2= float(x2), float(y2)
            linha = QGraphicsLineItem(float(x1), float(y1), float(x2), float(y2))
            linha.setPen(QPen(Qt.black, 2))
            self.scene.addItem(linha)
            self.linhas_rotas[(rota["from"], rota["to"])] = linha

        for node in self.data.Dados["Nodos"]:
            x, y = node["x"], node["y"]
            x, y = float(x), float(y)
            id_ = node["id"]

            if id_ == 1:
                rota = []  # Rota vazia inicialmente
            else:
                circulo = QGraphicsEllipseItem(x - 10, y - 10, 20, 20)
                circulo.setBrush(QBrush(Qt.gray))
                self.scene.addItem(circulo)

            texto = QGraphicsTextItem(str(id_))
            texto.setFont(QFont("Arial", 10))
            texto.setPos(x - 5, y - 10)
            self.scene.addItem(texto)
        print("Mapa atualizado")

        for obstaculo in self.data.Dados["Obstaculos"]:
            rota_coordenadas = [self.data.Nodos[id_] for id_ in obstaculo]
            x1, y1 = rota_coordenadas[0]
            x2, y2 = rota_coordenadas[1]
            x_obstaculo = (x1 + x2) / 2
            y_obstaculo = (y1 + y2) / 2

            # Carrega a imagem do obstáculo e adiciona na cena
            pixmap = QPixmap(r"C:\Users\Admin\Desktop\SmartEntregas\SmartEntregas\imagem\obstacle.png")
            obstacle_item = QGraphicsPixmapItem(pixmap)
            obstacle_item.setPos(x_obstaculo - pixmap.width() / 2, y_obstaculo - pixmap.height() / 2)
            self.scene.addItem(obstacle_item)

