#Diccionarios

numbers = {1:"uno",2:"dos", 3:"tres"}
#print(numbers[2])

information = {"Nombre": "Miguel Angel", 
"Apellido": "Jaimes P.",
"Altura": 1.78,
"Edad": 22
}

#print(information)
del information["Edad"]
#print(information)

claves = information.keys()
print(claves)
#print(type(claves))

values = information.values()
#print(values)

pairs = information.items()
#print(pairs)

contacts = {
"Miguel Angel":
   {
        "Apellido": "Jaimes P.",
        "Altura": 1.78,
        "Edad": 22
    },
"Jhon":
    {
        "Apellido": "Doe",
        "Altura": 1.68,
        "Edad": 31
    },
"Michael":
    {
        "Apellido": "Jordan",
        "Altura": 1.68,
        "Edad": 32
    },
"Leo":
    {
        "Apellido": "Messi",
        "Altura": 1.68,
        "Edad": 33
    }
}

print(contacts)
print(contacts["Miguel Angel"])