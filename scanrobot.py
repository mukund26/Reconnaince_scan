from urllib import urlopen
from contextlib import closing
import io

def get_robots_txt( url ):
	if url.endswith('/'):
		path=url
	else:
		path=url+'/'
	with closing(urlopen(path+'robots.txt')) as req:
	#data=io.TextIOWrapper(req,encoding='utf-8')
		return req.read()
	
#print (get_robots_txt('https://www.reddit.com/'))
