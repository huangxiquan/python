import functools

sorted_ignore_case = functools.partial(sorted,cmp = lambda s1 , s2 : cmp(s1.lower(),s2.lower()))

if __name__ == '__main__':
    print sorted_ignore_case(['bob','about','Zoo','Credit'])
