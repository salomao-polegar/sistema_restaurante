import api from "./api"

export async function retornarProdutos() {
    try {
        const resultado = await api.get('/produtos')
        return resultado.data
    } catch (error) {
        console.log(error)
        return null
    }
} 