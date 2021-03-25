""" The purpose of this program is to demonstrate the function I created.
This function will compute the average of three test scores. """

def average(list):          # Declaring my function to compute the average.
    """ So I had to initialize the ave variable otherwise I was getting a error
stating that the local variable ave was referenced before assigning."""
    ave = 0                 # Initializing the ave veriable to 0
    
    """ By itirating over the range of the list I am able to access each element of the list
with 'i' so that they can be added to the local variable ave."""
    for i in range(3):      # Itirating over up untill the last score.
        ave += list[i]      # Adding all the list scores together.

    """ All I had to do then was devide the variable ave by the amount of elements in the lis
to return the average."""

    return ave / 3          # Returning the average of the scores.



def main():                 # Declaring the main function.
    """ This was somewhat of a strange one, since I normally declare my lists with
list[3]; However, in python I had to do it like this. Furthermore, I had to initialize the
list before using it, which to me, was quite strange since in python you normally don't declare
and then use but just use. """
    list = []               # Initializing the list.
    for i in range(3):      # Itirating over the list up until the 3 test scores.
        """ This was also a strange one to me since I could not let the user input the scores
straight into the list, I had to use a local variable to hold the score before adding it to the list."""
        score = int(input("Enter test score:\t"))   # Taking user input for the list.

        """ Since I coult not just say list[i] += score, I had to find another way of duing it.
so further research led me to believe I had to use a object to append it to the back of the list.
So I took a gamble and try append since thats the one we use in c++ as well to append strings though.
However it worked and I went with it. """
        list.append(score)  # Appending each score to the end of the list.

    print(average(list))    # Printing the average of the scores entered after calling the average function.

main()                      # Calling main to be executed.



# Input for the 'ave' variable with the error received.
# Enter test score:	4
# Enter test score:	5
# Enter test score:	6
# UnboundLocalError: local variable 'ave' referenced before assignment

# Input for the trying to store the scores in the list right away with error received.
# Enter test score:	4
# TypeError: 'type' object does not support item assignment

# Input for the final and accurate computing of the average.
# Enter test score:	55
# Enter test score:	96
# Enter test score:	78
# Output: 76.33333333333333





