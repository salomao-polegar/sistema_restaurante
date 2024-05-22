import { VStack, ScrollView, Text, Divider, Image } from "native-base";
import { Titulo } from "../components/Titulo";
import Logo from '../assets/Logo.png'
import { CardBusca } from "../components/CardBusca";

export default function Principal(){

    const depoimentos = [
        {
            key:1,
            texto:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            referencia:"Julio, 40 anos, São Paulo/SP."
        },

        {
            key:2,
            texto:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            referencia:"Julio, 40 anos, São Paulo/SP."
        },
    ]
    return(

        <ScrollView flex={1}>
            <VStack 
                p={10}
                flex={1}
                alignItems="center">
                <Image source={Logo} alt="Logo Restaurante" alignSelf="flex-start" />
                <Titulo color="blue.500" alignSelf="flex-start" mb={10}>Boas-vindas!</Titulo>
                <CardBusca />
                <Titulo color="blue.800" mb={10}>Depoimentos</Titulo>
                {depoimentos.map((depoimento) => (
                    <VStack key={depoimento.key}
                        alignItems="center">
                        
                        <Text mb={4} fontSize="sm">{depoimento.texto}</Text>
                        <Text fontSize="md" bold mb={10}>{depoimento.referencia}</Text>
                        <Divider />
                    </VStack>
                ))}
                


                
                
            </VStack>
        </ScrollView>
    )
}