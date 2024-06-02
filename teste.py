import sqlalchemy as sql

# Conectar ao banco de dados PostgreSQL
engine = sql.create_engine('postgresql://postgres:123@127.0.0.1:5432/smart_entregas_db')
# engine2 = sql.create_engine('postgresql://postgres:123@127.0.0.1:5432/smart_entregas_db')

# Criar uma tabela de exemplo chamada "teste2"
with engine.connect() as connection:

    create_table_sql = sql.text('CREATE TABLE matheus (id SERIAL PRIMARY KEY, nome VARCHAR(255), idade INTEGER)')

    connection.execute(create_table_sql)

print("Tabela 'teste2' criada com sucesso.")
