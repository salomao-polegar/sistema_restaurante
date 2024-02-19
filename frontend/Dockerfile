# Derivando da imagem oficial do Node
FROM node:alpine

# Definir o workdir
WORKDIR /code

# Copiar a pasta do projeto
COPY ./ /code/

# Instalar dependências do projeto
RUN npm i

# Comando para subir o app
CMD ["npm", "start"]