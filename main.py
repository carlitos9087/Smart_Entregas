import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
import sqlalchemy as sql

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inserir Dados no Banco de Dados")

        # Configura o widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Cria um layout vertical
        layout = QVBoxLayout(central_widget)

        # Cria campos de entrada para os dados
        self.nome_edit = QLineEdit()
        self.idade_edit = QLineEdit()

        # Cria botão para enviar os dados
        self.button = QPushButton("Inserir Dados")
        self.button.clicked.connect(self.on_button_clicked)

        # Cria um rótulo para exibir mensagens
        self.label = QLabel()

        # Adiciona os campos de entrada, botão e rótulo ao layout
        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.nome_edit)
        layout.addWidget(QLabel("Idade:"))
        layout.addWidget(self.idade_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        # Conectar ao banco de dados PostgreSQL
        self.engine = sql.create_engine('postgresql://postgres:123@127.0.0.1:5432/smart_entregas_db')

    def on_button_clicked(self):
        # Obter os dados dos campos de entrada
        nome = self.nome_edit.text()
        idade = self.idade_edit.text()

        # Verificar se os campos de entrada estão vazios
        if not nome or not idade:
            self.label.setText("Por favor, preencha todos os campos.")
            return

        # Inserir dados no banco de dados
        try:
            with self.engine.connect() as connection:
                insert_sql = sql.text('INSERT INTO teste (nome, idade) VALUES (:nome, :idade)')
                connection.execute(insert_sql, {"nome": nome, "idade": idade})
            self.label.setText("Dados inseridos com sucesso.")
        except Exception as e:
            self.label.setText(f"Erro ao inserir dados: {str(e)}")

# Cria a aplicação Qt
app = QApplication(sys.argv)

# Cria a janela principal
window = MainWindow()
window.show()

# Executa a aplicação
sys.exit(app.exec())
