#Functions
#1. Declare a function named evens_and_odds . 
#It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):

    even = 0
    odd = 0    
    for i in range(num):
        if i % 2 == 0:
            even +=1
        else:
            odd +=1
    return print(f"The number of evens are {even}, and the number of odds are {odd}")


while True:
    user_input = input('Insert a positive integer: ')

    if user_input.isdigit() and int(user_input) > 0:
        evens_and_odds(int(user_input))
        break  # ✅ Exit loop once valid input is received
    else:
        print('Invalid input! Please insert a positive integer greater than 0.')