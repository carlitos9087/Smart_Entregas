from model import Model

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QLineEdit


class RemessaController:
    def __init__(self):

        self.NAME_NODE_RELATIONSHIP = {
            "b": 1,
            "Jane_Doe": 2,
            "Billy the Kid": 3,
            "Trish Cinq": 9
        }

        self.model = Model()

    pass

    def get_dados_remessa(self, id_remessa):
        query = "SELECT * FROM remessa WHERE id_remessa = %s"
        self.model.cursor.execute(query, (id_remessa,))
        remessa_data = self.model.cursor.fetchone()

        return remessa_data

    def get_donos_pacote(self, remessa_data):
        ID_Pacote_1 = remessa_data['ID_Pacote_1']
        ID_Pacote_2 = remessa_data['ID_Pacote_2']
        names_remessa = []


        if ID_Pacote_1:
            query = "SELECT CLIENTE.Nome FROM CLIENTE INNER JOIN PACOTE on PACOTE.ID_Cliente = CLIENTE.ID_Cliente WHERE ID_Pacote = %s"
            self.model.cursor.execute(query, (ID_Pacote_1,))
            names_remessa.append(self.model.cursor.fetchone())

        if ID_Pacote_2:
            query = "SELECT CLIENTE.Nome FROM CLIENTE INNER JOIN PACOTE on PACOTE.ID_Cliente = CLIENTE.ID_Cliente WHERE ID_Pacote = %s"
            self.model.cursor.execute(query, (ID_Pacote_2,))
            names_remessa.append(self.model.cursor.fetchone())

        return names_remessa

    def relacionar_nomes_nodos(self, names_remessa):
        nodos_relacionados = []
        for name in names_remessa:
            print(name)

            node = self.NAME_NODE_RELATIONSHIP.get(name["Nome"])
            if node:
                nodos_relacionados.append(node)
        return nodos_relacionados

