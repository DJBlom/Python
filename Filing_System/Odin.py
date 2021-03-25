# This is a program for my dad to help with his filing system.


# All the imports used in this program.
import sqlite3


# Log in function.
def Login():
    
    # Opening the connection to sqlite3 database 
    # Creating cursor to access databse content.
    print("\n")
    print("Logg-in_Menu:")
    conn = sqlite3.connect("odin.db")
    c = conn.cursor()
    
    # Forcing user to only have 3 chances of logging in.
    count = 0
    for i in range(3):
        print("Please Enter Your Login Details.")
        username = input("Username: ")
        password = input("Password: ")
        
        # Executing sql query to check if the username and password is in the database.
        # If not forcing user to try again or to quit.
        search_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        c.execute(search_user, [(username), (password)])
        
        results = c.fetchall()
        
        if results:
            for i in results:
                print("\n")
                print("Welcome To ODIN,", username)
            break
        else:
            print("\n")
            print("Wrong Username OR Password!\n")
            again = input("Try Again, Yes/No: ")             
            
            if again.lower() == "no":
                print("\n")               
                print("Goodbye")
                return exit()
    
        count += 1
    
    # If user has tried to loging more than 3 times the program will exit.
    if count == 3:
        print("\n")
        print("You Have Exeded Your Chances!")
        c.close()                  
        conn.close()
        print("\n")
        print("Goodbye!")        
        return exit()





# Add or update user information.
def Add_Update_User():
    print("\n")
    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")

    # Creating a list to choose from.
    print("Add_User:")
    options = ["Add_User", "Update_User", "Main_Menu", "Quit"]
    
    # If a choice he made is not in the list the user will be prompted again to choose.
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("\n")
                print("You Chose Poorly!\n")
                break
        
        # If user chose one.
        if choice == 1:
            try:
                # Connection to database is opened
                conn = sqlite3.connect("odin.db")
                c = conn.cursor()
                
                # When trying to add a user to the system it will first check if the user
                # is not already in the system. If user is in the system then the user will be prompted to try again
                # else user will be granted to use the username chosen.
                found = 0
                while found == 0:
                    print("\n")
                    print("Check If Username Is Available.")
                    username = input("Username: ")     
                    
                    # Query to check if username is available.
                    add_user = ("SELECT * FROM user WHERE username = ?")
                    c.execute(add_user, [(username)])
                    
                    # Forcing user to only have three atempts.
                    for i in range(3):
                        if c.fetchall():
                            print("\n")
                            print("Username Not Available. Try Again.")
                        else:
                            found = 1
                
                # If username availble. Continue to give name surname and password.
                print("\n")
                print("Enter New Users Details.")
                name = input("First Name: ")
                surname = input("Last Name: ")
                password = input("Password: ")
                password1 = input("Re-Enter Password: ")
                date = input("Enter Data: ")
                
                # Checking that the password given matches.
                while password != password1:
                    print("\n")
                    print("Passwords Did Not Match.") 
                    pirnt("Please Try Again.")
                    password = input("Password: ")
                    password1 = input("Re-Enter Password: ")
                
                # If all is good user is added to the db with this query.
                add_user = ("INSERT INTO user(name, surname, username, password, date) VALUES(?, ?, ?, ?, ?)")
                c.execute(add_user, [(name), (surname), (username), (password), (date)])
                
                # Finaly check to make sure the user wants to add the new user.
                answer = input("Do You Want To Save? Yes/No: ")
                if answer.lower() == "yes": 
                    conn.commit()   
                    print("\n")
                    print("User Add Successfull!\n")                   
                else:
                    print("\n")
                    return Add_User()

            # If any sql errors accured exit with sql error message.
                c.close()
            except sqlite3.Error as error:
                print("\n")
                print("Failed To Add User.\n")
            
            # Finally closing connection and returning to This menu.
            finally:
                if (conn):
                    conn.close()
                    print("\n")

        elif choice == 2:
            # Open database connection and cursor.
            conn = sqlite3.connect("odin.db")
            c = conn.cursor()
            
            # Asking user to input their information.
            print("\n")
            print("Enter User Details.")
            name = input("First Name: ")
            surname = input("Last Name: ")
            username = input("Username: ")
            password = input("Password: ")           

            # Checking if user is in the database.
            search_client = ("SELECT user_id FROM user WHERE name = ? AND surname = ? AND username = ? AND password = ?")
            c.execute(search_client ,[(name), (surname), (username), (password)])            
            
            # if user is in the database they are asked to give their new informaton to be updated.
            user_id = c.fetchall() 
            if user_id: 
                print("(ID)")
                print(user_id)
                                
                Nname = input("New First Name: ")
                Nsurname = input("New Last Name: ")
                Nusername = input("New Username: ")
                Npassword = input("New Password: ") 
                
                u_id = None
                while u_id == None:
                    try:
                        # Cheking that the user only provides their id ind integer format and not alphabetical format.
                        u_id = int(input("Enter Client ID: "))                
                        update_user = ("UPDATE user SET name = ?, surname = ?, username = ?, password = ? WHERE user_id = ?")
                        c.execute(update_user, [(Nname), (Nsurname), (Nusername), (Npassword), (u_id)])
                        
                        # Final check to make sure user wants to add the new information.
                        answer = input("Are You Sure You Want To Update User? Yes/No: ")
                        if answer.lower() == "yes": 
                            conn.commit()
                            print("\n")
                            print("User Update Successfull!\n")
            
                        else:
                            print("\n")
                            print("User Not Found.")
                    # Standard slq error message if not the right value.
                    except ValueError:
                        print("\n")
                        print("ID Must Be A Number!\n")
                        return Add_Update_User()

            # Finally closing the sql connection.
            conn.close()
            print("\n")
        
        # Returns to main menu.
        elif choice == 3:
            print("\n")
            return main()
        
        # Quits program completely.
        elif choice == 4:
            print("\n")
            print("Connection To Database Closed!\n")
            print("Goodbye!")
            return exit()



