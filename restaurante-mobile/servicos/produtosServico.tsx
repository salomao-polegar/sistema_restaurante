import { Produto } from "@/src/interfaces/Produto"
import api from "./api"

export async function retornarProdutos() {
    try {
        const response = await api.get('/produtos')
            const resultado: [Produto] = response.data.sort((a:Produto,b:Produto) => a.categoria - b.categoria)
            console.log("sort: ", resultado)
            return resultado
        
    } catch (error) {
        console.log(error)
        return null
    }
} 