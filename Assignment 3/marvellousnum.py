
def chkprime(no):
	a = 2;
	count = 0;

	for i in range(no):
	
		n = no % a;
		if n == 0:
			count = count + 1;
		
		a = a + 1;
	

 
	if count < 2:
		check = True;
	else:
		check = False;

	return check;
