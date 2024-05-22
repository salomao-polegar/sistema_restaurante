import { VStack, ScrollView, Text, Divider, Image, Card, Avatar } from "native-base";
import { Titulo } from "../components/Titulo";
import Logo from '../assets/Logo.png'
import { CardBusca } from "../components/CardBusca";
import Botao from "../components/Botao";
import { CardProduto } from "../components/CardProduto";
import api from "@/servicos/api";

export default function Produtos() {

    async function listaProdutos(){
        await api.get('/produtos')
            .then(response => {
                const produtos = response.data
                return produtos
            })
            
    }
    
    // const produtos = listaProdutos()
    
    // console.log(produtos);

    const produtos = [
        {
            "id": 1,
            "nome": "Big Mac",
            "categoria": 1,
            "valor": 25.5,
            "descricao": "Dois hambúrgueres (100% carne bovina), alface americana, queijo sabor cheddar, molho especial, cebola, picles e pão com gergelim.",
            "ativo": 1
        },
        {
            "id": 2,
            "nome": "Quarterão com Queijo",
            "categoria": 1,
            "valor": 30.5,
            "descricao": "Um hambúrguer (100% carne bovina), queijo sabor cheddar, picles, cebola, ketchup, mostarda e pão com gergelim.",
            "ativo": 1
        },
        {
            "id": 3,
            "nome": "Hamburger",
            "categoria": 1,
            "valor": 20.5,
            "descricao": "Um Hamburguer (100% carne bovina), cebola, picles, ketchup, mostarda e pão sem gergelim.",
            "ativo": 1
        },
        {
            "id": 4,
            "nome": "Cheeseburger",
            "categoria": 1,
            "valor": 21.5,
            "descricao": "Um hamburguer (100% carne bovina), queijo sabor cheddar, cebola, picles, ketchup, mostarda e pão sem gergelim.",
            "ativo": 1
        },
        {
            "id": 5,
            "nome": "McFritas Pequena",
            "categoria": 2,
            "valor": 10.5,
            "descricao": "A batata frita mais famosa do mundo. Deliciosas batatas selecionadas, fritas, crocantes por fora, macias por dentro, douradas, irresistíveis, saborosas, famosas, e todos os outros adjetivos positivos que você quiser dar.",
            "ativo": 1
        },
        {
            "id": 6,
            "nome": "Chicken McNuggets 4 unidades",
            "categoria": 2,
            "valor": 10.5,
            "descricao": "4 Chicken McNuggets saborosos e crocantes de peito de frango.",
            "ativo": 1
        },
        {
            "id": 7,
            "nome": "Coca-Cola 300ml",
            "categoria": 3,
            "valor": 7.5,
            "descricao": "Refrescante e geladinha. Uma bebida assim refresca a vida.",
            "ativo": 1
        },
        {
            "id": 8,
            "nome": "Coca-Cola Zero 700ml",
            "categoria": 3,
            "valor": 15.5,
            "descricao": "Refrescante e geladinha. Uma bebida assim refresca a vida.",
            "ativo": 1
        },
        {
            "id": 9,
            "nome": "Sprite sem Açúcar 500ml",
            "categoria": 3,
            "valor": 10.5,
            "descricao": "Refrescante e geladinha. Uma bebida assim refresca a vida.",
            "ativo": 1
        },
        {
            "id": 10,
            "nome": "McFlurry M&Ms Caramelo",
            "categoria": 4,
            "valor": 16.9,
            "descricao": "Composto por bebida láctea sabor baunilha, cobertura de caramelo e M&M´s ® chocolate ao leite",
            "ativo": 1
        },
        {
            "id": 11,
            "nome": "McFlurry Ovomaltine Rocks Ao Leite Morango",
            "categoria": 4,
            "valor": 16.9,
            "descricao": "Para sua #FomeGeladinhadeMéqui nosso delicioso McFlurry Ovomaltine, com bebida láctea sabor baunilha, flocos de ovomaltine e cobertura de morango.",
            "ativo": 1
        },
        {
            "id": 12,
            "nome": "Kit Kat com Leite em Pó Mais Querido do Brasil Morango",
            "categoria": 4,
            "valor": 16.9,
            "descricao": "Sobremesa composta por bebida láctea sabor baunilha, cobertura de morango, leite em pó e chocolate Kit Kat.",
            "ativo": 1
        }
    ]
    return (

        <ScrollView flex={1}>
            <VStack
                p={10}
                flex={1}
                alignItems="center">
                <Image source={Logo} alt="Logo Restaurante" alignSelf="flex-start" />
                <Titulo color="blue.500" alignSelf="flex-start" mb={10} >Cardápio</Titulo>
                <Titulo color="black" alignSelf="flex-start" mb={10}>Lanches</Titulo>
                
                {produtos.map((produto) => (
                    <CardProduto descricao={produto.descricao} nome={produto.nome} valor={produto.valor}></CardProduto>
                ))}





            </VStack>
        </ScrollView>
    )
}