import markdown
import os
import os.path
from bs4 import BeautifulSoup

rootDir = '/Users/huangxiquan/huangxiquan/temp/FFWiki.wiki'

def walkDir(dir) :
    if(not dir or dir.startswith('.')) :
        return
    list = os.listdir(dir)
    for file in list :
        if(os.path.isdir(file)) :
            walkDir(file)
        elif(file.endswith('.md')) :
            md2html()

def md2html(file) :
    content = open(file,'r').read();
    content = unicode(content,"utf-8")
    content = markdown.markdown(content)
    content = content.encode('utf-8')
    fileName = file[ : file.rfind('.')]
    soup = BeautifulSoup(content,'html.parser')
    for li in soup.find_all('li') :
        if(li.find('a')) :
            str = li.a['href'].encode('utf-8')
            if(not str.startswith('#')) :
                if(str.startswith('/')) :
                    print str[1:]
                    content = content.replace(str,str[1:] + '.html')
                else :
                    content = content.replace(str,str + '.html')
    open(fileName + '.html','w').write(content)

if __name__ == '__main__':
    # walkDir(os.getcwd())
    for root,dirs,files in os.walk(rootDir):
        for file in files :
            if(file.endswith('.md')) :
                md2html(os.path.join(root,file))
