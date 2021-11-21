
import os;



def exisit(path):


	for foldername,subfolder,filename in os.walk(os.getcwd()):
		
		for filen in filename:

			if filen == path:
				return True;	

def main():

	print("File finder!");

	name = input("Enter file name which you want to find: ");

	try:
		if exisit(name):

			print("File is found");
		else:
			print("File is not found");	


	except Exception:

		print(Exception);
		

	


if __name__=="__main__":
	main();