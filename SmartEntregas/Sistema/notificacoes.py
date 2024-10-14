from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer


class Notificacoes:

    @staticmethod
    def confirmar_exclusao(id_item):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("EXCLUIR")
        msg_box.setText("Tem certeza que deseja excluir?")

        # Adicionando botões de resposta
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        btn = msg_box.exec_()

        if btn == QMessageBox.StandardButton.Yes:
            return id_item
        else:
            return 0

    @staticmethod
    def exclusao_concluida():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
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
        msg_box.setIcon(QMessageBox.Icon.Warning)
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
        msg_box.setIcon(QMessageBox.Icon.Information)
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
        msg_box.setIcon(QMessageBox.Icon.Information)
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
        msg_box.setIcon(QMessageBox.Icon.Information)
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
        msg_box.setIcon(QMessageBox.Icon.Warning)
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
        msg_box.setIcon(QMessageBox.Icon.Information)
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
        msg_box.setIcon(QMessageBox.Icon.Critical)
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
        msg_box.setIcon(QMessageBox.Icon.Warning)
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
        msg_box.setIcon(QMessageBox.Icon.Warning)
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
        msg_box.setIcon(QMessageBox.Icon.Warning)
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
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText(f"Pacote não existe.\nDigite um id válido.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def erro_excluir_morador():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText(f"Não é possível excluir um morador\nque possui pacotes cadastrados.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def escolha_receber_entrega():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("ENCOMENDA")

        botao_sim = msg_box.addButton("Sim", QMessageBox.ButtonRole.AcceptRole)
        msg_box.addButton("Não", QMessageBox.ButtonRole.RejectRole)

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Definindo o tempo inicial (em segundos)
        countdown = 5
        msg_box.setText(f"É possível receber sua encomenda neste momento?\nTempo restante: {countdown} segundos.")

        # Função para atualizar o texto da caixa de mensagem
        def atualizar_menssagem():
            nonlocal countdown
            if countdown > 0:
                msg_box.setText(f"É possível receber sua encomenda neste momento?"
                                f"\nTempo restante: {countdown} segundos.")
                countdown -= 1
            else:
                # Fecha a caixa de mensagem quando o tempo acaba
                msg_box.reject()
                timer.stop()

        # Configuração do QTimer para atualizar a cada segundo
        timer = QTimer()
        timer.timeout.connect(atualizar_menssagem)
        timer.start(1000)  # 1 segundo

        # Mostrar a caixa de mensagem
        msg_box.exec()

        # Parar o timer se o usuário interagir antes do tempo
        timer.stop()

        # Verificar o botão clicado
        clicked_button = msg_box.clickedButton()
        if clicked_button == botao_sim:
            return print('sim')
        else:
            return print('não')

    @staticmethod
    def entrega_recusada():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("RECUSADA")
        msg_box.setText("Entrega Recusada!")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def encomenda_recebida():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("ENCOMENDA")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Definindo o tempo inicial (em segundos)
        countdown = 5
        msg_box.setText(f"Clique em OK para confirmar que a encomenda foi recebida."
                        f"\nTempo restante: {countdown} segundos.")

        # Função para atualizar o texto da caixa de mensagem
        def atualizar_menssagem():
            nonlocal countdown
            if countdown > 0:
                msg_box.setText(f"Clique em OK para confirmar que a encomenda foi recebida."
                                f"\nTempo restante: {countdown} segundos.")
                countdown -= 1
            else:
                # Fecha a caixa de mensagem quando o tempo acaba
                msg_box.reject()
                timer.stop()

        # Configuração do QTimer para atualizar a cada segundo
        timer = QTimer()
        timer.timeout.connect(atualizar_menssagem)
        timer.start(1000)  # 1 segundo

        # Mostrar a caixa de mensagem
        btn = msg_box.exec()

        # Parar o timer se o usuário interagir antes do tempo
        timer.stop()

        # Verificar o botão clicado

        if btn == QMessageBox.StandardButton.Ok:
            print('clickou ok')
        else:
            Notificacoes.timer_expirado()

    @staticmethod
    def timer_expirado():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("TIMER EXPIRADO")
        msg_box.setText("Encomenda marcada automaticamente como entregue\napós o vencimento do prazo de confirmação")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def campos_vazios():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("CAMPO VAZIO")
        msg_box.setText("Informação necessária. Por favor, preencha os campos.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def conta_atualizada():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("ATUALIZADO")
        msg_box.setText("Conta atualizada.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def senha_atualizada():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("ATUALIZADO")
        msg_box.setText("Senha atualizada.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def erro_senha():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText("Senha atual inválida.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()

    @staticmethod
    def senhas_diferentes():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("ERRO")
        msg_box.setText("As senhas não correspondem.")

        # Configurando a fonte
        font = QFont("HeIvetica", 12)
        msg_box.setFont(font)

        # Exibindo a caixa de mensagem
        msg_box.exec_()