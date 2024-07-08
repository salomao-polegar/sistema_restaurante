# Tech Challenge - Restaurante

## Contexto

    Sistema para gestão de pedidos de um restaurante, com todos os processos gerenciados através da API, que é capaz de gerenciar os clientes, produtos do cardápio e os pedidos realizados.

    Os produtos são divididos entre Lanches, Acompanhamentos, Bebidas e Sobremesas. 
    
    O cliente poderá acompanhar os status do pedido, sendo eles: Recebido, Em preparação, Pronto e Finalizado e o atendente/funcionário poderá atualizar estes status em tempo real.

<i>A documentação da API estará disponível ao rodar o projeto, conforme passos abaixo descritos.</i>

- Projeto desenvolvido com base na Arquitetura Limpa.
- Utilização do framework [FastAPI](https://fastapi.tiangolo.com/), em Python. 
- O banco de dados deste projeto é o MySQL.
- O projeto é executado em containers do Docker. Você precisa ter o Docker instalado na sua máquina para executar a API.

### Arquitetura

### Infraestrutura


## Rodando o projeto

O projeto tem instruções para a criação de dois containers, orquestrados com o Docker Compose. 

### Subir o docker-compose

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

## Acessar a documentação da API

A documentação da API contém uma lista de todos os endpoints do serviço. Para acessá-la, após a execução da etapa anterior, acesse a URL [http://127.0.0.1/docs](http://127.0.0.1/docs) ou [http://127.0.0.1/redoc](http://127.0.0.1/redoc).

## Instruções ###

Novos endpoints desaa fase:

- 1.	Checkout Pedido que deverá receber os produtos solicitados e retornar a identificação do pedido.

Requisição POST no seguinte endpoint:

```bash 
http://127.0.0.1/pedidos/checkout/
```

BODY da requisição:
```bash
{
    "id_cliente": 1,
    "itens": [
        {
            "item": 3,
            "quantidade": 5,
            "descricao": "sem tomate",
            "valor": 15.2,
            
        },
        {
            "item": 2,
            "quantidade": 3,
            "descricao": "com tomate",
            "valor": 11,
            
        }
    ]
}
```

- ii.	Consultar status pagamento pedido, que informa se o pagamento foi aprovado ou não.

Requisição GET no seguinte endpoint:

```bash 
http://127.0.0.1/pedidos/status_pagamento/{id_pedido}
```

Retorno da requisição:
```bash
"1" --> Pagamento Enviado
"2" --> Aprovado
"3" --> Recusado
```

- iii.	Webhook para receber confirmação de pagamento aprovado ou recusado.

Requisição POST no seguinte endpoint:

```bash 
http://127.0.0.1/pedidos/status_pagamento/
```

BODY da requisição:
```bash
{
    "id": "94da0f6e-8ab3-4caf-a7aa-51aecb340e15",
    "type": "payment",
    "date_created": "2015-03-25 10:04:58",
    "user_id": 44444,
    "api_version": "v1",
    "action": "state_CANCELED"
}
```

- iv. A lista de pedidos deverá retorná-los com suas descrições, ordenados com a seguinte regra:
        1. Pronto &gt; Em Preparação &gt; Recebido;
        2. Pedidos mais antigos primeiro e mais novos depois;
        3. Pedidos com status Finalizado não devem aparecer na lista.

Requisição GET no seguinte endpoint:

```bash 
http://127.0.0.1/pedidos/
```

- v.	Atualizar o status do pedido.

<i>Para alterar o status do pedido, usamos o PUT com o endpoint de pedido, enviando um objeto com o ID e os dados a serem editados (no caso, o status):</i>

```bash 
http://127.0.0.1/pedidos/
```

Body da requisição:
```bash
{
    "id": 2,
    "status_pedido": 4
}
```
Retorno ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR ARRUMAR :
```bash
{
    "id": 2,
    "status_pedido": 4,
    "cliente": 2
}
```
### Pagamento
Integração com Mercado Pago para gerar o QRCode para pagamento e integrar com o WebHook para capturar os pagamentos realizados. 

Como referência, acesse o <a href="https://www.mercadopago.com.br/developers/pt/docs/qr-code/integration-configuration/qr-dynamic/integration" rel="noopener" target="_blank">site do mercado pago</a>.

Ao realizar o checkout do pagamento, o sistema envia um pedido de pagamento ao sistema do MercadoPago, salvando no bando de dados o id do pagamento retornado pelo MercadoPago.

Para receber a confirmação do pagamento, foi configurado um endpoint POST (WebHook) em que o MercadoPago vai enviar uma confirmação de pagamento ou de cancelamento.

A requisição recebida segue o seguinte padrão:

```bash
{
    "id": "94da0f6e-8ab3-4caf-a7aa-51aecb340e15",
    "type": "payment",
    "date_created": "2015-03-25 10:04:58",
    "user_id": 44444,
    "api_version": "v1",
    "action": "state_CANCELED"
}
```

onde:
<i>
```bash
"action": "state_FINISHED" --> FINALIZADO
"action": "state_CANCELED" --> CANCELADO
```
</i>

## Demonstração

https://youtube.com/dkjsafnksjdfbsdfsdhf

## Créditos
Sistema e documentação desenvolvidos por <Salomão Pôlegar>.