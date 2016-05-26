import os
import os.path
rootdir = "/Users/huangxiquan/huangxiquan/git/App_Android"                                   

for parent,dirnames,filenames in os.walk(rootdir):    
	for filename in filenames:                        
		print (os.path.join(parent,filename)) 
		index = filename.find(".orgin")
		if(index != -1):
			print ("delete")
			os.remove(os.path.join(parent,filename))
		
