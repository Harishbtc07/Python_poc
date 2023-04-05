#OOPS Python
class Car:
    def __init__(self,window,door,engine):
        self.windows=window
        self.doors=door
        self.engine=engine
    def self_driving(self):
        return "This is {} car".format(self.engine)
obj=Car(4,5,'petrol')
obj2=Car(3,6,"diesel")
print(obj.windows)
print(obj2.doors)
print(obj.self_driving())
print(obj2.self_driving())



# Base class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

# Subclass of Animal
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def meow(self):
        print(f"{self.name} is meowing")
        
# Subclass of Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def bark(self):
        print(f"{self.name} is barking")

# Create an instance of the Animal class
animal = Animal("Generic Animal")
animal.eat()    
animal.sleep() 
# Create an instance of the Cat class
cat = Cat("Whiskers")
cat.eat()  
cat.sleep() 
cat.meow()  
# Create an instance of the Dog class
dog = Dog("Fido")
dog.eat()   
dog.sleep() 
dog.bark()  

        