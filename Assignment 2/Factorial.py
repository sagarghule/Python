 
def fun(no):

	fact = 1;

	a = 1;

	for i in range(no):
	
		fact = fact * a;
	
		a = a+1;
 
	print("Factorial of",no,"is",fact);




print("Enter a number to calculate factorial");

no = int(input());


fun(no);

