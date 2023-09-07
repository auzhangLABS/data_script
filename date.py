

print ('Congrats, you got a date')
datename = input('Enter your date name: ')
print(f'Wonderful, you on a date with {datename}')
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



bill = float(0.00)

if (float(budget) >= 1):
    print('Perfect, welcome to the Krusty Crab, here is our menu')
    print(menu)
    korder = 'y'
    order = str(input('What would you like to order: ')).lower()

    
    
    while korder == 'y':
        if order in menu:
            bill = bill + menu.get(order)
            print(f'your bill is {bill}')
            budget1 = float(budget) - float(bill)
            print(f'your remaining cash is {budget1}')
            budget1 = budget
            order == 'out'
            korder = str(input("Would you like to keep order (y or n)? ").lower())
            while korder != "y" and korder != "n":
                print('Please enter y or n')
                korder = str(input("Would you like to keep order (y or n)? ").lower())

            if(korder == 'y'):
                order = str(input('What would you like to order: ').lower())
            if(korder == 'n'):
                korder == 'n'
                budget1 = float(budget) - float(bill)
                print(f'You dinner date with {datename} was ${bill} and your remaining balance is ${budget1}')
                if(float(budget1) > 10.0):
                    print("Congrats, you can go on another date")
                else:
                    print("Please go to work")
                
        else:
            
            print('items is not in menu')
            korder = input("Would you like to keep order (y or n)? ")
            while korder != "y" and korder != "n":
                print('Please enter y or n')
                korder = str(input("Would you like to keep order (y or n)? ").lower())
            if(korder == 'y'):
                order = str(input('What would you like to order: '))
            budget1=budget
            if(korder == 'n'):
                korder == 'n'
                budget1 = float(budget) - float(bill)
                print(f'You dinner date with {datename} was ${bill} and your remain balance is ${budget1}')
                if(float(budget1) > 10.0):
                    print("Congrats, you can go on another date")
                else:
                    print("Please go to work")

            

else:
    print("You can't afford a date")
