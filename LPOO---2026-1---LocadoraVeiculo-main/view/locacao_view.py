import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from control.veiculo_controller import VeiculoController

class LocacaoView(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Locação de Veículos")
        self.geometry("800x400")

        self.controller = VeiculoController()

        self.criar_widgets()
        self.carregar_veiculos_disponiveis()

    def criar_widgets(self):

        tk.Label(self, text="Data Início:").grid(row=0, column=0)
        self.data_inicio = tk.Entry(self)
        self.data_inicio.grid(row=0, column=1)

        tk.Label(self, text="Data Final:").grid(row=1, column=0)
        self.data_fim = tk.Entry(self)
        self.data_fim.grid(row=1, column=1)

        tk.Label(self, text="Classe").grid(row=2, column=0)
        self.combo_classe = ttk.Combobox(self, values=["Econômico", "Sedan", "SUV"])
        self.combo_classe.grid(row=2, column=1)

        tk.Label(self, text="Estratégia").grid(row=3, column=0)
        self.combo_estrategia = ttk.Combobox(self, values=["Padrão", "Promocional"])
        self.combo_estrategia.grid(row=3, column=1)

        tk.Button(self, text="Buscar Veículos", command=self.buscar_veiculos).grid(
            row=4, column=0, columnspan=2
        )

        self.lista = tk.Listbox(self, width=50)
        self.lista.grid(row=5, column=0, columnspan=2)

        tk.Button(self, text="Locar Veículo", command=self.locar_veiculo).grid(
            row=6, column=0, columnspan=2
        )

    def carregar_veiculos_disponiveis(self):
        self.lista.delete(0, tk.END)

        veiculos = self.controller.listar_disponiveis()

        for v in veiculos:
            self.lista.insert(tk.END, f"{v.id} - {v.modelo} ({v.classe})")

    def buscar_veiculos(self):
        classe = self.combo_classe.get()

        self.lista.delete(0, tk.END)

        veiculos = self.controller.listar_disponiveis(classe)

        for v in veiculos:
            self.lista.insert(tk.END, f"{v.id} - {v.modelo}")

    def locar_veiculo(self):
        selecionado = self.lista.get(tk.ACTIVE)

        if not selecionado:
            messagebox.showerror("Erro", "Selecione um veículo")
            return

        try:
            data_inicio = datetime.strptime(self.data_inicio.get(), "%d/%m/%Y")
            data_fim = datetime.strptime(self.data_fim.get(), "%d/%m/%Y")
        except:
            messagebox.showerror("Erro", "Datas inválidas")
            return

        if data_fim <= data_inicio:
            messagebox.showerror("Erro", "Data fim deve ser maior")
            return

        self.controller.locar_veiculo(selecionado)

        messagebox.showinfo("Sucesso", f"Veículo locado: {selecionado}")

        self.carregar_veiculos_disponiveis()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  #esconde janela principal
    app = LocacaoView(root)
    app.mainloop()