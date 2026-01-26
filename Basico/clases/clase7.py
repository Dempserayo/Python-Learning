#Cualquier dato ingresado con input sera str a menos que se haga un casting
#Lo que significa que vamos a cambiar el tipo de dato.

name = input("nombre: ")
print("Mi nombre es ", name)

#age = input ("edad: ")
#print("Mi edad es: ", age)


#EJEMPLO de casting
# Debemos agregar el tipo de dato que queremos que sea la variable, seguido ya de en () lo que estemos agregando en este caso es un input
age = int(input("edad: "))
print(age)
print(type(age))

#okey