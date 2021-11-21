
def fun(no):
	if(no > 0):
		print("*  ", end=" ");
		no = no - 1;
		fun(no);


def main():
	num = int(input("Enter a number"));
	fun(num);



if(__name__ == "__main__"):
	main();





