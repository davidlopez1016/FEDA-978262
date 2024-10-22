class Person: 
    def __init__(self, name, age, id, rh):
        self.__name = name
        self.__age = age
        self.__cc = id
        self.__rh = rh
    
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age =new_age    

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name =new_name

person1=Person('juan', 18, 1144193296,'o+')
# print(person1._name, person1._age)
       

print(person1.get_age())       
person1.set_age(19)
print(person1.get_age())       
       
print(person1.get_name())
person1.set_name('camilo') 
print(person1.get_name())