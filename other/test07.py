import time

def performance(f):
    def fn(n):
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print time.localtime()
        return f(n)
    return fn

@performance
def test(n):
    return reduce(lambda x,y : x + y,range(1,n+1))

if __name__ == '__main__':
    print test(4)
