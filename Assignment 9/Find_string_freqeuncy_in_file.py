import sys;

def strfind(file, name):
	
	count = 0;
	fd = open(file);

	txt = str(fd.read());
	
	x = txt.split();

	for i in range(len(x)):

		if name.lower() in x[i]:
			
			count = count + 1;
	return count;

def main():
	print("Find how much time a word is there in a given strinng");
	
	print("The word %s is occured %d times in given file "%(sys.argv[2],strfind(sys.argv[1], sys.argv[2])));
	

if __name__=="__main__":
	
	main();
