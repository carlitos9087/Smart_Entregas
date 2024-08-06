import tkinter as tk
from tkinter import ttk


class UserView:
    def __init__(self, root, controller, user_info, packages):
        self.controller = controller
        self.root = root
        self.root.title("User Page")

        self.root.protocol("WM_DELETE_WINDOW", self.controller.on_closing)
        self.root.geometry("600x400")  # Define o tamanho da janela para ser consistente com a tela do login

        # Saudações
        self.label_greeting = tk.Label(root, text=f"Olá {user_info['Nome']}!", font=("Helvetica", 18, "bold"))
        self.label_greeting.grid(row=0, column=0, columnspan=4, pady=20)
        self.label_greeting.configure(anchor="center")

        # Informações do usuário
        info_frame = tk.Frame(root)
        info_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        tk.Label(info_frame, text="Nome:", font=("Helvetica", 12)).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.label_name = tk.Label(info_frame, text=user_info['Nome'], font=("Helvetica", 12))
        self.label_name.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(info_frame, text="Endereço:", font=("Helvetica", 12)).grid(row=1, column=0, sticky=tk.W, padx=5,
                                                                            pady=5)
        self.label_address = tk.Label(info_frame, text=user_info['Endereco'], font=("Helvetica", 12))
        self.label_address.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)


        # Informações do Pacote
        package_info_frame = tk.Frame(root, bg="lightblue", bd=2, relief=tk.SUNKEN)
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
        self.label_table = tk.Label(root, text="Pacotes - Tabela", font=("Helvetica", 18, "bold"))
        self.label_table.grid(row=5, column=0, columnspan=4, pady=20)
        self.label_table.configure(anchor="center")

        self.table = ttk.Treeview(root, columns=("ID_Pacote", "Volume", "Peso", "Descricao"), show="headings")
        self.table.heading("ID_Pacote", text="ID_Pacote")
        self.table.heading("Volume", text="Volume")
        self.table.heading("Peso", text="Peso")
        self.table.heading("Descricao", text="Descricao")

        for package in packages:
            self.table.insert("", tk.END,
                              values=(package['ID_Pacote'], package['Volume'], package['Peso'], package['Descricao']))

        self.table.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        # Botão de logout
        self.logout_button = tk.Button(root, text="Logout", command=self.controller.logout, bg="grey", fg="white",
                                       width=10)
        self.logout_button.grid(row=7, column=0, columnspan=4, pady=10)
