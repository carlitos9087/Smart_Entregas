# Use a imagem oficial do PostgreSQL
FROM postgres:latest

# Defina a variável de ambiente POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD=123

# Exponha a porta 5432 para acessar o PostgreSQL
EXPOSE 5432

# Defina o nome do contêiner como "smart_entregas"
# Isso é opcional, mas útil para referência futura
# e para garantir que você possa iniciar o contêiner com o mesmo nome
# usando "docker start smart_entregas"
CMD ["--name", "smart_entregas"]

# Criar um banco de dados chamado "smart_entregas_db" na inicialização do contêiner
RUN echo "CREATE DATABASE smart_entregas_db;" >> /docker-entrypoint-initdb.d/init.sql
