import { Image, Box, ScrollView, useToast, VStack } from 'native-base'
import Logo from './../assets/Logo.png'
import { useState } from 'react';
import { cadastrarCliente } from '@/servicos/clienteServico';
import { sha256 } from 'js-sha256';
import { secoes } from '@/src/utils/CadastroEntradaTexto';
import { Titulo } from '../components/TItulo/Titulo';
import { EntradaTexto } from '../components/Form/Entradas/EntradaTexto';
import Botao from '../components/Botao/Botao';

export default function Cadastro({ navigation }: any) {
  const [numSecao, setNumSecao] = useState(0);
  const [dados, setDados] = useState({} as any);
  // const [planos, setPlanos] = useState([] as number[])
  const toast = useToast();
  // Vamos criar seções com diferentes atributos 


  function avancarSecao() {
    if (numSecao < secoes.length - 1) {
      setNumSecao(numSecao + 1)
    }
    else {
      console.log(dados)
      // console.log(planos)
    }


  }

  function voltarSecao() {
    if (numSecao > 0) {
      setNumSecao(numSecao - 1)
    }
  }

  function voltarParaLogin() {
    navigation.navigate("Login")
  }

  function atualizarDados(id: string, valor: string) {
    setDados({ ...dados, [id]: valor })
  }

  async function cadastrar() {

    const resultado = await cadastrarCliente({
      cpf: dados.cpf,
      email: dados.email,
      nome: dados.nome,
      hashed_password: sha256(dados.senha),
      telefone: dados.telefone,
      endereco: dados.rua + dados.numero + dados.complemento + dados.bairro + dados.cidade + dados.estado,
      administrador: false

    })
    console.log(resultado)
    if (resultado?.response?.data?.detail) {
      console.log(resultado.response.data.detail)

      toast.show({
        title: "Erro no cadastro",
        description: resultado.response.data.detail,
        backgroundColor: "red.500"
      })
    } else if (!resultado) {
      toast.show({
        title: "Erro no cadastro",
        description: "Erro ao realizar cadastro",
        backgroundColor: "red.500"
      })
    }
    else {
      toast.show({
        title: "Sucesso",
        description: "Cadastro realizado com sucesso",
        backgroundColor: "green.500"
      })
      navigation.navigate("Login", {emailParam: dados.email})
    }
  }

  return (
    // VStack: componente padrão do native base, com tela fixa, sem rolagem
    <ScrollView
      flex={1}
      p={5}
    >
      <VStack
      flex={1} 
      alignItems="center" 
      p={5}>
      <Image source={Logo} alt="Logo Restaurante" mt={10} alignSelf="center" />
      <Titulo>
        {secoes[numSecao].titulo}
      </Titulo>
      <Box>
        {
          secoes[numSecao]?.entradaTexto?.map(entrada => {
            return (
              <EntradaTexto label={entrada.label} placeholder={entrada.placeholder} key={entrada.name}
                secureTextEntry={entrada.secureTextEntry}
                value={dados[entrada.name]}
                required={entrada.required}
                onChangeText={(text) => atualizarDados(entrada.name, text)} />
            )
          })
        }
      </Box>
      {/* <Box>
        {numSecao == 2 && <Text color="blue.800" fontWeight="bold" fontSize="md" mt={1} mb={4}>
          Selecione os planos:
        </Text>}
        {
          secoes[numSecao]?.checkbox?.map(checkbox => {
            return (
              <Checkbox 
                value={checkbox.value} 
                key={checkbox.id} 
                onChange={() => {
                  setPlanos((planosAnteriores) => {
                    if (planosAnteriores.includes(checkbox.id)) {
                      return planosAnteriores.filter((id) => id !== checkbox.id)
                    }
                    return [...planosAnteriores, checkbox.id]
                  })
                }}
                isChecked={planos.includes(checkbox.id)}
                >
                {checkbox.value}
              </Checkbox>)
          })
        }
      </Box> */}
      {numSecao > 0 && <Botao onPress={() => voltarSecao()} bgColor="gray.400">
        Voltar
      </Botao>}
      
      {secoes.length-1 == numSecao ? 
      <Botao onPress={cadastrar} mt={4}>Cadastrar</Botao> :
      <Botao onPress={() => avancarSecao()} mt={4}>Avançar</Botao>
      }

      <Botao onPress={() => voltarParaLogin()} mt={4} >Voltar para login</Botao>
      </VStack>
    </ScrollView>
  );
}
