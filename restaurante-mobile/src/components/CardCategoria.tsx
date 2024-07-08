import {  Button, Text, VStack } from "native-base";

interface CardCategoriaProps {
    texto: string;
}

export function CardCategoria({
    texto,
}: CardCategoriaProps) {
    return (
        <VStack >
            <Button w="95%" bg="white" mx="2%" shadow={2} borderRadius={3}>
                <Text
                    fontFamily="Inter"
                    fontSize="lg"
                    bold
                >{texto}</Text>
            </Button>
        </VStack>
    )
}