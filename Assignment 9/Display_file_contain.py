
import os;



def openfile(name):

	f = open(name,'r');

	print(f.read());


def main():

	print("File finder!");

	name = input("Enter file name which you want to read: ");

	openfile(name);	
		



if __name__=="__main__":
	main();