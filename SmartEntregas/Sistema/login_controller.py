import sys
import tkinter as tk
from tkinter import messagebox

from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem)
from PySide6.QtGui import QPixmap
from model import Model
import sys
import os
from admin_view import Ui_MainWindow
from model import Model
from user_controller import UserController


class LoginController:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.create_login_view()

    def create_login_view(self):
        self.root.title("Login")
        self.root.geometry("400x300")

        self.label_name = tk.Label(self.root, text="Nome:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self.root, text="Senha:")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.button_admin_login = tk.Button(self.root, text="Login Admin", command=self.admin_login)
        self.button_admin_login.grid(row=2, column=0, columnspan=2, pady=10)

        self.button_user_login = tk.Button(self.root, text="Login Usuario", command=self.user_login)
        self.button_user_login.grid(row=3, column=0, columnspan=2, pady=10)

    def admin_login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        if self.model.validate_admin(name, password):
            messagebox.showinfo("Login Sucesso", "Bem-vindo, Admin!")
            self.open_admin_view(name)
        else:
            messagebox.showerror("Login Falhou", "Nome ou Senha inválidos")

    def user_login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        if self.model.validate_user(name, password):
            messagebox.showinfo("Login Sucesso", "Bem-vindo, Usuario!")
            self.open_user_view(name)
        else:
            messagebox.showerror("Login Falhou", "Nome ou Senha inválidos")

    def open_admin_view(self, name):
        self.root.withdraw()
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.setWindowTitle(f'Bem-vindo, {name}!')
        main_window.show()
        sys.exit(app.exec())

    def open_user_view(self, name):
        self.root.withdraw()
        user_window = tk.Toplevel(self.root)
        UserController(user_window, name)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Smart Entregas')
        self.model = Model()

        # botão realizar cadastro - cadastro de pacotes
        self.botao_realizar_cadastro.clicked.connect(self.precionar_botao_realizar_cadastro)

        # preenche o endereço na cricao da remessa
        self.lineEdit_id_pacote_1.editingFinished.connect(self.endereco_pacote_1)
        self.lineEdit_id_pacote_2.editingFinished.connect(self.endereco_pacote_2)

        # botão gerar json/ cadastrar remessa - criacao de remessa
        self.botao_json_remessa.clicked.connect(self.precionar_botao_json_remessa)

        # preenche as tabelas
        self.tabWidget_telas.currentChanged.connect(self.atualizar_tabelas)

        # coloca as imagens dos mapas
        self.imagem_mapa()

    def precionar_botao_realizar_cadastro(self):
        descricao = self.lineEdit_descricao.text()
        id_cliente = self.lineEdit_id_morador.text()
        status = self.lineEdit_status.text()
        volume = self.lineEdit_volume.text()
        peso = self.lineEdit_peso.text()
        id_cadastrado = self.model.cadastrar_pacote(descricao, id_cliente, status, volume, peso)
        self.label_resultado_cadastro.setText(f'O pacote foi inserido com o id:\n{id_cadastrado}')
        self.lineEdit_descricao.clear()
        self.lineEdit_id_morador.clear()
        self.lineEdit_status.clear()
        self.lineEdit_volume.clear()
        self.lineEdit_peso.clear()

    def precionar_botao_json_remessa(self):
        id_pacote_1 = self.lineEdit_id_pacote_1.text()
        id_pacote_2 = self.lineEdit_id_pacote_2.text()
        id_cadastrado = self.model.cadastrar_remessa(id_pacote_1, id_pacote_2)
        self.label_texto_remessa.setText(str(id_cadastrado))
        self.lineEdit_id_pacote_1.clear()
        self.lineEdit_id_pacote_2.clear()
        self.label_texto_endereco_1.clear()
        self.label_texto_endereco_2.clear()

    def endereco_pacote_1(self):
        id_pacote_1 = self.lineEdit_id_pacote_1.text()
        endereco = self.model.endereco_pacotes(id_pacote_1)
        self.label_texto_endereco_1.setText(endereco)

    def endereco_pacote_2(self):
        id_pacote_2 = self.lineEdit_id_pacote_2.text()
        endereco = self.model.endereco_pacotes(id_pacote_2)
        self.label_texto_endereco_2.setText(endereco)

    def tabela_moradores(self):
        moradores = self.model.lista_de_moradores()
        self.tableWidget_morador.clearContents()
        self.tableWidget_morador.setRowCount(len(moradores))

        for row, text in enumerate(moradores):
            self.tableWidget_morador.setItem(row, 0, QTableWidgetItem(str(text['ID_Cliente'])))
            self.tableWidget_morador.setItem(row, 1, QTableWidgetItem(text['Nome']))
            self.tableWidget_morador.setItem(row, 2, QTableWidgetItem(text['Endereco']))

    def tabela_pacotes(self):
        pacotes = self.model.lista_de_pacotes()
        self.tableWidget_pacote.clearContents()
        self.tableWidget_pacote.setRowCount(len(pacotes))

        for row, text in enumerate(pacotes):
            self.tableWidget_pacote.setItem(row, 0, QTableWidgetItem(str(text['ID_Pacote'])))
            self.tableWidget_pacote.setItem(row, 1, QTableWidgetItem(text['Descricao']))
            self.tableWidget_pacote.setItem(row, 2, QTableWidgetItem(str(text['ID_Cliente'])))
            self.tableWidget_pacote.setItem(row, 3, QTableWidgetItem(text['Status']))
            self.tableWidget_pacote.setItem(row, 4, QTableWidgetItem(text['Volume']))
            self.tableWidget_pacote.setItem(row, 5, QTableWidgetItem(str(text['Peso'])))

    def atualizar_tabelas(self):
        self.tabela_moradores()
        self.tabela_pacotes()

    def imagem_mapa(self):
        self.scene = QGraphicsScene()
        self.graphicsView_remessa.setScene(self.scene)
        self.graphicsView_acompanhamento.setScene(self.scene)
        # Caminho relativo para carregar a imagem
        image_path = os.path.join(os.path.dirname(__file__), '..', 'imagem', 'mapa.jpeg')
        self.load_image(image_path)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.scene.clear()
            pixmap_item = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(pixmap_item)
        else:
            print("Erro ao carregar a imagem.")

    def closeEvent(self, event):
        self.model.close()
        event.accept()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginController(root)
    root.mainloop()
