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