x = 0
def count():
    fs = []
    for i in range(1,4):
        def f(j):
            def g():
                return j * j
            return g
        r = f(i)
        fs.append(r)
    return fs

if __name__ == '__main__':
    f1,f2,f3 = count()
    print f1(),f2(),f3()
