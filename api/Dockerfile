# Derivando da imagem oficial do Python 3.12.1
FROM python:3.12.1

# Definir o workdir
WORKDIR /code

# Mover o arquivo de dependência do projeto para a pasta code
COPY ./requirements.txt /code/requirements.txt

# Instalar dependências do projeto
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar a pasta do projeto
COPY ./ /code/

# Comando para subir o app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]