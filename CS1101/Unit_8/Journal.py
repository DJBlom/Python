""" This is a program to demonstrate how to read from a file into a dictionary. """
import pickle

# A function used to get data from a file and upload it to a python dictionary.
def file_to_dict():         
    d = dict()                              # Creating a empty dictionary.
    with open("input.txt") as file:         # Opening file to work with.
        for line in file:                   # Iterating over the file
            (key, val) = line.split()       # Splitting the file into keys and values.
            d[str(key)] = val               # Assigning the values to a the keys.


    return d                                # Returning the dictionary.
            


        




# A function used to conver the data of the dictionary a file.
def dict_to_file(d):
    data = invert_dict(d)                   # inverting the dictionary and assigning it to a variable.
    with open('output.txt', 'w') as file:   # Opening the file to be written to.
        for key, value in data.items():     # Iterating over the items in the dictionary
            file.write(f'Car Brand is "{key}": Car Number is "{value}".\n')     # Formatting the data and writing it to the new file.
            
    
    
    


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
    d = file_to_dict()
    dict_to_file(d)
    
    
    

    


# Calling main to be executed.
main()




    
    












