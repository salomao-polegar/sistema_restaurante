import { NativeBaseProvider, StatusBar } from 'native-base'

import { TEMAS } from '@/src/estilos/temas';
import Rotas from '@/src/Rotas/Rotas';


// import Cadastro from '@/src/Cadastro';

export default function HomeScreen() {

  return (
    <NativeBaseProvider theme={TEMAS}>
      {/* Altera a cor da StatusBar */}
      <StatusBar backgroundColor={TEMAS.colors.blue[800]} /> 

      <Rotas />
    </NativeBaseProvider>
    
  );
}
