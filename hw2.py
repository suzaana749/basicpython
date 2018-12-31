from __future__ import print_function
class College:
    def __init__(self):
        self.college = "nec"
class Faculty(College):
    def __init__(self,FN):
        self.facultyName = FN
        College.__init__(self)
class Teacher(Faculty):
    def __init__(self,TN,s,p,facult):
        self.teacherName = TN
        self.salary = s
        self.period = p
        Faculty.__init__(self, facult)
    def information(self):
        print("name :",self.teacherName)
        print("salary:",self.salary)
        print("period:",self.period)
        print("faculty",self.facultyName)
class Student(Faculty):
    def __init__(self,std,sub,mrk,facult):
        self.student = std
        self.subject = sub
        self.marks = mrk
        Faculty.__init__(self,facult)
    def information(self):
        print("name :",self.student, end="\t")
        print("salary:",self.subject,end="\t")
        print("period:",self.marks,end="\t")
        print("faculty",self.facultyName,end="\t")
    def remarks(self):
        if(self.marks >= 90):
            print("excellent")
        elif(self.marks >= 80):
            print("good")
        elif(self.marks ==50):
            print("average")
        else:
            print("not satisfactory")

t1 = Teacher("ram",50000,4,"Computer")
s1 = Student("hari","maths",90,"civil")
s2 = Student("gita","science",60,"elx")
# print("faculty",f1.facultyName,",","teacher name",t1.teacherName, "salary",t1.salary,"period",t1.period,"facultyname",\
#       t1.facultyName,",","student name",s1.student,"subject",s1.subject,"marks",s1.marks,"facultyname",s1.facultyName)
t1.information()
s1.information()
s2.information()


