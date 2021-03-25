""" Hi guys. Here is my discussion post code example. """

""" The idea of catching error is used to minimize the problems that can happen along the way of your
    program running. Therefore, if you think there might be a problem later on in your code you can use the
    try, execpt, and finally to help ease the programs flow. Furthermore, you can also give more concise
    descriptions of what caused the error. Moreover, these descriptions can help the user trouble shoot the problem"""

# Function used to open a file in read mode.
def file_except1():
    try:
        file = open('test.txt', 'r')
        contents = file.read()
        print(contents)
    except FileNotFoundError:
        print(f'No such file or directory: {file}')
    finally:
        file.close()
        print('File closed.\n')


""" FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'"""

""" This error occurs when you attempt to open a file in read mode
    but it does not exist yet. You can fix it by creating the file."""


# Function used to open a file in append mode.
def file_except2():
    try:
        with open('test.txt', 'a') as file:
            msg = 'Hello, World'
            file.write(f' {msg}\n')
        
    except PermissionError:
        print('You do not have permission to append to the file.\n')
    finally:
        print('File is closed\n')

""" PermissionError: [Errno 13] Permission denied: 'test.txt' """

""" This error occurs when you attempt to append/write to a file you do not
    have permission/ownership to. You can fix it by giving your account the
    permission/ownership needed to do the operation."""


# Function used to open a file in read mode but attempt to write to it.
def file_except3():
    try:
        with open('text', 'r') as file:
            file.write('I love coding')
    except IOError:
        print('io.UnsupportedOperation: not writable')
    finally:
        print('File closed.')

""" io.UnsupportedOperation: not writable """

""" This error occurs when you attempt to write
    to a file in read mode. You can fix this by opening the file
    in write mode instead of opening the file in read mode"""
    




# Main function used to call all other functions.
def main():
    file_except1()
    file_except2()
    file_except3()



main()
