import tkinter as tk
from tkinter import ttk


class UserView:
    def __init__(self, root, controller, user_info, packages):
        self.controller = controller
        self.root = root
        self.root.title("User Page")
        self.user_info = user_info

        self.root.protocol("WM_DELETE_WINDOW", self.controller.on_closing)
        self.root.geometry("820x800")  # Define o tamanho da janela para ser consistente com a tela do login

        # Container onde os frames serão empilhados
        self.container = tk.Frame(root)
        self.container.grid(row=0, column=0, sticky="nsew")

        # Frame para parte do informações usuário e pacotes
        self.home_frame = tk.Frame(self.container)
        self.home_frame.grid(row=0, column=0, sticky="nsew")
        self.conta_frame = tk.Frame(self.container)
        self.conta_frame.grid(row=1, column=0, sticky="nsew")
        self.mapa_frame = tk.Frame(self.container)
        self.mapa_frame.grid(row=2, column=0, sticky="nsew")

        # Saudações
        self.label_greeting = tk.Label(self.home_frame, text=f"Olá {self.user_info['Nome']}!",
                                       font=("Helvetica", 18, "bold"))
        self.label_greeting.grid(row=0, column=0, columnspan=4, pady=20)
        self.label_greeting.configure(anchor="center")

        # Informações do usuário
        info_frame = tk.Frame(self.home_frame)
        info_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        tk.Label(info_frame, text="Nome:", font=("Helvetica", 12)).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.label_name = tk.Label(info_frame, text=self.user_info['Nome'], font=("Helvetica", 12))
        self.label_name.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(info_frame, text="Endereço:", font=("Helvetica", 12)).grid(row=1, column=0, sticky=tk.W, padx=5,
                                                                            pady=5)
        self.label_address = tk.Label(info_frame, text=self.user_info['Endereco'], font=("Helvetica", 12))
        self.label_address.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(info_frame, text="Telefone:", font=("Helvetica", 12)).grid(row=2, column=0, sticky=tk.W, padx=5,
                                                                            pady=5)
        self.label_phone = tk.Label(info_frame, text=self.user_info['Telefone'], font=("Helvetica", 12))
        self.label_phone.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Informações do Pacote
        package_info_frame = tk.Frame(self.home_frame, bg="lightblue", bd=2, relief=tk.SUNKEN)
        package_info_frame.grid(row=1, column=3, rowspan=3, padx=20, pady=10, sticky="nsew")

        tk.Label(package_info_frame, text="Informações do Pacote", font=("Helvetica", 12, "bold"), bg="lightblue").grid(
            row=0, column=0, columnspan=2, pady=10)

        tk.Label(package_info_frame, text="ID Pacote:", font=("Helvetica", 12), bg="lightblue").grid(row=1, column=0,
                                                                                                     sticky=tk.W,
                                                                                                     padx=5, pady=5)
        self.label_package_id = tk.Label(package_info_frame, text="", font=("Helvetica", 12), bg="lightblue")
        self.label_package_id.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(package_info_frame, text="Descrição:", font=("Helvetica", 12), bg="lightblue").grid(row=2, column=0,
                                                                                                     sticky=tk.W,
                                                                                                     padx=5, pady=5)
        self.label_package_description = tk.Label(package_info_frame, text="", font=("Helvetica", 12), bg="lightblue")
        self.label_package_description.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Atualiza as informações do pacote
        if packages:
            self.label_package_id.config(text=packages[0]['ID_Pacote'])
            self.label_package_description.config(text=packages[0]['Descricao'])
        else:
            self.label_package_id.config(text="Nenhuma Entrega")
            self.label_package_description.config(text="Nenhuma Entrega Detectada.")

        # Tabela de pacotes
        self.label_table = tk.Label(self.home_frame, text="Pacotes - Tabela", font=("Helvetica", 18, "bold"))
        self.label_table.grid(row=5, column=0, columnspan=4, pady=20)
        self.label_table.configure(anchor="center")

        self.table = ttk.Treeview(self.home_frame, columns=("ID_Pacote", "Volume", "Peso", "Descricao"),
                                  show="headings")
        self.table.heading("ID_Pacote", text="ID_Pacote")
        self.table.heading("Volume", text="Volume")
        self.table.heading("Peso", text="Peso")
        self.table.heading("Descricao", text="Descricao")

        for package in packages:
            self.table.insert("", tk.END,
                              values=(package['ID_Pacote'], package['Volume'], package['Peso'], package['Descricao']))

        self.table.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        # Frame para botões
        button_frame = tk.Frame(self.home_frame)
        button_frame.grid(row=7, column=2, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Botão mapa
        self.botao_mapa = tk.Button(button_frame, text="Mapa",
                                           command=lambda: self.controller.show_frame("mapa_frame"),
                                           font=("Helvetica", 10), bg="grey", fg="white", width=10)
        self.botao_mapa.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

        # Botão configurar conta
        self.configurar_button = tk.Button(button_frame, text="Configurar conta",
                                           command=lambda: self.controller.show_frame("conta_frame"),
                                           font=("Helvetica", 10), bg="grey", fg="white", width=15)
        self.configurar_button.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

        # Botão de logout
        self.logout_button = tk.Button(button_frame, text="Logout", command=self.controller.logout,
                                       font=("Helvetica", 10),
                                       bg="grey", fg="white", width=10)
        self.logout_button.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

    # Página de configurar conta
    def conta(self):

        # Botão Página Inicial
        self.botao_pag_inicial = tk.Button(self.conta_frame, text="Página inicial",
                                           command=lambda: self.controller.show_frame(
                                               "home_frame"), font=("Helvetica", 10), bg="grey", fg="white",
                                           width=10)
        self.botao_pag_inicial.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

        # Título
        titulo = tk.Label(self.conta_frame, text=f"Minha conta", font=("Helvetica", 18, "bold"))
        titulo.grid(row=1, column=0, columnspan=4, pady=20, sticky="nsew")
        titulo.configure(anchor="center")

        # Nome
        tk.Label(self.conta_frame, text="Nome:", font=("Helvetica", 12)).grid(row=2, column=0, sticky=tk.W, padx=5,
                                                                              pady=5)
        self.entry_name = tk.Entry(self.conta_frame, font=("Helvetica", 12), width=30)
        self.entry_name.grid(row=2, column=1, padx=5, pady=5)
        self.entry_name.insert(0, self.user_info['Nome'])
        self.entry_name.config(state="readonly")

        # Endereco
        tk.Label(self.conta_frame, text="Endereço:", font=("Helvetica", 12)).grid(row=3, column=0, sticky=tk.W,
                                                                                  padx=5,
                                                                                  pady=5)
        self.entry_adress = tk.Entry(self.conta_frame, font=("Helvetica", 12), width=30)
        self.entry_adress.grid(row=3, column=1, padx=5, pady=5)
        self.entry_adress.insert(0, self.user_info['Endereco'])
        self.entry_adress.config(state="readonly")

        # Telefone
        tk.Label(self.conta_frame, text="Telefone:", font=("Helvetica", 12)).grid(row=4, column=0, sticky=tk.W,
                                                                                  padx=5,
                                                                                  pady=5)
        self.entry_phone = tk.Entry(self.conta_frame, font=("Helvetica", 12), width=30)
        self.entry_phone.grid(row=4, column=1, padx=5, pady=5)
        self.entry_phone.insert(0, self.user_info['Telefone'])
        self.entry_phone.config(state="readonly")

        # Botão editar
        self.botao_editar = tk.Button(self.conta_frame, text="Editar",
                                      command=lambda: self.controller.botao_editar_conta(),
                                      font=("Helvetica", 10), bg="grey", fg="white", width=10)
        self.botao_editar.grid(row=2, column=2, columnspan=1, padx=10, pady=10)

        # Botão alterar senha
        botao_alterar_senha = tk.Button(self.conta_frame, text="Alterar senha",
                                        command=lambda: self.controller.botao_alterar_senha(),
                                        font=("Helvetica", 10), bg="grey", fg="white", width=10)
        botao_alterar_senha.grid(row=3, column=2, columnspan=1, padx=10, pady=10)



    def botoes_salvar_cancelar(self):

        # Frame botões salvar e cancelar editar conta
        self.botao_frame = tk.Frame(self.conta_frame)
        self.botao_frame.grid(row=5, column=1, sticky="nsew")

        # Botao salvar
        self.botao_salvar = tk.Button(self.botao_frame, text="Salvar",
                                      command=lambda: self.controller.botao_salvar(),
                                      font=("Helvetica", 10), bg="grey", fg="white", width=10)
        self.botao_salvar.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

        # Botao cancelar
        self.botao_cancelar = tk.Button(self.botao_frame, text="Cancelar",
                                        command=lambda: self.controller.botao_cancelar(),
                                        font=("Helvetica", 10), bg="grey", fg="white", width=10)
        self.botao_cancelar.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

    # Página do mapa
    def mapa(self):
        label2 = tk.Label(self.mapa_frame, text=f"frame mapa", font=("Helvetica", 18, "bold"))
        label2.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
        botao2 = tk.Button(self.mapa_frame, text="Home", command=lambda: self.controller.show_frame("home_frame"))
        botao2.grid(row=1, column=0, columnspan=1, padx=10, pady=10)