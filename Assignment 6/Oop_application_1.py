
class demo():

	value = 10;

	def __init__(self, no1, no2):

		self.no1 = no1;
		
		self.no2 = no2;

	
	def fun(self):

		print("From fun values are ",self.no1 , self.no2);

	def gun(self):

		print("From gun values are ",self.no1 , self.no2);
	
		



def main():

	obj1 = demo(11, 21);
	
	obj2 = demo(51, 101);

	
	obj1.fun();
	obj2.fun();
	obj1.gun();
	obj2.gun();

 


if(__name__ == "__main__"):
	
	main();
