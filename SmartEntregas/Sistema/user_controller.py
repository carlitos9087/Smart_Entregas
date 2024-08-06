from model import Model
from user_view import UserView


class UserController:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.model = Model()

        user_info = self.get_user_info(username)
        packages = self.get_user_packages(user_info['ID_Cliente'])

        self.user_view = UserView(root, self, user_info, packages)

    def get_user_info(self, username):
        query = "SELECT * FROM CLIENTE WHERE Nome=%s"
        self.model.cursor.execute(query, (username,))
        result = self.model.cursor.fetchone()
        return {"ID_Cliente": result["ID_Cliente"], "Nome": result["Nome"], "Endereco": result["Endereco"]}

    def get_user_packages(self, user_id):
        query = "SELECT * FROM PACOTE WHERE ID_Cliente=%s"
        self.model.cursor.execute(query, (user_id,))
        results = self.model.cursor.fetchall()
        return results

    def logout(self):
        self.model.close()
        self.root.quit()  # Fecha a aplicação

    def on_closing(self):
        self.logout()
