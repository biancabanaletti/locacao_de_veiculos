from model.locacao import Locacao
from model.veiculo import VeiculoFactory

class LocacaoDAO:

    def __init__(self, conexao):
        self.conn = conexao

    def inserir(self, locacao):
#inserir locacao
        sql = """
            INSERT INTO tb_locacoes
            (veiculo_id, data_inicio, data_fim, status, valor_total)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """

        cur = self.conn.cursor()

        cur.execute(sql, (
            locacao.veiculo_id,
            locacao.data_inicio,
            locacao.data_fim,
            locacao.status,
            locacao.valor_total
        ))

        locacao.id = cur.fetchone()[0]

        self.conn.commit()
        cur.close()

#att
    def update_status_e_datas(self, locacao):

        sql = """
            UPDATE tb_locacoes
            SET status = %s,
                data_inicio = %s,
                data_fim = %s,
                valor_total = %s
            WHERE id = %s
        """

        cur = self.conn.cursor()

        cur.execute(sql, (
            locacao.status,
            locacao.data_inicio,
            locacao.data_fim,
            locacao.valor_total,
            locacao.id
        ))

        self.conn.commit()
        cur.close()

    def listar_todos(self):

        sql = """
            SELECT
                l.id,
                v.placa,
                v.tipo,
                l.data_inicio,
                l.data_fim,
                l.status,
                l.valor_total
            FROM tb_locacoes l
            JOIN tb_veiculos v
                ON l.veiculo_id = v.placa
        """

        cur = self.conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()

        locacoes = []

        for row in rows:

            loc = Locacao(
                row[0],
                row[1],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            loc.modelo_veiculo = row[2]

            locacoes.append(loc)

        cur.close()

        return locacoes