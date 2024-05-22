
const secoes = [
    {
      id: 1,
      titulo: "Insira seus dados básicos:",
      entradaTexto: [
        {
          id: 1,
          label: "Nome",
          placeholder: 'Digite seu nome completo',
          secureTextEntry:false
          
        },
        {
          id: 2,
          label: "Email",
          placeholder: 'Digite seu e-mail',
          secureTextEntry:false
        },
      ]
    },
    {
      id: 2,
      titulo: "Agora, mais alguns dados sobre você:",
      entradaTexto: [
        {
          id: 1,
          label: "CEP",
          placeholder: 'Insira seu CEP',
          secureTextEntry:false
        },
        {
          id: 2,
          label: "Endereço",
          placeholder: 'Insira seu endereço',
          secureTextEntry:false
        },
        {
          id: 3,
          label: "Número",
          placeholder: 'Insira seu número',
          secureTextEntry:false
        },
        {
          id: 4,
          label: "Complemento",
          placeholder: 'Insira seu complemento',
          secureTextEntry:false
        },
        {
          id: 5,
          label: "Telefone",
          placeholder: '(00) 00000-0000',
          secureTextEntry:false
        },
      ]
    },
    {
      id: 3,
      titulo: "Para finalizar, qual seu plano de saúde?",
      checkbox: [
        {
          id: 1,
          value: "Sulamerica"
        },
        {
          id: 2,
          value: "Unimed"
        },
        {
            id: 3,
            value: "Bradesco"
          },
          {
            id: 4,
            value: "Amil"
          },
          {
            id: 5,
            value: "Biosaúde"
          },
          {
            id: 6,
            value: "Biovida"
          },
          {
            id: 7,
            value: "Outros"
          },
          {
            id: 8,
            value: "Não tenho plano"
          },
       
      ]
    }
  ]

  export {secoes}