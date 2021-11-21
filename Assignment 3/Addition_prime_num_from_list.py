
import marvellousnum;

def listprime():
	
	sum = 0;

	for i in range(0,a):
		
		if marvellousnum.chkprime(arr[i]):
			
			sum = sum + arr[i];

			print(arr[i], end=" ");

	print("This is the list of prime numbers");

	print("Addition of all prime numbers is ",sum);
		
		
#create object of the list 

arr = list();

a = int(input("How many number of element you want to enter "));

for i in range(0,a):

	no = input("Enter a number ");


	arr.append(int(no));

print("Entered elements are", arr);

listprime();





