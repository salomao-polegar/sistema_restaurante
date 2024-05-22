import { VStack, Text, ScrollView , Avatar, Divider, Card } from "native-base";
import { Titulo } from "../components/Titulo";
import Botao from "../components/Botao";
import { CardConsulta } from "../components/CardConsulta";

export default function Consultas(){
    return(
        <ScrollView flex={1}>
            <VStack 
                p={10}
                flex={1}
                alignItems="center"
                
                >
                <Titulo color="blue.500">Minhas consultas</Titulo>
                <Botao mt="5" mb={5}>Agendar outra consulta</Botao>
                <Titulo color="blue.500" fontSize="lg" alignSelf="flex-start" mb={2}>Próximas consultas</Titulo>
                <CardConsulta 
                    nome="Dra. Ana Paula" 
                    especialidade="Cardiologista" 
                    foto="https://github.com/salomao-polegar.png"
                    data="20/05/2024"
                    foiAgendado
                     />
                <Divider mt={5} />
                
                <Titulo color="blue.500" fontSize="lg" alignSelf="flex-start" mb={2}>Consultas passadas</Titulo>
                <CardConsulta 
                    nome="Dra. Ana Paula" 
                    especialidade="Cardiologista" 
                    foto="https://github.com/salomao-polegar.png"
                    data="20/05/2024"
                    
                    foiAtendido
                     />
                <CardConsulta 
                    nome="Dra. Ana Paula" 
                    especialidade="Cardiologista" 
                    foto="https://github.com/salomao-polegar.png"
                    data="20/05/2024"
                    foiAtendido
                     />
                <CardConsulta 
                    nome="Dra. Ana Paula" 
                    especialidade="Cardiologista" 
                    foto="https://github.com/salomao-polegar.png"
                    data="20/05/2024"
                    foiAtendido
                     />

                <Divider mt={5} />

            </VStack>
        </ScrollView>
    )
}