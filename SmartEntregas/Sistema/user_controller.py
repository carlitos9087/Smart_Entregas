import sysfrom PySide6.QtWidgets import QApplicationfrom notificacoes import Notificacoesfrom senha_controller import SenhaControllerfrom model import Modelfrom user_view import UserViewimport tkinter as tkclass UserController:    def __init__(self, root, username):        self.root = root        self.username = username        self.model = Model()        user_info = self.get_user_info(username)        packages = self.get_user_packages(user_info['ID_Cliente'])        self.user_view = UserView(root, self, user_info, packages)        app = QApplication.instance()        if app is None:  # Se não houver uma instância, crie uma nova            QApplication(sys.argv)    def get_user_info(self, username):        query = "SELECT * FROM CLIENTE WHERE Nome=%s"        self.model.cursor.execute(query, (username,))        result = self.model.cursor.fetchone()        return {"ID_Cliente": result["ID_Cliente"], "Nome": result["Nome"], "Endereco": result["Endereco"],                "Telefone": result["Telefone"]}    def get_user_packages(self, user_id):        query = "SELECT * FROM PACOTE WHERE ID_Cliente=%s"        self.model.cursor.execute(query, (user_id,))        results = self.model.cursor.fetchall()        return results    def logout(self):        self.model.close()        self.root.quit()  # Fecha a aplicação    def on_closing(self):        self.logout()    def show_frame(self, frame):        try:            if frame == "home_frame":                self.user_view.home_frame.grid(row=0, column=0, sticky="nsew")                self.user_view.conta_frame.grid_forget()  # Esconde a página conta                self.user_view.mapa_frame.grid_forget()  # Esconde a página mapa            elif frame == "conta_frame":                self.user_view.conta_frame.grid(row=0, column=0, sticky="nsew")                self.user_view.conta()                self.user_view.home_frame.grid_forget()  # Esconde a página home                self.user_view.mapa_frame.grid_forget()  # Esconde a página mapa                self.user_view.botao_frame.grid_forget()  # Esconde botões salvar e cancelar            else:                self.user_view.mapa_frame.grid(row=0, column=0, sticky="nsew")                self.user_view.mapa()                self.user_view.home_frame.grid_forget()  # Esconde a página home                self.user_view.conta_frame.grid_forget()  # Esconde a página conta        except AttributeError:            pass    def botao_editar_conta(self):        # self.user_view.botao_frame.grid(row=5, column=1, sticky="nsew")        self.user_view.botoes_salvar_cancelar()        self.user_view.entry_name.config(state="normal")        self.user_view.entry_adress.config(state="normal")        self.user_view.entry_phone.config(state="normal")    def botao_salvar(self):        id_cliente = self.user_view.user_info['ID_Cliente']        nome = self.user_view.entry_name.get().strip()        endereco = self.user_view.entry_adress.get().strip()        telefone = self.user_view.entry_phone.get().strip()        if nome != "" and endereco != "" and telefone != "":            self.model.atualizar_morador(id_cliente, nome, endereco, telefone)            self.user_view.user_info = self.get_user_info(nome)            self.atualizar_interface()            Notificacoes.conta_atualizada()            self.user_view.botao_frame.grid_forget()        else:            Notificacoes.campos_vazios()    def botao_cancelar(self):        self.user_view.botao_frame.grid_forget()        self.user_view.entry_name.delete(0, "end")        self.user_view.entry_adress.delete(0, "end")        self.user_view.entry_phone.delete(0, "end")        self.user_view.entry_name.insert(0, self.user_view.user_info['Nome'])        self.user_view.entry_name.config(state="readonly")        self.user_view.entry_adress.insert(0, self.user_view.user_info['Endereco'])        self.user_view.entry_adress.config(state="readonly")        self.user_view.entry_phone.insert(0, self.user_view.user_info['Telefone'])        self.user_view.entry_phone.config(state="readonly")    def botao_alterar_senha(self):        id_usuario = self.user_view.user_info['ID_Cliente']        tipo = 'morador'        SenhaController(id_usuario, tipo)    def atualizar_interface(self):        self.user_view.label_greeting.config(text=f"Olá {self.user_view.user_info['Nome']}!")        self.user_view.label_name.config(text=self.user_view.user_info['Nome'])        self.user_view.label_address.config(text=self.user_view.user_info['Endereco'])        self.user_view.label_phone.config(text=self.user_view.user_info['Telefone'])        self.user_view.entry_name.delete(0, tk.END)        self.user_view.entry_name.insert(0, self.user_view.user_info['Nome'])        self.user_view.entry_name.config(state="readonly")        self.user_view.entry_adress.delete(0, tk.END)        self.user_view.entry_adress.insert(0, self.user_view.user_info['Endereco'])        self.user_view.entry_adress.config(state="readonly")        self.user_view.entry_phone.delete(0, tk.END)        self.user_view.entry_phone.insert(0, self.user_view.user_info['Telefone'])        self.user_view.entry_phone.config(state="readonly")