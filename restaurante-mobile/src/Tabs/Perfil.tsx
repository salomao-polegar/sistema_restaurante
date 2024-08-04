import { VStack, Text, ScrollView, Avatar, Divider } from "native-base";
import { Titulo } from "../components/TItulo/Titulo";
import { useEffect, useState } from "react";
import { pegarDadosClienteLogado as pegarDadosCliente, retornarHistoricoCliente } from "@/servicos/clienteServico";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Cliente } from "../interfaces/Cliente";
import { Pedido } from "../interfaces/Pedido";
import { CardPedido } from "../components/Cards/Pedidos/CardPedido";
import Botao from "../components/Botao/Botao";

export default function Perfil({ navigation }: any) {

    const [dadosCliente, setDadosCliente] = useState({} as Cliente)
    const [dadosPedidos, setDadosPedidos] = useState([{} as Pedido])

    useEffect(() => {
        async function carregarCliente() {
            const clienteId = await AsyncStorage.getItem("userId")
            console.log(clienteId)
            if (!clienteId) return null
            const resultado = await pegarDadosCliente(clienteId)
            if (resultado) {
                setDadosCliente(resultado[0])
                console.log(dadosCliente)
            }
        }

        async function carregarHistorico() {
            const clienteId = await AsyncStorage.getItem("userId")
            if (!clienteId) return null
            const resultado = await retornarHistoricoCliente(clienteId)
            // console.log(resultado)
            if (resultado) {
                setDadosPedidos(resultado)
                console.log("dados pedidos:")
                console.log(dadosPedidos)
                console.log('fim dados pedidos')
            }
        }
        carregarCliente()
        carregarHistorico()
    }, [])

    async function sair() {
        AsyncStorage.removeItem('token')
        navigation.replace("Login")
    }



    return (
        <ScrollView flex={1}>
            <VStack
                p={10}
                flex={1}
               
                alignSelf="center"
                w="100%"
                maxW={800}
                
                
                

            >
                {dadosCliente.nome ? <></> :
                    <Botao onPress={() => navigation.navigate("Login")} mt={4}>Login</Botao>
                }
                <Titulo color="blue.800">Meu Perfil</Titulo>
                <Avatar
                    alignSelf="center"
                    source={{ uri: "https://github.com/salomao-polegar.png" }}
                    mt={5}
                    size="xl" />
                <Titulo color="blue.800">Informações pessoais</Titulo>
                <Titulo fontSize="lg" mb={1} color="blue.700">{dadosCliente.nome}</Titulo>
                <Text textAlign="center">{dadosCliente.email}</Text>
                <Text textAlign="center">{dadosPedidos.length} pedidos realizados</Text>
                

                <Divider mt={5} />

                <Text my={5} bold textAlign="left" fontSize='lg'>Histórico de Pedidos</Text>
                {dadosPedidos.map((pedido: Pedido) => (<CardPedido
                    pedido={pedido}
                    navigation={navigation} />)
                )}
                <Botao onPress={sair} alignSelf="center">Sair</Botao>



            </VStack>
        </ScrollView>
    )
}