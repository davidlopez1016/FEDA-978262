class Person:
    def __init__(self,name, age):
        self.__name = name 
        self.__age = age


    @property
    def name (self):
        return self.__name

    name.setter
    def name(self, name):
        self.__name = name

    @property
    def age (self):
        return self.__age

    age.setter
    def age(self):
        self.__age = age 




person_1 = Person("maria", 14)
print(person_1.name, person_1.age)       
person_1.name = "maria camila"
person_1.age = 34
print(person_1.name, person_1.age)   

print(person_1)