# Function to Remove a user.
def Remove_User():
    print("\n")
    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")

    # List of options you can do.
    print("Remove_User:")
    options = ["Remove_User", "Main_Menu", "Quit"]
    
    # Checking that the user only chooses an option thats listed in the list.
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("\n")
                print("You Chose Poorly!\n")
                break

        # Choice one is Removing the user.
        if choice == 1:
            try:
                # Opening the database connection.
                conn = sqlite3.connect("odin.db")
                c = conn.cursor()
                
                # Searching for user in the database.
                print("\n")
                print("Enter User To Be Deleted Details")
                name = input("First Name: ")
                surname = input("Last Name: ")            

                remove_user = ("DELETE FROM user WHERE name = ? AND surname = ?")
                c.execute(remove_user, [(name), (surname)])
                
                # Final check before deleting the user.
                answer = input("Are You Sure You Want To Remove User? Yes/No: ")
                if answer.lower() == "yes":  
                    conn.commit()
                    print("\n")
                    print("User Remove Successfull.\n")

                # if answer is no the user is returned to the list of option.
                else:
                    print("\n")
                    return Remove_User()

                c.close()
            # Standard sql error message.
            except sqlite3.Error as error:
                print("\n")
                print("Failed To Remove User.\n")
            
            # Finally closing the database connection.
            finally:
                if (conn):
                    conn.close()
                    print("\n")
        # Return to main menu for more option.
        elif choice == 2:
            print("\n")
            return main()

        # Exit program completely.
        elif choice == 3:
            print("\n")
            print("Connection To Database Closed!\n")
            print("Goodbye!")
            return exit()
          




