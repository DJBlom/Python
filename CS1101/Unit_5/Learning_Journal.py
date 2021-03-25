def concat():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    suffix2 = 'uack'
    
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + suffix2)
        else:
            print(letter + suffix)
        

concat()
