def calc_prod(lst):

    def prod(x,y):
        return x * y;

    def f():
        return reduce(prod,lst)
    return f
if __name__ == '__main__':
    x = calc_prod([1,2,3,4])
    print x()
