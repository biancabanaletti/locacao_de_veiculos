from dao.locacao_dao import LocacaoDAO
from dao.db_config import DatabaseConfig
from datetime import date

class LocacaoController:
    def __init__(self):
        conexao = DatabaseConfig.get_connection()

        if conexao is None:
            raise Exception("Erro ao conectar ao banco!")

        self.dao = LocacaoDAO(conexao)

    def locar(self, loc_id):
        locacao = self.dao.buscar_por_id(loc_id)

        locacao.status = "locado"
        locacao.data_inicio = date.today()

        self.dao.update_status_e_datas(locacao)

    def devolver(self, loc_id):
        locacao = self.dao.buscar_por_id(loc_id)

        locacao.status = "devolvido"
        locacao.data_fim = date.today()

        valor = locacao.calcular_valor_locacao()

        locacao.valor_total = valor

        self.dao.update_status_e_datas(locacao)

        return valor

    def cancelar(self, loc_id):
        locacao = self.dao.buscar_por_id(loc_id)

        locacao.status = "cancelado"

        self.dao.update_status_e_datas(locacao)