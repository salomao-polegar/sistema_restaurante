import { VStack } from "native-base";
import { EntradaTexto } from "./EntradaTexto";
import Botao from "./Botao";



export function CardBusca() {
    return (
        <VStack w="100%" bg="white" p="5" borderRadius="lg" shadow={2} mb={5}>
            <EntradaTexto placeholder="Digite a especialidade" key="especialidade" />
            <EntradaTexto placeholder="Digite sua localizaçãoe" key="localizacao" />
            <Botao mt={5}>Buscar</Botao>
        </VStack>

        
    )
}