import tkinter as tk


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Smart Entregas")
        self.root.protocol("WM_DELETE_WINDOW", self.controller.on_closing)

        self.root.geometry("600x400")  # Define o tamanho da janela para ser consistente com a tela do usuário

        # Frame principal
        main_frame = tk.Frame(root, padx=10, pady=10)
        main_frame.pack(expand=True, fill='both')

        # Título
        self.title_label = tk.Label(main_frame, text="Login", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=20)

        # Frame para campos de entrada
        input_frame = tk.Frame(main_frame)
        input_frame.pack(pady=10)

        # Campo de Nome
        self.label_name = tk.Label(input_frame, text="Nome:", font=("Helvetica", 12))
        self.label_name.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.entry_name = tk.Entry(input_frame, font=("Helvetica", 12), width=30)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Campo de Senha
        self.label_password = tk.Label(input_frame, text="Senha:", font=("Helvetica", 12))
        self.label_password.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.entry_password = tk.Entry(input_frame, font=("Helvetica", 12), show="*", width=30)
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        # Botões
        self.button_frame = tk.Frame(main_frame)
        self.button_frame.pack(pady=20)

        self.button_admin = tk.Button(self.button_frame, text="Login Funcionário", command=self.admin_login, bg="blue",
                                      fg="white", font=("Helvetica", 12), width=15)
        self.button_admin.grid(row=0, column=0, padx=5, pady=5)

        self.button_user = tk.Button(self.button_frame, text="Login Morador", command=self.user_login, bg="green",
                                     fg="white", font=("Helvetica", 12), width=15)
        self.button_user.grid(row=0, column=1, padx=5, pady=5)

        # Mensagem
        self.message_label = tk.Label(main_frame, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=10)

    def admin_login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        self.controller.login(name, password, is_admin=True)

    def user_login(self):
        name = self.entry_name.get()
        password = self.entry_password.get()
        self.controller.login(name, password, is_admin=False)

    def show_message(self, message):
        self.message_label.config(text=message)
