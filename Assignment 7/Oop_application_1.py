
class bookstore():

	no_of_books = 0;


	def __init__(self, name, author):

		self.name = name;
		
		self.author = author;
		
		bookstore.no_of_books = bookstore.no_of_books + 1;

	
	def display(self):

		print(self.name,"by",self.author,",No of books",bookstore.no_of_books);



def main():

	obj1 = bookstore("Linux System Programming","Robert Love");

	obj1.display();
	
	obj2 = bookstore("C Programming","Dennis Ritchie");

	obj2.display();

	


if(__name__ == "__main__"):
	
	main();
