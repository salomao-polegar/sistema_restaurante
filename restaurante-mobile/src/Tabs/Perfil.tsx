import { VStack, Text, ScrollView, Avatar, Divider } from "native-base";
import { Titulo } from "../components/Titulo";

export default function Perfil(){
    return(
        <ScrollView flex={1}>
            <VStack 
                p={10}
                flex={1}
                alignItems="center"
                >
                <Titulo color="blue.500">Meu Perfil</Titulo>
                <Avatar 
                    source={{uri: "https://github.com/salomao-polegar.png"}} 
                    mt={5}
                    size="xl" />
                <Titulo color="blue.500">Informações pessoais</Titulo>
                <Titulo fontSize="lg" mb={1}>Salomão Pôlegar</Titulo>
                <Text>03/06/1996</Text>
                <Text>São Paulo</Text>
                
                <Divider mt={5} />

                <Titulo color="blue.500" mb={1}>Histórico Médico</Titulo>
                <Text>Bronquite</Text>
                <Text>Amigdalite</Text>
                <Text>Sinusite</Text>
                

            </VStack>
        </ScrollView>
    )
}