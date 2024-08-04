import { VStack, ScrollView, Avatar, useToast, HStack } from "native-base";
import { useState } from "react";
import { EditarProdutoAPI, DeletarProdutoAPI, IncluirFotoAPI } from "@/servicos/produtoServico";
import { ImagePickerResponse } from "react-native-image-picker";
import { Titulo } from "@/src/components/TItulo/Titulo";
import { EntradaTexto } from "@/src/components/Form/Entradas/EntradaTexto";
import { EntradaTextArea } from "@/src/components/Form/Entradas/EntradaTextArea";
import { EntradaSelect } from "@/src/components/Form/Entradas/EntradaSelect";
import { EntradaImagem } from "@/src/components/Form/Entradas/EntradaImagem";
import Botao from "@/src/components/Botao/Botao";

export interface ColourOption {
  readonly value: string;
  readonly label: string;
  readonly color: string;
  readonly isFixed?: boolean;
  readonly isDisabled?: boolean;

}


export default function EditarProduto({ route, navigation }: any) {

  const { produto, carregarProdutos, titulo } = route.params;
  console.log("ProdutoParam: ")
  const [selectedImage, setSelectedImage] = useState<ImagePickerResponse>();
  console.log(produto)
  const [nomeProduto, setNomeProduto] = useState(produto.nome)
  const [descricaoProduto, setDescricaoProduto] = useState(produto.descricao)
  const [valorProduto, setValorProduto] = useState(produto.valor.toString())
  const idProduto = produto.id.toString()
  const [categoriaProduto, setCategoriaProduto] = useState(produto.categoria.toString())
  const toast = useToast();
  

  async function editar() {

    const resultado = await EditarProdutoAPI({
      id: idProduto,
      nome: nomeProduto,
      descricao: descricaoProduto,
      valor: valorProduto,
      categoria: Number(categoriaProduto)
    })

    if (resultado?.response?.data?.detail) {
      console.log(resultado.response.data.detail)

      toast.show({
        title: "Erro ao editar produto",
        description: resultado.response.data.detail,
        backgroundColor: "red.500"
      })
    } else if (!resultado) {
      toast.show({
        title: "Erro",
        description: "Erro ao editar produto",
        backgroundColor: "red.500"
      })
    }
    else {
      console.log("Iniciando foto")
      const resultado = await IncluirFotoAPI(selectedImage)

      if (resultado?.response?.data?.detail) {
        console.log(resultado.response.data.detail)

        toast.show({
          title: "Erro ao editar produto",
          description: resultado.response.data.detail,
          backgroundColor: "red.500"
        })
      } else if (!resultado) {
        toast.show({
          title: "Erro",
          description: "Erro ao editar produto",
          backgroundColor: "red.500"
        })
      }
      else {
        console.log("resultado", resultado)
        toast.show({
          title: "Sucesso",
          description: "Edição realizada",
          backgroundColor: "green.500"
        })
        await carregarProdutos()
      }

    }
  }


    async function deletar() {

      const resultado = await DeletarProdutoAPI(String(idProduto))

      console.log("Deletado: ")
      console.log(resultado)

      if (resultado?.response?.data?.detail) {
        console.log(resultado.response.data.detail)

        toast.show({
          title: "Erro",
          description: resultado.response.data.detail,
          backgroundColor: "red.500"
        })
      } else if (!resultado) {
        toast.show({
          title: "Erro",
          description: "Erro ao deletar produto",
          backgroundColor: "red.500"
        })
      }
      else {
        toast.show({
          title: "Sucesso",
          description: "Deletado com sucesso",
          backgroundColor: "green.500"
        })
        await carregarProdutos()
      }

    }

    return (
      <ScrollView flex={1} p={5}>

        <VStack
          flex={1}
          mx={10}
          p={10}
          alignSelf="center"
          w="100%"
          maxW={800}
        >

          <Titulo>
            {titulo}
          </Titulo>

          {idProduto && (<EntradaTexto
            label="Id"
            placeholder="Id"
            key="id"
            value={idProduto}
            required
            readonly
            disabled
          />)}

          <EntradaTexto
            label="Nome"
            placeholder="Nome"
            key="nome"
            value={nomeProduto}
            required
            onChangeText={(text) => setNomeProduto(text)} />

          <EntradaTextArea
            label="Descrição"
            placeholder="Descrição"
            key="descricao"
            value={descricaoProduto}
            required
            onChangeText={(text) => setDescricaoProduto(text)} />

          <EntradaTexto
            label="Valor"
            placeholder="Valor"
            key="valor"
            value={valorProduto}
            required
            onChangeText={(text) => setValorProduto(text)} />

          <EntradaSelect
            label="Categoria"
            key="categoria"
            value={categoriaProduto}
            onValueChange={(itemValue) => setCategoriaProduto(itemValue)} />

          <EntradaImagem
            label="Foto principal"
            selectedImage={selectedImage}
            setSelectedImage={setSelectedImage}
            fotoPrincipal={produto.foto_principal}
            required
             />

         

          <HStack justifyContent="space-between">

            {(idProduto != 0) ? <Botao w="48%" onPress={editar} >Editar</Botao> : <Botao w="48%" onPress={editar} >Adicionar</Botao>}
            <Botao w="48%" onPress={() => { navigation.navigate("Tabs") }} >Voltar</Botao>
          </HStack>
          {(idProduto != 0) && <Botao w="100%" bg="red.800" mt={5} onPress={deletar} maxW={500}>Deletar</Botao>}
        </VStack>
      </ScrollView>
    )
}