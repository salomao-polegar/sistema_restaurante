import { EntradaTexto } from "../components/Form/Entradas/EntradaTexto"



const secoes = [
    {
      id: 1,
      titulo: "Insira seus dados básicos:",
      entradaTexto: [
        {
          id: 1,
          label: "Nome",
          placeholder: 'Digite seu nome',
          secureTextEntry:false,
          name: "nome",
          required:true
          
        },
        {
          id: 2,
          label: "Email",
          placeholder: 'Digite seu e-mail',
          secureTextEntry:false,
          name: "email",
          required:true
        },
        {
          id: 3,
          label: "Senha",
          placeholder: 'Crie uma senha',
          secureTextEntry:true,
          name: "senha",
          required:true
        },
        {
          id: 4,
          label: "Confirme sua senha",
          placeholder: 'Insira sua senha',
          secureTextEntry:true,
          name: "confirmaSenha",
          required:true
        },
        {
          id: 5,
          label: "CPF",
          placeholder: 'Insira seu CPF',
          name: "cpf",
          required:true
        },
      ],
      checkbox: []
    },
    {
      id: 2,
      titulo: "Agora, mais alguns dados sobre você:",
      entradaTexto: [
        {
          id: 1,
          label: "CEP",
          placeholder: 'Insira seu CEP',
          secureTextEntry:false,
          name: "cep",
          required:false
        },
        {
          id: 2,
          label: "Rua",
          placeholder: 'Nome da rua',
          secureTextEntry:false,
          name: "rua",
          required:false
        },
        {
          id: 3,
          label: "Número",
          placeholder: 'Insira seu número',
          secureTextEntry:false,
          name: "numero",
          required:false
        },
        {
          id: 4,
          label: "Bairro",
          placeholder: 'Insira seu número',
          secureTextEntry:false,
          name: "bairro",
          required:false
        },
        {
          id: 5,
          label: "Cidade",
          placeholder: 'Insira seu número',
          secureTextEntry:false,
          name: "cidade",
          required:false
        },
        {
          id: 6,
          label: "Estado",
          placeholder: 'Insira seu complemento',
          secureTextEntry:false,
          name: "estado",
          required:false
        },
        {
          id: 7,
          label: "Telefone",
          placeholder: '(00) 00000-0000',
          secureTextEntry:false,
          name: "telefone",
          required:false
        },
      ],
      checkbox: []
    },
    // {
    //   id: 3,
    //   titulo: "Para finalizar, qual seu plano de saúde?",
    //   EntradaTexto: [],
    //   checkbox: [
    //     {
    //       id: 1,
    //       value: "Sulamerica"
    //     },
    //     {
    //       id: 2,
    //       value: "Unimed"
    //     },
    //     {
    //         id: 3,
    //         value: "Bradesco"
    //       },
    //       {
    //         id: 4,
    //         value: "Amil"
    //       },
    //       {
    //         id: 5,
    //         value: "Biosaúde"
    //       },
    //       {
    //         id: 6,
    //         value: "Biovida"
    //       },
    //       {
    //         id: 7,
    //         value: "Outros"
    //       },
       
    //   ]
    // }
  ]

  export {secoes}