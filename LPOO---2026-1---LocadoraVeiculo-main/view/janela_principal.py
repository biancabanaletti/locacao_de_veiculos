import tkinter as tk

from view.locacao_usuario_view import JanelaLocacaoUsuario
from view.veiculo_list_view import JanelaListagemVeiculos

class JanelaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Locadora de Veículos")
        self.geometry("900x600")

        titulo = tk.Label(
            self,
            text="SISTEMA DE LOCADORA DE VEÍCULOS",
            font=("Arial", 22, "bold")
        )

        titulo.pack(pady=30)

        subtitulo = tk.Label(
            self,
            text="Locadora - LPOO",
            font=("Arial", 14)
        )

        subtitulo.pack(pady=10)

        descricao = tk.Label(
            self,
            text=(
                "Implementação:\n\n"
                "- Python\n"
                "- Tkinter\n"
                "- PostgreSQL\n"
                "- MVC + DAO\n"
                "- Linguagem de Programação Orientada a Objetos"
            ),
            font=("Arial", 12),
            justify="left"
        )

        descricao.pack(pady=20)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=40)

        tk.Button(
            btn_frame,
            text="Abrir Veículos",
            width=20,
            height=2,
            command=self.abrir_veiculos
        ).pack(side="left", padx=15)

        tk.Button(
            btn_frame,
            text="Locar Veículo",
            width=20,
            height=2,
            command=self.abrir_locar_usuario
        ).pack(side="left", padx=15)

    def abrir_veiculos(self):
        JanelaListagemVeiculos(self)

    def abrir_locar_usuario(self):
        JanelaLocacaoUsuario(self)