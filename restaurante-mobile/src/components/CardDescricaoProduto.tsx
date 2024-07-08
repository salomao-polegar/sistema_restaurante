import { Avatar, Divider, Image, Text, VStack } from "native-base";
import Logo from '../assets/Logo.png'
import { Alert, Pressable } from "react-native";
import { Produto } from "../interfaces/Produto";


interface CardDescricaoProdutoProps {
    produto: Produto
    navigation?: any
    size?: string
    imagem: any
}

export function CardDescricaoProduto({
    produto,
    navigation,
    size,
    imagem
}: CardDescricaoProdutoProps) {
    return (
        <VStack
            w="100%"
            bg="white"
            px="5"
            pt={5}
            m={5}
            shadow={2}
            width={size}
            alignSelf="center"
            borderRadius={10}>
            <VStack>
                <Text
                    fontFamily="Montserrat"
                    fontSize={28}
                    bold
                    alignSelf="center"
                    mb={5}
                >{produto.nome}</Text>
                <VStack><Image

                    source={imagem}
                    my={5}
                    alignSelf="center"
                    borderRadius={10}
                    height="250"
                    

                /></VStack>

                <Text fontFamily="Montserrat"
fontSize="lg"
textAlign="justify"
style={{"text-indent": "8%"}}
                    mb={5}
                    alignSelf="justify">{produto.descricao}</Text>
                <Text fontFamily="Montserrat"
                    mb={5}
                    fontSize="lg"
                    alignSelf="end">R$ {(produto.valor).toLocaleString('pt-br', { minimumFractionDigits: 2 })}</Text>
            </VStack>


        </VStack>
    )
}