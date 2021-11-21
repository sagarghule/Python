
def fun(no):
	
	a = no;
	for i in range(no):
		print("*  "*a);
		a = a - 1;



 
print("Enter a number to draw a pattern");

no = int(input());


fun(no);

