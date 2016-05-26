# coding = utf-8
import sys
def lines(text):
	for line in text:
		yield line
		yield '\n'



if __name__ == '__main__':
	text = open("text.txt").read()
	c = lines(text)
	str = c.next()
	unicode(str,"ascii")
	print str
	print sys.getdefaultencoding()
	print c.next()