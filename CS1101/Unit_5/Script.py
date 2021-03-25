""" This is a program to demonstrate the use of loops by implementing a square root function and comparing it to the math.sqrt() function. """

import math                         # Math library to be used for the math.sqrt() function.


""" This function is the self impleneted square root function used to compare the output with the math libraries square root function. """
def my_sqrt(a):                     # Declaring the function.
    x = 10                          # Assigning 'x' a value to be used.

    while True:                     # Itirating until a return value is found.
        y = (x + a / x) / 2.0       # Assigning 'y' the result of (x + a /a x) / 2.0.

        if y == x:                  # Checking if y is equal to x and if so 
            return y                # the return value is found and returned.
        
        x = y                       # Updating the loop to move on to the next.




""" This is a function used to print out 25 versions of updated information. """
def test_sqrt():                    # Declaring the function.
    
    a = 1                           # Assign 'a' a value of 1.
    while a <= 25:
        # This print statement will print 25 times with updated information.
        print(f"a = {a} | my_sqrt(a) = {my_sqrt(a)} | math.sqrt(a) = {math.sqrt(a)} | diff = {abs(my_sqrt(a) - math.sqrt(a))}")
        
        a = a + 1                   # Increment 'a' so that the loop can continue and not print the same thing for infinity.





test_sqrt()                         # Calling the test_sqrt() function to get the program started.
