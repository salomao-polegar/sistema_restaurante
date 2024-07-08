import { Avatar, Button, HStack, Text, VStack, useToast } from "native-base";

import Botao from "./Botao";
import { Titulo } from "./Titulo";
import { useEffect, useState } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Item } from "../interfaces/Item";
import { Ionicons } from "@expo/vector-icons";



export function CardCarrinho({ carregar_carrinho }: any) {

  const [carrinho, setCarrinho] = useState<Item[]>([])
  const toast = useToast();


  const remover = async (id: number) => {


    setCarrinho(carrinho => carrinho.filter(item => item.produto.id != id))

    await AsyncStorage.setItem('carrinho', JSON.stringify(carrinho)).then(() => console.log(carrinho))
    carregar_carrinho()
  }

  const esvaziarCarrinho = async () => {
    setCarrinho([])
    await AsyncStorage.removeItem('carrinho')
  }
  const realizarPedido = async () => {
    toast.show({
      title: "Realizando pedido",
      description: "Aguarde",
      backgroundColor: "yellow.500"
    })
  }
  return (
    <VStack w="100%" bg="white" p="5" borderRadius="lg" shadow={2} mb={5} px="10">
      <Titulo color="blue.800" mb={10}>Carrinho</Titulo>
      <HStack justifyContent="space-around" alignItems="center">
        <Botao onPress={esvaziarCarrinho} w="49%" bgColor="blue.800">
          <HStack justifyContent="space-between">
            <Text color="white" fontSize="md" alignContent="center">Esvaziar carrinho   </Text>
            <Ionicons name="trash" color="white" size={30} />
          </HStack>
        </Botao>
        {carrinho.length != 0 ?
          <Botao w="49%" bgColor="blue.800" onPress={realizarPedido}>
            <HStack justifyContent="space-between"  >
              <Text color="white" fontSize="md" alignContent="center">Realizar pedido   </Text>
              <Ionicons name="send" color="white" size={30} />
            </HStack></Botao> : <></>
        }
      </HStack>
      <Text color="blue.800" mt={5} bold fontSize="md">Itens adicionados</Text>


      {carrinho.map((item) => (
        <HStack key={item.produto.id} pt={10}>
          <Avatar></Avatar>
          <VStack>
            <Text bold>{item.produto.nome}</Text>
            <Text>{item.produto.descricao}</Text>
            <Text>R$ {item.produto.valor * Number(item.quantidade)}</Text>
            <Botao mt={5}>Realizar pedido</Botao>

          </VStack>

          <Button w={20} h="8" onPress={() => remover(item.produto.id)}>Remover</Button>


        </HStack>
      ))}

    </VStack>


  )
}