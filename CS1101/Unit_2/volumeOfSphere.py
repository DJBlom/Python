def print_volume(radius):                           # This function is used to get the volume of a sphere.
    pi = 3.141592653589793                          # Stating the value of pi to use as a variable.
    result = (4 / 3) * pi * radius ** 3             # Algorithm used to find the volume of a sphere.

    print('Volume of sphere is:>\t'f"{result:.2f}") # Printing to stdout the volume of a sphere up to 2 decimal places.




def main():                                             # Main function used in this program.
    radius = int(input('Enter radius of sphere:\t'))    # Asking user for input.

    print_volume(radius)                                # Calling the print_volume function to be executed.



main()
