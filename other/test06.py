def log(f):
    def fn(x):
        print 'call' + f.__name__ + '()... ...'
        return f(x)
    return fn

@log
def test(n):
    return reduce(lambda x , y : x * y ,range(1,n+1))

if __name__ == '__main__':
    print test(4)