def Search_User():
    # Name of program.

    print("\n")
    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")
    
    # List of options user can do.
    print("Search_User:")
    options = ["Search_User", "Main_Menu", "Quit"]

    # Checking that the user only chooses an option thats listed in the list.
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("\n")
                print("You Chose Poorly!\n")
                break
        # Searching for a user in the database 
        if choice == 1:
            try:
                # Creating the connection to the database.
                conn = sqlite3.connect("odin.db")
                c = conn.cursor()
                
                # Asking who to search for.
                print("\n")
                print("Enter User Details to Search.")
                name = input("First Name: ")
                surname = input("Last Name: ")
                
                # Sending the query to sqlite3
                search_user = ("SELECT * FROM user WHERE name = ? AND surname = ?")
                c.execute(search_user, [(name), (surname)])            
            
                # Printing out the data searched for.
                print("\n")
                print("(ID | NAME | SURNAME | USERNAME | PASSWORD | DATE JOINED)")
                [print(row) for row in c.fetchall()]

                c.close()
            
            # Standard sqlite3 error if error accured.
            except sqlite3.Error as error:
                print("\n")
                print("Failed To Find User.")
            
            # Finally closing the connection to the database.
            finally:
                if (conn):
                    conn.close()
                    print("\n")


        # Return to the main menu.   
        elif choice == 2:
            print("\n")
            return main()
        
        # Quits the program completely.
        elif choice == 3:
            print("\n")
            print("Connection To Database Closed!\n")
            print("Goodbye!")
            return exit()



def Search_Client():
    # Name of the program.

    print("\n")
    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")
    
    # List of option.
    print("Search_Client:")
    options = ["Search_Client", "Main_Menu", "Quit"]
    
    # Checking that the user only chooses an option thats listed in the list.
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("\n")
                print("You Chose Poorly!\n")
                break

        # Searching for a client in the database.
        if choice == 1:
            try:
                # Openning a connction to the database.
                conn = sqlite3.connect("odin.db")
                c = conn.cursor()
                
                # Ask user for the name and surname of the client to search for.
                print("\n")
                print("Enter Client Details.")
                name = input("Company Name/First Name: ")
                surname = input("Last Name: ")
                
                search_client = ("SELECT * FROM client WHERE name = ? AND surname = ?")
                c.execute(search_client, [(name), (surname)])

                # Printing the information out.
                print("\n")
                print("ID | NAME | SURNAME | EMAIL | MOBILE NUMBER | DATE JOINED")
                [print(row) for row in c.fetchall()]
                
                # Checking the user inputs client id to check in the linked DATA TABLE that the work id corresponds.
                wid = None
                while wid == None:
                    try:
                        # When client id is inputed the work that has been done for that client is displayed.
                        print("Enter ID To See Work Done For Client.")
                        wid = int(input("Client_ID: "))

                        search_work = ("SELECT Price_Paid, work FROM work JOIN client ON work.c_id = client.client_id WHERE client_id = ?")
                        c.execute(search_work, [(wid)]) 

                        print("\n")
                        print("PRICE_PAID | WORK_DONE")
                        [print(row) for row in c.fetchall()]
                    # Standard sql error message.
                    except ValueError:
                        print("Must Be A Number.")
                        break


                c.close()
            # Standard sql error message.
            except sqlite3.Error as error:
                print("\n")
                print("Failed To Find Client.\n")
            
            # Finally closing the database connection.
            finally:
                if (conn):
                    conn.close()
                    print("\n")
        # Return Main menu.        
        elif choice == 2:
            print("\n")
            return main()
        
        # Quits the program completely.
        elif choice == 3:
            print("\n")
            print("Connection To Database Closed!\n")
            print("Goodbye!")
            return exit()


    

