# Calculator
# making functions

def addition(x, y):
    return x + y


# subtract
def subtraction(x, y):
    return x - y


# multiply
def multiplication(x, y):
    return x * y


# divide
def division(x, y):
    return x / y


dict_calculator = {'+': addition,
                   '-': subtraction,
                   '/': division,
                   '*': multiplication
                   }
run_again = True
while run_again is not False:
    num1 = int(input("whats the first number?"))
    num2 = int(input("whats the second number?"))
    operation = input("whats the operation you want to perform?")

    for each in operation:
        print((dict_calculator[each](num1, num2)))
    question = input("do you want to run again? reply 'y for yes or 'n' for no")

    if question == 'n':
        run_again = False
    elif question == 'y':
        run_again = True
    else:
        print("invalid answer. please try again")
        run_again = True
