""" This is a program to check if there are duplicate characters in a
    list of strings. """


""" PART 1 """
# Declaring the histogram function given by the Professor.
def histogram(s):
    # Declaring a empty dictionary.
     d = dict()

     # Iterating over the function argument string.
     for c in s:
         # If there is one of these characters in the string then
         # assign the value one to it.
          if c not in d:
               d[c] = 1

         # Else if there are two of the same characters to the string then
         # add one to it/increment it.
          else:
               d[c] += 1

     # Return the dictionary.
     return d


# Declaring the has_duplicates() function.
def has_duplicates(s):
    # Calling the histogram function and
    # assigning the return value to a variable.
    com = histogram(s)

    # Iterating over the values associated with the
    # dictionary returned by histogram.
    for i in com.values():
        # if the value return from the histogram function is greater
        # than 1 keep itirating over the list else return True.
        if i > 1:
            return True
    return False
       



""" PART 2 """
# Global variable alphabet.
ALPHABET = "abcdefghijklmnopqrstuvwxyz" 


# Declaring the missing_letters function.
def missing_letters(s):
    # Making sure that the global variable gets seen as a global variable.
    global ALPHABET

    # Assigning the global variable to a local variable since it will change.
    result = ALPHABET

    # Calling the histogram function to use and compare the characters.
    com = histogram(s)

    # Iterating over the return value of histogram and sorting it in
    # alphabetical order.
    com = sorted(com)
    for i in com:
        if i in ALPHABET:
            result = result.replace(i, '')
    return result
              


# Declaring the main function used in this program.
def main():
    """ PART 1 """
    print('Part 1')
    # Creating the test_dubs list of strings.
    test_dubs = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]

    # Iterating over the list and checking each element if
    # there are any duplicates in the string.
    for s in test_dubs:   
        if has_duplicates(s):
            print(f'{s} has duplicates')
        else:
            print(f'{s} has no duplicates.')

    """ PART 2 """
    print('\nPart 2')
    # Creating a list of random letters.
    test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

    # Iterating over the list of random characters and checking which letter of the
    # alphabet is missing.
    for i in test_miss:
        if len(missing_letters(i)) == 0:
            print(f'{i} uses all the letters.')
        else:
            print(f'{i} is missing these letters {missing_letters(i)}')
    
   

main()

