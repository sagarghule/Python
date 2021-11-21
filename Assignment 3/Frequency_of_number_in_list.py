
#create object of the list 

arr = list();

a = int(input("How many number of element you want to enter "));

for i in range(0,a):

	no = input("Enter a number ");


	arr.append(int(no));

print("Entered elements are", arr);

no = 0;

b = int(input("Enter a number to search "));

for i in range(0,a):
	
	if b == arr[i]:

		no = no + 1; 
	

print("The number is ",no,"time in the list");






