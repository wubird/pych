import wave, urllib2, base64, re, array

#python HTTP authentication snippet taken from stackoverflow
request = urllib2.Request("http://www.pythonchallenge.com/pc/hex/bin.html")
base64string = base64.encodestring('%s:%s' % ('butter', 'fly')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)

m = re.search('base64\n\n(.*)\n\n', result.read(), re.S)
#decode base64 block, then write to .wav file
f = open('india.wav', 'wb') 
f.write(base64.decodestring(m.group(1)))

#audio file says "sorry"
#sent email to <leopold.moz@pythonchallenge.com> with subject sorry and message sorry, 

wi = wave.open('india.wav','rb')
wo = wave.open('19_indian_inv.wav', 'wb')
wo.setparams(wi.getparams())
a = array.array('i')
a.fromstring(wi.readframes(wi.getnframes()))
a.byteswap()
wo.writeframes(a.tostring())
wi.close(),wo.close()