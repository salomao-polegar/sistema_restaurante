import { VStack, ScrollView, Text, Button } from "native-base";
import { Titulo } from "../components/Titulo";
import { CardConsulta } from "../components/CardConsulta";
import { CardBusca } from "../components/CardBusca";
import { CardCarrinho } from "../components/CardCarrinho";
import Botao from "../components/Botao";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { useEffect, useState } from "react";
import { Item } from "../interfaces/Item";

export default function Carrinho(){

    // const resultadoBusca = [
    //     {
    //         nome:"Dra. Ana Paula",
    //         especialidade: "Cardiologista",
    //         foto: "https://github.com/salomao-polegar.png"
    //     },
    //     {
    //         nome:"Dra. Júlia Maria",
    //         especialidade: "Endócrinologista",
    //         foto: "https://github.com/salomao-polegar.png"
    //     },
    //     {
    //         nome:"Dra. Mara Maravilha",
    //         especialidade: "Cardiologista",
    //         foto: "https://github.com/salomao-polegar.png"
    //     }
    // ]
    const [carrinho, setCarrinho] = useState<Item[]>([])
    const carregar_carrinho = async () => {
        try {
          const carrinhoStorage = await AsyncStorage.getItem('carrinho');
          if (carrinhoStorage !== null) {
            setCarrinho(JSON.parse(carrinhoStorage));
          }
        } catch (error) {
          console.error('Erro carregando carrinho', error);
        }
      };
    
      useEffect(() => {
        // Fetch data from AsyncStorage
    
    
        carregar_carrinho();
      }, []);

    return(
        <ScrollView flex={1}>
            <VStack 
                p={10}
                flex={1}
                alignItems="center"
                alignSelf="center"
                w="100%"
                maxW={800}>
                <CardCarrinho carregar_carrinho={carregar_carrinho} />

                <Text bold >Resumo dos valores</Text>

                <Text bold >Subtotal:</Text>
                <Text bold >Taxa de entrega:</Text>
                <Text bold >Total: </Text>

                <Button onPress={carregar_carrinho} w="49%" bgColor="blue.800">Atualizar carrinho</Button>

                
                
                
                
            </VStack>
        </ScrollView>
    )
}