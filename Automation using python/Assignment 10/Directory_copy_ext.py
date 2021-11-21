import sys;
import os;
import shutil;

def search(path, dest, ext):

	no = 0;
		
	if not(os.path.isabs(path)):

		path = os.path.abspath(path);


	os.mkdir(dest)
		
	if(os.path.isdir(path)):
		
		for folder,subfolders,files in os.walk(path):
		
			for fname in files:

				if fname.endswith(ext):

					fname = os.path.join(folder , fname);


					shutil.copy(fname, os.path.abspath(dest));

					no += 1;


	print("%d Files copyed successfully"%(no));

				



def main():
	
	print("Application Name",sys.argv[0]);

	if len(sys.argv) == 2:

		if lower(sys.argv[1]) == -u:

			print("Command should be:- python application_name.py folder_name extension_of_file_to_search");
	
		if lower(sys.argv[1] == -h):
		
			print("This is the application in which you find a file in directory with the specific extension. For usege of application use command '-u'");


	elif len(sys.argv) == 4:
		
		try:
			
			search(sys.argv[1],sys.argv[2],sys.argv[3]);

		except Exception:
		
			print("Error : Invaild input");

	
	else:

		print("Ivalid Argument or worng use of application");





if __name__=="__main__":
	
	main();