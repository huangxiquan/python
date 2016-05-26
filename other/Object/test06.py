class Person(object) :
    def __init__(self,name,score) :
        self.name = name
        self.score = score
        self.get_grade = lambda : 'A'

if __name__ == '__main__':
    p1 = Person('Bob',90)
    print p1.get_grade
    print p1.get_grade()
