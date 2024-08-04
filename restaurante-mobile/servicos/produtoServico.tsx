import { Cliente } from "@/src/interfaces/Cliente";
import api from "./api";
import { Produto } from "@/src/interfaces/Produto";
import { ImagePickerResponse } from "react-native-image-picker";
import { Platform } from "react-native";


export async function IncluirFotoAPI(foto: ImagePickerResponse | undefined) {
    if (!foto) return null;
    
    try {
        const data = new FormData();

        if (foto.assets) {
            console.log("base64: ", foto.assets[0].uri)
            const resultado = await api.post('/foto/', {img_bytes: foto.assets[0].uri})
            console.log(resultado.data)
            return resultado.data
        }
    }
    catch (error) {
        console.log(error)
        return null
    }
}

export async function EditarProdutoAPI(produto: Produto) {
    if (!produto) return null;
    try {
        const resultado = await api.put('/produtos/', produto)
        console.log(resultado.data)
        return resultado.data
    }
    catch (error) {

        console.log(error)
        return error
    }
}

export async function CadastrarProdutoAPI(produto: Produto) {
    if (!produto) return null;
    console.log("Produto:")
    console.log(produto)
    try {
        const resultado = await api.post('/produtos/', produto)
        console.log(resultado.data)
        return resultado.data
    }
    catch (error) {

        console.log(error)
        return error
    }
}

export async function DeletarProdutoAPI(produto: string) {
    if (!produto) return null;
    console.log("Produto:")

    try {
        const resultado = await api.delete('/produtos/' + produto)
        console.log(resultado.data)
        return resultado.data
    }
    catch (error) {

        console.log(error)
        return error
    }
}

export async function ativarProdutoAPI(produto: string) {
    if (!produto) return null;
    console.log("Produto:")

    try {
        const resultado = await api.delete('/produtos/' + produto)
        console.log(resultado.data)
        return resultado.data
    }
    catch (error) {

        console.log(error)
        return error
    }
}
