import api from "./api"

export async function fazerLogin(username:string, password:string) {
    if (!username || !password) return null
        
    try {
        var formdata = new FormData();
        
        formdata.append('username', username)
        formdata.append('password', password)
        
        
        console.log(formdata)


        // ##################### NÃO FUNCIONA NO CELULAR ;(
        // Não identifica o Form Data (nem envia a requisição para o servidor)
        const resultado = await api.post('/token/', formdata)
        // Sem o formdata ele envia a requisição
        // FUNCIONA NO COMPUTADOR
        console.log(resultado.data)
        return resultado.data

    } catch (error: any){
        if (error.response) {
          // A requisição foi feita e o servidor respondeu com um código de status
          // que sai do alcance de 2xx
          console.log("ERROR.RESPONSE")
          console.log("\nData\n")
          console.error(error.response.data);
          console.log("\nStatus\n")
          console.error(error.response.status);
          console.log("\nHeaders\n")
          console.error(error.response.headers);
        } else if (error.request) {
          // A requisição foi feita mas nenhuma resposta foi recebida
          // `error.request` é uma instância do XMLHttpRequest no navegador e uma instância de
          // http.ClientRequest no node.js
          console.log("\nERROR.REQUEST\n")
          console.error(error.request);
        } else {
          // Alguma coisa acontenceu ao configurar a requisição que acionou este erro.
          console.log("\nERROR.MESSAGE\n")
          console.error('Error', error.message);
        }
        console.log("\nERROR.CONFIG\n")
        console.error(error.config);
      }
        return null
    }
    
