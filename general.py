#! /usr/bin/python
import os

def create_dir(directory):
	if not os.path.exists(directory):
		os.mkdir(directory)

def write_file(path,data):
	f=open(path,'w')
	f.write(data)
	f.close()	
	
