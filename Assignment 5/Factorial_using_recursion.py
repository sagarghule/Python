fact = 1;

def fun(no):

	global fact;
  
	if(no > 0):
    
		fact = fact * no; 

		no = no - 1;
    
		fun(no);

	return(fact);
	
	

		

def main():

  
	num1 = int(input("Enter a number "));
 
	print(" Addition of all digits are ", fun(num1));



if(__name__ == "__main__"):
  
	main();
