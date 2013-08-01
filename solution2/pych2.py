import fileinput

dict = {}

for line in fileinput.input():
    for x in line:
		if dict.has_key(x):
			dict[x] = dict[x] + 1
		else:
			dict[x] = 0
		

print dict

			
