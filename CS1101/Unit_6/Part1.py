""" This is a program to work with strings and lists. """





""" The following function is used for removing elements from the list until
otherwise specified. """
# Pop function used to remove a element form a list.
def poped(carsL):
    newCarsL = carsL.pop(1)

    print('List after popping a element: ')
    print(carsL)
    print('\n')


# Remove function used to remove a element from a list.
def removed(carsL):
    carsL.remove('Volvo')

    print('List after removing a element: ')
    print(carsL)
    print('\n')
    

# Del function used to remove a element form a list.
def deleted(carsL):
    del carsL[5]

    print('List after removing a element: ')
    print(carsL)
    print('\n')

""" End of the remove function. """







# Sorting function used to sort a list
def sorts(carsL):
    print('Sorted list: ')
    carsL.sort()
    print(carsL)
    print('\n')









""" The following functions are used to add elements to a list
until otherwised specified. """

# A function used to add a element with append.
def add(carsL):
    carsL.append('Ferrari')

    print('List after adding a element with the append function: ')
    print(carsL)
    print('\n')


# A function used to add a element with extend
def addMore(carsL):
    car = ['Tesla X']
    carsL.extend(car)

    print('List after adding a element with the extend function: ')
    print(carsL)
    print('\n')

# A function used to add a element with the + sign.
def addMoreMore(carsL):
    car = ['Jaguar']
    carsL += car

    print('List after adding a element with the + sign function: ')
    print(carsL)
    print('\n')

""" Finished with the add functions. """





# A function used put the list into a string.
def toString(carsL):
    delimeter = ' '
    cars = delimeter.join(carsL)

    print('Creating a string from the list: ')
    print(cars)
    print('\n')
    

def main():
    cars = 'Volvo Volkswagen Toyota Ford Kia Nissan Suzuki Honda'
    carsL = cars.split(' ')

    # Printing the original list.
    print('Original list: ')
    print(carsL)
    print('\n')


    # Calling all the function created.
    poped(carsL)
    removed(carsL)
    deleted(carsL)

    
    sorts(carsL)


    add(carsL)
    addMore(carsL)
    addMoreMore(carsL)

    toString(carsL)


    
    

# Calling the main functions.
main()

