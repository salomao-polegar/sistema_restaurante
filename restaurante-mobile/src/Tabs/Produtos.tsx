import { VStack, ScrollView } from "native-base";
import { Titulo } from "../components/Titulo";
import { CardProduto } from "../components/CardProduto";
import lanche1 from '../assets/lanche1.png'
import { ReactElement, useEffect, useState } from "react";
import { retornarProdutos } from "@/servicos/produtosServico";
import { Produto } from "../interfaces/Produto";
import { Cliente } from "../interfaces/Cliente";

interface ProdutosCard {
    navigation: any,
    administrador: boolean
}

export default function Produtos({ navigation, administrador }: ProdutosCard) {

    const [dadosProdutos, setDadosProdutos] = useState([])

    useEffect(() => {
        async function carregarProdutos() {
            const resultado = await retornarProdutos()
            if (resultado) {
                setDadosProdutos(resultado)
                console.log(dadosProdutos)
            }
        }
        carregarProdutos()

    }, []);
    let categoria_atual = 0;

    return (

        
            <VStack

                alignItems="center">

                {

                    dadosProdutos.map((produto: Produto) => {


                        if (produto.categoria != categoria_atual) {
                            categoria_atual = produto.categoria


                            switch (produto.categoria) {

                                case 1:
                                    return (
                                        <>
                                            <Titulo color="black" alignSelf="flex-start" mb={10} ml={5}>Lanches</Titulo>
                                            <CardProduto
                                                key={produto.id}
                                                produto={produto}
                                                navigation={navigation}
                                                administrador = {administrador} />
                                        </>
                                    )

                                    break
                                case 2:
                                    return (
                                        <>
                                            <Titulo color="black" alignSelf="flex-start" mb={10} ml={5}>Acompanhamentos</Titulo>
                                            <CardProduto
                                                key={produto.id}
                                                produto={produto}
                                                navigation={navigation} />
                                        </>)
                                    break

                                case 3:
                                    return (<>
                                        <Titulo color="black" alignSelf="flex-start" mb={10} ml={5}>Bebidas</Titulo>
                                        <CardProduto
                                            key={produto.id}
                                            produto={produto}
                                            navigation={navigation} />
                                    </>)
                                    break
                                case 4:
                                    return (<>
                                        <Titulo color="black" alignSelf="flex-start" mb={10} ml={5}>Sobremesas</Titulo>
                                        <CardProduto
                                            key={produto.id}
                                            produto={produto}
                                            navigation={navigation} />
                                    </>)
                                    break
                            }
                        }
                        else {
                            return (<CardProduto
                                                key={produto.id}
                                                produto={produto}
                                                navigation={navigation} />)
                        }

                    }
                    )
                }





            </VStack>
        
    )
}