
#create object of the list 

arr = list();

sum = 0;

a = int(input("How many number of element you want to enter "));

for i in range(0,a):

	no = input("Enter a number ");


	arr.append(int(no));

print("Entered elements are", arr);

for i in range(a):

	sum = sum + arr[i];

print("Addition of all element is ",sum);

