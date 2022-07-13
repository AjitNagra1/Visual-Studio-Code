# Example of Class for a bunch of students with
# different grades and all part of same course

class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade # grade is between 0 and 100

        # can now define some methods such as returning
        # a students grade
    
    def get_grade(self):
        return self.grade

# now defining a new class which will have ability to
# add new students to the course

class Course:
    def __init__(self, name, max_students): # name = name of course
        self.name=name
        self.max_students=max_students
        self.students=[]
    
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value=0
        for i in self.students:
            value += i.get_grade()
        return value/len(self.students)


s1 = Student("Tim",19,95)
s2 = Student("Bill",19,75)
s3 = Student("Jill",19,65)

course = Course("Chemical Engineering", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students)
print(course.get_average_grade())