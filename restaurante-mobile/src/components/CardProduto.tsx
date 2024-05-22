import { Avatar, Text, VStack } from "native-base";
import Logo from '../assets/Logo.png'

interface CardProps {
    nome: string;
    foto?: string;
    descricao: string;
    valor: number;
    foiAtendido?: boolean;
    foiAgendado?: boolean;
}

export function CardProduto({
    nome,
    foto,
    descricao,
    valor
    }:CardProps) {
    return (
        <VStack w="100%" bg="white" p="5" borderRadius="lg" shadow={2} mb={5}>
            
            <VStack flexDir="row"  >
                <Avatar     
                    source={Logo} 
                    size="lg" />

                <VStack pr="20" pl={4}>
                    <Text fontSize="md" bold>{nome}</Text>
                    <Text>{descricao}</Text>
                    <Text>R$ {valor}</Text>
                </VStack>
                
                
            </VStack>
        </VStack>
    )
}