""" This is program to illustrate the difference between a object and a value. """

# Declaring the identical function to demonstrate what identical means.
def identical():
    """ Identical in python means that, both objects created has the same memory address.
        Both objects pointers points/refers to the same memroy address."""

    print('Identical demonstration')
    print('-----------Both has the same memory location-----------\n')
    # Object1
    str1 = 'I love coding'
    print(f'Memory Address of Object1 str1. {id(str1)} \n')

    # Object2
    str2 = 'I love coding'
    print(f'Memory Address of Object2 str2. {id(str2)} \n')
    


    # The result variable 
    result = str1 is str2
    
    # Checking if result is true or false
    if result == True:
        print('Objects Are Identical.\n')
    else:
        print('Object1, and Object2 Are Not Identical.\n')
    print('-----------End-----------\n')
    print('\n')



# Declaring the equivalent function to demonstrate what equivalent means.
def equivalent():
    """ Equivalent in python means that two objects have separate memory addresses but they
        have the same values.
        The objects pointers points/refers to separate memory addresses but they have the
        same values."""
    
    print('Equivalent demonstration')
    print('-----------Each object has a different memory location-----------\n')
    # Object1
    cars1 = ['Ferrari', 'Jaguar', 'Volvo', 'Lamborghini']
    print(f'Memory Address of Object1 cars1. {id(cars1)} \n')
    

    # Object2
    cars2 = ['Ferrari', 'Jaguar', 'Volvo', 'Lamborghini']
    print(f'Memory Address of Object2 cars2. {id(cars2)} \n')

    result = cars1 is cars2

    if result == False:
        print('Objects Are Equivalent.\n')
    else:
        print('Object1, and Object2 Are Not Equivalent.\n')
    print('-----------End-----------\n')
    print('\n')


# Declaring the function aliasing to demonstrate what happens when you aliase a variable.
def aliasing():
    """ Aliasing is the basically assigning a variable with values to another variable.
        However, if you dive deeper into this concept you will see that again when you aliase
        the second object's pointer/reference created, will point to the memory address of the first object.
        Becoming an identical twin of that object. """

    print('Aliasing demonstration')
    print('-----------Both has the same memory location-----------\n')
    # Object1
    cars1 = ['Ferrari', 'Jaguar', 'Volvo', 'Lamborghini']
    print(f'Memory Address of Object1 cars1. {id(cars1)} \n')
    

    # Object2 Gets Assigned Object1
    cars2 = cars1
    print(f'Memory Address of Object2 cars2. {id(cars2)} \n')
    print('-----------End-----------')
    print('\n')




# Declaring my ownFunction used to demonstrate what happens when a list is passed in as an argument.
def ownFunction(cars):
    """ When any object is created it's created with a memory address. When you pass a list object as an argument to a function you
        basically pass the pointer to the memory address of that list (also called a reference).
        Which means that every change you make to the list object will be to the memory address of that list.
        That means, that the list passed as an argument is not a copy of that list but rather the list it self. """

    # Printing the list unchanged.
    print('My own function demonstration')
    print('---This line is printed in the function (ownFunction).---')
    print('---This is the list before any modifications has been made to it.---')
    print(f'{cars} \n')

    # I will attempt to remove all the a's in the whole list.
    # Itirating over the list of cars.
    for i in range(len(cars)):

        # Assigning the car at element 'i' to a variable cars.
        # Making it a string.
        car = cars[i]
        
        # Itirating over the car variable holding the value of the car element at index i.
        for j in range(len(car)):

            # If the character 'a' is there,
            # then replace it with a blank,
            # append the new car value to the list cars,
            # pop the element at index i,
            # and sort the list.
            if car[j] == 'a':
                newCar = car.replace('a', '')
                cars.append(newCar)
                cars.pop(i)
                cars.sort()
                break
    
    





def main():
    cars = ['Ferrari', 'Jaguar', 'Volvo', 'Lamborghini']
    identical()
    equivalent()
    aliasing()
    ownFunction(cars)

    print('---This line is printed form main, where the list is declared.---')
    print('---This is the list after the modifications has been made to it.---')
    print(cars)


main()
