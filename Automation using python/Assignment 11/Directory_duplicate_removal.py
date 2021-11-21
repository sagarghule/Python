
import sys;

from checksum import*;

import os;

import time;


def findchecksum(path):

	flag = os.path.isabs(path);

	if not flag:

		path = os.path.abspath(path);

	exists = os.path.isdir(path);

	dict = {};

	if exists:

		for folder,subfolder,files in os.walk(path):
		
			for file in files:
	
				path = os.path.join(folder,file);

				hash_file = hashfile(path);

				if hash_file in dict.keys():

					dict[hash_file].append(path);


				else:

					dict[hash_file] = [path];

		

	else:

		print("Invalid path");


	return dict;


		


def finddup(dict1):


	result = list(filter(lambda x:len(x) > 1 , dict1.values()));

	if len(result) > 0:

		fd = open("log%d.txt"%time.time(),'w');

		print("Duplicate files found");

		fd.write('Duplicate files are:\n');

		for re in result:

			icnt = 0;

			for subre in re:
	
				icnt += 1;

				if icnt > 1:

					fd.write("\t\t%s\n"%subre);

		fd.close();


	else:

		print("Duplicate files are not found");	

	return result;
	


def delete(dict1):

	result = list(filter(lambda x:len(x) > 1 , dict1.values()));
	
	if len(result) > 0:

		for re in result:
		
			icnt = 0;

			for subre in re:
				
				icnt += 1;

				if icnt > 1:
					
					os.remove(subre);
		
			

	

def main():

	print("Application name :",sys.argv[0]);

	try:
		
		
		arr = findchecksum(sys.argv[1]);

		finddup(arr);
			
		delete(arr);

	
	except Exception:

		print(Exception);




if __name__=="__main__":

	main();
