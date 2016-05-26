def compare_ignore_case(s1,s2):
    if(s1[0].lower() > s2[0].lower()):
        return 1
    if(s1[0].lower() < s2[0].lower()):
        return -1
    return 0

if __name__ == '__main__':
    print sorted(['bob','about','Zoo','Credit'],compare_ignore_case)
