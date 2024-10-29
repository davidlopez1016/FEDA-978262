from abc import ABC, abstractmethod
class Animal :
    def __init__(self, nombre, edad, dueno):
        self.nombre = nombre
        self.edad = edad
        self.dueno = dueno
        
    @abstractmethod
    def  hacersonido(self):
        return f"el animal hace un sonido"



class Perro(Animal):
    def __init__(self, nombre, edad, dueno,raza,color):
        super().__init__(nombre,edad,dueno)
        self.raza = raza
        self.color = color
    def hacersonido(self):
        return "guau"



animal_1 = Animal("gato",1, "maria")        
perro = Perro("copito", 2 ,"luis","labrador","negro")     


print(animal_1.nombre, animal_1.edad,animal_1.dueno)
print(perro.nombre, perro.edad,perro.dueno,perro.raza,perro.color)

print(perro.hacersonido())