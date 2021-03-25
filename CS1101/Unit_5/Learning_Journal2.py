def slice1(string):             # Declaring the function slice 1.
    begin = 5                   # Assigning 5 to the variable begin. This will be the place that the slicing begins.
    end = len(string)           # Assigning the full length of the string to end.
    return string[begin:end]    # Return the sliced piece from index 4 up to the end of the string.


def slice2(string):             # Declaring the function slice 2.
    begin = 10                  # Assigning 10 to the variable begin.
    return string[begin:]       # Returning the sliced piece to be printed to stdout.
    


def slice3(string):             # Declaring the function slice 3.
    end = 10                    # Assigning 10 to the variable end. This is the place where the slice will end.
    return string[:end]         # Returning the sliced piece to be printed to stdout.



def main():                     # Declaring the main method used to controll and call the other methods.
    string = "I love coding and computer science."      # Declaring the string used in this program
    

    print(slice1(string))       # Calling and printing all the function.
    print(slice2(string))
    print(slice3(string))



main()                          # Calling the main function.
