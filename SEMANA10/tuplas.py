tupla_1 = ('Hola','Mundo',9, 24.3)

tupla_2 = ('mundo','cruel')

tupla_3 = tupla_1+tupla_2

#sale lo que este en el lugar 0

print (tupla_1[0])
# posicion de el dato

#print(tupla_1.index("mundo"))

#slicing // busca datos desde el primero que llamas hasta justo el anterior
print (tupla_1[1:3])

print (tupla_3)
# castear una tupla y volverla lista 
tupla_1 = ('Hola','Mundo',9, 24.3)

#volver una tupla lista para poder agregarle datos
tupla_to_list = list(tupla_1)

#agregar algo a una tupla
tupla_to_list.append(10)

#volverlo de lista a tupla
list_to_tupla = tuple (tupla_to_list)

print (tupla_to_list)

print (list_to_tupla)