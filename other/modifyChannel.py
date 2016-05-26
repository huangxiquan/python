import os
import os.path

def change(text) :
    texts = text.split(':')
    newText = texts[1].replace('\n','') + "#" + texts[0]
    open('newText.txt','a').write(newText + '\n')

if __name__ == '__main__':
    lines = open('channel.txt').readlines()
    map(change,lines)
