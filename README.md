# locacao_de_veiculos
Projeto de Locação de Veículos com implementação de interface gráfica e lógica de negócio para o CRUD de Locações. Contém Visão do Usuário e Visão do Administrador. 

Neste projeto foram utilizados os arquivos: locacao_controller.py, locacao_dao.py, janela_principal.py, locacao_usuario_view.py, locacao_view.py, reservado_view.py e locacaopostgres.sql. Além de outros arquivos semi-editados, como: veiculo_controller.py, veiculo_dao.py, locacao.py.

Entre as principais funcionalidades estão:

- Cadastro de veículos com informações como placa, categoria, tipo, taxa diária e estado atual.
- Listagem, atualização e remoção de veículos cadastrados.
- Criação de locações vinculando veículos a períodos de uso.
- Controle do status das locações (reservado, locado e devolvido/cancelado).
- Cálculo automático do valor da locação com base no período de uso.
- Interface gráfica para interação do usuário com o sistema.
- Integração com banco de dados PostgreSQL para persistência das informações.

Durante o desenvolvimento desta atividade, a principal dificuldade encontrada foi a integração entre as camadas do padrão MVC, especialmente na comunicação entre as Views, Controllers e PostgreSQL. Também houve dificuldades relacionadas à manipulação de janelas "TopLevel" atualização das tabelas ("TreeView") após operações de CRUD.

Para resolver os problemas, foram realizadas revisões das aulas, testes no sistema, ajustes na estrutura das telas e consultas SQL, além de uso de IA.

O principal aprendizado obtido foi compreender melhor:

- O funcionamento da arquitetura MVC;

- A persistência de dados com PostgreSQL;

- A utilização de DAO para separação das responsabilidades;

- O gerenciamento de interfaces gráficas com Tkinter.

- Declaração de uso de IA.

(X) Utilizei IA como ferramenta de apoio.
Ferramenta utilizada: ChatGPT (OpenAI)

- Finalidade:
A IA foi utilizada como apoio para correção de erros, organização da estrutura MVC, ajustes de integração entre telas Tkinter, consultas SQL e explicações sobre problemas encontrados durante o desenvolvimento.

Validação:
Declaro que todo o código gerado foi revisado, testado e compreendido antes de ser utilizado no projeto.


*** IMPLEMENTAÇÃO ***

Tela principal do Sistema de Locadora de Veículos:

<img width="899" height="628" alt="image" src="https://github.com/user-attachments/assets/0eccf8db-20f3-4f1b-a657-ee54974167f8" />

Tela de Veículos Cadastrados (dois exemplos):

<img width="798" height="430" alt="image" src="https://github.com/user-attachments/assets/b1a13dad-eb55-49e9-be2e-adb383359530" />

Tela de Locação:

<img width="800" height="430" alt="image" src="https://github.com/user-attachments/assets/a12fcc60-7755-4d84-a815-b2a99f4c2469" />

