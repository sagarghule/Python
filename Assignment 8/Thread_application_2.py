
from threading import*;

def evenfactor(no):
	add = 0;
	for i in range(no):
		if (no % (i+1)==0):
			if ((i+1) % 2 == 0):
				add = add + (i+1);
				
	print(add);


def oddfactor(no):
	add = 0;
	for i in range(no):
		if (no % (i+1) == 0):
			if ((i+1) % 2 != 0):
				add = add + (i+1);
				
	print(add);

def main():

	number = 6;

	t1 = Thread(target = evenfactor, args = (number,));
	t2 = Thread(target = oddfactor,args = (number,));

	t1.start();
	t2.start();

	t1.join();
	t2.join();

	print("Exit from main");



if __name__=="__main__":
	main();
