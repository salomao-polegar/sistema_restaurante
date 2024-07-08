import { Avatar, Button, Divider, HStack, Text, VStack } from "native-base";
import Logo from '../assets/Logo.png'
import { Alert, Pressable } from "react-native";
import { Pedido } from "../interfaces/Pedido";
import { Ionicons } from "@expo/vector-icons";
import Botao from "./Botao";
import moment from "moment";

interface CardProps {
    pedido: Pedido
    navigation: any
}

export function CardPedido({
    pedido, navigation
}: CardProps) {
    return (

        pedido.itens ? <VStack bg="white" px="5" pt={5} shadow={2} w="100%">
            {/* <Pressable onPress={() => {navigation.navigate("Produto")}}> */}
            <VStack flexDir="row" p={1}>
                <VStack pl={4} w="100%">
                    <Text fontSize="md" bold mb={2}><Ionicons name="checkmark-circle" size={20} color="green" /> Pedido concluído Nº {pedido.id}</Text>
                
                    <Text fontSize='sm' mb={2}>{moment(pedido.datahora_recebido).format("DD/MM/YYYY")}</Text>
                    <Divider my="5" />
                        {pedido.itens?.map((item, index) => {
                        console.log('index: ', index)
                        if (index == 0) { return (<Text fontSize='sm' mb={2}><Text bold> {item.quantidade}</Text>  {item.nome}</Text>) }
                        else { return (<Text color="gray.500" fontSize='sm' mb={5}>Mais {pedido.itens.length-1} itens</Text>)}
                        // <Text fontSize='sm' mb={5}><Text bold>{index+1} </Text>- R$ {(Number(item.valor) * item.quantidade).toLocaleString('pt-br', {minimumFractionDigits: 2})} ({item.quantidade} x R$ {(Number(item.valor)).toLocaleString('pt-br', {minimumFractionDigits: 2})}) - {item.nome}</Text>
                    })}
                    {/* <Text mb={5}>R$ {(pedido.valor_total).toLocaleString('pt-br', { minimumFractionDigits: 2 })}</Text> */}
                    <Divider mb="5" />
                    <HStack
                        flex={1}
                        alignContent="space-between"
                    >

                        <Button width="45%" backgroundColor={"blue.900"} size="sm" mx='3' onPress={()=> navigation.navigate('PedidoDescricao', {pedido: pedido})}>Mais detalhes</Button>
                        <Button width="45%" backgroundColor={"blue.900"} size="sm" mx='3'>Comprar novamente</Button>
                    </HStack>
                </VStack>


            </VStack>
            <Divider width="100%" mt={5} />
            {/* </Pressable> */}
        </VStack> : <></>
    )
}