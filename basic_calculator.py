def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1*num2

def div(num1, num2):
	return num1 / num2

def main():

	exit=False

	while(exit == False): 
		
		validInput=False
		
		while(validInput != True):
			try:
				num1_string = input("enter first number: ")  # By default, input function always returns a string
				num1 = int(num1_string)						 # "int" function converts a string to an integer if its a number
																 # alternatively we write: num1 = int(input("enter first number: "))
				num2_string = input("enter second number: ")
				num2 = int(num2_string)

				action_string = input("what operation would you like to do (1=add, 2=sub, 3=mul, 4=div): ") 
				action = int(action_string)
				
				validInput=True

			except:
				print("invalid input, please check select option between (1,2,3,4)") #exceptions are only triggered for differences in type 

		if(action == 1):
			Answer = add(num1, num2)
			print(Answer)
		elif(action == 2):
			Answer = sub(num1, num2)
			print(Answer)
		elif(action == 3):
			Answer = mul(num1, num2)
			print(Answer)
		elif(action == 4):
			Answer = div(num1, num2)
			print(Answer)
		else:
			print("operation not known")
				

		exit_string = input("Would you like to continue (yes = y, no = press any other key): ")

		if(exit_string!="y"): #All three numbers must be valid to trigger the exit option
			exit=True
			break
		else:
			continue

main()
