import { Cliente } from "@/src/interfaces/Cliente";
import api from "./api";



export async function cadastrarCliente(cliente: Cliente) {
    if (!cliente) return null;
    console.log(cliente)
    try {
        const resultado = await api.post('/clientes/', cliente)
        console.log(resultado.data)
        return resultado.data
    }
    catch (error) {

        console.log(error)
        return error
    }
}

export async function pegarDadosClienteLogado(id: string) {
    try {
        const resultado = await api.get(`/clientes/${id}`)
        return resultado.data
    }
    catch (error) {
        console.log(error)
        return null
    }
}

export async function retornarHistoricoCliente(id: string) {

    try {
        const resultadoRequest = await api.get(`/clientes/${id}/pedidos`)
        console.log(resultadoRequest.data)
        return resultadoRequest.data
    }
    catch (error) {
        console.log(error)
        return null
    }
}
