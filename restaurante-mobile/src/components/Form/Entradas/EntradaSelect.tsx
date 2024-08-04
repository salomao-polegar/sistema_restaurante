import { Input, FormControl, useToast, View, Button, Image, Select, CheckIcon, WarningOutlineIcon, Center, Box } from "native-base";
import { useState } from "react";
import { launchImageLibrary } from "react-native-image-picker";

interface InputProps {
  label?: string;
  value: string;
  onValueChange?: (text: string) => void;
}

export function EntradaSelect({
  label,
  value,
  onValueChange
}: InputProps): JSX.Element {
  


  return (
    <Center>
      <Box maxW="300"></Box>
    <FormControl mt={3}>
      {label && <FormControl.Label>{label}</FormControl.Label>}
      <Select
        selectedValue={value}
        minWidth="200"
        accessibilityLabel="Selecione a categoria"
        placeholder="Selecione a categoria"
        _selectedItem={{
          bg: "teal.600",
          endIcon: <CheckIcon size="5" />
        }}
        mt={1}
        onValueChange={onValueChange}>
        <Select.Item label="Lanche" value="1" />
        <Select.Item label="Acompanhamento" value="2" />
        <Select.Item label="Bebida" value="3" />
        <Select.Item label="Sobremesa" value="4" />
      </Select>
    </FormControl>
    </Center>
    

  );
};