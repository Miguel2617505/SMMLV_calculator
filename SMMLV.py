# SMMLV calculator
#This program allows you to calculate the SMMLV in COP (Colombia)
#Is writen in english because I like to program in this language
#Author: Miguel Hernandez 

#---------------------
#Dictionary: SMMLV by year
#---------------------
SMMLV = {
    2020 : 980656,
    2021 : 1014980,
    2022 : 1117172,
    2023 : 1300606,
    2024 : 1462000,
    2025 : 1623500,
}
#Function to request the year of the dictionary we want to calculate
def calculate_SMMLV(number):
   try:
       year = int(input("What is the year you want to calculate the SMMLV (2020-2025): "))
       if year in SMMLV:
          return SMMLV[year] * number
       else:
          print("Sorry, we do not have data from this year")
   except ValueError:
      print("Invalid input enter a right number") 
      return None
def calculator():      
#Interactive calculator for SMMLV (Colombian minimum wage).
#Asks the user how many salaries they want to calculate,
#handles invalid input, and repeats until the user decides to exit.
    
  print("Hello welcome to the calculator") #welcome message
  print("°-------------------------------------°")
  text = input("Do you want to calculate the SMMLV?(yes/no): ") # Ask the user how many minimum wages they want to calculate
  keep_calculating= text.lower() #normalize input
  while keep_calculating == "yes": 
    try:
        # Ask how many minimum wages the user wants to calculate
        number = int(input("How many SMMLV do you want to calculate?: "))                    
        result = calculate_SMMLV(number)

         # Display the result
        if result is not None:
           print(f"\nThe total amount is: {result:,} COP")
        else:
           print("There was an error try again please")
    except ValueError:
        print("You entered a wrong number try with a integer pls")
    # Ask if the user wants to do another calculation
    text = input("Do you want to perform another calculation? (yes/no):")   
    keep_calculating = text.lower()
  print("°-------------------------------------°")
  print ("Thanks for using our SMMLV calculator! ")
#--------------
#Entry Point
#--------------
def show_data():
   import pandas as pd
   import matplotlib.pyplot as plt

#convert dictionary into a dataframe  
   smmlv_df = pd.DataFrame(list(SMMLV.items()), columns=["Year", "SMMLV"])

#Calculate the percentage year-to-year 
   smmlv_df["Change (%)"] = smmlv_df["SMMLV"].pct_change().fillna(0) *  100
   smmlv_df["Change (%)"] = smmlv_df["Change (%)"].round(2)

#print DF (DaraFrame)
   print("\nHistorical SMMLV data (2020-2025)")
   print(smmlv_df)

# Plot the SMMLV values
   plt.figure(figsize=(8, 4))
   plt.plot(smmlv_df["Year"], smmlv_df["SMMLV"], marker = "o", linestyle="-", color="blue", label="SMMLV")
   plt.title("SMMLV Evolution (2020-2025)")
   plt.xlabel("Year")
   plt.ylabel("SMMLV (COP)")
   plt.grid(True)
   plt.legend()
   plt.tight_layout()
   plt.show()
if __name__ == "__main__":
    calculator()
#Ask the user if wants to see the chart
    text = input("Do you want to see the historical SMMLV data and chart? (yes/no): ").lower
    if text == "yes":
     show_data()
    