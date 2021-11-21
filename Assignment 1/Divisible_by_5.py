def chk(no):
	a = no % 5;
	if a == 0:
		print("True");
	else:
		print("False");
    
print("Enter a number to check");
no = int(input());	
chk(no);
