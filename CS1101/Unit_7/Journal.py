""" This is a program to demonstrate the data structure dictionary/hashtable. """

# My invented function.
def dictDemo(li):
    d = dict()                  # Declaring a dictionary.
    count = 1                   # Counter.

    for i in li:                # Iterating over the string and adding 
				# the counter to each element in the list.
        if i in li:
            d[i] = count

        count += 1


    return d                    # Returning the dictionary.




# Invert function from the text book.
def invert_dict(d):                     
     inverse = dict()                       # Declaring a dictionary.
     
     
     for key in d:                          # Iterating over the dictionary
          val = d[key]
          if val not in inverse:            # If the value of the key given is not 
					    # in the dictionary
               inverse[val] = [key]         # then assign the value to the key.
          else:
               inverse[val].append(key)     # Else add the key with it's value to 
					    # the end of the dicitonary.
               
               
     return inverse                         # Return the dictionary.




    
# Declaring the mian function used to call all other functions.
def main():
    # Creating a list for demonstration purposes.
    li = ['Dawid', 'Berta', 'Charel', 'Ben', 'Hein', 'Jacques','Bell', 'John']

    # Assigning the value return from the dictDemo function to a variable.
    d = dictDemo(li)
    print(d, '\n')

    # Assigning the value returned from the invert_dict function to a variable.
    b = invert_dict(d)
    print(b)

    


# Calling main to be executed.
main()




    
    












