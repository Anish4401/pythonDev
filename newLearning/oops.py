class car:
    total_cars=0
    def __init__(self, model,__brand):   #here __init__ is a constructor which is acting like to pass the values and self is making connetion in between
        self.model=model         #the values and the class
        self.__brand=__brand
        car.total_cars+=1
    def full_name(self):         #here we are defining a function to return the values of the class  adding self is mandatory and we can add multiple functions
        return f"{self.model} {self.__brand}" #here we are returning the values of the class
    @staticmethod  #here we are defining a static method which is a decorator which is used to restrict the access of the method
    def  desc():   #here we are defining a function to return the values of the class
        return "This is a car class the super class"
    @property  #here we are defining a property which is a decorator which is used to restrict the access of the method
    def __getbrand(self):
        return self.__brand
mynewcar=car('A6','Audi')      #here we are passing the values to the clas
print(mynewcar.model)
print(mynewcar._car__getbrand)
print(mynewcar._car__brand)  #here we are accessing the private variable by using the class name and the variable name
print(mynewcar.full_name())



#Inheritance
#here we are creating a new class car1 and inheriting the class car to car1

class car1(car):   #here we are inheriting the class car to car1
    def __init__(self,brand,model,price):   #here we are passing the price to the class
        super().__init__(brand,model)
        self.price=price
    def fueltype(self):         #here we are defining a function to return the values of the class
        return "Petrol or Diesel"
     #here we are returning the values of the class
mynewcar1=car1("Hyundai","verna",5000000)       #here we are passing the values to the class
print(mynewcar1.price)
print(mynewcar1.full_name())

#Encapsulation

class car2(car1):
    def __init__(self, model, brand,price):
        super().__init__(model, brand,price)
        self.__price=5000000    #here we are making the price as private by adding __ before the price
    def get_price(self):     #here we are defining a function to return the values of the class
        return self.__price  #here we are returning the values of the class
    def set_price(self,price):  #here we are defining a function to set the values of the class
        self.__price=price    #here we are setting the values of the class
        return self.__price
    def fueltype(self):
        return "Electric"
mynewcar2=car2("Hyundai","verna",5000000)
print(mynewcar2.get_price())
# print(mynewcar2.__price)  #here we can't access the private variable directly

print(mynewcar2.set_price(6000000))

#Polymorphism

class car3(car2,car1):
    def __init__(self, model, brand, price):
        super().__init__(model, brand, price)
print(mynewcar2.fueltype())   #here we are calling the function fueltype from the class car2
print(mynewcar1.fueltype())    #here we are calling the function fueltype from the class car1
print(car.total_cars)  #here we are calling the total_cars from the class car
print(car.desc())  #here we are calling the desc from the class car which is a static method and we can call it by using the class name
print(mynewcar.desc())  #here we are calling the desc from the class car which is a static method and we can call it by using the method name
print(mynewcar1.desc()) #here we are calling the desc from the class car which is a static method and we can call it by using the method name
print(isinstance(mynewcar1,car1))  #here we are checking whether the object mynewcar1 is an instance of the class car1 or not and it will return true if it is an instance of the class car1


#Multiple Inheritance
#here we are creating a new class car4 and inheriting the class car1 and car2 to car4
class car4(car2,car1):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
        pass
mynewcar4=car4("Hyundai","verna",5000000)
print(mynewcar4.full_name())  #here we are checking the method resolution order of the class 
print(mynewcar4.desc())

