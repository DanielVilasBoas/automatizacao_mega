import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="resultado_mega"
)

# Criando um cursor
cursor = conexao.cursor()

# Definindo o comando SQL para criar a tabela
comando_sql = """
CREATE TABLE IF NOT EXISTS geral (
    Concurso INT PRIMARY KEY,
    Data_do_Sorteio DATE,
    Bola1 INT,
    Bola2 INT,
    Bola3 INT,
    Bola4 INT,
    Bola5 INT,
    Bola6 INT,
    Ganhadores_6_acertos INT,
    Cidade_UF VARCHAR(255),
    Rateio_6_acertos DECIMAL(12, 2),
    Ganhadores_5_acertos INT,
    Rateio_5_acertos DECIMAL(12, 2),
    Ganhadores_4_acertos INT,
    Rateio_4_acertos DECIMAL(12, 2),
    Acumulado_6_acertos DECIMAL(12, 2),
    Arrecadacao_Total DECIMAL(12, 2),
    Estimativa_premio DECIMAL(12, 2),
    Acumulado_Sorteio_Especial_Mega_da_Virada DECIMAL(12, 2),
    Observacao TEXT
)
"""

# Executando o comando SQL
cursor.execute(comando_sql)

# Commitando as alterações
conexao.commit()

# Fechando o cursor e a conexão
cursor.close()
conexao.close()

print("Tabela 'geral' criada com sucesso.")
