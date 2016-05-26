class Person(object) :
    def __init__(self,name) :
        self.name = name

class Teacher(Person) :
    def __init__(self,name,course) :
        super(Teacher,self).__init__(name)
        self.course = course

if __name__ == '__main__':
    t = Teacher('Tom','chinese')
    print t.name
    print t.course
