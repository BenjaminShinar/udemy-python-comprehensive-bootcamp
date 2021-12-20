<!--
// cSpell:ignore
-->

[main](../README.md)

## Section 11: Object Orientated Programming

<details>
<summary>
Classes and some OOP basics.
</summary>

OOP - object oriented programming, breaking things into objects that interact with one another, objects are created from classes (templates), we re-use code by having classes.

an object is an entity, while a class is a blueprint for a class. classes have properties (attributes) and methods.

### Classes

we use the keyword _class_ to define the class, the convention is PascalCase.

#### Creating a class

a class has variables (attributes) and functions (methods)

```py
class Instructors:
    #class attribute?
    companyName = "BlueLime"
    #constructor
    def __init__(self,course):
        self.course=course

print(Instructors.companyName)
instructor = Instructors("sociology")
print(instructor.course)
```

the \_\_\_init\_\_\_ method is the constructor functions. we can have class attribute and instance properties.

we can also create an empty class with the _pass_ keyword

```py
class Bar:
    pass
```

#### instantiating a class

instantiating a class mean creating an object out of it. there is no _new_ keyword, we simply use the class name. then the _init_ method is called. methods with double underscore \_\_ are used by the language itself.

#### Modifying Classes

we can update the class even after it was created.

```py
class foo():
    def __init__(self, bar):
        self.bar=bar

Foo.Bar = 55
```

#### Class and instance Variables

| class variable                           | instance Variable                 |
| ---------------------------------------- | --------------------------------- |
| defined outside any method               | defined inside class methods      |
| accessed with the class name object      | accessed with the object name     |
| not prefixed                             | prefixed with _self_              |
| modification effects all class instances | modifications to object are local |
| classes are indented                     | instances are not indented        |

### Inheritance

Inheritance is creating classes by reusing code from other classes (parent). (parent, super, base) and (child, sub, derived) classes.

we first define a base class.

```py
class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def printName(self):
        print(f"{self.first_name},{self.last_name}")

dan = Person("dan","green")
dan.printName()
```

now we define a subclass. we start by creating the class and not adding anything. this is done with the _pass_ keyword.

```py
class Lawyer(Person):
    pass


jane = Lawyer("jane","roe")
jane.printName()
```

but child classes can have different constructors. we can call the base constructor. we can also add attributes to the child class.

```py
class Painter(Person):
    def __init__(self,first_name, last_name,color):
        super(self, first_name, last_name)
        self.color=color


    #override
    def printName(self):
        print(f"{self.first_name} {self.last_name} the {self.color} painter")
```

### Polymorphism

Multiple forms. methods that behave differently in the child class and the base class, or functions that work differently on different kinds of objects. like `print` and `len`

```py
len("hello")
len([1,2,3])
print("hello")
print([1,2,3])
```

lets make a polymorphic function.

```py
def addNumbers(a,b,c=1):
    return a+b+c


print(addNumbers(8,9))
print(addNumbers(8,9,4))

class UK():
    def capital_city(self):
        print("London is the capital of UK")
    def language(self):
        print("english is the primary language")

class Spain():
    def capital_city(self):
        print("Madrid is the capital of UK")
    def language(self):
        print("spanish is the primary language")

queen = UK()
queen.capital_city()
zara = Spain()
zara.capital_city()

for country in (queen, zara):
    country.capital_city()
    country.language()
```

### Encapsulation

restricting access to methods and members in the class, hiding the internal representation from the outside world.

there aren't access modifiers in python, but there are conventions of using an underscore to denote that something is private and shouldn't be used.

at any case, we shouldn't set members directly, even if python allows us to.

actually, using a double underscore prefixes the value with the class name. so it's a different name.

```py
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
nissan._Car__speed=75 #this does work!
print(nissan.get_speed())
```

### Abstraction

Hiding implementation, show only functionality. abstract classes and methods.

```py
class Shape:
    def area(self):
        pass #empty method
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

myShape = Shape()
```

to use real abstraction we need to import a module **abc** and use decorators... this actually allows us to use abstraction. we simply inherit from the **ABC** class and decorate our methods.

```py
from abc import ABC, abstractmethod

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

myShape = AbstractShape()
```

this forces us to provide implementations in the sub classes.

```py
class Square(AbstractShape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side **2
    def perimeter(self):
        return self.side *4

mySquare = Square(5)
print(mySquare.area,mySquare.perimeter)
```

</details>

## Section 12: Modules and Packages

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

### What are Modules

### How to use Modules

### Built-in Modules

### What are Python Packages

### Python dir function

### Pycache directory

### Python name attribute

<details>

[main](../README.md)
