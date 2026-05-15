import tkinter as tk
from tkinter import ttk, messagebox
from control.locacao_controller import LocacaoController

#tela gráfica (GUI) responsável por exibir e gerenciar locações do usuário
#utiliza Tkinter + padrão MVC (Controller + DAO + Model)

class JanelaLocacaoUsuario(tk.Toplevel):
    def __init__(self, master): #inicializa a janela, configura título e dimensões
                                #cria o controller responsável pela lógica de negócio
                                #carrega os dados iniciais do banco
        super().__init__(master)

        print("entrou na tela")

        self.title("Operações de Locação - Usuário")
        self.geometry("800x400")

        self.controller = LocacaoController()

        self.criar_widgets()
        self.carregar_dados()

    def criar_widgets(self): #método responsável por construir toda a interface gráfica:
                             #tabela (Treeview) + botões de ação
        print("criando widgets")

        titulo = tk.Label(
            self,
            text="Locações de Veículos",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=10)

        #tabela que exibe todas as locações do sistema
        #colunas representam atributos da entidade Locacao
        self.tree = ttk.Treeview(
            self,
            columns=("id", "veiculo", "status", "inicio", "fim"),
            show="headings"
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("veiculo", text="Veículo")
        self.tree.heading("status", text="Status")
        self.tree.heading("inicio", text="Data Início")
        self.tree.heading("fim", text="Data Fim")

        self.tree.column("id", width=50)
        self.tree.column("veiculo", width=180)
        self.tree.column("status", width=120)
        self.tree.column("inicio", width=150)
        self.tree.column("fim", width=150)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        #botões de ações principais do sistema:
        # - Nova Reserva
        # - Locar veículo
        # - Devolver veículo
        # - Cancelar reserva

        tk.Button(
            btn_frame,
            text="Nova Reserva",
            command=self.abrir_reserva
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame,
            text="Locar",
            command=self.executar_locar
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame,
            text="Devolver",
            command=self.executar_devolver
        ).pack(side="left", padx=5)

        tk.Button(
            btn_frame,
            text="Cancelar",
            command=self.executar_cancelar
        ).pack(side="left", padx=5)

    #atualiza a interface com dados do banco de dados
    #remove registros antigos da tabela e recarrega tudo
    #garantindo sincronização com o DAO

    def carregar_dados(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        locacoes = self.controller.dao.listar_todos()

        for loc in locacoes:
            self.tree.insert(
                "",
                "end",
                values=(
                    loc.id,
                    loc.modelo_veiculo,
                    loc.status,
                    loc.data_inicio,
                    loc.data_fim
                )
            )

    def abrir_reserva(self):
        messagebox.showinfo(
            "Reserva",
            "Tela de nova reserva ainda não implementada."
        )

    def executar_locar(self):
        selecionado = self.tree.selection()

        if not selecionado:
            messagebox.showwarning(
                "Aviso",
                "Selecione uma reserva!"
            )
            return

        item = self.tree.item(selecionado[0])

        loc_id = item['values'][0]
        status = item['values'][2]

        if status != "reservado":
            messagebox.showerror(
                "Erro",
                "Somente reservas podem ser locadas!"
            )
            return

        self.controller.locar(loc_id)

        messagebox.showinfo(
            "Sucesso",
            "Veículo retirado com sucesso!"
        )

        self.carregar_dados()

    def executar_devolver(self):
        selecionado = self.tree.selection()

        if not selecionado:
            messagebox.showwarning(
                "Aviso",
                "Selecione uma locação!"
            )
            return

        item = self.tree.item(selecionado[0])

        loc_id = item['values'][0]
        status = item['values'][2]

        if status != "locado":
            messagebox.showerror(
                "Erro",
                "Somente veículos locados podem ser devolvidos!"
            )
            return

        valor = self.controller.devolver(loc_id)

        messagebox.showinfo(
            "Devolução",
            f"Locação devolvida!\nValor Total: R$ {valor:.2f}"
        )

        self.carregar_dados()

    def executar_cancelar(self):
        selecionado = self.tree.selection()

        if not selecionado:
            messagebox.showwarning(
                "Aviso",
                "Selecione uma reserva!"
            )
            return

        item = self.tree.item(selecionado[0])

        loc_id = item['values'][0]
        status = item['values'][2]

        if status != "reservado":
            messagebox.showerror(
                "Erro",
                "Somente reservas podem ser canceladas!"
            )
            return

        self.controller.cancelar(loc_id)

        messagebox.showinfo(
            "Sucesso",
            "Reserva cancelada!"
        )

        self.carregar_dados()