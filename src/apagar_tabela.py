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

# Definindo o comando SQL para apagar a tabela
comando_sql = "DROP TABLE IF EXISTS geral"

# Executando o comando SQL
cursor.execute(comando_sql)

# Commitando as alterações
conexao.commit()

# Fechando o cursor e a conexão
cursor.close()
conexao.close()

print("Tabela 'geral' apagada com sucesso.")
