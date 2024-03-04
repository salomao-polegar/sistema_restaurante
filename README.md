# Tech Challenge - Restaurante

## Contexto

Entrega da seguinte documentação no ReadMe
    
### a. Desenho da arquitetura pensado por você, pessoa arquiteta de software, contemplando: ###
- i.	Os requisitos do negócio (problema).
- ii.	Os requisitos de infraestrutura:
Você pode utilizar o MiniKube, Docker Kubernetes, AKS, EKS, GKE ou qualquer nuvem que você desenha. 
    
### b. Collection com todas as APIs desenvolvidas com exemplo de requisição (que não seja vazia): ###
- i.	Link do Swagger no projeto ou link para download da collection do Postman (JSON).
### c. Guia completo com todas as instruções para execução do projeto e a ordem de execução das APIs, caso seja necessário. ###
### d. Link para vídeo demonstrando a arquitetura desenvolvida na nuvem ou localmente ###
- i.	O vídeo deve ser postado no Youtube ou Vimeo.
- ii.	Não esqueça de deixá-lo público ou não listado.
 No arquivo entregue na plataforma, é necessário somente colocar a URL do Github com as informações.

O projeto é um back-end para gestão de pedidos através de totens automáticos de uma lanchonete, com todos os processos gerenciados através da API, que é capaz de gerenciar os clientes, produtos do cardápio e os pedidos realizados.

Os produtos são divididos entre Lanches, Acompanhamentos, Bebidas e Sobremesas. 
O cliente poderá acompanhar os status do pedido, sendo eles: Recebido, Em preparação, Pronto e Finalizado e o atendente/funcionário poderá atualizar estes status em tempo real.

<i>A documentação da API estará disponível ao rodar o projeto, conforme passos abaixo descritos.</i>

- Utilizamos arquitetura hexagonal para estruturar a API deste projeto, e o framework utilizado foi [FastAPI](https://fastapi.tiangolo.com/), em Python. 
- O banco de dados deste projeto é o MySQL.
- O projeto é executado em containers do Docker. Você precisa ter o Docker instalado na sua máquina para executar a API.

## Rodando o projeto

O projeto tem instruções para a criação de dois containers, orquestrados com o Docker Compose. 

### 1. Subir o docker-compose

Na pasta `root` do repositório:

```bash
docker-compose up
```
Ou, para rodar os containers em segundo plano:
```bash
docker-compose up -d
```

Para apagar os containers criados:
```bash
docker rm tc_api -f; docker rm tc_database -f; 
```

### 2. Acessar a documentação da API

A documentação da API contém uma lista de todos os endpoints do serviço. Para acessá-la, após a execução da etapa anterior, acesse a URL [http://127.0.0.1/redoc](http://127.0.0.1/redoc) .

## Testes

Para executar os testes unitários, com o container do banco de dados rodando, execute dentro da pasta api:
```bash
python -m pytest
```
<i>Para rodar os testes, é necessário ter o pacote pytest instalado. Se precisar, execute:
```bash
pip install pytest
```

</i>