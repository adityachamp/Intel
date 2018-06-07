import re
import sys
#print sys.argv[1]

def header_file_extraction(header_file_directory): 	
	
	pattern = re.compile(r'#define [a-zA-Z0-9_]+ [a-zA-Z0-9]+')

	with open(header_file_directory,'r') as f:
		mydict = {}
		contents = f.read()
		matches = pattern.finditer(contents)                    ###### MATCHING THE PATERN
		
		for match in matches:                                  	##### SPLITTING INTO NAME AND ADDRESS
			spl = match.group(0).split(" ")
			int_val_h = int(spl[2][2:],16)
			mydict[spl[1]] = int_val_h

		#print len(mydict)
		return mydict
		
		#for key,val in mydict.items():                			#### PRINTING ENTIRE DICTIONARY
		#	print key, val

def huawei_rwrite_extraction(huawei_file_directory): 	
	dict2 = {}
	pattern = re.compile(r'rwrite[(a-z0-9_,]+ [A-Za-z0-9)]+')

	with open(huawei_file_directory,'r') as f:
		contents = f.read()
		#print contents
		matches = pattern.finditer(contents)                    ###### MATCHING THE PATERN

		for match in matches:                                  	##### EXTRACTING THE ADDRESS
			spl = (match.group(0).split(" "))
			addr = spl[0][7:-1]
			data = spl[1][:-1]
			#print data
			str(addr)
			#print addr
			int_val_txt = int(addr[2:],16)							####converting hex to int 	
			dict2[int_val_txt] = data
			#print int_val
		#print 'func start'
		lookup_addr(dict2)
		#print len(dict2)
		return dict2 
		
		#print dict2.keys()

def lookup_addr(dict2):
	for key in dict2.keys():
		if(True):
			pass
			for name, addr in mydict.iteritems():		
				#print 'checking'   										
				if addr == key:
					#print 'entered'
					print name , ' ' + ' ' + dict2[key]
					#pass
		else:
			print 'address ' + str(key) + ' not found in header file '

#mydict = header_file_extraction('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/header/nr_top_32bit.h')		
#dict2 = huawei_rwrite_extraction('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/programming/huawei_csirs_trs_gryffindor_rmi.txt')

mydict = header_file_extraction(sys.argv[1])		
dict2 = huawei_rwrite_extraction(sys.argv[2])


#lookup_addr(int(sys.argv[1]),dict2[int(sys.argv[1])])
