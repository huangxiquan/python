import time

def performance(unit) :
    def log_decorator(f) :
        def fn(n) :
            if(unit == 's') :
                print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            elif (unit == 'ms') :
                print time.strftime("%Y-%m-%d %H:%M:%S:%s", time.localtime())
            return f(n)
        return fn
    return log_decorator

@performance('ms')
def factorial(n) :
    return reduce(lambda x , y : x * y ,range(1,n+1))

if __name__ == '__main__':
    print factorial(4)
    print factorial.__name__
