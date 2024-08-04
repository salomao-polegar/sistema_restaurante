import { VStack, Image, Text, Box, Link, useToast } from 'native-base'
import Logo from './../assets/Logo.png'
import { TouchableOpacity } from 'react-native';
import { useEffect, useState } from 'react';
import { fazerLogin } from '@/servicos/autenticacaoServico';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { EntradaTexto } from '../components/Form/Entradas/EntradaTexto';
import { Titulo } from '../components/TItulo/Titulo';
import Botao from '../components/Botao/Botao';

// import { useParams }  from 'react-router-dom'

export default function Login({ route, navigation }:any) {
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [carregando, setCarregando] = useState(true)
  const toast = useToast();
  // const { emailParam } = useParams()

  useEffect(() => {
    
    // setEmail(String(emailParam))
    async function verificarLogin(){
      const token = await AsyncStorage.getItem('token')
      if (token) {
        navigation.replace("Tabs")
      }
      setCarregando(false)
    }
    verificarLogin()
  })

  async function login() {
    
    const resultado = await fazerLogin(email, senha)
    if (resultado){
      // AsyncStorage: armazena informações namemória do dispositivo
      const { access_token, user } = resultado
      AsyncStorage.setItem('token', access_token)
      AsyncStorage.setItem("userId", user.id)
      AsyncStorage.getItem("userId").then((item)=>console.log(item))
      navigation.navigate("Tabs")
    }
    else{
      toast.show({
        title: "Erro no login",
        description: "E-mail ou senha não conferem",
        backgroundColor: "red.500"
      })
    }

  }

  if (carregando){
    return null
  }
  return (
    // VStack: componente padrão do native base
    <VStack 
      flex={1} 
      alignItems="center" 
      p={5}
      justifyContent="center"
      >
      <Image source={Logo} alt="Logo Restaurante" />
      <Titulo>Faça login em sua conta!</Titulo>
      <Box>
        <EntradaTexto 
          label="E-mail" 
          placeholder='Insira eu endereço de e-mail'
          value={email}
          onChangeText={setEmail} />
        <EntradaTexto 
          label="Senha" 
          placeholder='Insira sua senha'
          value={senha}
          onChangeText={setSenha}
          secureTextEntry />
      </Box>
      <Botao
        onPress={login}        
      >
        Entrar
      </Botao>
      <Link href='https://www.alura.com.br' mt={2}>
        Esqueceu sua senha?
      </Link>

      <Box 
        w="100%" 
        flexDirection="row"
        justifyContent='center'
        mt={8}>
        <Text>Ainda não tem cadastro? </Text>
          <TouchableOpacity onPress={() => navigation.navigate('Cadastro')}>
            <Text color="blue.500">Faça seu cadastro!</Text>
          </TouchableOpacity>
      </Box>
    </VStack>
   );
}
