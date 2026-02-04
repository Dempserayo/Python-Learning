numbers = [1,2,3,4,5,6]
print(numbers[1])
print(numbers)


for i in numbers:
    # print("Aqui i es igual a :",i)
    print("Aqui i es igual a :",i+1)


for i in range(5):
    print("range:",i)


print(len(range(10)))
print(range(10))


nombres = ["miguel","angel","jaimes","parra","mige"]
for i in range(2):
    print(nombres[i])   

#Range no es una lista, pero podemos volverlo una lista.
#Range repite algo una cantidad de veces, comenzando desde el 0 hasta detenerse
# en la cantidad inicial agregada. 

range(4)

#0,1,2,3

list(range(10))
print(len(numbers))


frutas = ["Pera","Banano","Fresa","Manzana"]
for i in range(len(frutas)):
    print("Ejemplo 1",frutas[i])

for fruta in frutas:
    print("Ejemplo 2",fruta)



#Un ejemplo, por si quiero iterar y mostrar los datos, de atras para adelante
#usando reversed() la cual es la mas limpia y recomendada, pero podemos usar esta otra:
nombres = ["Silvia", "Antonio", "Angie", "Miguel"]
for i in reversed(nombres):
    print(i)


test = [1,2,3,4,5]


paises = ["colombia","peru","venezuela",]
#for i in range(len(paises) -1,-1, -1):
#    print(paises[i])



#Range( empieza, termina, pasa)
#en este for se comienza por el 100, termina el 0 (no se incluye en el print) 
# y luego se regresa

#for i in range(100,0,-1):
#    print(i)

for i in reversed(range(6)):
    print(i)


fruits = ["Manzana","Pera", "Uva","Naranja","Tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "Naranja":
        print ("Naranja encontrada")




for test in range(20,0, -1):
    print(test)



pruebas = [1,2,3,4,5]
print("prueba:",len(pruebas))

for prueba in range(len(pruebas)):
    print(prueba)


for par in range(6,1,-2):
    print("prueba",par)
