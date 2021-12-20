from abc import ABC, abstractmethod

class Instructors:
    #class attribute?
    companyName = "BlueLime"
    #constructor
    def __init__(self,course):
        self.course=course
    def printMe():
        print("zz")
    def printIt(self):
        print(self.course)


print(Instructors.companyName)
Instructors.printMe()
#Instructors.printIt(5)

instructor = Instructors("sociology")
instructor2 = Instructors("math")
print(instructor.course)
instructor.printIt()
Instructors.printIt(instructor2)

Instructors.Tale ="abc"
#Instructors.TellIt= 

class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.color = color

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

ford = Car(60,"black")
nissan = Car(35,"green")
toyota = Car(45,"red")

ford.set_speed(65)
print(nissan.get_speed())
nissan.__speed = 30 #direct access doesn't work!
print(nissan.get_speed())
nissan._Car__speed=75
print(nissan.get_speed())

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass #empty method
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(AbstractShape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side **2
    def perimeter(self):
        return self.side *4

mySquare = Square(5)
print(mySquare.area(),mySquare.perimeter())
#myShape = AbstractShape()