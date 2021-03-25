def myFunction(kilometers, fuelusage, carType): # Function to calculate the fuel consuption of a vehicle.
    result = kilometers / fuelusage             # Algorithm used to calculate it.

    print(f"Your {carType} gave {result:.1f}ltr, per kilometer.")



def main(): # Main function used to take user input and call the other function.
    kilometers = float(input('Enter amount of kilometers driven:\t'))
    fuelusage = float(input('Enter fuel consumption:\t'))
    carType = input('Enter type of car:\t')
    
    myFunction(kilometers, fuelusage,carType)


main() # Calling other function.
