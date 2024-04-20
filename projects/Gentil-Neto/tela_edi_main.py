import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

#criando classe
class Aplicacao:
    #metodo construtor da classe
    def __init__(self, master):
        
        self.master = master
        self.master.title("Configurador EDI - NOVPN")
        self.master.geometry("600x400")
        #icone e imagem de fundo
        self.master.iconbitmap('axway_logo.ico')
        self.caminho_imagem = "fundo.png"
        self.imagem_fundo = Image.open(self.caminho_imagem)
        self.imagem_fundo = self.imagem_fundo.resize((600, 400), Image.Resampling.LANCZOS)
        self.foto_fundo = ImageTk.PhotoImage(self.imagem_fundo)

        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        self.tela_inicial = tk.Frame(self.master)
        self.tela_inicial.pack(fill="both", expand=True)

        label_fundo = tk.Label(self.tela_inicial, image=self.foto_fundo)
        label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

        ttk.Button(label_fundo, text="AXWAY", command=self.executar_axway).place(x=370, y=20)
        ttk.Button(label_fundo, text="B2Bi", command=self.executar_b2bi).place(x=480, y=20)
        
        # Campos e botão para login
        ttk.Label(label_fundo, text="Login:").place(x=380, y=80)
        self.usuario_entry = ttk.Entry(label_fundo)
        self.usuario_entry.place(x=430, y=80)

        ttk.Label(label_fundo, text="Senha:").place(x=380, y=120)
        self.senha_entry = ttk.Entry(label_fundo, show="*")
        self.senha_entry.place(x=430, y=120)
        
        ttk.Button(label_fundo, text="Sair", command=self.master.quit).place(x=40, y=100)

        #ttk.Button(label_fundo, text="Entrar", command=self.executar_login).place(x=100, y=220)

    # def executar_login(self):
    #     usuario = self.usuario_entry.get()
    #     senha = self.senha_entry.get()
    #     print(f"Login: {usuario}, Senha: {senha}")

    def executar_b2bi(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        try:
            subprocess.run(["python", "config_edi_B2Bi_novpn.py", usuario, senha], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar b2bi.py: {e}")

    def executar_axway(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        try:
            subprocess.run(["python", "config_edi_axway_novpn.py", usuario, senha], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar axway.py: {e}")

def main():
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()

if __name__ == "__main__":
    main()