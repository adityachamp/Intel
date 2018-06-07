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


'''
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

'''
def huawei_rwrite_extraction(huawei_file_directory): 	
	pattern = re.compile(r'rwrite[(a-z0-9,]+ [A-Za-z0-9)]+')
	with open(huawei_file_directory,'r') as f:
		for line in f:
			dict2 = {}
			#print line	
			matches = pattern.match(line)
			if matches:
				#print 'entered match'
				#print match.group()                    ###### MATCHING THE PATERN
				spl = (matches.group(0).split(" "))
				addr = spl[0][7:-1]
				data = spl[1][:-1]
				#print data
				str(addr)
				#print addr
				int_val_txt = int(addr[2:],16)							####converting hex to int 	
				dict2[int_val_txt] = data
				#print int_val
				#print dict2
				lookup_addr(dict2)
				#print len(dict2)
			else:
				#print 'entered else'
				out_file.write (line + '\n')
				#pass


def lookup_addr(dict2):
	#print dict2
	for key in dict2.keys():
		if(True):
			pass
			for name, addr in mydict.iteritems():		
				#print 'checking'   										
				if addr == key:
					#print 'entered'
					out_file.write( name + ' ' + ' ' + dict2[key] + '\n')
					#pass
		else:
			out_file.write('address ' + str(key) + ' not found in header file\n ')


out_file = open('out.txt','w')
mydict = header_file_extraction(sys.argv[1])		
dict2 = huawei_rwrite_extraction(sys.argv[2])

#mydict = header_file_extraction('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/header/nr_top_32bit.h')		
#dict2 = huawei_rwrite_extraction('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/programming/huawei_csirs_trs_gryffindor_rmi.txt')
#lookup_addr(int(sys.argv[1]),dict2[int(sys.argv[1])])




