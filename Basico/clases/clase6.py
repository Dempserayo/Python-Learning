#Operadores numericos
a = 10
b = 3

#print("Suma: ", a + b)
#print("Resta: ", a - b)
#print("Division: ", a / b)
#print("Multiplicacion: ", a * b)

#Si queremos solo el valor entero de la division usamos doble //
#print("Parte entera de la division: ", a // b)

#Si queremos que a ( 10 ) elevarlo en b ( 3 ) usamos doble multiplicador
#print("Potenciacion: ", a ** b)

#print("Modulo: ", a % b)

a += 2
#print(a)


#REGLA PEMDAS
# ( P )arentesis ( E )exponenciacion ( M )atematicas ( D )ivision ( A )dicion y ( S )ustracion
# basicamente un orden en realizar operaciones, por ejemplo si agregamos a una operacion entre ( ) lo que este dentro sera lo primero en realizarce 
# y su resultado se sumara, multiplicara o lo que fuera, por la continuacion de la operacion.

#  Como ejemplo el operation_2 ( 2 + 3 ) * 4
#  primero se realiza entre los () que da 5 seguido de esto, se continua la operacion multiplicando ese resultado * 4 = 20

operation_1 = 2 + 3 * 4
operation_2 = (2 + 3) * 4
operation_3 = (2 + 3) * (4**2) / 8 - 1

#print(operation_1)
#print(operation_2)
#print(operation_3)


mayor = 5
menor = 4

#Imprime True si es verdad o False si es falso, dependiendo de los valores de ambas variables
print(mayor > menor)
print(mayor < menor)