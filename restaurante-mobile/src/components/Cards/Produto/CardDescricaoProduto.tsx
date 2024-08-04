import { Avatar, Image, Text, VStack } from "native-base";
import api from "@/servicos/api";
import { Produto } from "../../../interfaces/Produto";


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
    const source = String(api.getUri() + "foto/" + String(produto.foto_principal) + "/")
    console.log("FOtoPrincipal:")
    console.log(source)
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
                <VStack>
                <Image source={{ uri: source }} 
                    alt="Produto" size="2xl"
                    my={5}
                    alignSelf="center"
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