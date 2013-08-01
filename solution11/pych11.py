#generate the 30th term of this sequence, then find it's length
a = [1, 11, 21, 1211]


for i in range(4, 31):
	next = ''
	counter = 1
	previous = str(a[i-1])
	for x in range(0, len(previous)):
		#if it is not last digit and next digit is the same, counter up, move pointer
		if x+1 < len(previous) and previous[x] == previous[x+1]: 
			counter += 1
		#if it is not last digit and next digit is different, print how many of current digit, reset counter	
		elif x+1 < len(previous) and previous[x] != previous[x+1]:
			next += str (counter)
			next += previous[x]
			counter = 1
		#if it is last digit, print what counter is currently at and append to a
		else:
			next += str (counter)
			next += previous[x]
	a.append(int(next))
		

print len(str(a[30]))

