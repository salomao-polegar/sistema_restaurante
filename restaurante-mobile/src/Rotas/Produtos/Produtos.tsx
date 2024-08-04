import { VStack, ScrollView } from "native-base";
import { useEffect, useState } from "react";
import { retornarProdutos } from "@/servicos/produtosServico";
import { Produto } from "@/src/interfaces/Produto";
import Botao from "@/src/components/Botao/Botao";
import { Titulo } from "@/src/components/TItulo/Titulo";
import { CardProduto } from "@/src/components/Cards/Produto/CardProduto";

interface ProdutosCard {
    navigation: any,
    administrador: boolean
}

export default function Produtos({ navigation, administrador }: ProdutosCard) {

    const [dadosProdutos, setDadosProdutos] = useState<[Produto]>([])
    
    async function carregarProdutos() {
        const resultado = await retornarProdutos()
        if (resultado) setDadosProdutos(resultado)
        console.log(resultado)
        
    }

    useEffect(() => {
        
        carregarProdutos()

    }, []);
    let categoria_atual = 0;

    return (

        
            <VStack

                alignItems="center">
                    <Botao onPress={() => { navigation.navigate("EditarProduto", 
                        { 
                            produto: {
                                nome:"", 
                                descricao:"", 
                                valor:0, 
                                categoria:0, 
                                id: 0,
                                foto_principal:null}, 
                                carregarProdutos: carregarProdutos, 
                                titulo: "Adicionar Produto" }) }}>Adicionar produto</Botao>

                {

                    dadosProdutos.map((produto: Produto) => {
                        if (produto.categoria != categoria_atual) {
                            categoria_atual = produto.categoria
                            switch (produto.categoria) {
                                case 1:
                                    return (
                                        <>
                                            <Titulo color="black" alignSelf="flex-start" mb={10} ml={5} key="produto.id">Lanches</Titulo>
                                            <CardProduto
                                                key={produto.id}
                                                produto={produto}
                                                
                                                navigation={navigation}
                                                administrador = {administrador}
                                                carregarProdutos = {carregarProdutos} />
                                        </>
                                    )

                                    break
                                case 2:
                                    return (
                                        <>
                                            <Titulo color="black" alignSelf="flex-start" mb={10} ml={5} key="produto.id">Acompanhamentos</Titulo>
                                            <CardProduto
                                                key={produto.id}
                                                produto={produto}
                                                navigation={navigation}
                                                administrador = {administrador}
                                                carregarProdutos = {carregarProdutos}  />
                                        </>)
                                    break

                                case 3:
                                    return (<>
                                        <Titulo color="black" alignSelf="flex-start" mb={10} ml={5} key="produto.id">Bebidas</Titulo>
                                        <CardProduto
                                            key={produto.id}
                                            produto={produto}
                                            navigation={navigation}
                                            administrador = {administrador}
                                            carregarProdutos = {carregarProdutos}  />
                                    </>)
                                    break
                                case 4:
                                    return (<>
                                        <Titulo color="black" alignSelf="flex-start" mb={10} ml={5} key="produto.id">Sobremesas</Titulo>
                                        <CardProduto
                                            key={produto.id}
                                            produto={produto}
                                            navigation={navigation}
                                            administrador = {administrador} 
                                            carregarProdutos = {carregarProdutos} />
                                    </>)
                                    break
                            }
                        }
                        else {
                            return (<CardProduto
                                                key={produto.id}
                                                produto={produto}
                                                navigation={navigation}
                                                administrador = {administrador}
                                                carregarProdutos = {carregarProdutos} />)
                        }

                    }
                    )
                }





            </VStack>
        
    )
}