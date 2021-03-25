import math


# The code between this block is only for some extra fun.

""" By encapsulating the self square_root() function I was able to abstract it and use it in my hypotenuse2() function. """
def square_root(num):                       # Declaring my square_root() function.
    for i in range(num):                    # Running a loop that will go until the length of side3
        if i * i == num:                    # Checking if i * i equals the side
            return i                        # if it does then If conclude that it is the square_root of side3
        else:           
            i *= i                          # Else keep running and multiplying.


""" Using the same strategy but without help of the math function and object. """
def hypotenuse2(side1, side2):              # Declaring my function.
    side3 = (side1 ** 2) + (side2 ** 2)     # Assigning side 3 the values of side1 to the power of 2 and side2 to the power of 2.

    side3 = square_root(side3)              # Calling my custom square_root() function to compute the square_root of side3
        


    return side3                            # Since the square_root of side3 is the length of the hypotenuse I can just return it.

# The real program is down below.






# REAL PROGRAM.
""" The purpose of this program is to compute the Hypotenuse of a right triangle. """

""" My strategy for computing the hypotenuse of a right triangle is using the pythagoras theorem. """
def hypotenuse(side1, side2):               # Declaring my function
    side3 = pow(side1, 2) + pow(side2, 2)   # Using the pow function in the math library
                                            # This is the first part where the function gets
                                            # complex, thus I decided to print the output of side three to check if
                                            # side1 and sid2 was properly computed to the second power.
                                            
                                            # I was able to compute the side lengths of the two sides I knew.
    side3 = math.sqrt(side3)                # After that I used the sqrt object in the math library to find the
                                            # square root of the third side which in the end is the length of the third side.

    return side3                            # Lastly I return the unknown side to be presented as the hypotenuse.



def main():                                 # Defining my main function to use as a control board.
    side1 = int( input("Enter first side of triangle:\t"))          # Taking user input for the first side.
    side2 = int( input("Enter second side of triangle:\t"))         # Taking user input for the second side.

    print(hypotenuse(side1, side2))                                 # Printing the final value after calling the hypotenuse function to be executed.



main()                                                              # Calling main to set the program in motion.
