from datetime import date
from .LocacaoStrategy import CalculoPadraoStrategy

class Locacao:

    def __init__(self, id, veiculo_id, data_inicio, data_fim, status, valor_total):

        self.id = id
        self.veiculo_id = veiculo_id

        self.data_inicio = data_inicio
        self.data_fim = data_fim

        self.status = status
        self.valor_total = valor_total

        self.modelo_veiculo = None

        self.estrategia = CalculoPadraoStrategy()

    def calcular_valor_locacao(self) -> float:

        if self.data_fim is None:
            self.data_fim = date.today()

        dias = (self.data_fim - self.data_inicio).days

        if dias <= 0:
            dias = 1

        class VeiculoFake:
            taxa_diaria = 100
            valor_seguro = 20

        veiculo = VeiculoFake()

        return float(self.estrategia.calcular_diarias(veiculo, dias))