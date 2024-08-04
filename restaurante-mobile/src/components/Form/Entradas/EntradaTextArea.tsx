import { Input, FormControl } from "native-base";

interface InputProps {
  label?: string;
  placeholder: string;
  secureTextEntry?: boolean;
  value?: string;
  required?: boolean;
  readonly?: boolean;
  disabled?: boolean;
  w?: string | number;
  
  
  onChangeText?: (text: string) => void;
}

export function EntradaTextArea ({ 
  label, 
  placeholder, 
  secureTextEntry = false,
  value,
  required = false,
  readonly = false,
  disabled = false,
  w = "100%",
  
  onChangeText,
  

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
        readOnly={readonly}
        isDisabled={disabled}
        multiline
        numberOfLines={5}
        verticalAlign={"top"}
        textAlignVertical="top"

        
      />
    </FormControl>
  );
};