import api from "./api"

export async function fazerLogin(username:string, password:string) {
    if (!username || !password) return null
        
    try {
        var formdata = new FormData();
        formdata.append('username', username)
        formdata.append('password', password)
        formdata.append('grant_type', "password")
    
        const resultado = await api.post('/token', formdata)
        console.log(resultado.data)
        return resultado.data

    } catch (error) {
        console.log(error)
        return null
    }
    
}