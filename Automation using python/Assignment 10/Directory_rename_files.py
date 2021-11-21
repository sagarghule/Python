import sys;
import os;

def search(path, ext1, ext2):

	no = 0;
		
	if not(os.path.isabs(path)):

		path = os.path.abspath(path);
		
	if(os.path.isdir(path)):
		
		for folder,subfolders,files in os.walk(path):
		
			for fname in files:
	
				if (fname.endswith(ext1)):

					fname = os.path.join(folder, fname);

					base = os.path.splitext(fname)[0];

					os.rename(fname, base + ext2);

					no = no + 1;


	print("%d files rename with the extension %s"%(no, ext2));

				



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