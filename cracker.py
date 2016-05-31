#!/usr/bin/python
import zipfile
import argparse

def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		print "[+] Found password = " + password
		return True
	except:
		return False

def main():
	parser = argparse.ArgumentParser("%prog -f <zipfile> -d <dictionary>")
	parser.add_argument("-f", dest="zname", help="specify zip file")
	parser.add_argument("-d", dest="dname", help="specify dictionary file")
	args = parser.parse_args()

	if (args.zname == None):
		print parser.usage
		exit(0)
	elif (args.dname == None):
		zname = args.zname
		dname = 'passwords.txt'
	else:
		zname = args.zname
		dname = args.dname

	zFile = zipfile.ZipFile(zname)
	passFile = open(dname)

	for line in passFile.readlines():
		password = line.strip("\n")
		found = extractFile(zFile, password)
		# Exit if password found
		if found == True:
			exit(0)

	# If it makes it here password has not been found...
	print '[-] Password not found'

if __name__ == "__main__":
	main()