# Add or update a clients details.
def Add_Update_Client():
    # Program name.

    print("\n")
    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")
    
    # List of options the user can do.
    print("Add_Update_Client:")
    options = ["Add_Work", "Add_Client", "Update_Client", "Main_Menu", "Quit"]
    
    # Checking that the user only chooses an option thats listed in the list.
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("You Chose Poorly!\n")
                break
        
        # Add a work information to an existing client. 
        if choice == 1:

            # Openning the connection to the database.
            conn = sqlite3.connect("odin.db")
            c = conn.cursor()
            
            # Asking user who to add the work description to.
            print("\n")
            print("Enter Client Details.")
            name = input("Company Name/First Name: ")
            surname = input("Last Name: ")
            
            search_client = ("SELECT * FROM client WHERE name = ? AND surname = ?")
            c.execute(search_client, [(name), (surname)])
            
            print("\n")
            print("(ID | NAME | SURNAME | EMAIL | MOBILE NUMBER | DATE JOINED)")
            [print(row) for row in c.fetchall()]
            
            
            # Input the id of the client and if not id inputed the program will return to this point.
            print("\n")
            print("Enter Work Done For Client.")
            c_id = None
            while c_id == None:
                try:
                    c_id = int(input("Client ID: "))
                    price = input("Price Paid For Work: ")
                    work = input("Work Description: ")
                    date = input("Enter Date: ")

                    update_work = ("INSERT INTO work(c_id, price_paid, work, date) VALUES(?, ?, ?, ?)")
                    c.execute(update_work, [(c_id), (price), (work), (date)])
                    
                    # Final user check to make sure they want to save the changes.
                    # Closing the database connection after saving.
                    answer = input("Do You Want To Save? Yes/No: ")
                    if answer.lower() == "yes":  
                        conn.commit()
                        conn.close()
                        print("\n")
                        print("Job Card Add Successfull.\n")
                    else:
                        print("\n")
                        return Add_Update_Client()

                # Standard sql error message.
                except ValueError:
                    print("\n")
                    print("ID Must Be A Number!\n")
                    return Add_Update_Client()
        
        # Adding a new client to the database.
        elif choice == 2:
            try:
                # Openning a connection to the database
                conn = sqlite3.connect("odin.db")
                c = conn.cursor()
                
                # Asking user for clients details and adding the data to the datebase.
                print("\n")
                print("Enter Client Details.")
                name = input("First Name: ")
                surname = input("Last Name: ")
                email = input("Email: ")
                mobile = input("Mobile Number: ")
                date = input("Enter Date: ")
                
                add_client = ("INSERT INTO client(name, surname, email, mobile, date) VALUES(?, ?, ?, ?, ?)")
                c.execute(add_client, [(name), (surname), (email), (mobile), (date)])

                # Asking the user if they want to save the changes.
                # If yes saving and closing the database returning to list.
                # If no returning to the list.
                answer = input("Are You Sure You Want To Remove User? Yes/No: ")
                if answer.lower() == "yes": 
                    conn.commit()
                    print("\n")
                    print("Client Add Successfull!\n")

                c.close()            
            # Standard sql error message.
            except sqlite3.Error as error:
                print("\n")
                print("Failed To Add Client.")
            
            # Finally closing the connection.
            finally:
                if (conn):
                    conn.close()
                    print("\n")
        
        # Update existing clients data.
        elif choice == 3:
            # Openning the database connection.
            conn = sqlite3.connect("odin.db")
            c = conn.cursor()
            
            # Asking user to search for the client they want to update.
            print("\n")
            print("Enter Client Details.")
            name = input("First Name: ")
            surname = input("Last Name: ")
            email = input("Email: ")
            mobile = input("Mobile Number: ")                                    
            
            search_client = ("SELECT client_id FROM client WHERE name = ? AND surname = ? AND email = ? AND mobile = ?")
            c.execute(search_client ,[(name), (surname), (email), (mobile)])            
            
            # Checking that the client is in the system and updating the clients data according to their id.
            client_id = c.fetchall() 
            if client_id: 
                print("(ID)")
                print(client_id)

                # Asking for the new clients details.                
                Nname = input("New First Name: ")
                Nsurname = input("New Last Name: ")
                Nemail = input("New Email: ")
                Nmobile = input("New Mobile: ") 
                date = input("Date Of Update: ")
                
                # Making sure the id is of integer value and not alphabetical.
                c_id = None
                while c_id == None:
                    try:
                        # Updating the clients information.
                        c_id = int(input("Enter Client ID: "))                
                        update_client = ("UPDATE client SET name = ?, surname = ?, email = ?, mobile = ? AND date = ? WHERE client_id = ?")
                        c.execute(update_client, [(Nname), (Nsurname), (Nemail), (Nmobile), (date), (c_id)])

                        # Final Check for user to make sure they want to save the changes.
                        answer = input("Are You Sure You Want To Update User? Yes/No: ")
                        if answer.lower() == "yes": 
                            conn.commit()
                            print("\n")
                            print("Client Update Successfull!\n")
            
                        else:
                            print("\n")
                            print("User Not Found.")

                    # If value is not of integer type return to list with a message.
                    except ValueError:
                        print("\n")
                        print("ID Must Be A Number!\n")
                        return Add_Update_Client()
            
            # Closing the database connection.
            conn.close()
            print("\n")
                    
        # Return to main menu.                                        
        elif choice == 4:
            print("\n")
            return main()
        # Quits program completely.
        elif choice == 5:
            print("\n")
            print("Connection To Database Closed!\n")
            print("Goodbye!")
            return exit()




