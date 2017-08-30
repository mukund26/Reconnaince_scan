#! usr/bin/python -tt
import os

def get_nmap (ip):
	command = 'nmap -F -Pn '+ip
	process = os.popen( command )
	results = str( process.read() )
	return results

#print (get_nmap('-F','54.186.250.79'))
