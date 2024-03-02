# Imagem oficial do Python 3.12.1
FROM python:3.12.1

# Definindo o WORKDIR
WORKDIR /code

# Copiar requirements
COPY ./requirements.txt /code/requirements.txt

# Instalando requerimentos do projeto
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiando pasta do projeto
COPY ./ /code/

# Subindo a API
CMD ["uvicorn", "external.api.main:app", "--host", "0.0.0.0", "--port", "80"]