import urllib2
import re
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

request = urllib2.Request(url + '25357')
response = urllib2.urlopen(request)
page = response.read()
m = re.search('(and the next nothing is )([0-9]+)', page)
i = 0

while i < 400 and m:
	request = urllib2.Request(url + m.group(2))
	response = urllib2.urlopen(request)
	page = response.read()
	m = re.search('(and the next nothing is )([0-9]+)', page)
	print page

print 'end'