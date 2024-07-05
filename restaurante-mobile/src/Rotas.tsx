import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Tab = createNativeStackNavigator();

import Login from "./Login";
import Cadastro from "./Cadastro";
import Tabs from "./Tabs";
import ProdutoDescricao from "./Tabs/ProdutoDescricao";
import { PedidoDescricao } from "./Tabs/PedidoDescricao";

export default function Rotas() {
    return (
        <NavigationContainer independent={true}>
            <Tab.Navigator>
                <Tab.Screen
                    name="Tabs"
                    component={Tabs}
                    options={{
                        headerShown: false // não mostra o header
                    }}

                />

                <Tab.Screen
                    name="Login"
                    component={Login}
                    options={{
                        headerShown: false // não mostra o header
                    }}
                />

                <Tab.Screen
                    name="Cadastro"
                    component={Cadastro}
                    options={{
                        headerShown: false // não mostra o header
                    }}
                />


                <Tab.Screen
                    name="ProdutoDescricao"
                    component={ProdutoDescricao}
                    options={{
                        headerShown: false // não mostra o header
                    }}
                />
                <Tab.Screen
                    name="PedidoDescricao"
                    component={PedidoDescricao}
                    options={{
                        headerShown: false // não mostra o header
                    }}
                />

            </Tab.Navigator>
        </NavigationContainer>
    )
}