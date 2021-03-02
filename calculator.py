print("Welcome to the calculator made by Atif")
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
**for power
% for modulo
// for getting  floor division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    try:
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)

        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)

        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
        elif operation == '':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 ** number_2)
        elif operation == '//':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 // number_2)
        elif operation == '%':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 % number_2)
        else:
            print('You have not typed a valid operator, please run the program again and try again.')
    except ZeroDivisionError:
        print("You cannot divide a number with 0")

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()