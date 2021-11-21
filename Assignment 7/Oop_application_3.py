
class numbers():


	def __init__(self):

		self.value = int(input("Enter the first value "));



	
	def chkprime(self):

		a = 0;

		for i in range(self.value):
		
			if (self.value % (i+1) == 0):

				a = a + 1;
		
		if a <= 2:

			return(True);
		else:

			return(False);


	def chkperfect(self):

		if ((numbers.sumfactors(self) - self.value) == self.value):

			return(True);

		else:

			return(False);

		

	def factors(self):
		
		for i in range(self.value):
		
			if (self.value % (i+1) == 0):

				print(i+1, end = " ");
		

	def sumfactors(self):

		sum = 0;

		for i in range(self.value):
		
			if (self.value % (i+1) == 0):
				sum = sum + (i+1);

		return(sum);
	
		



def main():

	obj1 = numbers();
	
	print("prime number ",obj1.chkprime());

	print("Perfect number",obj1.chkperfect());

	print("Factors",obj1.factors());

	print("Sum of all factors",obj1.sumfactors());

	print();

	
	obj2 = numbers();
	
	print("prime number ",obj2.chkprime());

	print("Perfect number",obj2.chkperfect());

	print("Factors",obj2.factors());

	print("Sum of all factors",obj2.sumfactors());
	

	
 


if(__name__ == "__main__"):
	
	main();
