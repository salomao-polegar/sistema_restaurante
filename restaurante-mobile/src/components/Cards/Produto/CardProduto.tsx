import { Avatar, Button, Divider, HStack, Text, useToast, VStack } from "native-base";
import { Alert, Pressable } from "react-native";
import { Produto } from '../../../interfaces/Produto'
import Botao from "../../Botao/Botao";
import api from "@/servicos/api";
import { useState } from "react";
import { EditarProdutoAPI } from "@/servicos/produtoServico";


interface CardProps {

    produto: Produto

    navigation?: any
    administrador: boolean
    carregarProdutos: () => void
}

export function CardProduto({

    produto,

    navigation,
    administrador,
    carregarProdutos
}: CardProps) {

    const [ativo, setAtivo] = useState(produto.ativo);
    const toast = useToast();

    function ajustar_texto(texto: string, limite: number) {
        if (texto.length <= limite) return texto
        return texto.substring(0, limite - 3) + "..."

    }
    async function toggleAtivo() {
        
        

        const resultado = await EditarProdutoAPI({
            categoria: produto.categoria,
            descricao: produto.descricao,
            nome: produto.nome,
            valor: produto.valor,
            ativo: ativo? false : true,
            foto_principal: produto.foto_principal,
            id: produto.id
        })
        if (resultado?.response?.data?.detail) {
            console.log(resultado.response.data.detail)

            toast.show({
                title: "Erro",
                description: resultado.response.data.detail,
                backgroundColor: "red.500"
            })
        } else if (!resultado) {
            toast.show({
                title: "Erro",
                description: "Erro ao editar produto",
                backgroundColor: "red.500"
            })
        }
        else {
            setAtivo(!ativo);
            toast.show({
                title: "Sucesso",
                description: "Edição realizada com sucesso",
                backgroundColor: "green.500"
            })
        }
    }
    const ativar = () => {
        setAtivo(true);
    }
    return (
        <VStack w="100%" bg={ativo ? "white" : "gray:300"} px="5" pt={5} shadow={2} opacity={ativo ? "100" : "50%"}>
            <Pressable onPress={() => { navigation.navigate("ProdutoDescricao", { produto: produto }) }}>
                <HStack p={1}>

                    <Avatar
                        source={{ uri: api.getUri() + "foto/" + String(produto.foto_principal) + "/" }}
                        size="lg" />

                    <VStack w="80%" pl='18'>

                        <Text fontSize="md" bold> {produto.nome} </Text>
                        <Text pt={5} textAlign="justify">{ajustar_texto(produto.descricao, 100)}</Text>
                        <Text pt={5} fontSize='md'>R$ {(produto.valor).toLocaleString('pt-br', { minimumFractionDigits: 2 })}</Text>
                        <HStack justifyContent="space-between">
                            <Botao w="48%" onPress={() => { navigation.navigate("EditarProduto", { produto: produto, carregarProdutos: carregarProdutos, titulo: "Editar Produto" }) }}>Editar</Botao>
                            <Botao w="48%" onPress={toggleAtivo}>{ativo ? "Desativar" : "Ativar"}</Botao>
                        </HStack>
                    </VStack>


                </HStack>
                <Divider width="100%" mt={5} />
            </Pressable>
        </VStack>
    )
}