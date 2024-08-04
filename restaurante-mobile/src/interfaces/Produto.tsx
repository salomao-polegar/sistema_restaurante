
export interface Produto {
    id?: number;
    nome: string;
    categoria: number;
    foto_principal?: number;
    descricao: string;
    valor: number;
    ativo?: boolean;
}