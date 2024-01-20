SET CHARSET UTF8;

CREATE TABLE produtos (id int NOT NULL AUTO_INCREMENT, 
                        nome varchar(100), 
                        categoria int, 
                        valor decimal(7, 2), 
                        descricao varchar (500), 
                        ativo int,  
                        PRIMARY KEY (id))
        ENGINE = InnoDB
        DEFAULT CHARSET = utf8mb4;;


INSERT INTO produtos (nome, categoria, valor, descricao, ativo) 
VALUES 
('Big Mac', 1, 25.5, 'Dois hambúrgueres (100% carne bovina), alface americana, queijo sabor cheddar, molho especial, cebola, picles e pão com gergelim.', 1),
('Quarterão com Queijo', 1, 30.5, 'Um hambúrguer (100% carne bovina), queijo sabor cheddar, picles, cebola, ketchup, mostarda e pão com gergelim.', 1),
('Hamburger', 1, 20.5, 'Um Hamburguer (100% carne bovina), cebola, picles, ketchup, mostarda e pão sem gergelim.', 1),
('Cheeseburger', 1, 21.5, 'Um hamburguer (100% carne bovina), queijo sabor cheddar, cebola, picles, ketchup, mostarda e pão sem gergelim.', 1),
('McFritas Pequena', 2, 10.5, 'A batata frita mais famosa do mundo. Deliciosas batatas selecionadas, fritas, crocantes por fora, macias por dentro, douradas, irresistíveis, saborosas, famosas, e todos os outros adjetivos positivos que você quiser dar.', 1),
('Chicken McNuggets 4 unidades', 2, 10.5, '4 Chicken McNuggets saborosos e crocantes de peito de frango.', 1),
('Coca-Cola 300ml', 3, 7.5, 'Refrescante e geladinha. Uma bebida assim refresca a vida.', 1),
('Coca-Cola Zero 700ml', 3, 15.5, 'Refrescante e geladinha. Uma bebida assim refresca a vida.', 1),
('Sprite sem Açúcar 500ml', 3, 10.5, 'Refrescante e geladinha. Uma bebida assim refresca a vida.', 1),
('McFlurry M&Ms Caramelo', 4, 16.9, 'Composto por bebida láctea sabor baunilha, cobertura de caramelo e M&M´s ® chocolate ao leite', 1),
('McFlurry Ovomaltine Rocks Ao Leite Morango', 4, 16.9, 'Para sua #FomeGeladinhadeMéqui nosso delicioso McFlurry Ovomaltine, com bebida láctea sabor baunilha, flocos de ovomaltine e cobertura de morango.', 1),
('Kit Kat com Leite em Pó Mais Querido do Brasil Morango', 4, 16.9, 'Sobremesa composta por bebida láctea sabor baunilha, cobertura de morango, leite em pó e chocolate Kit Kat.', 1);



CREATE TABLE clientes (id int NOT NULL AUTO_INCREMENT,
                        cpf varchar(11),
                        nome varchar(50),
                        email varchar(150),
                        telefone varchar(11)
                        PRIMARY KEY (id),
                        UNIQUE (cpf));
-- PENSAR NA CHAVE PRIMÁRIA DO CLIENTE, VISTO QUE ELE PODE NÃO SE IDENTIFICAR. UTILIZAR O E-MAIL COMO OBJETO DE VALOR?

INSERT INTO clientes (ID, nome) VALUES 
(0, 'SEM IDENTIFICAÇÃO');

INSERT INTO clientes (cpf, nome, email, telefone) VALUES 
('11111111111', 'nome 1', 'nome1@teste', '1112345678'),
('22222222222', 'nome 2', 'nome2@teste', '1112345678'),
('33333333333', 'nome 3', 'nome3@teste', '1112345678'),
('44444444444', 'nome 4', 'nome4@teste', '1112345678'),
('55555555555', 'nome 5', 'nome5@teste', '1112345678'),
('66666666666', 'nome 6', 'nome6@teste', '1112345678');

CREATE TABLE pedidos (id int NOT NULL AUTO_INCREMENT, 
                    PRIMARY KEY (id),
                    datahora_pedido datetime DEFAULT CURRENT_TIMESTAMP,
                    status_pedido int,
                    cliente int,
                    FOREIGN KEY (cliente) REFERENCES clientes(id));

INSERT INTO pedidos(status_pedido, cliente) VALUES
(1, 1),
(1, 2),
(1, 3);

CREATE TABLE produtos_do_pedido (id_pedido int, id_produto int, quantidade int,
    FOREIGN KEY (id_produto) REFERENCES produtos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id) ON DELETE CASCADE);

INSERT INTO produtos_do_pedido(id_pedido, id_produto, quantidade) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 2),
(2, 1, 3),
(1, 1, 4);

-- CATEGORIAS 

-- LANCHE = 1
-- ACOMPANHAMENTO = 2
-- BEBIDA = 3
-- SOBREMESA = 4

-- STATUS_PEDIDO

-- RECEBIDO = 1
-- EM PREPARAÇÃO = 2
-- PRONTO = 3
-- FINALIZADO = 4