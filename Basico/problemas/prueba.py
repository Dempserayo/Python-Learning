#Recorrer Lista
#Imprimir cada fruta con su Indice

frutas = ["manzana", "pera", "uva", "naranja"]
for indice, fruta in enumerate(frutas):
    print(indice, "-", fruta)



#NIVEL 1 - FUNDAMENTOS
#Calculadora, pedir al usuario dos valores, luego imprimir
#la suma, resta, multiplicacion o division.

primerValor = int(input("ingresa un numero:"))
segundoValor = int(input("ingresa un segundo valor:"))
operacion = int(input("1.(multiplicar) 2.(Sumar) 3.(Restar) 4.(dividir)  Ingresa un numero:"))

if operacion == 1:
    print(primerValor * segundoValor)
elif operacion == 2:
    print(primerValor + segundoValor)
elif operacion == 3:
    print(primerValor - segundoValor)
elif operacion == 4:
    print(primerValor / segundoValor)
else:
    print("El operador ingresado no funciona")


#_____________________________________________________________________________________

#EDAD
#Preguntar la edad y mostrar esta misma en consola

edad = int(input("Ingrese su edad:"))

if edad >= 18 :
    print("Ere mayor de edad:", edad)
else:
    print("Eres menor de edad:", edad)


#_____________________________________________________________________________________

#NIVEL 2 - BUCLES
#Imprimir numeros del 1 al 10 

for i in range(1,11,1):
    print(i)


    

#_____________________________________________________________________________________

#TABLA DE MULTIPLICAR 
#pedir un numero e imprimir su tabla del 1 al 10

b = int(input("Ingresar una tabla de multiplicacion:"))

for i in range(1,11,1):
    print(i*b)


#_____________________________________________________________________________________

#Numero mayor 
#Pedir 5 numeros y mostrar el numero mayor

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))
d = int(input("Ingrese un numero: "))
e = int(input("Ingrese un numero: "))

numeros = [a,b,c,d,e]
mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print("El numero mayor es: ", mayor)



#_____________________________________________________________________________________


#VOCALES
#ingresar una palabra y mostrar cuantas palabras tiene

palabra = input("Ingresar palabra: ")
print("Tu palabra tiene: ", len(palabra), "letras")