import sys
from PySide6.QtWidgets import QDialog, QLineEdit, QApplication
from model import Model
from notificacoes import Notificacoes
from senha_view import Ui_Dialog


class SenhaController:

    def __init__(self, id_usuario, tipo):
        app = QApplication.instance()
        if app is None:  # Se não houver uma instância, crie uma nova
            app = QApplication(sys.argv)
        self.dialog = QDialog()  # Cria a janela de diálogo
        self.dialog.setWindowTitle("Alterar senha")
        self.dialog_ui = Ui_Dialog()  # Cria uma instância de Ui_Dialog
        self.dialog_ui.setupUi(self.dialog)  # Configura a interface do diálogo

        # deixa a lineEdit no modo de exibição de senha ***
        self.dialog_ui.lineEdit_senha_atual.setEchoMode(QLineEdit.EchoMode.Password)
        self.dialog_ui.lineEdit_senha_atual.setPlaceholderText("Senha atual")
        self.dialog_ui.lineEdit_nova_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.dialog_ui.lineEdit_nova_senha.setPlaceholderText("Nova senha")
        self.dialog_ui.lineEdit_confirmar_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.dialog_ui.lineEdit_confirmar_senha.setPlaceholderText("Confirmar a senha")

        self.dialog_ui.lineEdit_nova_senha.textChanged.connect(self.comparar_senha)
        self.dialog_ui.lineEdit_confirmar_senha.textChanged.connect(self.comparar_senha)

        # botão salvar nova senha
        self.dialog_ui.botao_salvar_nova_senha.clicked.connect(lambda: self.salvar_senha_conta(id_usuario,tipo))

        # botão cancelar nova senha
        self.dialog_ui.botao_cancelar_alterar_senha.clicked.connect(self.cancelar_alterar_senha)

        # botão mostrar senha atual
        self.dialog_ui.botao_mostrar_senha_atual.clicked.connect(self.mostrar_senha_atual)

        # botão mostrar nova senha
        self.dialog_ui.botao_mostrar_nova_senha.clicked.connect(self.mostrar_nova_senha)

        # botão mostrar senha atual
        self.dialog_ui.botao_mostrar_confirmar_senha.clicked.connect(self.mostrar_confirmar_senha)

        self.dialog.exec_()  # Exibe o diálogo de forma modal

    def comparar_senha(self):
        nova_senha = self.dialog_ui.lineEdit_nova_senha.text()
        confirmar_senha = self.dialog_ui.lineEdit_confirmar_senha.text()
        estilo_igual = """
                QLineEdit{
                    border: 1px solid green;
                    border-radius: 2px;}
                QLabel{
                    color: green;
                    font: 10 pt "HeIvetica";}"""
        estilo_diferente = """
                QLineEdit{
                    border: 1px solid red;
                    border-radius: 2px;}
                 QLabel{
                    color: red;
                    font: 10 pt "HeIvetica";}"""

        if nova_senha == confirmar_senha:
            self.dialog_ui.lineEdit_nova_senha.setStyleSheet(estilo_igual)
            self.dialog_ui.lineEdit_confirmar_senha.setStyleSheet(estilo_igual)
            self.dialog_ui.label_correspondem.setStyleSheet(estilo_igual)
            self.dialog_ui.label_correspondem.setText("As senhas correspondem.")
            return "igual"
        else:
            self.dialog_ui.lineEdit_nova_senha.setStyleSheet(estilo_diferente)
            self.dialog_ui.lineEdit_confirmar_senha.setStyleSheet(estilo_diferente)
            self.dialog_ui.label_correspondem.setStyleSheet(estilo_diferente)
            self.dialog_ui.label_correspondem.setText("As senhas não correspondem.")
            return "diferente"

    def cancelar_alterar_senha(self):
        self.dialog.close()

    def mostrar_senha_atual(self):
        texto_botao = self.dialog_ui.botao_mostrar_senha_atual.text()
        if texto_botao == 'Mostrar':
            self.dialog_ui.lineEdit_senha_atual.setEchoMode(QLineEdit.EchoMode.Normal)
            self.dialog_ui.botao_mostrar_senha_atual.setText('Ocultar')
        else:
            self.dialog_ui.lineEdit_senha_atual.setEchoMode(QLineEdit.EchoMode.Password)
            self.dialog_ui.botao_mostrar_senha_atual.setText('Mostrar')

    def mostrar_nova_senha(self):
        texto_botao = self.dialog_ui.botao_mostrar_nova_senha.text()
        if texto_botao == 'Mostrar':
            self.dialog_ui.lineEdit_nova_senha.setEchoMode(QLineEdit.EchoMode.Normal)
            self.dialog_ui.botao_mostrar_nova_senha.setText('Ocultar')
        else:
            self.dialog_ui.lineEdit_nova_senha.setEchoMode(QLineEdit.EchoMode.Password)
            self.dialog_ui.botao_mostrar_nova_senha.setText('Mostrar')

    def mostrar_confirmar_senha(self):
        texto_botao = self.dialog_ui.botao_mostrar_confirmar_senha.text()
        if texto_botao == 'Mostrar':
            self.dialog_ui.lineEdit_confirmar_senha.setEchoMode(QLineEdit.EchoMode.Normal)
            self.dialog_ui.botao_mostrar_confirmar_senha.setText('Ocultar')
        else:
            self.dialog_ui.lineEdit_confirmar_senha.setEchoMode(QLineEdit.EchoMode.Password)
            self.dialog_ui.botao_mostrar_confirmar_senha.setText('Mostrar')

    def salvar_senha_conta(self, id_usuario, tipo):
        model = Model()
        match tipo:
            case "morador":
                id_morador = id_usuario
                morador = model.conta_morador(id_morador)
                senha_atual = self.dialog_ui.lineEdit_senha_atual.text()
                nova_senha = self.dialog_ui.lineEdit_nova_senha.text()
                comparar_senha = self.comparar_senha()
                if senha_atual == morador['Senha'] and nova_senha.strip() != "" and comparar_senha == "igual":
                    model.alterar_senha_morador(id_morador, nova_senha)
                    self.dialog.close()
                    Notificacoes.senha_atualizada()
                elif senha_atual != morador['Senha']:
                    Notificacoes.erro_senha()
                elif comparar_senha == "diferente":
                    Notificacoes.senhas_diferentes()
                else:
                    Notificacoes.campos_vazios()
            case "admin":
                id_admin = id_usuario
                admin = model.conta_admin(id_admin)
                senha_atual = self.dialog_ui.lineEdit_senha_atual.text()
                nova_senha = self.dialog_ui.lineEdit_nova_senha.text()
                comparar_senha = self.comparar_senha()
                if senha_atual == admin['Senha'] and nova_senha.strip() != "" and comparar_senha == "igual":
                    model.alterar_senha_admin(id_admin, nova_senha)
                    self.dialog.close()
                    Notificacoes.senha_atualizada()
                elif senha_atual != admin['Senha']:
                    Notificacoes.erro_senha()
                elif comparar_senha == "diferente":
                    Notificacoes.senhas_diferentes()
                else:
                    Notificacoes.campos_vazios()
            case _:
                print("Erro atualizar senha")
