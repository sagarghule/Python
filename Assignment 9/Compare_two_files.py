
import sys;



def chkfile(name,name1):

	f = open(name,'r');

	f1 = open(name1,'r');
	
	r1 = f.read();

	r2 = f1.read();

	if r1 == r2:

		print("Success");
	else:
		print("Failure");



def main():

	print("Compare content of two files!");

	chkfile(sys.argv[1],sys.argv[2]);	
		



if __name__=="__main__":
	main();