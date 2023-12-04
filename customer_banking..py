# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():

    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
# Prompt the user to set the savings balance, interest rate, and months for the savings account.
# ADD YOUR CODE HERE
# Add blank lines
print()
print()

print("Welcome to the Brannon Family Bank!")
print("------------------------------------")
print("We are happy to help you with your savings account.")
savings_balance = float(input("What is the savings account balance? "))
savings_interest = float(input("What is the current savings account interest rate? " ))
savings_maturity = int(input("How many months will the savings account be held? "))

updated_savings_balance = 0    
interest_earned, updated_savings_balance = create_savings_account(savings_balance, savings_interest, savings_maturity)

# Add blank lines
print()
print()

    # Call the create_savings_account function and pass the variables from the user.
create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print("The interest earned is $", updated_savings_balance, "and the updated savings account balance is $", interest_earned)
   
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # Add blank lines
print()
print()  
print("Do you have a CD account? We can help you with that as well...")
cd_balance = float(input("What is the current CD account balance? "))
cd_interest = float(input("what is thre current CD account interest rate? "))
cd_maturity = int(input("How many months will the cd account be held? "))


updated_CD_balance = 0
interest_earned, updated_CD_balance = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Add blank lines
print()
print() 
    # Call the create_cd_account function and pass the variables from the user.
create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
print("The interest earned on your CD is $", interest_earned, "and the new CD balance is $", updated_CD_balance)
# Add blank lines
print()
print() 
print("Thank you for banking with us today. Have a great day!")

if __name__ == "__main__":

    # Call the main function.
    main()