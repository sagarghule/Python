

def fun(no):
	print(__name__);
	sum = 0;
	while(no != 0):
		tmp = no % 10;
		sum = sum + tmp;
		no = no // 10;
	print("sum of all digits of given number is",sum);
	




print("Enter a number");

no = int(input());

fun(no);

