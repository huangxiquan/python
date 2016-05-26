class Person(object) :
    def __init__(self,name,score):
        self.name = name
        self.__score = score

if __name__ == '__main__':
    tom = Person("tom",89);
    print tom.name
    print tom.__score
