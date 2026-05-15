from dao.db_config import DatabaseConfig
from view.janela_principal import JanelaPrincipal

conn = DatabaseConfig.get_connection()

if conn:
    print("Conectou no banco!")
else:
    print("Erro ao conectar!")

app = JanelaPrincipal()
app.mainloop()