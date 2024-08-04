import api from "@/servicos/api";
import { useToast, View, Button, Avatar, HStack, ArrowForwardIcon, VStack } from "native-base";
import { Dispatch, SetStateAction } from "react";
import { ImagePickerResponse, launchImageLibrary } from "react-native-image-picker";
import Botao from "../../Botao/Botao";

interface InputProps {
  label?: string;
  required?: boolean;
  w?: string | number;
  selectedImage: ImagePickerResponse | undefined;
  setSelectedImage: Dispatch<SetStateAction<ImagePickerResponse | undefined>>
  fotoPrincipal: string | null

}

export function EntradaImagem({
  label,
  required = false,
  w = "100%",
  selectedImage,
  setSelectedImage,
  fotoPrincipal: foto_principal = null

}: InputProps): JSX.Element {

  const toast = useToast();

  const handleChooseImage = () => {
    launchImageLibrary({ mediaType: "photo" }, (response) => {
      if (response.didCancel) {
        toast.show({
          title: 'Ação cancelada',
        });
      } else if (response.errorCode) {
        toast.show({
          title: 'Erro ao escolher imagem',

        });
      } else {

        setSelectedImage(response)

        //setImageUri();
      }
    });
  };

  return (
    <View style={{ padding: 20 }}>
      <Button onPress={handleChooseImage} my={5}>Escolher Imagem</Button>
      <HStack justifyContent={"space-around"} alignItems={"center"}>
        {foto_principal && (
          <Avatar
            source={{ uri: api.getUri() + "foto/" + foto_principal + "/" }}
            size={"2xl"}
            alignSelf="center"
            opacity={selectedImage ? "40%" : "100%"}
          />
        )}
        
        {selectedImage && (<>
          <ArrowForwardIcon size={10} />
          <VStack>
          <Avatar
            source={{ uri: selectedImage.assets ? selectedImage.assets[0].uri : "" }}
            size={"2xl"}
            
          />
          <Botao mt={2} bg="red.700">Remover imagem</Botao>
          </VStack>
          </>
        )}

      </HStack>

    </View>
    // <FormControl mt={3}>
    //   {label && <FormControl.Label>{label}</FormControl.Label>}
    //   <Input
    //     type="undefined"
    //     placeholder={placeholder}
    //     size="lg"
    //     w={w}
    //     borderRadius="lg"
    //     bgColor="gray.100"
    //     secureTextEntry={secureTextEntry}
    //     shadow={3}
    //     value={value}
    //     onChangeText={onChangeText}
    //     isRequired={required}
    //   />
    // </FormControl>
  );
};