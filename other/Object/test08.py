import json

class Student(object) :
    def read(self) :
        return r'["Tom","Bob","Alice"]'

if __name__ == '__main__':
    s = Student()
    print json.load(s)
