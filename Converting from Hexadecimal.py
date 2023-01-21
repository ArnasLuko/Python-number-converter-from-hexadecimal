#The program takes a number in base 10 and a base supplied by the user, both positive ints, and returns the number in the base supplied by the user.
#It first asks the user for two integers.
#A function is then defined for converting the first number provided by the user in a base of the second number provided.
#The function first creates a list varaible to hold of the results of the function.
#A while loop is used to itterate over the characters of the first number provided by the user.
#A list is created for converting numbers to characters in hexidecimal and higher.
#The function then divided the number by the base.
#The remainder of the division is then checked to be >10, if it is higher than 10, then the figure is converted to a letter character.
#The remainder is then sent to the emptry string created earlier.
#The function then takes the result of the division and divides by the base again, untill the number raches 0.
#The function then cycles through the list using a for loop, and prints the resulting characters as one string.
#The program then calls the function on the two numbers given by the user intially.

num = int(input("Give me an number (an integer); "))
base = int(input("Now give me a base (an integer); "))


def baseten(x, y):
    '''Function converts numbers from base 10 (x), to a different number in a base given by the user (y). Does this using a while loop to apply operators according to a formula. Letters are converted accordingly.'''
    ans = 0
    answer = list('')
    while x > 0:
        letters = (str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"))
        ans = x // y
        rem = x % y
        if rem > 10:
            rem = str(letters[rem-10])
            answer.insert(0, rem)
        elif rem < 10:    
            answer.insert(0, rem)
        x = ans 
    for i in answer:
        print(i, end="")
        
baseten(num, base)


