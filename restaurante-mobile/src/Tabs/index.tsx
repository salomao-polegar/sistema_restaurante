import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import Principal from "./Principal"
import Consultas from "./Consultas";
import Explorar from "./Explorar";
import Perfil from "./Perfil";

import { Ionicons } from "@expo/vector-icons";
import Produtos from "./Produtos";
import Carrinho from "./Carrinho";

const Tab = createBottomTabNavigator()

const screenOptions = {
    tabBarStyle: {
        backgroundColor: "#002858"
    },
    tabBarActiveTintColor: "#339cff",
    tabBarInactiveTintColor: "#fff"
}

const tabs = [
    // {
    //     name: 'Produtos',
    //     component: Produtos,
    //     icon: 'ice-cream'
    // },
    {
        name: 'Início',
        component: Principal,
        icon: 'ice-cream'
    },
    {
        name: 'Carrinho',
        component: Carrinho,
        icon: 'list-box'
    },

    // {
    //     name: 'Explorar',
    //     component: Explorar,
    //     icon: 'search'
    // },
    {
        name: 'Perfil',
        component: Perfil,
        icon: 'person'
    },
    
]

export default function Tabs() {
    return (
        <Tab.Navigator
            screenOptions={screenOptions}
            >
                {tabs.map((tab) => (
                    <Tab.Screen
                    key={tab.name}
                    name = {tab.name}
                    component={tab.component}
                    options={{
                        headerShown: false,
                        tabBarIcon: ({color, size}) => (
                            <Ionicons name={tab.icon} color={color} size = {size} />
                        )
                    }}
                />
                ))
            
}
        </Tab.Navigator>
    )
}