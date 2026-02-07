#Fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 ...

def fibonacci(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b =  b, a+ b

for num in fibonacci(55):
    print(num)


def sumar(a,b):
    return a + b

resultado = sumar(2,2)
print(resultado)



def numeros (a):
    if a / 2 == 0:
        print("El numero:",a,"es impar")
    else:
        print("El numero:",a,"es par")
        

numeros(9)        

def mayorque(a,b):
    if a > b:
        print(a,"es mayor que",b)
    else:
        print(b,"es mayor que",a)

mayorque(2,4)




a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

lista_total = [a,b,c]
def sumatotal(lista_total):
    print(lista_total[0] + lista_total[1] + lista_total[2])

sumatotal(lista_total)




lista = [1,2,3,4,5]
def sumar_pares (lista):
    valor = 0
    for i in lista:
        valor = i
        if valor % 2 == 0:
            print(i, "es numero par")
        else:
            print(i, "es numero impar")

sumar_pares(lista)



edades = [12,14,22,23,8]
print(edades)

def edade_mayores (edades):
    nueva_edades = []
    for i in edades:
        if i >=18:
            nueva_edades.append(i)
            print(nueva_edades)

edade_mayores(edades)
 




a = int(input("Ingrese valor: "))
b = int(input("Ingrese valor: "))
c = int(input("1.Suma 2.Resta 3.Multiplicacion 4.Division: "))

operacion2 = [a,b,c]

def calculadora (operacion2):
    if c == 1:
        print(a + b)
    elif c == 2:
        print(a - b)
    elif c == 3:
        print(a * b)
    elif c == 4:
        print(a / b)
    else:
        print("Valores Incorrectos")

calculadora(operacion2)


