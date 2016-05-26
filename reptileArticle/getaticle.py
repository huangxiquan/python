import urllib
import re
from bs4 import BeautifulSoup
import types
import os

# src="//139.196.14.76/uploads/default/optimized/1X/85263968e9a90e0a109af64aeb090e0f5046c460_1_690x419.png

def download_image(text) :
    url = "http:" + text[text.find('/'):]
    fileName = url[text.rfind('/') + 1 :]
    stream = urllib.urlopen(url).read()
    if(not os.path.exists('image')) :
        os.mkdir('image')
    open('image/' + fileName,'wb').write(stream)

def download_page(url,pageName) :
    pageName = pageName + ".html"
    print "url:" + url
    pageName = pageName.encode('UTF-8')
    pageName = pageName.replace('/','')
    print "pageName:" + pageName
    open('index.html','a').write(r'<a href = "'+pageName+'">'+pageName+'</a></br>')
    open(pageName,'w').write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<title>Untitled Document</title>\n</head>\n<body>')
    content = urllib.urlopen(url).read()
    start = content.find(r'"cooked":')
    end = content.find(r',"post_number":')
    temp = content[start + 10 : end -1].replace(r'\n','huang*xi*quan').replace(r'\t','tab*tab*tab').replace('\\','')
    temp = temp.replace('huang*xi*quan',r'</br>').replace('tab*tab*tab',r'&#09;');
    urlList =  re.findall(r'src.+?[p,P][n,N][g,G]',temp)
    for text in urlList :
        try :
            download_image(text)
        except Exception as e :
            print e
            continue
    for oldStr in urlList:
        temp = temp.replace(oldStr,"src=\"image/" + oldStr[oldStr.rfind('/') + 1 :])
    open(pageName,'a').write(temp)
    open(pageName,'a').write('\n</body>\n</html>')

def parse_to_url(paragraph) :
    pageUrl = paragraph.meta['content']
    pageName = paragraph.meta.a.span.string
    download_page(pageUrl,pageName)

def next_url(tag):
    if('next' in tag['rel']) :
        return True


def start_download(url) :
    print url
    if(not url):
        return
    content = urllib.urlopen(url).read()
    soup = BeautifulSoup(content,"html.parser")
    paragraphList = soup.find_all(itemprop='itemListElement');
    map(parse_to_url,paragraphList)
    navigation = soup.find(role='navigation')
    if(navigation) :
        aList = navigation.find_all('a')
        tag = filter(next_url,aList).pop()
        url = 'http://139.196.14.76' + tag['href']
    else :
        url = None
    start_download(url)

if __name__ == '__main__':
    open('index.html','w').write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n<title>Untitled Document</title>\n</head>\n<body>')
    # url = "http://139.196.14.76/t/git-gitlab/230"
    # download_page(url,'test');
    start_download('http://139.196.14.76/c/techniq')
    open('index.html','a').write('\n</body>\n</html>')
