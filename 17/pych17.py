from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib
import re
import bz2
import urllib

cj = cookielib.CookieJar()
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

index = '12345'
m = True
i = 0

cookieInfo = ""

while i < 400 and m:
	request = Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + index)
	response = opener.open(request)
	page = response.read()
	m = re.search('(and the next busynothing is )([0-9]+)', page)
	if m:
		index = m.group(2)
	else: 
		break
	for cookie in cj:
		cookieInfo +=cookie.value
		
print page
print 'raw cookie info: ' + cookieInfo
cookieInfo = urllib.unquote_plus(cookieInfo)
print 'compressed message: ' + cookieInfo

print 'decompressed message: ' + bz2.BZ2Decompressor().decompress(cookieInfo)
#decompressed message: is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
#use server to call mozart father from challenge 13

import xmlrpclib

server=xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('Leopold')

request = Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
response = opener.open(request)
page = response.read()
print page

#pass him the message
for cookie in cj:
	cookie.value=("the flowers are on their way")
	
request = Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
response = opener.open(request)
page = response.read()
print page

#next level: http://www.pythonchallenge.com/pc/return/balloons.html