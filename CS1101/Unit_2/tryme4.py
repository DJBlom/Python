def new_line():     # Function used to print one line..
    print('.')      # This is the output that every function will give
                    # it might vary in number, depending on the function being called.


def three_lines():  # Function used to print three lines.
    new_line()      # Using nested function, this function print 3 new lines.
    new_line()      
    new_line()


def nine_lines():       # Function used to print nine_lines.
    for i in range(3):  # Using a for-loop with a nested function in side it,
        three_lines()	# I print three_lines three times.


def clear_screan():     # Function used to clear the screan.
    for i in range(2):  # By using nested function technique, and a
        nine_lines()	# for-loop, I print nine and three new lines two times.
        three_lines()

    new_line()      	# By using a nested function I print one new line to bring the total
			# of new lines printed to twenty five.
    

def main(): # The main function used to call all the other functions.
    print('Printing nine new lines.')
    nine_lines()
    
    print('Clearing the screan.')
    clear_screan()

        

main()     # Calling the main function --main-- to be executed from the start.
        
    
