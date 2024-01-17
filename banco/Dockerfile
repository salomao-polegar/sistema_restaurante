# Derivando da imagem oficial do MySQL
FROM mysql:8.0.35-debian

# Adicionando um database
ENV MYSQL_DATABASE TechChallenge


# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./database/ /docker-entrypoint-initdb.d/