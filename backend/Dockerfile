# Imagem oficial do Python 3.12.1
FROM python:3.12.1

# Definindo o WORKDIR
WORKDIR /code

# Copiar a pasta do projeto
COPY ./ /code/

# Instalando requerimentos do projeto
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Subindo a API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]