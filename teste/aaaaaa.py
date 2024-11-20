import sys
import math
import heapq
from itertools import permutations
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout, 
                               QGraphicsPixmapItem, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem, QGraphicsLineItem, QLineEdit)
from PySide6.QtGui import QPen, QFont, QWheelEvent, QMouseEvent, QTransform, QBrush, QPixmap
from PySide6.QtCore import Qt, QTimer

# data = {
#     "nodos": [
#         {"id": 1, "x": 10, "y": 40},
#         {"id": 2, "x": 100, "y": 20},
#         {"id": 3, "x": 200, "y": 20},
#         {"id": 4, "x": 10, "y": 100},
#         {"id": 5, "x": 200, "y": 100},
#         {"id": 6, "x": 400, "y": 100},
#         {"id": 7, "x": 10, "y": 300},
#         {"id": 8, "x": 300, "y": 300},
#         {"id": 9, "x": 400, "y": 300},
#     ],
#     "rotas": [
#         {"from": 1, "to": 2}, {"from": 1, "to": 4},
#         {"from": 2, "to": 3},
#         {"from": 3, "to": 6}, {"from": 3, "to": 5},
#         {"from": 4, "to": 5}, {"from": 4, "to": 7},
#         {"from": 5, "to": 6}, {"from": 5, "to": 8},
#         {"from": 6, "to": 9},
#         {"from": 7, "to": 8},
#         {"from": 8, "to": 9},
#     ]
# }



class Mapa_rota(dict):
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
            if x == nodo["x"] and y == nodo["y"]:               
                print("Nodo já existe, pulando Criação")
                return
                    
        self.Dados['Nodos'].append({"id": id, "x": x, "y": y})
        print("Nodo Criado")
        pass
        
    def criar_rota(self, id_nodo_origem, id_nodo_destino):
        rota = [(id_nodo_origem, id_nodo_destino), (id_nodo_destino, id_nodo_origem)]
        nodos_existentes = self.nodos_existentes()
        
        if id_nodo_origem not in nodos_existentes or id_nodo_destino not in nodos_existentes:
            print("Nodos informados não existem, rota não criada")
            return
        
        for rota in self.Dados['Rotas']:
            if (rota["from"], rota["to"]) in rota:
                print("Rota já existe, pulando Criação")
                return

            
        self.Dados['Rotas'].append({"from": id_nodo_origem, "to": id_nodo_destino})
        print("Rota Criada")     
        pass

    def criar_obstac(self, id_nodo_1, id_nodo_2):
        ids = [(id_nodo_1, id_nodo_2), (id_nodo_2, id_nodo_1)]
        for obstaculo in self.Dados['Obstaculos']:
            if obstaculo in ids:
                print("Obstaculo já existe, pulando Criação")
                return
                
        for rota in self.Dados['Rotas']:
            if (rota["from"], rota["to"]) in ids:
                self.Dados['Obstaculos'].append((id_nodo_1, id_nodo_2))
                print("Obstaculo Criado")
                return
                   
        print("Rota não existe, impossível criar obstáculo")
        pass

    #Funções de Deleção de dados

    def deletar_nodo(self, id):
        
        for i, nodo in enumerate(self.Dados["Nodos"]):
            if nodo["id"]== str(id):
                del self.Dados["Nodos"][i]
                print("Nodo Deletada")
                return
        print("Nodo não encontrado para deleção")
        pass

    def deletar_rota(self, id_nodo_origem, id_nodo_destino):
        
        for i, rota in enumerate(self.Dados["Rotas"]):
           
            if (rota["from"], rota["to"]) == (str(id_nodo_origem),str(id_nodo_destino)) or \
                (rota["from"], rota["to"]) == (str(id_nodo_destino), str(id_nodo_origem)):
                del self.Dados["Rotas"][i]
                print("Rota Deletada")
                return
        print("Rota não encontrada para deleção")
        
    def deletar_obstac(self, id_nodo_1, id_nodo_2):
        
        for i, obstac in enumerate(self.Dados["Obstaculos"]):

            if  obstac == (str(id_nodo_1),str(id_nodo_2)) or \
                obstac == (str(id_nodo_2),str(id_nodo_1)):
                del self.Dados["Obstaculos"][i]
                print("Obstaculo Deletado")
                return
        print("Obstaculo não encontrado para deleção")

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
    
    def get_pos_2_Nodos(self, id_nodo_origem, id_nodo_destino):
        coordenadas_2_nodos = []
        for nodo in self.Dados["Nodos"]:           
            if str(nodo["id"]) == str(id_nodo_origem):
                coordenadas_2_nodos.insert(0, (nodo["x"], nodo["y"]))

            if str(nodo["id"]) == str(id_nodo_destino):
                coordenadas_2_nodos.insert(1, (nodo["x"], nodo["y"]))
        print(coordenadas_2_nodos)
        # self.atualiza_Nodos()
        return coordenadas_2_nodos
    
    def atualiza_Nodos(self):
        self.Nodos = {node["id"]: (node["x"], node["y"]) for node in self.Dados["Nodos"]}

        


        


data = Mapa_rota()

data.importar_mapa("teste/arquivo_mapa.txt")

# print(data.Dados)
nodos = {node["id"]: (node["x"], node["y"]) for node in data.Dados["Nodos"]}
# print("\n",nodos)
# print(nodos, "\n")
# print(data.Dados["Nodos"], "\n")
# print(data.Nodos)
# print(data.Nodos.get("1"))
# print(data.Dados["Rotas"])

# data.limpar_mapa()
data.print_mapa()
data.criar_nodo(11,150,150)
data.print_mapa()











# data.criar_rota("1","5")
# print(data.print_mapa())
# for i in data.Dados['Obstaculos']:
#     print(type(i),i)
# print(data.Dados["Obstaculos"])
# for i in data.Dados["Nodos"]:
#     # print(i.get("id"))
#     # print(i.get("id"))
#     print(i.get("x"),i.get("y"))

# print(data.print_mapa())

#             # Armazena a linha da rota no dicionário com a chave sendo o par de nodos
#             self.linhas_rotas[(rota["from"], rota["to"])] = linha

#         # Desenha os nodos (círculos ou carro)
#         for node in data["nodos"]:
#             x, y = node["x"], node["y"]
#             id_ = node["id"]

#             # Verifica se é o nodo de id 1 para desenhar o carro
#             if id_ == 1:
#                 rota = []  # Rota vazia inicialmente
#                 self.carro = Carro(x, y, "SmartEntregas/imagem/carro.png", rota=rota)
#                 self.scene.addItem(self.carro)
#             else:
#                 circulo = QGraphicsEllipseItem(x - 10, y - 10, 20, 20)
#                 circulo.setBrush(QBrush(Qt.gray))
#                 self.scene.addItem(circulo)

#             # Adiciona um texto no centro do nodo com o ID
#             texto = QGraphicsTextItem(str(id_))
#             texto.setFont(QFont("Arial", 10))
#             texto.setPos(x - 5, y - 10)
#             self.scene.addItem(texto)


