import { Produto } from "./Produto"

export interface Item{
    id?: number
    nome?: string
    valor?: number
    produto: Produto
    quantidade: number
    
}