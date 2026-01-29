a = [1,2,3]
b = a

print(a)
print(b)

del a[1]
print(a)
print(b)
print(id(a))
print(id(b))


#Aca tenemos un problema y es que la variable (b) al estar apuntando a la variable (a) todo lo que haga en esta misma, se vera reflejada en la variable (b)
#para evitar esto debemos usar slicing

c = a[:]
print(id(c))
a.append(4)
print(a)
print(b)
print(c)

