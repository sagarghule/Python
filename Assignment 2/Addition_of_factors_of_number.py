 

def fun(no):

	a = 1;
	Addition = 0;

	for i in range(no-1):
	
		n = no % a;

		if n == 0:
			Addition = Addition + a;
		a = a + 1;
	
	print("Addition of factors of given number is",Addition);



print("Enter a number");

no = int(input());


fun(no);
 
