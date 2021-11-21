from functools import*;

def implist():
	
	arr1 =list();

	no1 = int(input("Enter number of elements wnt put into list "));

	print("Enter element in list ");

	for i in range(no1):

		no2 = int(input("Number: "));

		arr1.append(no2);

	return(arr1);


def fun(no):
	
	a = 0;
	for i in range(no):
		if(no % 2 == 0):
			a = a+1;
	if a > 2:
		return(no);
	

def gun(no):

	return(no * 2);

def man(no1,no2):
	max = no1;

	if (no1 < no2):
		max = no2;
	return(max);

def main():
	
	arr = list(implist());
	
	print("Entered list is ",arr); 

	list1 = list(filter(fun,arr));

	print("prime numbers are",list1);

	list2 = list(map(gun,list1));

	print("Squre of all numbers",list2);

	product = reduce(man,list2);

	print("Addition of all elements",product);




if(__name__ =="__main__"):

	main();





