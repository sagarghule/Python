 

def fun(no):
	a = 2;
	count = 0;

	for i in range(no):
	
		n = no % a;
		if n == 0:
			count = count + 1;
		
		a = a + 1;
	

 
	if count < 2:
		print("Given number is prime");
	else:
		print("Given number is not prime");



print("Enter a number");

no = int(input());


fun(no);
