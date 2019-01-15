
# This function is used to make sure user inputs a valid number for each question

def validInput(question):

    UI = input(question)

# The following will run until a positive real number is entered
    while True:
        try:
            num = float(UI)
            while num < 0:
                num = float(input("Error: Please enter a positive real number: "))          
            
        except ValueError:                                                      
            UI = input("Error: Please enter a positive real number: ")
            continue

        else:
            return num
            break
    
# Use function to ask for input
expenses = validInput("How much did you spend last year to support your current lifestyle? ")   
inf_rate = validInput("Please enter the expected inflation rate: ")
savings = validInput("How much do you currently have saved for investment? ")
interest = validInput("What is the expected average annual interest rate? ")
test_years = int(validInput("How many years do you want to test? "))        

# Print the header
print("Year     Remaining Balace")

# For loop to calculate each year
for x in range(0, test_years):
    if savings > 0:
        expenses = expenses + (expenses * inf_rate)                         # Adds inflation to expenses
        savings = savings - expenses                                        # Subtracts expenses from savings
        savings = savings + (savings * interest)                            # Adds interest onto savings

        if (x+1) < 10:
            print("", x+1, "     ", format(savings, '0.2f'))                # Prints out current balance to two decimal places
        else:
            print("", x+1, "    ", format(savings, '0.2f'))                 # Loses a space for formatting purposes

    else:
        print("Not financially independant!")                               # Waits for user input before exiting                  
        input("Press enter to exit")
        exit()
    

print("Financially independant!")
input("Press enter to exit")
exit()


