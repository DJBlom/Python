

""" This program to display Nested lists,
The '*' operator, List slices, The '+=' operator,
A list filter,
and a legal operation that does the opposite of what the programmer wanted. """


# A function used to demonstrate a nested list.
def nested():
    carsCats = ['Volvo', 'Volkswagen', 'Toyota',
                'Jaguar', 'Suzuki', 'Nissan',
               ['Black Cats', 'Pink Cats', 'Blue Cats',],
                'Kia', 'Honda']

    print('Demonstration of the  nested list: ')
    print(carsCats)
    print('\n')



# A function to demonstrate how the astrix operator is used in a list.
def astrix():
    cars = ['Volvo', 'Volgswagen', 'Toyota',
                'Jaguar', 'Suzuki', 'Nissan',
                'Kia', 'Honda']
    cars[2] *= 2

    print('Demonstrating the *= operator: ')
    print(cars)
    print('\n')




# A function used slice a list.
def sliced():
    cars = ['Volvo', 'Volgswagen', 'Toyota',
                'Jaguar', 'Suzuki', 'Nissan',
                'Kia', 'Honda']
    newCars = cars[3:5]

    print('Demonstrating the use of list slicing: ')
    print(newCars)
    print('\n')



# A function used to demonstrate the += operator.
def plus():
    cars = ['Volvo', 'Volkswagen', 'Toyota',
                'Jaguar', 'Suzuki', 'Nissan',
                'Kia', 'Honda']
    
    cars[2] += 'Hilux'

    print('Demonstrating the += operator: ')
    print(cars)
    print('\n')



# A function used to check if a element is in a list.
def filters():
    cars = ['Volvo', 'Volkswagen', 'Toyota',
                'Jaguar', 'Suzuki', 'Nissan',
                'Kia', 'Honda']

    print('Demonstrating of traversing a list and finding elements:')
    for i in range(len(cars)):
        if cars[i] == 'Toyota':
            print(f'Found the brand at index {i}')

    print('\n')




# A function used to demonstrate a list operation that does not do what the programmer
# but that is legal.
def legalButNotGood():
    theSum = 1
    
    for i in range(10):
        theSum *= i

    print('The sum of One is')
    print(theSum)
        




# A main function used to controll all the other functions.     
def main():
    nested()
    astrix()
    sliced()
    plus()
    filters()

    # This function is suppose to be 45 but it give zero
    # You can fix it by replacing the * operator with the + operator.
    legalButNotGood()
    
    


main()





            
    























    
