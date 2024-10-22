class Vehicle:
    def __init__(self, speed):
        self.__speed = speed 

    def accelerate(self, value): 
        if value > 0:
            self.__speed += value
            return "aumenta la velocidad a "
        return "valor no valido."  

    def brake(self, value):
        if value > 0:
            self.__speed -= value
            if self.__speed < 0:
                self.__speed = 0  
            return "su velocidad disminuye a"
        return "valor no valido"  

    def __str__(self):
        return f"su velocidad es: {self.__speed}"


vehicle1 = Vehicle(100)
print(vehicle1)


print(vehicle1.accelerate(50))
print(vehicle1)

print(vehicle1.brake(80))
print(vehicle1)

print(vehicle1.brake(100))
print(vehicle1)