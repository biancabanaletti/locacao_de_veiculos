import tkinter as tk
from tkinter import ttk

class JanelaNovaReserva(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Nova Reserva")
        self.geometry("400x500")
        self.criar_widgets()

    def criar_widgets(self):
        #campo Data Início
        tk.Label(self, text="Data Início (dd/mm/aaaa):").pack(pady=5)
        self.ent_inicio = tk.Entry(self)
        self.ent_inicio.pack() 

        #campo Data Fim
        tk.Label(self, text="Data Fim (dd/mm/aaaa):").pack(pady=5)
        self.ent_fim = tk.Entry(self)
        self.ent_fim.pack()

        #sel categoria
        tk.Label(self, text="Categoria:").pack(pady=5)
        self.combo_cat = ttk.Combobox(self, values=["ECONOMICO", "EXECUTIVO"])
        self.combo_cat.pack()

        #botão buscar
        tk.Button(self, text="Buscar Veículos", command=self.buscar).pack(pady=10)
        
        self.lista = tk.Listbox(self, width=50)
        self.lista.pack(pady=5)

        tk.Button(self, text="Confirmar Reserva", command=self.salvar).pack(pady=10)

    def buscar_disponiveis(self):
        #implementa
        veiculos = self.controller.dao.buscar_veiculos_disponiveis(
            self.ent_inicio.get(), self.ent_fim.get(), self.combo_cat.get()
        )
        self.lista.delete(0, tk.END)
        for v in veiculos:
            self.lista.insert(tk.END, f"{v[0]} - {v[1]}")