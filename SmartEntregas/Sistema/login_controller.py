import os
import sys
import tkinter as tk
from tkinter import messagebox

import pymysql
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, QGraphicsScene, QGraphicsPixmapItem)

from SmartEntregas.Sistema.notificacoes import Notificacoes
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

        # linha selecionada nas tabelas
        self.linha_selecionada = -1
        self.tableWidget_lista_pacotes.cellClicked.connect(self.tableWidget_lista_pacotes.selectRow)
        self.tableWidget_lista_admin.cellClicked.connect(self.tableWidget_lista_admin.selectRow)
        self.tableWidget_lista_remessa.cellClicked.connect(self.tableWidget_lista_remessa.selectRow)

        # botão cadastrar admin
        self.botao_cadastro_admin.clicked.connect(self.precionar_cadastrar_admin)

        # botão mostar tela de alteração de admin
        self.frame_alteracoes_admin.setMaximumWidth(9)
        self.botao_alterar_admin.clicked.connect(self.mostrar_alterar_admin)

        # botão salvar alterar admin
        self.botao_salvar_alterar_admin.clicked.connect(self.atualizar_admin)

        # botão cancelar alterar admin
        self.botao_cancelar_alterar_admin.clicked.connect(self.mostrar_alterar_admin)

        # botão excluir admin
        self.botao_excluir_admin.clicked.connect(self.excluir_admin)

        # botão filtro da lista de admin
        self.frame_filtro_admin.setMaximumWidth(9)
        self.botao_filtro_admin.clicked.connect(self.mostrar_filtro_admin)

        # botão aplicar filtro admin
        self.botao_aplicar_admin.clicked.connect(self.filtro_admin)

        # botão restaurar filtro admin
        self.botao_restaurar_filtro_admin.clicked.connect(self.lista_admin)

        # botão filtro da lista de pacotes
        self.frame_filtro_pacotes.setMaximumWidth(9)
        self.botao_filtro_pacote.clicked.connect(self.mostrar_filtro_pacote)

        # botão aplicar filtro pacotes
        self.botao_aplicar_pacotes.clicked.connect(self.filtro_pacote)

        # botao restaurar filtro pacotes
        self.botao_restaurar_filtro_pacotes.clicked.connect(self.lista_pacotes)

        # botão mostrar tela de alteração de pacotes
        self.frame_alteracoes_pacote.setMaximumWidth(9)
        self.botao_alterar_pacote.clicked.connect(self.mostrar_alterar_pacote)

        # botão salvar alterar pacote
        self.botao_salvar_alterar_pacote.clicked.connect(self.botao_atualizar_pacote)

        # botão cancelar alterar pacote
        self.botao_cancelar_alterar_pacote.clicked.connect(self.mostrar_alterar_pacote)

        # botão excluir pacote
        self.botao_excluir_pacote.clicked.connect(self.excluir_pacote)

        # botão mostrar filtro remessa
        self.frame_filtro_remessa.setMaximumWidth(9)
        self.botao_filtro_remessa.clicked.connect(self.mostar_filtro_remessa)

        # botão aplicar filtro remessa
        self.botao_aplicar_remessa.clicked.connect(self.filtro_remessa)

        # botão restaurar filtro remessa
        self.botao_restaurar_filtro_remessa.clicked.connect(self.lista_remessa)

        # botão mostar alterações remessa
        self.frame_alteracoes_remessa.setMaximumWidth(9)
        self.botao_alterar_remessa.clicked.connect(self.mostrar_alterar_remessa)

        # botão salvar alterações remessa
        self.botao_salvar_alterar_remessa.clicked.connect(self.botao_atualizar_remessa)

        # botão cancelar alterar remessa
        self.botao_cancelar_alterar_remessa.clicked.connect(self.mostrar_alterar_remessa)

        # botão excluir remessa
        self.botao_excluir_remessa.clicked.connect(self.excluir_remessa)

        #PT1
        # botão cadastrar morador
        self.botao_cadastro_morador.clicked.connect(self.precionar_cadastrar_morador)

        # botão mostar tela de alteração de morador
        self.frame_alteracoes_morador.setMaximumWidth(9)
        self.botao_alterar_morador.clicked.connect(self.mostrar_alterar_morador)

        # botão salvar alterar morador
        self.botao_salvar_alterar_morador.clicked.connect(self.atualizar_morador)

        # botão cancelar alterar morador
        self.botao_cancelar_alterar_morador.clicked.connect(self.mostrar_alterar_morador)

        # botão excluir morador
        self.botao_excluir_morador.clicked.connect(self.excluir_morador)

        # botão filtro da lista de morador
        self.label_filtro_morador.setMaximumWidth(9)
        self.botao_filtro_morador.clicked.connect(self.mostrar_filtro_morador)

        # botão aplicar filtro morador
        self.botao_aplicar_morador.clicked.connect(self.filtro_morador)

        # botão restaurar filtro morador
        self.botao_restaurar_filtro_morador.clicked.connect(self.lista_morador)

        

    def precionar_botao_realizar_cadastro(self):
        try:
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
        except pymysql.err.IntegrityError:
            Notificacoes.morador_nao_existe()

    def precionar_botao_json_remessa(self):
        try:
            id_pacote_1 = self.lineEdit_id_pacote_1.text()
            id_pacote_2 = self.lineEdit_id_pacote_2.text()
            id_remessa = self.model.cadastrar_remessa(id_pacote_1, id_pacote_2)
            self.lineEdit_id_pacote_1.clear()
            self.lineEdit_id_pacote_2.clear()
            self.label_texto_endereco_1.clear()
            self.label_texto_endereco_2.clear()
            Notificacoes.remessa_cadastrada(id_remessa)
        except pymysql.err.IntegrityError:
            Notificacoes.erro_cadastrar_remessa()

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

        for text in moradores:
            if all(key in text for key in ['ID_Cliente', 'Nome', 'Endereco', 'Telefone']):
                row = self.tableWidget_morador.rowCount()
                self.tableWidget_morador.insertRow(row)

                item_id_cliente = QTableWidgetItem(str(text['ID_Cliente']))
                item_id_cliente.setFlags(item_id_cliente.flags() & ~Qt.ItemIsEditable)
                item_nome = QTableWidgetItem(str(text['Nome']))
                item_nome.setFlags(item_nome.flags() & ~Qt.ItemIsEditable)
                item_endereco = QTableWidgetItem(str(text['Endereco']))
                item_endereco.setFlags(item_endereco.flags() & ~Qt.ItemIsEditable)
                item_telefone = QTableWidgetItem(str(text['Telefone']))
                item_telefone.setFlags(item_telefone.flags() & ~Qt.ItemIsEditable)

                self.tableWidget_morador.setItem(row, 0, item_id_cliente)
                self.tableWidget_morador.setItem(row, 1, item_nome)
                self.tableWidget_morador.setItem(row, 2, item_endereco)
                self.tableWidget_morador.setItem(row, 3, item_telefone)

    #PT3
    def precionar_cadastrar_morador(self):
        # Função para cadastrar um novo morador (Create)
        nome = self.lineEdit_nome_morador.text()
        senha = self.lineEdit_senha_morador.text()
        endereco = self.lineEdit_endereco.text()
        telefone = self.lineEdit_telefone.text()


        # Cadastra o morador no banco de dados e retorna o ID cadastrado
        id_cadastrado = self.model.cadastrar_morador(nome, senha, endereco, telefone)

        # Atualiza a interface para mostrar o ID do morador cadastrado
        self.label_resultado_morador.setText(f'Morador cadastrado com o id:\n{id_cadastrado}')

        # Limpa os campos de entrada após o cadastro
        self.lineEdit_nome_morador.clear()
        self.lineEdit_senha_morador.clear()
        self.lineEdit_endereco.clear()
        self.lineEdit_telefone.clear()

    def mostrar_filtro_morador(self):
        # Função para mostrar ou esconder a interface de filtro (Read/Filter)
        width = self.label_filtro_morador.width()


        if width == 9:
            new_width = 300
            self.label_filtro_morador.setMaximumWidth(new_width)
            self.label_filtro_morador.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
        else:
            new_width = 9
            self.label_filtro_morador.setMaximumWidth(new_width)
            self.label_filtro_morador.setStyleSheet("""
                QFrame{
                    border: 0px solid black;
                    border-radius: 2px;
                }
            """)

        # Animação para transição suave ao mostrar ou esconder o filtro
        self.animation = QtCore.QPropertyAnimation(self.label_filtro_morador, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mostrar_alterar_morador(self):
        # Função para mostrar a interface de alteração de morador (Update)
        width = self.frame_alteracoes_morador.width()
        select_model = self.tableWidget_lista_moradores.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_moradores.currentRow()
        elif self.linha_selecionada == -1:
            Notificacoes.selecione_linha("ALTERAR", "modificar um Morador")

        if width == 9 and self.linha_selecionada != -1:
            new_width = 300
            self.frame_alteracoes_morador.setMaximumWidth(new_width)
            self.frame_alteracoes_morador.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
            # Preenche os campos com os dados do morador selecionado para edição
            self.label_id_morador_num.setText(self.tableWidget_lista_moradores.item(self.linha_selecionada, 0).text())
            self.lineEdit_nome_morador_alterar.setText(
                self.tableWidget_lista_moradores.item(self.linha_selecionada, 1).text())
            self.lineEdit_endereco_alterar.setText(
                self.tableWidget_lista_moradores.item(self.linha_selecionada, 2).text())
            self.lineEdit_telefone_alterar.setText(
                self.tableWidget_lista_moradores.item(self.linha_selecionada, 3).text())

        else:
            new_width = 9
            self.frame_alteracoes_morador.setMaximumWidth(new_width)
            self.frame_alteracoes_morador.setStyleSheet("""
                 QFrame{
                     border: 0px solid black;
                     border-radius: 2px;
                 }
            """)
            self.linha_selecionada = -1
            self.tableWidget_lista_moradores.clearSelection()

        # Animação para transição suave ao mostrar ou esconder a interface de alteração
        self.animation = QtCore.QPropertyAnimation(self.frame_alteracoes_morador, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def lista_morador(self):
        # Função para listar todos os moradores (Read)
        self.lineEdit_filtro_morador.clear()
        morador = self.model.lista_morador()
        self.tableWidget_lista_moradores.clearContents()
        self.tableWidget_lista_moradores.setRowCount(len(morador))

        for row, text in enumerate(morador):
            # Preenche a tabela com os dados dos moradores
            item_id_morador = QTableWidgetItem(str(text['ID_Cliente']))
            item_id_morador.setFlags(item_id_morador.flags() & ~Qt.ItemIsEditable)
            item_nome = QTableWidgetItem(text['Nome'])
            item_nome.setFlags(item_nome.flags() & ~Qt.ItemIsEditable)
            item_endereco = QTableWidgetItem(str(text['Endereco']))
            item_endereco.setFlags(item_endereco.flags() & ~Qt.ItemIsEditable)
            item_telefone = QTableWidgetItem(str(text['Telefone']))
            item_telefone.setFlags(item_telefone.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_moradores.setItem(row, 0, item_id_morador)
            self.tableWidget_lista_moradores.setItem(row, 1, item_nome)
            self.tableWidget_lista_moradores.setItem(row, 2, item_endereco)
            self.tableWidget_lista_moradores.setItem(row, 3, item_telefone)

        # Ajusta o tamanho das colunas ao conteúdo
        self.tableWidget_lista_moradores.resizeColumnsToContents()

    def excluir_morador(self):
        # Função para excluir um morador (Delete)
        select_model = self.tableWidget_lista_moradores.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_moradores.currentRow()
        else:
            Notificacoes.selecione_linha("EXCLUIR", "excluir um Morador")
            return

        if self.linha_selecionada != -1:
            id_cliente = self.tableWidget_lista_moradores.item(self.linha_selecionada, 0).text()
            btn = Notificacoes.confirmar_exclusao(id_cliente)

            if btn != 0:
                # Chama o método para excluir o morador do banco de dados
                self.model.excluir_morador(btn)
                Notificacoes.exclusao_concluida()
            else:
                print("Exclusão cancelada.")

        # Atualiza a lista de moradores após a exclusão
        self.lista_morador()

    def atualizar_morador(self):
        # Função para atualizar os dados de um morador (Update)
        id_cliente = self.label_id_morador_num.text()
        nome = self.lineEdit_nome_morador_alterar.text()
        endereco = self.lineEdit_endereco_alterar.text()
        telefone = self.lineEdit_telefone_alterar.text()

        # Atualiza os dados do morador no banco de dados
        self.model.atualizar_morador(id_cliente, nome, endereco, telefone)

        # Limpa os campos de alteração após a atualização
        self.label_id_morador_num.clear()
        self.lineEdit_nome_morador_alterar.clear()
        self.lineEdit_endereco_alterar.clear()
        self.lineEdit_telefone_alterar.clear()

        # Atualiza a lista de moradores e esconde a interface de alteração
        self.lista_morador()
        self.mostrar_alterar_morador()
        Notificacoes.atualizacao_concluida()

    def filtro_morador(self):
        # Função para filtrar os moradores na lista (Read/Filter)
        num_filtro = self.comboBox_filtro_morador.currentIndex()
        pesquisa = self.lineEdit_filtro_morador.text()
        morador = self.model.filtro_morador(num_filtro, pesquisa)
        self.tableWidget_lista_moradores.clearContents()
        self.tableWidget_lista_moradores.setRowCount(len(morador))

        for row, text in enumerate(morador):
            # Preenche a tabela com os dados filtrados dos moradores
            item_id_morador = QTableWidgetItem(str(text['ID_Cliente']))
            item_id_morador.setFlags(item_id_morador.flags() & ~Qt.ItemIsEditable)
            item_nome = QTableWidgetItem(text['Nome'])
            item_nome.setFlags(item_nome.flags() & ~Qt.ItemIsEditable)
            item_endereco = QTableWidgetItem(str(text['Endereco']))
            item_endereco.setFlags(item_endereco.flags() & ~Qt.ItemIsEditable)
            item_telefone = QTableWidgetItem(str(text['Telefone']))
            item_telefone.setFlags(item_telefone.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens filtrados à tabela
            self.tableWidget_lista_moradores.setItem(row, 0, item_id_morador)
            self.tableWidget_lista_moradores.setItem(row, 1, item_nome)
            self.tableWidget_lista_moradores.setItem(row, 2, item_endereco)
            self.tableWidget_lista_moradores.setItem(row, 3, item_telefone)

        # Ajusta o tamanho das colunas ao conteúdo
        self.tableWidget_lista_moradores.resizeColumnsToContents()

    def tabela_pacotes(self):
        pacotes = self.model.lista_de_pacotes()
        self.tableWidget_pacote.clearContents()
        self.tableWidget_pacote.setRowCount(len(pacotes))

        for row, text in enumerate(pacotes):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_pacote = QTableWidgetItem(str(text['ID_Pacote']))
            item_id_pacote.setFlags(item_id_pacote.flags() & ~Qt.ItemIsEditable)
            item_descricao = QTableWidgetItem(text['Descricao'])
            item_descricao.setFlags(item_descricao.flags() & ~Qt.ItemIsEditable)
            item_id_cliente = QTableWidgetItem(str(text['ID_Cliente']))
            item_id_cliente.setFlags(item_id_cliente.flags() & ~Qt.ItemIsEditable)
            item_status = QTableWidgetItem(text['Status'])
            item_status.setFlags(item_status.flags() & ~Qt.ItemIsEditable)
            item_volume = QTableWidgetItem(text['Volume'])
            item_volume.setFlags(item_volume.flags() & ~Qt.ItemIsEditable)
            item_peso = QTableWidgetItem(str(text['Peso']))
            item_peso.setFlags(item_peso.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_pacote.setItem(row, 0, item_id_pacote)
            self.tableWidget_pacote.setItem(row, 1, item_descricao)
            self.tableWidget_pacote.setItem(row, 2, item_id_cliente)
            self.tableWidget_pacote.setItem(row, 3, item_status)
            self.tableWidget_pacote.setItem(row, 4, item_volume)
            self.tableWidget_pacote.setItem(row, 5, item_peso)

    def atualizar_tabelas(self):
        self.tabela_moradores()
        self.tabela_pacotes()
        self.lista_admin()
        self.lista_pacotes()
        self.lista_remessa()
        self.restaurar_labels_resultado()

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

    def restaurar_labels_resultado(self):
        self.label_resultado_cadastro.setText(f'O pacote foi inserido com o id:')
        self.label_resultado_admin.setText(f'Administrador cadastrado com o id:')

    def precionar_cadastrar_admin(self):
        nome = self.lineEdit_nome_admin.text()
        senha = self.lineEdit_senha_admin.text()
        email = self.lineEdit_email_admin.text()
        id_cadastrado = self.model.cadastrar_admin(nome, email, senha)
        self.label_resultado_admin.setText(f'Administrador cadastrado com o id:\n{id_cadastrado}')
        self.lineEdit_nome_admin.clear()
        self.lineEdit_email_admin.clear()
        self.lineEdit_senha_admin.clear()

    def mostrar_filtro_admin(self):
        width = self.frame_filtro_admin.width()

        if width == 9:
            new_width = 300
            self.frame_filtro_admin.setMaximumWidth(new_width)
            self.frame_filtro_admin.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
        else:
            new_width = 9
            self.frame_filtro_admin.setMaximumWidth(new_width)
            self.frame_filtro_admin.setStyleSheet("""
                QFrame{
                    border: 0px solid black;
                    border-radius: 2px;
                }
            """)

        self.animation = QtCore.QPropertyAnimation(self.frame_filtro_admin, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mostrar_alterar_admin(self):
        width = self.frame_alteracoes_admin.width()
        select_model = self.tableWidget_lista_admin.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_admin.currentRow()
        elif self.linha_selecionada == -1:
            Notificacoes.selecione_linha("ALTERAR", "modificar um administrador")

        if width == 9 and self.linha_selecionada != -1:
            new_width = 300
            self.frame_alteracoes_admin.setMaximumWidth(new_width)
            self.frame_alteracoes_admin.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
            self.label_id_admin_num.setText(self.tableWidget_lista_admin.item(self.linha_selecionada, 0).text())
            self.lineEdit_nome_admin_alterar.setText(
                self.tableWidget_lista_admin.item(self.linha_selecionada, 1).text())
            self.lineEdit_email_alterar.setText(
                self.tableWidget_lista_admin.item(self.linha_selecionada, 2).text())

        else:
            new_width = 9
            self.frame_alteracoes_admin.setMaximumWidth(new_width)
            self.frame_alteracoes_admin.setStyleSheet("""
                 QFrame{
                     border: 0px solid black;
                     border-radius: 2px;
                 }
            """)
            self.linha_selecionada = -1
            self.tableWidget_lista_admin.clearSelection()

        self.animation = QtCore.QPropertyAnimation(self.frame_alteracoes_admin, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def lista_admin(self):
        self.lineEdit_filtro_admin.clear()
        admin = self.model.lista_admin()
        self.tableWidget_lista_admin.clearContents()
        self.tableWidget_lista_admin.setRowCount(len(admin))

        for row, text in enumerate(admin):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_admin = QTableWidgetItem(str(text['ID_Admin']))
            item_id_admin.setFlags(item_id_admin.flags() & ~Qt.ItemIsEditable)
            item_nome = QTableWidgetItem(text['Nome'])
            item_nome.setFlags(item_nome.flags() & ~Qt.ItemIsEditable)
            item_email = QTableWidgetItem(str(text['Email']))
            item_email.setFlags(item_email.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_admin.setItem(row, 0, item_id_admin)
            self.tableWidget_lista_admin.setItem(row, 1, item_nome)
            self.tableWidget_lista_admin.setItem(row, 2, item_email)

        self.tableWidget_lista_admin.resizeColumnsToContents()

    def excluir_admin(self):
        select_model = self.tableWidget_lista_admin.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_admin.currentRow()
        else:
            Notificacoes.selecione_linha("EXCLUIR", "excluir um administrador")
            return

        if self.linha_selecionada != -1:
            id_admin = self.tableWidget_lista_admin.item(self.linha_selecionada, 0).text()
            btn = Notificacoes.confirmar_exclusao(id_admin)

            if btn != 0:
                self.model.excluir_admin(btn)
                Notificacoes.exclusao_concluida()
            else:
                print("Exclusão cancelada.")

        self.lista_admin()

    def atualizar_admin(self):
        id_admin = self.label_id_admin_num.text()
        nome = self.lineEdit_nome_admin_alterar.text()
        email = self.lineEdit_email_alterar.text()
        self.model.atualizar_admin(id_admin, nome, email)
        self.label_id_admin_num.clear()
        self.lineEdit_nome_admin_alterar.clear()
        self.lineEdit_email_alterar.clear()
        self.lista_admin()
        self.mostrar_alterar_admin()
        Notificacoes.atualizacao_concluida()

    def filtro_admin(self):
        num_filtro = self.comboBox_filtro_admin.currentIndex()
        pesquisa = self.lineEdit_filtro_admin.text()
        admin = self.model.filtro_admin(num_filtro, pesquisa)
        self.tableWidget_lista_admin.clearContents()
        self.tableWidget_lista_admin.setRowCount(len(admin))

        for row, text in enumerate(admin):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_admin = QTableWidgetItem(str(text['ID_Admin']))
            item_id_admin.setFlags(item_id_admin.flags() & ~Qt.ItemIsEditable)
            item_nome = QTableWidgetItem(text['Nome'])
            item_nome.setFlags(item_nome.flags() & ~Qt.ItemIsEditable)
            item_email = QTableWidgetItem(str(text['Email']))
            item_email.setFlags(item_email.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_admin.setItem(row, 0, item_id_admin)
            self.tableWidget_lista_admin.setItem(row, 1, item_nome)
            self.tableWidget_lista_admin.setItem(row, 2, item_email)

        self.tableWidget_lista_admin.resizeColumnsToContents()

    def mostrar_filtro_pacote(self):
        width = self.frame_filtro_pacotes.width()

        if width == 9:
            new_width = 300
            self.frame_filtro_pacotes.setMaximumWidth(new_width)
            self.frame_filtro_pacotes.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
        else:
            new_width = 9
            self.frame_filtro_pacotes.setMaximumWidth(new_width)
            self.frame_filtro_pacotes.setStyleSheet("""
                QFrame{
                    border: 0px solid black;
                    border-radius: 2px;
                }
            """)

        self.animation = QtCore.QPropertyAnimation(self.frame_filtro_pacotes, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mostrar_alterar_pacote(self):
        width = self.frame_alteracoes_pacote.width()
        select_model = self.tableWidget_lista_pacotes.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_pacotes.currentRow()
        elif self.linha_selecionada == -1:
            Notificacoes.selecione_linha("ALTERAR", "modificar um pacote")

        if width == 9 and self.linha_selecionada != -1:
            new_width = 300
            self.frame_alteracoes_pacote.setMaximumWidth(new_width)
            self.frame_alteracoes_pacote.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
            self.label_id_pacote_num.setText(self.tableWidget_lista_pacotes.item(self.linha_selecionada, 0).text())
            self.lineEdit_descricao_alterar.setText(
                self.tableWidget_lista_pacotes.item(self.linha_selecionada, 1).text())
            self.lineEdit_id_morador_alterar.setText(
                self.tableWidget_lista_pacotes.item(self.linha_selecionada, 2).text())
            self.lineEdit_status_alterar.setText(self.tableWidget_lista_pacotes.item(self.linha_selecionada, 3).text())
            self.lineEdit_volume_alterar.setText(self.tableWidget_lista_pacotes.item(self.linha_selecionada, 4).text())
            self.lineEdit_peso_alterar.setText(self.tableWidget_lista_pacotes.item(self.linha_selecionada, 5).text())

        else:
            new_width = 9
            self.frame_alteracoes_pacote.setMaximumWidth(new_width)
            self.frame_alteracoes_pacote.setStyleSheet("""
                 QFrame{
                     border: 0px solid black;
                     border-radius: 2px;
                 }
            """)
            self.linha_selecionada = -1
            self.tableWidget_lista_pacotes.clearSelection()

        self.animation = QtCore.QPropertyAnimation(self.frame_alteracoes_pacote, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def filtro_pacote(self):
        num_filtro = self.comboBox_filtro_pacotes.currentIndex()
        pesquisa = self.lineEdit_filtro_pacotes.text()
        pacotes = self.model.filtro_pacotes(num_filtro, pesquisa)
        self.tableWidget_lista_pacotes.clearContents()
        self.tableWidget_lista_pacotes.setRowCount(len(pacotes))

        for row, text in enumerate(pacotes):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_pacote = QTableWidgetItem(str(text['ID_Pacote']))
            item_id_pacote.setFlags(item_id_pacote.flags() & ~Qt.ItemIsEditable)
            item_descricao = QTableWidgetItem(text['Descricao'])
            item_descricao.setFlags(item_descricao.flags() & ~Qt.ItemIsEditable)
            item_id_cliente = QTableWidgetItem(str(text['ID_Cliente']))
            item_id_cliente.setFlags(item_id_cliente.flags() & ~Qt.ItemIsEditable)
            item_status = QTableWidgetItem(text['Status'])
            item_status.setFlags(item_status.flags() & ~Qt.ItemIsEditable)
            item_volume = QTableWidgetItem(text['Volume'])
            item_volume.setFlags(item_volume.flags() & ~Qt.ItemIsEditable)
            item_peso = QTableWidgetItem(str(text['Peso']))
            item_peso.setFlags(item_peso.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_pacotes.setItem(row, 0, item_id_pacote)
            self.tableWidget_lista_pacotes.setItem(row, 1, item_descricao)
            self.tableWidget_lista_pacotes.setItem(row, 2, item_id_cliente)
            self.tableWidget_lista_pacotes.setItem(row, 3, item_status)
            self.tableWidget_lista_pacotes.setItem(row, 4, item_volume)
            self.tableWidget_lista_pacotes.setItem(row, 5, item_peso)

        self.tableWidget_lista_pacotes.resizeColumnsToContents()

    def lista_pacotes(self):
        self.lineEdit_filtro_pacotes.clear()
        pacotes = self.model.lista_de_pacotes()
        self.tableWidget_lista_pacotes.clearContents()
        self.tableWidget_lista_pacotes.setRowCount(len(pacotes))

        for row, text in enumerate(pacotes):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_pacote = QTableWidgetItem(str(text['ID_Pacote']))
            item_id_pacote.setFlags(item_id_pacote.flags() & ~Qt.ItemIsEditable)
            item_descricao = QTableWidgetItem(text['Descricao'])
            item_descricao.setFlags(item_descricao.flags() & ~Qt.ItemIsEditable)
            item_id_cliente = QTableWidgetItem(str(text['ID_Cliente']))
            item_id_cliente.setFlags(item_id_cliente.flags() & ~Qt.ItemIsEditable)
            item_status = QTableWidgetItem(text['Status'])
            item_status.setFlags(item_status.flags() & ~Qt.ItemIsEditable)
            item_volume = QTableWidgetItem(text['Volume'])
            item_volume.setFlags(item_volume.flags() & ~Qt.ItemIsEditable)
            item_peso = QTableWidgetItem(str(text['Peso']))
            item_peso.setFlags(item_peso.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_pacotes.setItem(row, 0, item_id_pacote)
            self.tableWidget_lista_pacotes.setItem(row, 1, item_descricao)
            self.tableWidget_lista_pacotes.setItem(row, 2, item_id_cliente)
            self.tableWidget_lista_pacotes.setItem(row, 3, item_status)
            self.tableWidget_lista_pacotes.setItem(row, 4, item_volume)
            self.tableWidget_lista_pacotes.setItem(row, 5, item_peso)

        self.tableWidget_lista_pacotes.resizeColumnsToContents()

    def botao_atualizar_pacote(self):
        try:
            id_pacote = self.label_id_pacote_num.text()
            descricao = self.lineEdit_descricao_alterar.text()
            id_morador = self.lineEdit_id_morador_alterar.text()
            status = self.lineEdit_status_alterar.text()
            volume = self.lineEdit_volume_alterar.text()
            peso = self.lineEdit_peso_alterar.text()
            self.model.atualizar_pacote(id_pacote, descricao, id_morador, status, volume, peso)
            self.lineEdit_descricao_alterar.clear()
            self.lineEdit_id_morador_alterar.clear()
            self.lineEdit_status_alterar.clear()
            self.lineEdit_volume_alterar.clear()
            self.lineEdit_peso_alterar.clear()
            self.lista_pacotes()
            self.mostrar_alterar_pacote()
            Notificacoes.atualizacao_concluida()
        except pymysql.err.IntegrityError:
            Notificacoes.morador_nao_existe()

    def excluir_pacote(self):
        try:
            select_model = self.tableWidget_lista_pacotes.selectionModel().hasSelection()

            if select_model is True:
                self.linha_selecionada = self.tableWidget_lista_pacotes.currentRow()
            else:
                Notificacoes.selecione_linha("EXCLUIR", "excluir um pacote")
                return

            if self.linha_selecionada != -1:
                id_pacote = self.tableWidget_lista_pacotes.item(self.linha_selecionada, 0).text()
                btn = Notificacoes.confirmar_exclusao(id_pacote)

                if btn != 0:
                    self.model.excluir_pacote(btn)
                    Notificacoes.exclusao_concluida()
                else:
                    print("Exclusão cancelada.")

            self.lista_pacotes()
        except pymysql.err.IntegrityError:
            Notificacoes.erro_exclusao_pacote()

    def mostar_filtro_remessa(self):
        width = self.frame_filtro_remessa.width()

        if width == 9:
            new_width = 300
            self.frame_filtro_remessa.setMaximumWidth(new_width)
            self.frame_filtro_remessa.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
        else:
            new_width = 9
            self.frame_filtro_remessa.setMaximumWidth(new_width)
            self.frame_filtro_remessa.setStyleSheet("""
                QFrame{
                    border: 0px solid black;
                    border-radius: 2px;
                }
            """)

        self.animation = QtCore.QPropertyAnimation(self.frame_filtro_remessa, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mostrar_alterar_remessa(self):
        width = self.frame_alteracoes_remessa.width()
        select_model = self.tableWidget_lista_remessa.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_remessa.currentRow()
        elif self.linha_selecionada == -1:
            Notificacoes.selecione_linha("ALTERAR", "modificar uma remessa")

        if width == 9 and self.linha_selecionada != -1:
            new_width = 300
            self.frame_alteracoes_remessa.setMaximumWidth(new_width)
            self.frame_alteracoes_remessa.setStyleSheet("""
                QFrame{
                    border: 1px solid black;
                    border-radius: 2px;
                }
            """)
            self.label_id_remessa_alterar_num.setText(
                self.tableWidget_lista_remessa.item(self.linha_selecionada, 0).text())
            self.lineEdit_id_pacote_1_alterar.setText(
                self.tableWidget_lista_remessa.item(self.linha_selecionada, 1).text())
            self.lineEdit_id_pacote_2_alterar.setText(
                self.tableWidget_lista_remessa.item(self.linha_selecionada, 2).text())

        else:
            new_width = 9
            self.frame_alteracoes_remessa.setMaximumWidth(new_width)
            self.frame_alteracoes_remessa.setStyleSheet("""
                 QFrame{
                     border: 0px solid black;
                     border-radius: 2px;
                 }
            """)
            self.linha_selecionada = -1
            self.tableWidget_lista_remessa.clearSelection()

        self.animation = QtCore.QPropertyAnimation(self.frame_alteracoes_remessa, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def filtro_remessa(self):
        num_filtro = self.comboBox_filtro_remessa.currentIndex()
        pesquisa = self.lineEdit_filtro_remessa.text()
        remessas = self.model.filtro_remessa(num_filtro, pesquisa)
        self.tableWidget_lista_remessa.clearContents()
        self.tableWidget_lista_remessa.setRowCount(len(remessas))

        for row, text in enumerate(remessas):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_remessa = QTableWidgetItem(str(text['ID_Remessa']))
            item_id_remessa.setFlags(item_id_remessa.flags() & ~Qt.ItemIsEditable)
            item_id_pacote_1 = QTableWidgetItem(str(text['ID_Pacote_1']))
            item_id_pacote_1.setFlags(item_id_pacote_1.flags() & ~Qt.ItemIsEditable)
            item_id_pacote_2 = QTableWidgetItem(str(text['ID_Pacote_2']))
            item_id_pacote_2.setFlags(item_id_pacote_2.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_remessa.setItem(row, 0, item_id_remessa)
            self.tableWidget_lista_remessa.setItem(row, 1, item_id_pacote_1)
            self.tableWidget_lista_remessa.setItem(row, 2, item_id_pacote_2)

    def lista_remessa(self):
        self.lineEdit_filtro_remessa.clear()
        remessas = self.model.lista_remessa()
        self.tableWidget_lista_remessa.clearContents()
        self.tableWidget_lista_remessa.setRowCount(len(remessas))

        for row, text in enumerate(remessas):
            # Cria itens para cada célula e remove a capacidade de edição
            item_id_remessa = QTableWidgetItem(str(text['ID_Remessa']))
            item_id_remessa.setFlags(item_id_remessa.flags() & ~Qt.ItemIsEditable)
            item_id_pacote_1 = QTableWidgetItem(str(text['ID_Pacote_1']))
            item_id_pacote_1.setFlags(item_id_pacote_1.flags() & ~Qt.ItemIsEditable)
            item_id_pacote_2 = QTableWidgetItem(str(text['ID_Pacote_2']))
            item_id_pacote_2.setFlags(item_id_pacote_2.flags() & ~Qt.ItemIsEditable)

            # Adiciona os itens à tabela
            self.tableWidget_lista_remessa.setItem(row, 0, item_id_remessa)
            self.tableWidget_lista_remessa.setItem(row, 1, item_id_pacote_1)
            self.tableWidget_lista_remessa.setItem(row, 2, item_id_pacote_2)

    def botao_atualizar_remessa(self):
        try:
            id_remessa = self.label_id_remessa_alterar_num.text()
            id_pacote_1 = self.lineEdit_id_pacote_1_alterar.text()
            id_pacote_2 = self.lineEdit_id_pacote_2_alterar.text()
            self.model.atualizar_remessa(id_remessa, id_pacote_1, id_pacote_2)
            self.label_id_remessa_alterar_num.clear()
            self.lineEdit_id_pacote_1_alterar.clear()
            self.lineEdit_id_pacote_2_alterar.clear()
            self.lista_remessa()
            self.mostrar_alterar_remessa()
            Notificacoes.atualizacao_concluida()
        except pymysql.err.IntegrityError:
            Notificacoes.erro_cadastrar_remessa()

    def excluir_remessa(self):
        select_model = self.tableWidget_lista_remessa.selectionModel().hasSelection()

        if select_model is True:
            self.linha_selecionada = self.tableWidget_lista_remessa.currentRow()
        else:
            Notificacoes.selecione_linha("EXCLUIR", "excluir uma remessa")
            return

        if self.linha_selecionada != -1:
            id_remessa = self.tableWidget_lista_remessa.item(self.linha_selecionada, 0).text()
            btn = Notificacoes.confirmar_exclusao(id_remessa)

            if btn != 0:
                self.model.excluir_remessa(btn)
                Notificacoes.exclusao_concluida()
            else:
                print("Exclusão cancelada.")

        self.lista_remessa()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginController(root)
    root.mainloop()
