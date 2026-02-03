#Condicionales en python

from queue import Empty


x = input("Ingresa un valor: ")
z = input("Ingresa un valor: ")

if x > z:
    print(x,"Es mayor que:",z)
else:
    print(x,"Es menor que:",z)


is_member = True
age = 10


if is_member:
    if age >= 18:
        print("Eres miembro y eres mayor de edad, puedes entrar al club")
    else:
        print("Eres miembro y no eres mayor de edad, no puedes entrar al club")

elif age >= 18:
    print("Eres mayor de edad, puedes entrar al club")
else:
    print("No eres mayor de edad, no puedes entrar al club")


 

 