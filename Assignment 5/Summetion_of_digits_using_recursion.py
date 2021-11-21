
sum = 0; 

def fun(no):

	global sum;
  
	if(no > 0):
   
		num = no % 10;
    
		sum = sum + num;

		no = int(no / 10);

		fun(no);
		
	return(sum);
		 
		
	
def main():

  
	no = input("Enter a number ");

	fun(int(no));
 
	print(" Addition of all digits are ", sum);
	



if(__name__ == "__main__"):
  
	main();
