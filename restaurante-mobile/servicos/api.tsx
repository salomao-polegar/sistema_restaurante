import axios from "axios";

const api = axios.create({
    baseURL: "http://172.31.99.185/"
    //Não podemos usar o localhost na URL pois, ao testar no Android, ele cria um emulador com outra rede
    // Usamos então o IP do computador
})

export default api;