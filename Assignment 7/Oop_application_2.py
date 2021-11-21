
class bankaccount():

	ROI = 10.5;


	def __init__(self, name, amount):

		self.name = name;
		
		self.amount = amount;

	
	def display(self):

		print("Account name ",self.name);
		
		print("Balance",self.amount);


	def deposit(self):

		amount = int(input("Enter a amount to deposit "));
		
		self.amount = self.amount + amount;


	def withdraw(self):

		amount = int(input("Enter a amount to withdraw "));
		
		self.amount = self.amount - amount;


	def calculateintrest(self):

		print("Intrest on the account balance for 1 year is ",(self.amount * bankaccount.ROI) / 100);




def main():

	obj1 = bankaccount("Sagar",2000);

	obj1.display();

	obj1.deposit();

	obj1.withdraw();

	obj1.display();

	obj1.calculateintrest();
	
	obj2 = bankaccount("Shubham",10000);
	
	obj2.display();

	obj2.deposit();

	obj2.withdraw();

	obj2.display();

	obj2.calculateintrest();

	


if(__name__ == "__main__"):
	
	main();