def Remove_Client():
    # Pragram name.

    print("\n")
    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")
    
    # Options list.
    print("Remove_Client:")
    options = ["Delete_Client", "Main_Menu", "Quit"]

    # Checking that the user only chooses an option thats listed in the list.
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("You Chose Poorly!\n")
                break
        
        # Remove Client from database.
        if choice == 1:
            try:
                # Openning connection to database.
                conn = sqlite3.connect("odin.db")
                c = conn.cursor()
                
                # Asking for user to input client details to remove.
                print("\n")
                print("Enter Client Details.");
                name = input("First Name: ")
                surname = input("Last Name: ")
                email = input("Email: ")
                mobile = input("Mobile Number: ")
                
                remove_client = ("DELETE FROM client WHERE name = ? AND surname = ? AND email = ? AND mobile = ?")
                c.execute(remove_client,[(name), (surname), (email), (mobile)]) 
                
                # Final check for user to make sure they want to delete the client.
                answer = input("Are You Sure You Want To Remove User? Yes/No: ")
                if answer.lower() == "yes": 
                    conn.commit()
                    print("\n")
                    print("Client Remove Successfull!\n")

                c.close()                
            except sqlite3.Error as error:
                print("\n")
                print("Failed To Remove Client.\n")                     
            
            # Finally Closing the database connection.
            finally:
                if (conn):
                    conn.close()
                    print("\n")
        
        # Returns to menu.
        elif choice == 2:
            print("\n")
            return main()
        
        # Quits program completely.
        elif choice == 3:
            print("\n")
            print("Connection To Database Closed!\n")
            print("Goodbye!")
            return exit()



Login()

def main():

    print("   # # # #     # # # #       # # # # #     ##        #   #")
    print("  #       #    #       #         #         # #       #   #")
    print(" #         #   #        #        #         #  #      #   #")
    print(" #         #   #         #       #         #   #     #   #")
    print(" #         #   #         #       #         #    #    #   #")
    print(" #         #   #         #       #         #     #   #   #")
    print(" #         #   #        #        #         #      #  #   #")
    print("  #       #    #       #         #         #       # #    ")
    print("   # # # #     # # # #       # # # # #     #        ##   #")
    print("\n")


    print("Main_Menu:")
    options = ["Search_Client", "Add_Update_Client", "Remove_Client", "Search_User", "Add_Update_User", "Remove_User","Quit"]
    while True:
        for i in range(len(options)):
            print(str(i + 1) + ")", options[i])

        choice = None
        while choice is None:
            try:
                choice = int(input("Choose An Option: "))
            except ValueError:
                print("You Chose Poorly!\n")
                break
        
        
                                             
        if choice == 1:
            Search_Client()

        elif choice == 2:
            Add_Update_Client()

        elif choice == 3:
            Remove_Client()

        elif choice == 4:
            Search_User()

        elif choice == 5:
            Add_Update_User()

        elif choice == 6:
            Remove_User()

        elif choice == 7:
            print("\n")
            print("Connection To Database Closed!")
            print("Goodbye!")
            return exit()

        else:
            continue

        print("\n")
        print("Do You Want To Do Anything Else?")


if __name__ == "__main__":
    main()
