#Manipulación de Listas en Python: Creación, Indexación y Métodos Básicos

to_do = [
    "Dirigirnos al hotel",
    "ir a almorzar",
    "Visitar un museo",
    "Volver al hotel"
]

test = [
    1,
    "cuatro",
    [
        True,
        False
    ]
]

print(to_do)

print(to_do[1])

#Print de toda la vida, imprime sin mas.
print(test[2:1])

#Len me permite saber cuantos elementos hay
print(len(test))

#Me parece genial el Type, sin ejecutar en la terminal, ya me muestra con un [Any] el tipo de dato que es la variable test
#Capaz se deba a alguna extencion que tengo en mi Editor, pero bueno me parece genial.

print(type(test))

print("primer elemento", test[0])
print("segundo elemento", test[1])
print("tercer elemento", test[2])