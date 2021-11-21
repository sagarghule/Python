
#create object of the list 

arr = list();

a = int(input("How many number of element you want to enter "));

for i in range(0,a):

	no = input("Enter a number ");


	arr.append(int(no));

print("Entered elements are", arr);

no = 0;

for i in range(0,a):
	
	if no < arr[i]:

		no = arr[i]; 
	

print("Biggest number is ",no);




