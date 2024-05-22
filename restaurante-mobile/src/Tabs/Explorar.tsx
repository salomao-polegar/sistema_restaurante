import { VStack, ScrollView } from "native-base";
import { Titulo } from "../components/Titulo";
import { CardConsulta } from "../components/CardConsulta";
import { CardBusca } from "../components/CardBusca";

export default function Explorar(){

    const resultadoBusca = [
        {
            nome:"Dra. Ana Paula",
            especialidade: "Cardiologista",
            foto: "https://github.com/salomao-polegar.png"
        },
        {
            nome:"Dra. Júlia Maria",
            especialidade: "Endócrinologista",
            foto: "https://github.com/salomao-polegar.png"
        },
        {
            nome:"Dra. Mara Maravilha",
            especialidade: "Cardiologista",
            foto: "https://github.com/salomao-polegar.png"
        }
    ]

    return(
        <ScrollView flex={1}>
            <VStack 
                p={10}
                flex={1}
                alignItems="center">
                <CardBusca />

                <Titulo color="blue.500" mb={10}>Resultado da busca</Titulo>
                {resultadoBusca.map((resultado) => (
                    <CardConsulta 
                        nome = {resultado.nome}
                        especialidade= {resultado.especialidade}
                        foto= {resultado.foto}
                        />
                ))}
                
                
            </VStack>
        </ScrollView>
    )
}