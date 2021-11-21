def chk(no):
	if no == 0:
		print("Number is Zero");
	elif no > 0:
		print("Number is Positive");
	else:
		print("Number is Negative");

print("Enter a number to check");
no = int(input());
chk(no);
