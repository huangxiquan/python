class Person(object) :
    def __init__(self,name,**kw) :
        self.name = name
        for k , v in kw.iteritems() :
            setattr(self,k,v)

if __name__ == '__main__':
    tom = Person('tom',gender='male')
    print tom.name
    print tom.gender
