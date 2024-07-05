import { VStack, ScrollView } from "native-base";
import { CardInicialProduto } from "../components/CardInicial";
import Produtos from "./Produtos";
import { useEffect, useState } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { pegarDadosClienteLogado as pegarDadosCliente } from "@/servicos/clienteServico";
import { Cliente } from "../interfaces/Cliente";

export default function Principal({ navigation }: any) {

    const [dadosCliente, setDadosCliente] = useState({} as Cliente)

    useEffect(() => {
        async function carregarClientes() {

            const clienteId = await AsyncStorage.getItem("userId")
            console.log(clienteId)
            if (!clienteId) return null
            const resultado = await pegarDadosCliente(clienteId)
            if (resultado) {
                setDadosCliente(resultado[0])
                console.log(dadosCliente)
            }
        }

    })

    return (

        <ScrollView flex={1}>
            <VStack p={10}
                flex={1}

                alignSelf="center"
                w="100%"
                maxW={800}>
                <VStack
                    flex={1}
                    direction="row"
                    justifyContent="space-between">
                        
                    <CardInicialProduto icone="wallet-outline" texto="Formas de Pagamento" />
                    <CardInicialProduto icone="storefront-outline" texto="Sobre" />
                    <CardInicialProduto icone="share-social-outline" texto="Compartilhar" />
                </VStack>

                <Produtos navigation={navigation} administrador={dadosCliente.administrador} />


            </VStack>

        </ScrollView>
    )
}