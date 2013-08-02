import wave, urllib2, base64, re, array

#python HTTP authentication snippet taken from stackoverflow
request = urllib2.Request("http://www.pythonchallenge.com/pc/hex/unreal.jpg")
base64string = base64.encodestring('%s:%s' % ('butter', 'fly')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)
print result.info()
