#Listas Comprehension

numeros_ejercicio1 = [1,2,3,4,5,6,7,8]
pares = [n*10 for n in numeros_ejercicio1 if n %2 == 0]

print("Ejercicio 1: ")
print(pares)
print("_____________________________")


#Ejercicios Basico 
#Crear una funcion doble(numero) que retorne el doble del numero ingresado

def doble (numero):
    print(numero * numero)

print("Ejercicio 2: ")
doble(2)
print("_____________________________")



#Ejercicio 3
#Funcion que retorne el area de un rectangulo

def area_rectangulo (base, altura):
        return base * altura 

print("Ejercicio 3: ")
print("El area de un rectangulo es: ",area_rectangulo(2,2))
print("_____________________________")
    

#Ejercicio 4
#List comprehension para filtrar numeros pares

numeros_ejercicio4 = [1,2,3,8,20,43,4]
numeros_pares_ejercicio4 = [n for n in numeros_ejercicio4 if n % 2 == 0]
print("Ejercicio 4: ")
print(numeros_pares_ejercicio4)
print("_____________________________")



#Ejercicio 5
#en base a una lista de numeros, crear una nueva lista, si estos numeros son par y otra lista si son impar

numeros5 = [8,9,20,48,23]
def nueva_lista(numeros5):
    list_Par = []
    list_Impar = []

    for n in numeros5:
        if n % 2 == 0:
            list_Par.append(n)
        else:
            list_Impar.append(n)
    
    
    print("Lista par: ",list_Par)
    print("Lista impar: ",list_Impar)

        
print("Ejercicio 5: ")
print(numeros5)
nueva_lista(numeros5)        
print("_____________________________")



#Ejercicio 6

celcius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) *35 for temp in celcius]
print("Ejercicio 6: ")
print("Temperatura en F:",fahrenheit[0:2])
print("_____________________________")