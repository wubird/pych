import fileinput
import re

str = [""]

for line in fileinput.input():
	m = re.search('(?<![A-Z])([A-Z]{3})([a-z])([A-Z]{3})(?![A-Z])', line)
	if (m):
		print m.group(2)

			
