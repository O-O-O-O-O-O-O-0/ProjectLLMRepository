# Python program to explain os.mkdir() method 
	
# importing os module 
import os 

# Directory 
directory = "ListOfFiles"

# Parent Directory path 
parent_dir = "/Users/sriharithirumaligai/Downloads/project1-main"

# mode as read/write
mode = 0o666

# Path 
path = os.path.join(parent_dir, directory) 

os.mkdir(path, mode) 
print("Directory '%s' created" %directory) 