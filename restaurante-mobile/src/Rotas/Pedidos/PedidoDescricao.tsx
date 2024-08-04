import { Avatar, Divider, HStack, ScrollView, Text, VStack } from "native-base";
import moment from "moment";
import { useEffect, useState } from "react";
import { Pressable } from "react-native";
import { Item } from "@/src/interfaces/Item";
import { Titulo } from "@/src/components/TItulo/Titulo";
import Botao from "@/src/components/Botao/Botao";

export function PedidoDescricao({ route, navigation }: any) {

    const { pedido } = route.params
    const [subTotal, setSubTotal] = useState(0)
    console.log(pedido.id)


    function calcularSubtotal() {
        let subtotal = 0
        pedido.itens.forEach((item: Item) => {
            subtotal += Number(item.valor) * Number(item.quantidade)
        })
        setSubTotal(subtotal);
    }

    useEffect(() => {
    
        calcularSubtotal();
        
      }, [])



    const CardItemPedido = (item: Item) => {
        const totalItem = Number(item.valor) * Number(item.quantidade)

        return (<HStack p={1} >

            <Avatar

                size="lg" />

            <VStack w="80%" pl='18'>
                <HStack justifyContent="space-between">
                    <Text fontSize="md" bold>{item.nome}</Text>
                    <Text pt={2} fontSize='md'>R$ {(totalItem).toLocaleString('pt-br', { minimumFractionDigits: 2 })}</Text>
                </HStack>
                <Text pt={2} textAlign="justify">{item.nome}</Text>

                <Text pt={2} fontSize='md'><Text bold>5x</Text> R$ {Number(item.valor).toLocaleString('pt-br', { minimumFractionDigits: 2 })}</Text>



            </VStack>


        </HStack>)
    }
    return (
        <ScrollView >
            <Titulo my={5} color="blue.800" fontSize='xl'>DETALHES DO PEDIDO</Titulo>
            <VStack w="90%" bg="white" px="10" borderRadius="lg" shadow={2}
        
                flex={1}
               
                alignSelf="center"
                
                maxW={800}>
            

            <Text mt={5} fontSize='lg' bold>Pedido nº {pedido.id} - {moment(pedido.datahora_recebido).format("DD/MM/YYYY")}</Text>
            <Pressable><Text fontSize='md' color="red.500" bold>Ver cardápio</Text></Pressable>



            <Divider my={5} />
            {pedido.itens?.map((item: Item) => {
                console.log('pedido')
                console.log(pedido)
                return (<>
                    <CardItemPedido produto={item.produto} quantidade={item.quantidade} nome={item.nome} valor={item.valor} ></CardItemPedido>
                    <Divider width="100%" my={5} />
                </>)

            })}


            <Text bold fontSize="md">Resumo dos valores</Text>
            <HStack justifyContent="space-between">
                <Text fontSize="sm">Subtotal</Text>
                <Text>R$ {subTotal.toLocaleString('pt-br', { minimumFractionDigits: 2 })}</Text>
            </HStack>

            <HStack justifyContent="space-between">
                <Text fontSize="sm">Taxa de entrega</Text>
                { Number.isNaN(Number(pedido.taxa_entrega)) ? <Text color="green.700" bold>Grátis</Text> : <Text>{Number(pedido.taxa_entrega)}</Text>}
                
            </HStack>
            <HStack justifyContent="space-between">
                <Text bold fontSize="md">Total</Text>
                { Number.isNaN(Number(pedido.taxa_entrega)) ? <Text bold>R$ {subTotal.toLocaleString("pt-br", {minimumFractionDigits: 2})}</Text> : <Text bold>R$ {subTotal + pedido.taxa_entrega}</Text>}
                
            </HStack>
            <Divider width="100%" my={5} />
            <Text bold fontSize="md">Endereço de entrega</Text>
            <Text mt={1} fontSize="sm">Avenida Antártica, 2000</Text>
            <Text mt={1} fontSize="sm">Sumaré, São Paulo/SP</Text>

            <HStack justifyContent="space-between" mb={10}>
                <Botao width="45%">Adicionar ao carrinho</Botao>
                <Botao width="45%" onPress={()=>navigation.navigate("Tabs")}>Voltar</Botao>
                </HStack>


</VStack>
        </ScrollView>


    )
}