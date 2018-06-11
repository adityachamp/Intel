import re
import sys
import argparse
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
				temp_file.write (line + '\n')
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
					out_file.write('rwrite('+ name + ', ' + ' ' + dict2[key] +')' +'\n')
					temp_file.write( name + ' ' + ' ' + dict2[key] +'\n')
					#pass
		else:
			out_file.write('address ' + str(key) + ' not found in header file\n ')
			temp_file.write('address ' + str(key) + ' not found in header file\n ')



def regname_to_addr(regname_file):
	pattern_reverse = re.compile(r'[_A-Z0-9]+  [a-zA-Z0-9]+')
	with open(regname_file,'r') as f_reverse:
		for line in f_reverse:
			#print line	
			matches_reverse = pattern_reverse.match(line)
			if matches_reverse:
				#print 'entered match'
				#print matches_reverse.group()                    ###### MATCHING THE PATERN
				spl_reverse = (matches_reverse.group(0).split(" "))
				regname = str(spl_reverse[0])
				#print regname
				data = str(spl_reverse[2])
				#print str(data)
				for name, addr in mydict.iteritems():		
				#print 'checking'   										
					if name == regname:
						#print 'entered'
						out_file_reverse.write('rwrite('+ str(hex(mydict[name])) + ', ' + ' ' + data +')' + '\n')	
					#pass
				
			else:
				#print 'entered else'
				out_file_reverse.write (line + '\n')
				#pass

	

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v","--verbose",action="store_true")  ### for regname to address conversion
group.add_argument("-q","--quiet",action="store_true") ### for address to regname conversion
parser.add_argument("header", help= "The header file")
parser.add_argument("text", help= "The text file")
args = parser.parse_args()

if args.verbose:
	out_file = open('out.txt','w')
	temp_file = open('temp.txt','w')
	mydict = header_file_extraction(args.header)		
	dict2 = huawei_rwrite_extraction(args.text)

elif args.quiet:
	out_file_reverse = open ('out_reverse.txt','w')
	mydict = header_file_extraction(args.header)
	regname_to_addr(args.text)

else:
	print "Incorrect input format. Refer to help for instructions"
#regname_to_addr('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/out.txt')




#mydict = header_file_extraction('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/header/nr_top_32bit.h')		
#dict2 = huawei_rwrite_extraction('/nfs/sc/disks/ngs_proj_workspace001/singhad1/scripting_python/programming/huawei_csirs_trs_gryffindor_rmi.txt')
#lookup_addr(int(sys.argv[1]),dict2[int(sys.argv[1])])




