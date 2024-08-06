import pymysql


class Model:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sistema',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def validate_admin(self, name, password):
        query = "SELECT * FROM admin WHERE Nome=%s AND Senha=%s"
        self.cursor.execute(query, (name, password))
        return self.cursor.fetchone()

    def validate_user(self, name, password):
        query = "SELECT * FROM cliente WHERE Nome=%s AND Senha=%s"
        self.cursor.execute(query, (name, password))
        return self.cursor.fetchone()

    def cadastrar_pacote(self, descricao, id_cliente, status, volume, peso):
        query = "INSERT INTO pacote (Descricao, ID_Cliente, Status, Volume, Peso) VALUES (%s,%s,%s,%s,%s)"
        self.cursor.execute(query, (descricao, id_cliente, status, volume, peso))
        self.connection.commit()  # confirma a transação no banco de dados
        id_cadastrado = self.cursor.lastrowid
        return id_cadastrado

    def cadastrar_remessa(self, id_pacote_1, id_pacote_2):
        query = "INSERT INTO remessa (ID_Pacote_1, ID_Pacote_2) VALUES (%s, %s)"
        self.cursor.execute(query, (id_pacote_1, id_pacote_2))
        self.connection.commit()
        id_cadastro = self.cursor.lastrowid
        return id_cadastro

    def endereco_pacotes(self, id_pacote):
        query = '''SELECT Endereco FROM cliente LEFT OUTER JOIN pacote 
                   ON cliente.ID_Cliente = pacote.ID_Cliente
                   WHERE pacote.ID_Pacote = %s;
                '''
        self.cursor.execute(query, id_pacote)
        result = self.cursor.fetchone()
        if result:
            return result['Endereco']
        else:
            return "Não encontrado"
        return result

    def lista_de_moradores(self):
        query = "SELECT ID_Cliente, Nome, Endereco FROM cliente"
        self.cursor.execute(query)
        moradores = self.cursor.fetchall()
        return moradores

    def lista_de_pacotes(self):
        query = "SELECT * FROM pacote"
        self.cursor.execute(query)
        pacotes = self.cursor.fetchall()
        return pacotes

    def close(self):
        self.cursor.close()
        self.connection.close()
