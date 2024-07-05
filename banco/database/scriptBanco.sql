SET CHARSET UTF8;

CREATE TABLE categoria_produto (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(100), 
    descricao VARCHAR (400),
    ativo int DEFAULT 1,
    PRIMARY KEY (id));

INSERT INTO categoria_produto (nome, descricao) VALUES
('LANCHE', 'Lanches da casa'),
('ACOMPANHAMENTO', 'Acompanhamentos para seu lanche'),
('BEBIDA', 'Experimente nossas deliciosas bebidas!'),
('SOBREMESA', 'Você merece um docinho. Experimente nossas sobremesas');

CREATE TABLE produtos (
    id int NOT NULL AUTO_INCREMENT, 
    nome varchar(100), 
    categoria int, 
    valor decimal(7, 2), 
    descricao varchar (500), 
    ativo int DEFAULT 1,
    PRIMARY KEY (id),
    FOREIGN KEY (categoria) REFERENCES categoria_produto(id));

INSERT INTO produtos (nome, categoria, valor, descricao)  VALUES 
('Big Mac', 1, 25.5, 'Dois hambúrgueres (100% carne bovina), alface americana, queijo sabor cheddar, molho especial, cebola, picles e pão com gergelim.'),
('Quarterão com Queijo', 1, 30.5, 'Um hambúrguer (100% carne bovina), queijo sabor cheddar, picles, cebola, ketchup, mostarda e pão com gergelim.'),
('Hamburger', 1, 20.5, 'Um Hamburguer (100% carne bovina), cebola, picles, ketchup, mostarda e pão sem gergelim.'),
('Cheeseburger', 1, 21.5, 'Um hamburguer (100% carne bovina), queijo sabor cheddar, cebola, picles, ketchup, mostarda e pão sem gergelim.'),
('McFritas Pequena', 2, 10.5, 'A batata frita mais famosa do mundo. Deliciosas batatas selecionadas, fritas, crocantes por fora, macias por dentro, douradas, irresistíveis, saborosas, famosas, e todos os outros adjetivos positivos que você quiser dar.'),
('Chicken McNuggets 4 unidades', 2, 10.5, '4 Chicken McNuggets saborosos e crocantes de peito de frango.'),
('Coca-Cola 300ml', 3, 7.5, 'Refrescante e geladinha. Uma bebida assim refresca a vida.'),
('Coca-Cola Zero 700ml', 3, 15.5, 'Refrescante e geladinha. Uma bebida assim refresca a vida.'),
('Sprite sem Açúcar 500ml', 3, 10.5, 'Refrescante e geladinha. Uma bebida assim refresca a vida.'),
('McFlurry M&Ms Caramelo', 4, 16.9, 'Composto por bebida láctea sabor baunilha, cobertura de caramelo e M&M´s ® chocolate ao leite'),
('McFlurry Ovomaltine Rocks Ao Leite Morango', 4, 16.9, 'Para sua #FomeGeladinhadeMéqui nosso delicioso McFlurry Ovomaltine, com bebida láctea sabor baunilha, flocos de ovomaltine e cobertura de morango.'),
('Kit Kat com Leite em Pó Mais Querido do Brasil Morango', 4, 16.9, 'Sobremesa composta por bebida láctea sabor baunilha, cobertura de morango, leite em pó e chocolate Kit Kat.');



CREATE TABLE clientes (
    id int NOT NULL AUTO_INCREMENT,
    cpf varchar(11) NOT NULL,
    nome varchar(50) NOT NULL,
    email varchar(150) NOT NULL,
    hashed_password varchar(150),
    administrador int DEFAULT 0,
    telefone varchar(11),
    ativo int DEFAULT 1,
    PRIMARY KEY (id));

INSERT INTO clientes (id, nome, cpf, email, hashed_password, administrador) VALUES 
(0, 'Administrador', '12345678901', 'adm@adm', 'fdddc25a825d6f6ab8fe08b88fb1ef55f32560bfb563db818b58b008c865daf0', 1); 
-- #senha: testeagora

INSERT INTO clientes (cpf, nome, email, hashed_password, telefone) VALUES 
('11111111111', 'teste', 'testeagora', '6546', '1112345678'),
('22222222222', 'nome 2', 'nome2@teste', '5678',  '1112345678'),
('33333333333', 'nome 3', 'nome3@teste', '9012',  '1112345678'),
('44444444444', 'nome 4', 'nome4@teste', '3456',  '1112345678'),
('55555555555', 'nome 5', 'nome5@teste', '7890',  '1112345678'),
('66666666666', 'nome 6', 'nome6@teste', '0987',  '1112345678');

CREATE TABLE pedidos (
    id int NOT NULL AUTO_INCREMENT, 
    datahora_recebido datetime DEFAULT CURRENT_TIMESTAMP,
    datahora_preparacao datetime DEFAULT NULL,
    datahora_pronto datetime DEFAULT NULL,
    datahora_finalizado datetime DEFAULT NULL,
    status_pedido int DEFAULT 1,
    status_pagamento int DEFAULT 1,
    id_pagamento varchar(200) DEFAULT NULL,
    cliente int,
    PRIMARY KEY (id),
    FOREIGN KEY (cliente) REFERENCES clientes(id));
-- STATUS_PEDIDO
-- RECEBIDO = 1
-- EM PREPARAÇÃO = 2
-- PRONTO = 3
-- FINALIZADO = 4

-- STATUS_PAGAMENTO
-- AGUARDANDO = 1
-- APROVADO = 2
-- RECUSADO = 3

INSERT INTO pedidos(datahora_recebido, status_pedido, cliente) VALUES
('2024-03-10 20:38:05', 2, 1),
('2024-08-13 20:38:05', 3, 3),
('2024-01-14 20:38:05', 4, 3),
('2024-03-21 20:38:05', 1, 3),
('2024-09-03 20:38:05', 2, 2),
('2024-02-01 20:38:05', 3, 1),
('2024-12-25 20:38:05', 3, 2),
('2024-08-12 20:38:05', 2, 3),
('2024-01-14 20:38:05', 4, 1),
('2024-03-21 20:38:05', 1, 2),
('2024-09-03 20:38:05', 2, 3),
('2024-02-01 20:38:05', 3, 1),
('2024-12-25 20:38:05', 3, 2),
('2024-08-12 20:38:05', 2, 3);

CREATE TABLE itens (
    pedido int, 
    produto int, 
    quantidade int, 
    descricao VARCHAR (100),
    PRIMARY KEY (pedido, produto),
    FOREIGN KEY (produto) REFERENCES produtos(id) ON DELETE CASCADE,
    FOREIGN KEY (pedido) REFERENCES pedidos(id) ON DELETE CASCADE);
-- Tabela que contém os produtos adicionados em um pedido

INSERT INTO itens (pedido, produto, quantidade) VALUES
(1, 1, 42),
(1, 2, 21),
(2, 2, 2),
(3, 4, 4);