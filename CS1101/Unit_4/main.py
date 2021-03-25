""" This is a function to check whether or not two integers are divisible """

def is_divisible(num1, num2):               # Declaring the function.
    if (num1 % num2) == 0:                  # If there are no remainder after deviding num1 and num2
        return True                         # then the condition is true else the condition is false.
    else:
        return False


""" This is a function to recursively compute one int is a power of another int. """
def is_power(num1, num2):                                                       # Declaring the function.                 
    if num2 == 1:                                                               # First base case checks if the second argument given is 1.
        return num1 == 1                                                        # If it is 1 then return the opesite argument == 1.
    elif num1 == num2:                                                          # Else if the two arguments are the same.
        return num1 == num2                                                     # Then return, they are equal.
    else:                                                       
        return is_divisible(num1, num2) and is_power(num1 / num2, num2)         # else call the is_power() function recursively
                                                                                # with the is_divisible() function
                                                                                # By calling is_power() recursively you will keep deviding
                                                                                # num1 with num2 and until
                                                                                # the is_divisible() function returns false
                                                                                # and one of the base cases are reached.
        

""" This is the main function used to call all the other functions from and print the values hard coded in. """
def main():
    
    print("is_power(10, 2) returns: ", is_power(10, 2))                 # Values hard Coded in.
    print("is_power(27, 3) returns: ", is_power(27, 3))
    print("is_power(1, 1) returns: ", is_power(1, 1))
    print("is_power(10, 1) returns: ", is_power(10, 1))
    print("is_power(3, 3) returns: ", is_power(3, 3))


main()          # Calling the main function.




