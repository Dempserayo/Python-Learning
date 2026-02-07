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
    x = 0
    for i in lista_total:
        x = i + x

sumatotal(lista_total)
