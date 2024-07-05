import { Avatar, Button, Divider, HStack, Text, VStack } from "native-base";
import Logo from '../assets/Logo.png'
import { Alert, Pressable } from "react-native";
import { Produto } from '../interfaces/Produto'
import Botao from "./Botao";


interface CardProps {
    produto: Produto
    navigation?: any
    administrador: boolean
}

export function CardProduto({
    produto,
    navigation,
    administrador
    }:CardProps) {
        console.log(produto)
    
        function ajustar_texto(texto: string, limite: number){
            if (texto.length <= limite) return texto
            return texto.substring(0, limite-3) + "..."

        }

        


    return (
        <VStack w="100%" bg="white" px="5" pt={5} shadow={2}>
            <Pressable onPress={() => {navigation.navigate("ProdutoDescricao", {produto:produto})}}> 
            <HStack p={1}>
                
                    <Avatar     
                        source={produto.foto}
                        size="lg" />
                
                <VStack w="80%" pl='18'> 
                    <HStack justifyContent="space-between">
                    <Text fontSize="md" bold> {produto.nome} </Text>
                    {administrador ? <Text>ADM</Text> : <Botao w="30%">Editar</Botao>}
                    </HStack>
                    <Text pt={5} textAlign="justify">{ajustar_texto(produto.descricao, 100)}</Text>
                    <Text pt={5} fontSize='md'>R$ {(produto.valor).toLocaleString('pt-br', {minimumFractionDigits: 2})}</Text>
                    
                </VStack>
                
                
            </HStack>
            <Divider width="100%" mt={5} />
            </Pressable>
        </VStack>
    )
}