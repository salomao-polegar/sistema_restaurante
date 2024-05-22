import { Image, Text, Box, Checkbox, ScrollView } from 'native-base'
import Logo from './assets/Logo.png'
import { secoes } from './utils/CadastroEntradaTexto';
import { Titulo } from './components/Titulo';
import { EntradaTexto } from './components/EntradaTexto';
import { useState } from 'react';
import Botao from './components/Botao';

export default function Cadastro() {
  const [numSecao, setNumSecao] = useState(0);
  const [dados, setDados] = useState({} as any);
  // Vamos criar seções com diferentes atributos 
 

  function avancarSecao() {
    if(numSecao < secoes.length-1){
      setNumSecao(numSecao+1) 
    }
    else{
      console.log(dados)
    }

    
  }

  function voltarSecao() {
    if (numSecao > 0){
      setNumSecao(numSecao-1)
    }
  }

  function atualizarDados(id: string, valor: string) {
    setDados({...dados, [id]: valor})
  } 

  return (
    // VStack: componente padrão do native base, com tela fixa, sem rolagem
    <ScrollView 
      flex={1} 
      
      p={5}
      
      >
      <Image source={Logo} alt="Logo Restaurante" mt={10} alignSelf="center" />
      <Titulo>
        {secoes[numSecao].titulo}
      </Titulo>
      <Box>
        {
          secoes[numSecao]?.entradaTexto?.map(entrada => {
            return <EntradaTexto label={entrada.label} placeholder={entrada.placeholder} key={entrada.id}
              secureTextEntry={entrada.secureTextEntry}
              value={dados[entrada.label]}
              onChangeText={(text)=> {atualizarDados(entrada.label, text)}} />
          })
        }
      </Box>
      <Box>
        {numSecao == 2 && <Text color="blue.800" fontWeight="bold" fontSize="md" mt={1} mb={4}>
          Selecione os planos:
        </Text>}
        {
          secoes[numSecao]?.checkbox?.map(checkbox => {
            return <Checkbox value={checkbox.value} key={checkbox.id} >
              {checkbox.value}
            </Checkbox>
          }) 
        }
      </Box>
      {numSecao > 0 && <Botao onPress={() => voltarSecao()} bgColor="gray.400">
        Voltar
      </Botao>}
      <Botao onPress={() => avancarSecao()} mt= {4} mb={20}>
        Avançar
      </Botao>
      
    </ScrollView>
   );
}
