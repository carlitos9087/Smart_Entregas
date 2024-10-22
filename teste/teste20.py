import heapq
import math
from itertools import permutations

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



# Função Dijkstra modificada para evitar caminhos bloqueados
# def dijkstra(start, goal, blocked_edges=[]):
#     # Criando o grafo de adjacência
#     graph = {node["id"]: [] for node in data["nodos"]}
    
#     for edge in data["rotas"]:
#         frm, to = edge["from"], edge["to"]
#         if (frm, to) in blocked_edges or (to, frm) in blocked_edges:
#             continue  # Pula esta rota se estiver bloqueada
#         x1, y1 = nodos[frm]
#         x2, y2 = nodos[to]
#         dist = math.hypot(x2 - x1, y2 - y1)
#         graph[frm].append((dist, to))
#         graph[to].append((dist, frm))

#     queue = [(0, start, [])]
#     seen = set()
    
#     while queue:
#         (cost, node, path) = heapq.heappop(queue)
#         if node in seen:
#             continue
#         path = path + [node]
#         seen.add(node)
#         if node == goal:
#             return path
#         for next_cost, next_node in graph[node]:
#             if next_node not in seen:
#                 heapq.heappush(queue, (cost + next_cost, next_node, path))

#     return []

# # Função TSP modificada para passar rotas bloqueadas para o Dijkstra
# def tsp(points, blocked_edges=[]):
#     min_path = None
#     min_dist = float('inf')
    
#     for perm in permutations(points):
#         perm = list(perm)
#         total_dist = 0
#         path = []
        
#         for i in range(len(perm) - 1):
#             dijkstra_path = dijkstra(perm[i], perm[i + 1], blocked_edges)
#             if not dijkstra_path:
#                 break
#             path.extend(dijkstra_path if not path else dijkstra_path[1:])
            
#             for j in range(len(dijkstra_path) - 1):
#                 x1, y1 = nodos[dijkstra_path[j]]
#                 x2, y2 = nodos[dijkstra_path[j + 1]]
#                 total_dist += math.hypot(x2 - x1, y2 - y1)
                
#         else:
#             if total_dist < min_dist:
#                 min_dist = total_dist
#                 min_path = path

#     return min_path

# # Exemplo de uso bloqueando a rota entre os nós 2 e 3
# blocked_edges = [(2, 3)]
# rota_otimizada = tsp([1, 3, 5], blocked_edges)
# print(rota_otimizada)
# a = nodos.values()
# print(a)

def encontrar_nodo_por_coordenadas(x, y, nodos):
    for id_nodo, coordenadas in nodos.items():
        if coordenadas == (x, y):
            return id_nodo
    return None  # Caso não encontre correspondência




# Exemplo de uso:
nodos = {node["id"]: (node["x"], node["y"]) for node in data["nodos"]}
x_input, y_input = 200, 20
id_nodo = encontrar_nodo_por_coordenadas(x_input, y_input, nodos)

if id_nodo:
    print(f"As coordenadas ({x_input}, {y_input}) pertencem ao nodo com ID {id_nodo}.")
else:
    print(f"Nenhum nodo encontrado para as coordenadas ({x_input}, {y_input}).")

def obter_coordenadas_por_id(id_nodo, nodos):
    """
    Encontra as coordenadas do nodo com base no ID fornecido.
    
    Args:
    - id_nodo (int): ID do nodo a ser encontrado.
    - nodos (dict): Dicionário de nodos onde a chave é o ID do nodo e o valor é uma tupla (x, y).
    
    Returns:
    - tuple ou None: Retorna uma tupla (x, y) das coordenadas se encontrado, caso contrário None.
    """
    return nodos.get(id_nodo, None)

# Exemplo de uso:
nodos = {node["id"]: (node["x"], node["y"]) for node in data["nodos"]}
id_input = 3
coordenadas = obter_coordenadas_por_id(id_input, nodos)
print(coordenadas)  # Esperado: (200, 20)
