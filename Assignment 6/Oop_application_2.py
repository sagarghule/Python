
class circle():

	pi = 3.14;

	def __init__(self):

		self.radius = 0;
		
		self.area = 0;

		self.circumference = 0;

	
	def accept(self):

		self.radius = int(input("Enter the value of radius "));

	
	def calculatearea(self):

		self.area = circle.pi*self.radius**2;


	def calculatecircumference(self):

		self.circumference = 2*circle.pi*self.radius;


	def display(self):

		print("Radius of circle",self.radius);

		print("Area of circle",self.area);

		print("Circumference of circle",self.circumference);
	
		



def main():

	obj1 = circle();
	
	obj2 = circle();

	
	obj1.accept();
	obj1.calculatearea();
	obj1.calculatecircumference();
	obj1.display();

	obj2.accept();
	obj2.calculatearea();
	obj2.calculatecircumference();
	obj2.display();

 


if(__name__ == "__main__"):
	
	main();
