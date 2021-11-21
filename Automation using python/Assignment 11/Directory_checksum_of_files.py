
import sys;

from checksum import*;



def findchecksum(path):

	checksum(path);
	



def main():

	print("Application name :",sys.argv[0]);

	try:	

		findchecksum(sys.argv[1]);
	
	except Exception:

		print(Exception);




if __name__=="__main__":

	main();
