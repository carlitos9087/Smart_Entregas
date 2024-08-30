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
        self.connection.commit()
        return self.cursor.lastrowid

    def cadastrar_remessa(self, id_pacote_1, id_pacote_2):
        query = "INSERT INTO remessa (ID_Pacote_1, ID_Pacote_2) VALUES (%s, %s)"
        self.cursor.execute(query, (id_pacote_1, id_pacote_2))
        self.connection.commit()
        return self.cursor.lastrowid

    def endereco_pacotes(self, id_pacote):
        query = '''SELECT Endereco FROM cliente LEFT OUTER JOIN pacote 
                   ON cliente.ID_Cliente = pacote.ID_Cliente
                   WHERE pacote.ID_Pacote = %s;
                '''
        self.cursor.execute(query, (id_pacote,))
        result = self.cursor.fetchone()
        return result['Endereco'] if result else "Não encontrado"

    def lista_de_moradores(self):
        query = "SELECT ID_Cliente, Nome, Endereco FROM cliente"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def lista_de_pacotes(self):
        query = "SELECT * FROM pacote"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        try:
            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

    def cadastrar_admin(self, nome, email, senha):
        query = "INSERT INTO admin (Nome, Senha, Email) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nome, senha, email))
        self.connection.commit()
        return self.cursor.lastrowid

    def lista_admin(self):
        query = "SELECT ID_Admin, Nome, Email FROM admin"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def excluir_admin(self, id_admin):
        query = "DELETE FROM admin WHERE ID_Admin = %s"
        self.cursor.execute(query, (id_admin,))
        self.connection.commit()

    def atualizar_admin(self, id_admin, nome, email):
        query = "UPDATE admin SET Nome = %s, Email = %s WHERE ID_Admin = %s"
        self.cursor.execute(query, (nome, email, id_admin))
        self.connection.commit()

    def filtro_admin(self, num_filtro, pesquisa):
        match num_filtro:
            case 0:
                query = "SELECT ID_Admin, Nome, Email FROM admin WHERE ID_Admin = %s"
            case 1:
                query = "SELECT ID_Admin, Nome, Email FROM admin WHERE Nome = %s"
            case 2:
                query = "SELECT ID_Admin, Nome, Email FROM admin WHERE Email = %s"
            case _:
                return print("Erro.")
        self.cursor.execute(query, (pesquisa,))
        return self.cursor.fetchall()

    def filtro_pacotes(self, num_filtro, pesquisa):
        match num_filtro:
            case 0:
                query = "SELECT * FROM pacote WHERE ID_Pacote = %s"
            case 1:
                query = "SELECT * FROM pacote WHERE Descricao = %s"
            case 2:
                query = "SELECT * FROM pacote WHERE ID_Cliente = %s"
            case 3:
                query = "SELECT * FROM pacote WHERE Status = %s"
            case 4:
                query = "SELECT * FROM pacote WHERE Volume = %s"
            case 5:
                query = "SELECT * FROM pacote WHERE Peso = %s"
            case _:
                return print("Erro.")
        self.cursor.execute(query, (pesquisa,))
        return self.cursor.fetchall()

    def atualizar_pacote(self, id_pacote, descricao, id_cliente, status, volume, peso):
        query = '''UPDATE pacote SET Descricao = %s, ID_Cliente = %s, Status = %s, 
                    Volume = %s, Peso = %s
                    WHERE ID_Pacote = %s'''
        self.cursor.execute(query, (descricao, id_cliente, status, volume, peso, id_pacote))
        self.connection.commit()

    def excluir_pacote(self, id_pacote):
        query = "DELETE FROM pacote WHERE ID_Pacote = %s"
        self.cursor.execute(query, (id_pacote,))
        self.connection.commit()

    def lista_remessa(self):
        query = "SELECT * FROM remessa"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def atualizar_remessa(self, id_remessa, id_pacote_1, id_pacote_2):
        query = "UPDATE remessa SET ID_Pacote_1 = %s, ID_Pacote_2 = %s WHERE ID_Remessa = %s"
        self.cursor.execute(query, (id_pacote_1, id_pacote_2, id_remessa))
        self.connection.commit()

    def excluir_remessa(self, id_remessa):
        query = "DELETE FROM remessa WHERE ID_Remessa = %s"
        self.cursor.execute(query, (id_remessa,))
        self.connection.commit()

    def filtro_remessa(self, num_filtro, pesquisa):
        match num_filtro:
            case 0:
                query = "SELECT * FROM remessa WHERE ID_Remessa = %s"
            case 1:
                query = "SELECT * FROM remessa WHERE ID_Pacote_1 = %s"
            case 2:
                query = "SELECT * FROM remessa WHERE ID_Pacote_2 = %s"
            case _:
                return print("Erro.")
        self.cursor.execute(query, (pesquisa,))
        return self.cursor.fetchall()

    def cadastrar_morador(self, nome, senha, endereco, telefone):
        query = "INSERT INTO CLIENTE (Nome, Senha, Endereco, Telefone) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nome, senha, endereco, telefone))
        self.connection.commit()
        return self.cursor.lastrowid

    def lista_morador(self):
        query = "SELECT ID_Cliente, Nome, Endereco, Telefone FROM CLIENTE"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def excluir_morador(self, id_cliente):
        query = "DELETE FROM CLIENTE WHERE ID_Cliente = %s"
        self.cursor.execute(query, (id_cliente,))
        self.connection.commit()

    def atualizar_morador(self, id_cliente, nome, endereco, telefone):
        query = "UPDATE CLIENTE SET Nome = %s, Endereco = %s, Telefone = %s WHERE ID_Cliente = %s"
        self.cursor.execute(query, (nome, endereco, telefone, id_cliente))
        self.connection.commit()

    def filtro_morador(self, num_filtro, pesquisa):
        match num_filtro:
            case 0:
                query = "SELECT ID_Cliente, Nome, Endereco, Telefone FROM CLIENTE WHERE ID_Cliente = %s"
            case 1:
                query = "SELECT ID_Cliente, Nome, Endereco, Telefone FROM CLIENTE WHERE Nome = %s"
            case 2:
                query = "SELECT ID_Cliente, Nome, Endereco, Telefone FROM CLIENTE WHERE Endereco = %s"
            case 3:
                query = "SELECT ID_Cliente, Nome, Endereco, Telefone FROM CLIENTE WHERE Telefone = %s"
            case _:
                return print("Erro.")
        self.cursor.execute(query, (pesquisa,))
        return self.cursor.fetchall()
