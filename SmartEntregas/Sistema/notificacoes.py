from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QFont


class Notificacoes:

    @staticmethod
    def confirmar_exclusao(id_item):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("EXCLUIR")
        msg_box.setText("Tem certeza que deseja excluir?")

        # Adicionando botões de resposta
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        btn = msg_box.exec_()

        if btn == QMessageBox.Yes:
            return id_item
        else:
            return 0

    @staticmethod
    def exclusao_concluida():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("EXCLUÍDO")
        msg_box.setText("Item excluído.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def erro_exclusao_pacote():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText("Não é possível excluir um pacote\n que pertence a uma remessa.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def atualizacao_concluida():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("ATUALIZADO")
        msg_box.setText("Item atualizado.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def remessa_cadastrada(id_remessa):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("CADASTRO")
        msg_box.setText(f"Remessa cadastrada com o id: {id_remessa}")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def entrega_concluida():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("CONCLUÍDA")
        msg_box.setText("Entrega Concluída!")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def encomenda_pendente():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("PENDENTE")
        msg_box.setText("Encomenda Pendente.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def encomenda_confirmada():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("CONFIRMADA")
        msg_box.setText("Encomenda Confirmada!")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def entrega_nao_realizada():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("NÃO REALIZADO")
        msg_box.setText("Entrega não realizada")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def problemas_rota():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("PROBLEMAS")
        msg_box.setText("Problemas na rota")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def morador_nao_existe():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText("Morador não existe. \nDigite um id válido.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def selecione_linha(botao, acao):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("SELECIONAR")
        msg_box.setText(f"Selecione uma linha e clique em {botao}\npara {acao}.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def erro_cadastrar_remessa():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText(f"Pacote não existe.\nDigite um id válido.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()
