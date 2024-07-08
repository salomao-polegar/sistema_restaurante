import { Item } from "./Item";

export interface Pedido {
    id: string;
    statusPedido: number
    cliente: number
    datahora_recebido: Date
    datahora_preparacao: Date
    datahora_pronto: Date
    datahora_finalizado: Date
    status_pagamento: number
    id_pagamento: string
    valor_total: number
    itens: Item[]
    taxa_entrega: number
}