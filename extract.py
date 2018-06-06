import re

pattern = re.compile(r'#define [A-Z0-9_]+ [a-z0-9]+')

with open('nr_top_fpga4_32bit.h','r') as f:
	#for line in f:
		
	#	matches = pattern.search(line)
		#spl = line.split(" ")
		
	#	for match in matches:
	#		print(match.group())


	mydict = {}

	contents = f.read()
	matches = pattern.finditer(contents)
	
	for match in matches:
		spl = match.group(0).split(" ")
		#print(match.group(0))
		#print(spl[1] + ' ' + spl[2])

		mydict[spl[1]] = spl[2]
	'''	
	for key,val in mydict.items():
		print key, val
	'''
	print(mydict)