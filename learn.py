# SMMLV calculator
#This program allows you to calculate the SMMLV in COP (Colombia)
#Is writen in english because I like to program in this language
#Author: Miguel Hernandez 
def calculator():
     
#Interactive calculator for SMMLV (Colombian minimum wage).
#Asks the user how many salaries they want to calculate,
#handles invalid input, and repeats until the user decides to exit.
    
  print("Hello welcome to the calculator") #welcome message
  print("°-------------------------------------°")
  text = input("Do you want to calculate the SMMLV?: ") # Ask the user how many minimum wages they want to calculate
  fatality2= text.lower() #normalize input
  SMMLV = 1623500 #SMMLV in COP 
  while fatality2 == "yes": 
    try:
        # Ask how many minimum wages the user wants to calculate
        number = int(input("How many SMMLV? wants to calculate?: "))                    
        result = SMMLV * number

         # Display the result
        print(f"\nThe total a mount is: {result:,} COP")
        print("°-------------------------------------°")
    except ValueError:
        print("You entered a wrong number try with a integer pls")
    # Ask if the user wants to do another calculation
    text = input("Do you want to do any other calculate?: ")   
    fatality2= text.lower()
  print("°-------------------------------------°")
  print ("Thanks for calculate with us")

if __name__ == "__main__":
    calculator()
