class Student():
    def __init__(self,name,age,gender,level,grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self,course,grade):
        self.grades[course]=grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)


john=Student("John",12,"male",6,{"math":3.3})
shivam=Student("Shivam",14,"male",8,{"math":3.3})

print(john.getGPA())
print(shivam.getGPA())


        