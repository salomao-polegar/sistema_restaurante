import { VStack, Image, Text, Box, FormControl, Input, Button, Link, useToast } from 'native-base'
import Logo from './assets/Logo.png'
import { TouchableOpacity } from 'react-native';
import { Titulo } from './components/Titulo';
import { EntradaTexto } from './components/EntradaTexto';
import { useEffect, useState } from 'react';
import { fazerLogin } from '@/servicos/autenticacaoServico';
import { jwtDecode } from 'jwt-decode';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function Login({ navigation }:any) {
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const [carregando, setCarregando] = useState(true)
  const toast = useToast();
  
  useEffect(() => {
    AsyncStorage.removeItem('token')
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
      const { token } = resultado
      AsyncStorage.setItem('token', token)
      const tokenDecodificado = jwtDecode(token) as any
      const pacienteId = tokenDecodificado.id
      AsyncStorage.setItem("pacienteId", pacienteId)
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
      <Button
        w="100%"
        bg="blue.800"
        mt="10"
        borderRadius="lg"
        onPress={login}
      >
        Entrar
      </Button>
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
