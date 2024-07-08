export interface Cliente {
    cpf: string
    nome: string
    email: string
    
    hashed_password: string
    telefone: string
    endereco: string
    administrador: boolean
}