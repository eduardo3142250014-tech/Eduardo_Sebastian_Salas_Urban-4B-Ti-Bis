import tkinter as tk
from models.user_model import UserModel
from views.login_view import LoginView
from controller.auth_controller import Authentication


class System:
    def __init__(self):
        
        self.root = tk.Tk()

        
        modelo = UserModel()
        vista = LoginView(self.root)
        self.app = Authentication(modelo, vista)

    def start(self):
        
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.start()