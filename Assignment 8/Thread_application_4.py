
from threading import*;

def small(arr):
	add = 0;
	print("Thread name is small","and Id of thread is",get_ident());
	for i in range(len(arr)):
		if (arr[i].islower()):
			add += 1;
				
	print("Number of small case letters are",add);


def capital(arr):
	add = 0;
	print("Thread name is capital","and Id of thread is",get_ident());
	for i in range(len(arr)):
		if (arr[i].isupper()):
			add += 1;
	print("Number of upper case letters are",add);

def digits(arr):
	add = 0;
	print("Thread name is digit","and Id of thread is",get_ident());
	for i in range(len(arr)):
		if (arr[i].isdigit()):
			add += 1;
	print("Number of digits are",add);
	

def main():

	arr = input("Enter a string to check ");

	thread_small = Thread(target = small, args = (arr,));
	thread_capital = Thread(target = capital,args = (arr,));
	thread_digits = Thread(target = digits,args = (arr,));


	thread_small.start();
	thread_capital.start();
	thread_digits.start();

	thread_small.join();
	thread_capital.join();
	thread_digits.join();



if __name__=="__main__":
	main();
