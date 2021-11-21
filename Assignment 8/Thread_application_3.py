
from threading import*;

def evenlist(arr):
	add = 0;
	for i in range(len(arr)):
		if (arr[i] % 2 == 0):
			add = add + arr[i];
				
	print(add);


def oddlist(arr):
	add = 0;
	for i in range(len(arr)):
		if (arr[i] % 2 != 0):
			add = add + arr[i];
				
	print(add);

def main():

	arr = [1,2,3,4,5,6,7,8,9,10];

	t1 = Thread(target = evenlist, args = (arr,));
	t2 = Thread(target = oddlist,args = (arr,));

	t1.start();
	t2.start();

	t1.join();
	t2.join();

	print("Exit from main");



if __name__=="__main__":
	main();
