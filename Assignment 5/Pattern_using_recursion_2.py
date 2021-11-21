
def fun(no):

	max = no;

	if( no > 0):

		no = no - 1;

		fun(no);
		
		print(no + 1, end=" ");

	
	



def main():

	num = int(input("Enter a number "));

	fun(num);


if(__name__ == "__main__"):
	
	main();
