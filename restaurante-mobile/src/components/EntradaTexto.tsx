import { Input, FormControl } from "native-base";

interface InputProps {
  label?: string;
  placeholder: string;
  secureTextEntry?: boolean;
  value?: string;
  required?: boolean;
  w?: string | number;
  
  onChangeText?: (text: string) => void;
}

export function EntradaTexto ({ 
  label, 
  placeholder, 
  secureTextEntry = false,
  value,
  required = false,
  w = "100%",
  
  onChangeText

} : InputProps) : JSX.Element {
  return (
    <FormControl mt={3}>
      {label && <FormControl.Label>{label}</FormControl.Label>}
      <Input
        placeholder={placeholder}
        size="lg"
        w={w}
        borderRadius="lg"
        bgColor="gray.100"
        secureTextEntry={secureTextEntry}
        shadow={3}
        value={value}
        onChangeText={onChangeText}
        isRequired={required}
      />
    </FormControl>
  );
};