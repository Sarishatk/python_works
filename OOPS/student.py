class Student:
    school_name = "ABC"

    def __init__(self,id,name,total):

        self.id = id

        self.name = name

        self.total = total

    @classmethod

    def update_school_name(cls,new_school_name):

        cls.school_name = new_school_name

        print(cls.school_name)
    

    @staticmethod

    def is_pass(total):

        return True if total > 140 else False

student_instnace1 = Student(1000,"anu",150)

student_instnace2 = Student(1002,"arya",135)

Student.update_school_name("LSN")

print(Student.is_pass(student_instnace1.total))
    

        