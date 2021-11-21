
class arithmetic():


	def __init__(self):

		self.value1 = 0;
		
		self.value2 = 0;

	
	def accept(self):

		self.value1 = int(input("Enter the first value "));

		self.value2 = int(input("Enter the second value "));

	
	def addition(self):

		return(self.value1 + self.value2);


	def substraction(self):

		return(self.value1 - self.value2);

	def multiplication(self):

		return(self.value1 * self.value2);

	def division(self):

		return(self.value1 / self.value2);
	
	

def main():

	obj1 = arithmetic();
	
	obj2 = arithmetic();

	
	obj1.accept();
	print("Addition of two numbers ",obj1.addition());
	print("Substraction of two numbers ",obj1.substraction());
	print("Multiplication of two numbers ",obj1.multiplication());
	print("Division of two numbers ",obj1.division());

	obj2.accept();
	print("Addition of two numbers ",obj2.addition());
	print("Substraction of two numbers ",obj2.substraction());
	print("Multiplication of two numbers ",obj2.multiplication());
	print("Division of two numbers ",obj2.division());

 


if(__name__ == "__main__"):
	
	main();
