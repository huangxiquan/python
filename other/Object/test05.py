class Person(object) :
    def __init__(self,name,score) :
        self.name = name
        self.__score = score

    def getGrade(self) :
        if(self.__score >= 90) :
            return 'A'
        elif (self.__score >= 60) :
            return 'B'
        else :
            return 'C'

if __name__ == '__main__':
    p1 = Person('Bob',92)
    p2 = Person('Alice',65)
    p3 = Person('Tim',45)
    list = [p1,p2,p3]
    for p in list :
        print p.getGrade()
