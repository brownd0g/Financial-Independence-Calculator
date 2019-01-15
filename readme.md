==Financial Independance Calculator (FIT)==

Author : Andrew Brown

The FIT is used to calculate whether the user is financially stable enough to retire for x amount of years.

User input:

 - How much they spent last year
 - Current inflation rate (2% = 0.02)
 - How much savings the user has
 - Current interest rate for savings (5% = 0.05)
 - How many years the they want to test for

The output will be the amount of years the user will be financially independent up until the amount of years the user
wanted to test. If the output reaches a negative number before the end of the test range, the program will stop 
calculating. At the end of the program the output will tell the user whether they are financially independent
or not.

Functions:

userInput() # takes a question as a parameter then prompts the user to enter a figure. The function will test the 
	      input to check that it is both an integer or float and that it is positive. 


