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

    def __str__ (self):
        return f"{self.__name}, {self.__age}"

person1=Person(name='juan',age= 18,id= 1144193296,rh='o+')
# print(person1._name, person1._age)
       

      
       

print(person1)