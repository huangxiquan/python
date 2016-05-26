class Person(object) :
    pass

if __name__ == '__main__':
    p1 = Person()
    p1.name = 'Bart'

    p2 = Person()
    p2.name = 'Adam'

    p3 = Person()
    p3.name = 'Lisa'

    l1 = [p1,p2,p3]
    l2 = sorted(l1,lambda p1 , p2 : cmp(p1.name,p2.name))
    for p in l2 :
        print p.name
