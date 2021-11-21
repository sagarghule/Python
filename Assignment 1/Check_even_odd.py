def ChkNum(no):
	a = no % 2;
	if a == 0:
		print("Even Number");
	else:
		print("Odd Number");


print("Enter a number to check");

no = int(input());

ChkNum(no);
