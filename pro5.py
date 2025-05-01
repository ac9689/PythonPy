#working with directory
import os
#os.mkdir('/home/ashwani/Desktop/DAV') # create directory
os.mkdir('/home/ashwani/Desktop/DAV') 

#listing file and directory
obj= os.listdir('/home/ashwani/Desktop/DAV')
print(obj)

# checking if a file or directory exists
os.path.exists('/home/ashwani/Desktop/DAV/new 4.txt')