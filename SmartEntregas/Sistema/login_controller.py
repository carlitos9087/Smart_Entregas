import sys
import tkinter as tk
from tkinter import messagebox
from PySide6.QtWidgets import QApplication
from model import Model
from user_controller import UserController
from admin_controller import MainWindow

# HYPE

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
        admin_info = self.model.validate_admin(name, password)
        if admin_info:
            messagebox.showinfo("Login Sucesso", "Bem-vindo, Admin!")
            id_admin = admin_info['ID_Admin']
            self.open_admin_view(name, id_admin)
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

    def open_admin_view(self, name, id_admin):
        self.root.withdraw()
        app = QApplication(sys.argv)
        main_window = MainWindow(id_admin)
        main_window.setWindowTitle(f'Bem-vindo, {name}!')
        main_window.show()
        sys.exit(app.exec())

    def open_user_view(self, name):
        self.root.withdraw()
        user_window = tk.Toplevel(self.root)
        UserController(user_window, name)



if __name__ == "__main__":
    root = tk.Tk()
    app = LoginController(root)
    root.mainloop()