import { VStack, Text, ScrollView, useToast, View, Select, Checkbox, HStack } from "native-base";

import lanche1 from "../assets/lanche3.jpg"
import { useEffect, useState } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Item } from "../interfaces/Item";
import { CardDescricaoProduto } from "../components/Cards/Produto/CardDescricaoProduto";
import { EntradaTexto } from "../components/Form/Entradas/EntradaTexto";
import Botao from "../components/Botao/Botao";

export interface ColourOption {
  readonly value: string;
  readonly label: string;
  readonly color: string;
  readonly isFixed?: boolean;
  readonly isDisabled?: boolean;
}


export default function ProdutoDescricao({ route, navigation }: any) {

  const { produto } = route.params
  const toast = useToast();

  const [carrinho, setCarrinho] = useState<Item[]>([])
  const [item, setItem] = useState<Item>({ produto: produto, quantidade: 0 })

  useEffect(() => {
    // Fetch data from AsyncStorage

    const carregar_carrinho = async () => {
      try {
        const carrinho = await AsyncStorage.getItem('carrinho');
        if (carrinho !== null) {
          setCarrinho(JSON.parse(carrinho));
        }
      } catch (error) {
        console.error('Erro carregando carrinho', error);
      }
    };
    carregar_carrinho();
  }, []);

  const adicionar_ao_carrinho = async () => {



    try {
      if (item.quantidade == 0) {
        toast.show({
          title: "Quantidade inválida",
          description: "Digite um número válido.",
          backgroundColor: "red.500",

        })
        return
      }
      // let novoCarrinho: Item[] = []
      // let itemAtualizado = item
      //   function atualizar_carrinho(){
      //     carrinho.forEach((itemCarrinho) => {

      //     if (itemCarrinho.produto.id == itemAtualizado.produto.id) {
      //       itemAtualizado.quantidade += itemCarrinho.quantidade
      //       novoCarrinho.push(itemAtualizado)
      //     }
      //     else novoCarrinho.push(itemCarrinho)
      //   })
      // }
      //   atualizar_carrinho()

      //   console.log(novoCarrinho)
      console.log(item)
      console.log(carrinho)
      setCarrinho([...carrinho, item]);
      await AsyncStorage.setItem('carrinho', JSON.stringify(carrinho))
      console.log( AsyncStorage.getItem('carrinho').then((response) => console.log(response)));
      
      
      setItem({ produto: produto, quantidade: 0 })
      toast.show({
        title: "Adicionado",
        description: "Produto adicionado ao carrinho",
        backgroundColor: "green.800"
      })
      // navigation.navigate("Tabs")
    } catch (error) {
      console.error('Erro adicionando ao carrinho: ', error);
    }


  }



  return (
    <ScrollView flex={1}>
      <VStack

        flex={1}
        
        mx={10}
        p={10}

        alignSelf="center"
        w="100%"
        maxW={800}
      >


        <CardDescricaoProduto produto={produto} navigation={navigation} imagem={lanche1} />



        <EntradaTexto label="Quantidade" placeholder="Quantidade" w="30%" value={String(item.quantidade)}
          onChangeText={(text) => { setItem({ produto: item.produto, quantidade: Number(text) }) }}
           />
        <HStack justifyContent="space-between">
          
          <Botao w="48%" onPress={adicionar_ao_carrinho}>Adicionar ao carrinho</Botao>
          <Botao w="48%" onPress={() => { navigation.navigate("Tabs") }} >Voltar</Botao>
        </HStack>

      </VStack>
    </ScrollView>
  )
}