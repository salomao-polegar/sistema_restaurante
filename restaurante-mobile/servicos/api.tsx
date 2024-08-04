import axios from "axios";

const api = axios.create({
    // baseURL: "http://172.31.99.185/"
    // baseURL: "http://localhost/", 
    baseURL: "http://192.168.15.7/",
    // baseURL: "http://192.168.15.7:31000/",
    headers: {"Access-Control-Allow-Origin" : "*"}
    //Não podemos usar o localhost na URL pois, ao testar no Android, ele cria um emulador com outra rede
    // Usamos então o IP do computador
})

export default api;