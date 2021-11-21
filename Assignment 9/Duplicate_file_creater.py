
import sys;



def copyfile(name):

	f = open(name,'r');

	f1 = open('Demo.txt','a');

	f1.write(f.read());



def main():

	print("File copyer!");

	copyfile(sys.argv[1]);	
		



if __name__=="__main__":
	main();