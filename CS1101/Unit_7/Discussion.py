""" This is a program to demonstrate how tuples can be usefull loops over lists and dictionaries. """

def listZip():                                     
    st = 'Code'                            
    li = [0, 1, 2, 3]         

    print('Zip function demo.')
    t = zip(li, st)
    for i, j in t:
        print(i, j)

""" The zip function is used to iterate over two or more collections/lists in a parrallel way.
    Furthermore, the tuple collection it returns can be very useful to navigate the list """



def listEnum():
    print('\nEnumerate function demo.')
    for i, j in enumerate('Code'):
        print(i, j)
        
""" The enumerate function will iterate over list items and it's indices. """



def listItem():
    d = {0 : 'I', 1 : 'love', 2 : 'to', 3 : 'code', 4 : 'CodeForTheWin'}

    print('\nItem functions demo.')
    for i, j in d.items():
        print(i, j)
        
""" The items function will return a list of tuples/sequence of tuples that are
    mapped together with a key to the value of that key. """


    
def main():                     
    listZip()
    listEnum()
    listItem()
    
    

main()

