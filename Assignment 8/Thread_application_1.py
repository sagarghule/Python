
from threading import*;

def even():
	for i in range(20):
		if (i+1) % 2 == 0:
			print((i+1) ,"",end="");
	print();


def odd():
	for i in range(20):
		if (i+1) % 2 != 0:
			print((i+1),"",end="");
	print();


def main():

	t1 = Thread(target = even);
	t2 = Thread(target = odd);

	t1.start();
	t2.start();



	

if __name__=="__main__":
	main();
