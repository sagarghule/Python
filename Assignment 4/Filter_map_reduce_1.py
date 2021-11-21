from functools import*;

def fun(no):

	if(no >= 70 and no <= 90):
		return(no);
def gun(no):

	return(no + 10);

def man(no1,no2):
	prd = 1;
	prd = no2 * no1;
	return(prd);


def main():
	
	arr =list();

	no1 = int(input("Enter number of elements wnt put into list "));

	print("Enter element in list ");

	for i in range(no1):

		no2 = int(input("Number: "));

		arr.append(no2);

	print("Entered list is ",arr); 

	list1 = list(filter(fun,arr));

	print("Numbers 70 <= no >= 90",list1);

	list2 = list(map(gun,list1));

	print("list 1 numbers are incremented by 10",list2);

	product = reduce(man,list2);

	print("product of all elements",product);




if(__name__ =="__main__"):

	main();





