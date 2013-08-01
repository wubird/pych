import pickle
import urllib2

url='http://www.pythonchallenge.com/pc/def/banner.p'
request = urllib2.Request(url)
response = urllib2.urlopen(request)

object = pickle.load(response)

for line in object:
	for item in line:
		print(item[0] * item[1]),
	print ""