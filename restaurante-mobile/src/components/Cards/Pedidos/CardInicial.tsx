import { Avatar, Divider, Text, VStack } from "native-base";
import Logo from '../assets/Logo.png'
import { Alert, Pressable } from "react-native";
import { Ionicons } from "@expo/vector-icons";

interface CardInicialProps {
    icone: string;
    texto: string;
    
}

export function CardInicialProduto({
    icone,
    texto,
}: CardInicialProps) {
    return (
        <VStack w="30%" bg="white" p={5} shadow={2} borderRadius={10} alignItems="center" alignContent="center">
                <Ionicons name={icone} size={40} />
                <Text
                    fontFamily="Inter"
                    fontSize="md"
                    bold    
                    alignSelf="center"
                    
                    >{texto}</Text>
        </VStack>
    )
}