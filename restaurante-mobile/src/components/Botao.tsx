import { Button } from "native-base";

export default function Botao ({...rest}){
    return (
        <Button
            w="100%"
            bg="blue.800"
            mt="10"
            borderRadius="lg"
            maxW={300}
            justifyContent="center"
            alignItems="center"
            {...rest} />
    )
}