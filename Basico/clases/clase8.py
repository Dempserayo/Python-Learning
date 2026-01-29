#Manipulación de Listas en Python: Creación, Indexación y Métodos Básicos

to_do = [
    "Dirigirnos al hotel",
    "ir a almorzar",
    "Visitar un museo",
    "Volver al hotel"
]

test = [
    1,
    1.5,
    "cuatro",
    [
        True,
        False
    ]
]

#print(to_do)

#print(to_do[1])

#Print de toda la vida, imprime sin mas.
#print(test)

#Len me permite saber cuantos elementos hay
#print(len(test))

#Me parece genial el Type, sin ejecutar en la terminal, ya me muestra con un [Any] el tipo de dato que es la variable test
#Capaz se deba a alguna extencion que tengo en mi Editor, pero bueno me parece genial.

#print(type(test))

#print("primer elemento", test[0])
#print("segundo elemento", test[1])
#print("tercer elemento", test[2])


mix = ['uno',2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("primer elemento", mix[0])
print("segundo elemento", mix[1])
print("tercer elemento", mix[2])
print("ultimo elemento", mix[-1])

string = "hola mundo"
print("primer elemento", string[0])
print("segundo elemento", string[1])
print("tercer elemento", string[2])
print("ultimo elemento", string[-1])

print(mix[:2])
print(mix[2:])

print(mix)

# el .append sirve para insertar datos u elementos a nuestra variable que en este caso es mix, la cual es una lista
mix.append(False)
print(mix)

# con el .insert ocurre algo similar, podemos agregar nuevos datos a nuestra variable, pero con la peculiaridad de que podemos seleccionar el orden en donde se guardara.
# en este caso fue en el index 1 que se guardo esta nueva lista ['a','b']
mix.insert(1,['a','b'])
print(mix)

print(mix.index(['a','b']))