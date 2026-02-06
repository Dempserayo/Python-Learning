
text = "Hola"
text_Iterador = iter(text)

for char in text_Iterador:
    print(char)

#Al iterar, un string estaria haciendo algo como asi
# ["h","o","l","a"]

# eso es mas o menos lo que ocurre internamente, ya por eso al usar print(next(text_Iterador)) mostraria de una en una
# h 
# o 
# l 
# a 

#_____________________________________________________________________________________



#Crear un iterador para los numeros pares
#Limite

#Crear iterador
limit = 10
add_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in add_itter:
    print(num)


#_____________________________________________________________________________________


def my_generator():
    yield 1
    yield 2
    yield 3


for value in my_generator():
    print(value)