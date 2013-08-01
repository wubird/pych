import datetime

for i in range(1006, 1996, 10):
	d = datetime.date(i,1,26)
	if d.weekday() == 0: print d

	#mozart was born 1756-01-26