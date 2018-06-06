d1 = {'10':1,'15':2}
d2 = {'10':1,'15':2,'15':3}
#print(d(10))

l  = []
for key1 in (d1):
	for key2 in (d2):
		if key2==key1:
			l.append(key2)

print(l)