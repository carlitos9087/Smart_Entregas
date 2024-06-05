import sqlalchemy as sql

# Conectar ao banco de dados PostgreSQL
engine = sql.create_engine('postgresql://postgres:123@127.0.0.1:5432/postgres')

# Criar uma tabela de exemplo chamada "teste2"
with engine.connect() as connection:
    # Definir o comando SQL para criar a tabela
    create_table_sql = sql.text('CREATE TABLE teste (id SERIAL PRIMARY KEY, nome VARCHAR(255), idade INTEGER)')
    # Executar o comando SQL
    connection.execute(create_table_sql)

print("Tabela 'teste' criada com sucesso.")
