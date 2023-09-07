
#start by asking the user whats your date name
print ('Congrats, you got a date')
datename = input('Enter your date name: ')
print(f'Wonderful, you on a date with {datename}')
#asking the user for their budget for the date
budget = input("What's your budget for the date? ")

menu = {
    'krabby patty' : 2,
    'krabby patty with cheese' : 2.5,
    'double krabby patty' : 2.5,
    'double krabby patty with cheese' : 3.0,
    'small coral bits' : 1.0,
    'medium coral bits' : 1.5,
    'large coral bits' : 2.0,
    'kelp rings' : 1.50,
    'kelp shake' : 1.25
}
#setting bill to be a float because of dollar amount
bill = float(0.00)

#starting the if statement here if the person has 5 dollars or more then they can dine at the Krusty Crab 
if (float(budget) >= 5):
    print('Perfect, welcome to the Krusty Crab, here is our menu')
    print(menu)
    #setting a order to y so it can enter the while loop
    korder = 'y'
    #asking the user what they would like to order
    order = str(input('What would you like to order: ')).lower()

    # Enter a while loop where it keeps looping until korder or user chooses to stop ordering, selecting no
    while korder == 'y':
        #check if what the user order and check if we have that in our menu
        if order in menu:
            #totalling up the bill
            bill = bill + menu.get(order)
            print(f'your bill is {bill}')
            #deleting it from budget
            budget1 = float(budget) - float(bill)
            #printing out remaining cash on hand
            print(f'your remaining cash is {budget1}')
            budget1 = budget
            #setting order to something outside the menu to get out of this if statement
            order == 'out'
            #prompting the user if they would like to order more or no
            korder = str(input("Would you like to keep order (y or n)? ").lower())
            #only accepting y or n, if the user don't select y or no then it goes into a while loop that keeps prompting the user to select the right answer
            while korder != "y" and korder != "n":
                print('Please enter y or n')
                korder = str(input("Would you like to keep order (y or n)? ").lower())
            #if user select y then it goes to order
            if(korder == 'y'):
                order = str(input('What would you like to order: ').lower())
            # If user selects n then it calculates the bill and how was remaining
            if(korder == 'n'):
                korder == 'n'
                budget1 = float(budget) - float(bill)
                print(f'You dinner date with {datename} was ${bill} and your remaining balance is ${budget1}')
                # If user have more than 10$ then they can go on another date
                if(float(budget1) > 10.0):
                    print("Congrats, you can go on another date")
                # if they don't have more than 10$ then it will prompt them to work
                else:
                    print("Please go to work")
        #else statement if the user order something not on the menu     
        else:
            # Let the user know 
            print('items is not in menu')
            #asking the user if they would like to order again
            korder = input("Would you like to keep order (y or n)? ")
            #onlying accepting y and n or it will go into a while loop
            while korder != "y" and korder != "n":
                print('Please enter y or n')
                korder = str(input("Would you like to keep order (y or n)? ").lower())
            # if the user wants to continue ordering
            if(korder == 'y'):
                order = str(input('What would you like to order: '))
            budget1=budget
            #if the user dont want to continue ordering 
            if(korder == 'n'):
                korder == 'n'
                budget1 = float(budget) - float(bill)
                #let them know how much it was and how much was left over
                print(f'You dinner date with {datename} was ${bill} and your remain balance is ${budget1}')
                if(float(budget1) > 10.0):
                    print("Congrats, you can go on another date")
                else:
                    print("Please go to work")

            

else:
    print("You can't afford a date")
