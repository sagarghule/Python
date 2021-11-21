
from threading import*;

def fun(arr):
	arr.acquire();
	for i in range(50):
		print(i+1,"",end="");
		print();
	arr.release();

def gun(arr):
	arr.acquire();
	for i in range(50):
		print(50-i,"",end="");
	print();
	arr.release();


	

def main():

	arr = Lock();

	thread1 = Thread(target = fun, args = (arr,));
	thread2 = Thread(target = gun,args = (arr,));



	thread1.start();
	thread2.start();
	

	thread1.join();
	thread2.join();



if __name__=="__main__":
	main();
