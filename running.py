# import the art module where there is the ascii art
from art import logo
# import the termcolor module to color the string
from termcolor import colored
# impost os module to handle the clearing of the console
from os import system
# import the db_manager module to call the database functions
import db_manager as db

# create the menu string
menu = '''
Enter one of the following:

1. Enter Book
2. Update book
3. Delete book
4. Search books
5. View books
0. Exit
: '''

# define the clear function
def clear():
    system('cls')

# function to display the welcome message
def welcome_msg():
    print(colored(logo, 'yellow'))
    input("Press 'enter' to access the menu...")
    clear()

# define the function to edit the book depending
# on the user choice
def edit_book(id_book):
    while True:
        while True:
            try:
                choice = int(input(colored('''Which element do you want to edit?
                1. Title
                2. Author
                3. Quantity
                0. Cancel
                : ''', "blue")))
                break
            except ValueError:
                print("\nPlease enter a valid number.")
        # call the function from db_manager depending on choice
        # and pass within it the proper argument
        if choice == 1:
            db.edit_book(id_book, 'Title')
            break
        elif choice == 2:
            db.edit_book(id_book, 'Author')
            break
        elif choice == 3:
            db.edit_book(id_book, 'Qty')
            break
        elif choice == 0:
            clear()
            break
        else:
            print("\nPlease enter a valid choice.")
    input("\nPress 'enter' to continue...")
    clear()

# define the function to enter a new book
def enter_book():
    while True:
        print(colored("Enter a book in the database:", "blue"))
        # collect data and check for right data types
        try:
            id_book = int(input("\nEnter the id of the book: "))
            break
        except ValueError:
            clear()
            print(colored("Please enter a valid book ID\n", "red"))

    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")

    while True:
        try:
            qty = int(input("Enter the quantity of the book: "))
            break
        except ValueError:
            clear()
            print(colored("Please enter a valid quantity", "red"))
            print(colored("\nEnter a book in the database:", "blue"))
            print(f"\nEnter the id of the book: {id_book}\nEnter the title of the book: {title}\nEnter the author of the book: {author}")
    # call the function to enter the book by giving the parameters    
    db.enter_row(id_book= id_book,title= title,author= author,qty= qty)

    input("\nPress 'enter' to continue...")
    clear()

# define the function to update the values
# of a specific book choosen by ID
def update_book():
    while True:
        while True:
            try:
                choice = int(input(colored('''Update a book

Insert the ID of the book: ''', 'blue')))
                break
            except ValueError:
                clear()
                print("\nEnter a valid number.\n")
        id_list = db.check_id()
        if choice in id_list:
            clear()
            # call the print function to display the book's row
            # to make it visible
            db.print_table(where=f"WHERE id = {choice}")
            # call the edit function to update the book
            edit_book(choice)
            break
        elif choice == 0:
            break
        else:
            clear()
            print(f"\nThe id {choice} is not in the list of books.\nInsert a correct one or digit '0' to exit the editing.\n")
    clear()

# defining the function to delete the book
def delete_book():
    while True:
        while True:
            try:
                choice = int(input(colored('''Delete a book

Insert the ID of the book: ''', 'blue')))
                break
            except ValueError:
                clear()
                print("\nEnter a valid number.\n")
        id_list = db.check_id()
        if choice in id_list:
            clear()
            # call the print function to display the book's row
            # to make it visible
            db.print_table(where=f"WHERE id = {choice}")
            # double check before the elimination
            confirmation = input("Are you sure you want to delete this (y/n)? ").lower()
            if confirmation == "y":
                # call the delete function from db_manager
                db.delete_book(choice)
                break
            else:
                break
        elif choice == 0:
            break
        else:
            clear()
            print(f"\nThe id {choice} is not in the list of books.\nInsert a correct one or digit '0' to exit the editing.\n")
    input("\nPress 'enter' to continue...")
    clear()

# define the function to search for a specific book
# depending on the choice done
def search_book():
    while True:
        while True:
            try:
                choice = int(input(colored('''Search a Book

Search by one of the following:
1. ID
2. Title
3. Author
0. Cancel query
: ''', 'blue')))
                break
            except ValueError:
                clear()
                print("\nEnter a valid number.\n")
        if choice == 1:
            db.search_book('id')    
            break
        elif choice == 2:
            db.search_book('Title')
            break
        elif choice == 3:
            db.search_book('Author')
            break
        elif choice == 0:
            break   
        else:
            print("\nPlease enter one of the possible values.\n")

    input("\nPress 'enter' to continue...")
    clear()

# definie the choice from menu function to handle the main menu
# and the user's choices for calling the needed function
def choice_from_menu():
    while True:
        while True:
            try:
                choice = int(input(colored(menu, 'blue')))
                break
            except ValueError:
                clear()
                print("\nEnter a valid number from the menu.")
        if choice == 1:
            clear()
            enter_book()
        elif choice == 2:
            clear()
            update_book()
        elif choice == 3:
            clear()
            delete_book()
        elif choice == 4:
            clear()
            search_book()
        elif choice == 5:
            clear()
            db.print_table()
        elif choice == 0:
            return 0
        else:
            clear()
            print("\nEnter a valid number from the menu.")
