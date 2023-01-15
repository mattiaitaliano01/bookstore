# import sqlite to handle database
import sqlite3
# import tabulate to display db as grid
from tabulate import tabulate

# list of data to populate the db
TEST_DATA = [
    (3001, "A Tale of Two Cities", "Charles Dickens", 30),
    (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
    (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
    (3004, "The Lord of the Rings", "J.R.R. Tolkien", 37),
    (3005, "Alice in Wonderland", "Lewis Carroll", 12)
]

# define the function to connect to the db or
# create it if it doesn't exist
# it also create the table and populate it with the
# test data if it doesn't exist
def connect_db():
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    # try to create the table but if it exist pass as exemption
    try:
        cursor.execute('''
        CREATE TABLE books_stock (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Author TEXT,
            Qty INTEGER
        )
        ''')
        for book in TEST_DATA:
            cursor.execute('''
INSERT INTO books_stock(id, Title, Author, Qty)
VALUES (:id_book, :Title, :Author, :Qty)''', {'id_book': book[0], 'Title': book[1], 'Author': book[2], 'Qty': book[3]})
    except Exception:
        pass

    db.commit()
    db.close()

# define a function to enter a new row by taking
# parameters from the user
def enter_row(id_book, title, author, qty):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    #try to insert datas into the database
    try:
        cursor.execute('''
INSERT INTO books_stock(id, Title, Author, Qty)
VALUES (:id, :Title, :Author, :Qty)''', {'id': id_book, 'Title': title, 'Author': author, 'Qty': qty})
        print("\nBook created succesfully!")
        db.commit()
        print_table(where=f"WHERE id = {id_book}")

    except Exception as e:
        print(f"\nFailed to create the book.\nIs the id unique for the item?\n{e}\n")

    db.close()

# define the function to display the db as grid
# by taking as parameter(set by default in a generic selection)
# the condition chosen by the user
def print_table(selection='*', where=''):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()
    # select all table and list it in rows
    cursor.execute(f'''SELECT {selection} FROM books_stock {where}''')
    rows = cursor.fetchall()
    print("\n")
    # use tabulate to print the table
    print(tabulate(rows, headers=['Id', 'Title', 'Author', 'Quantity'], tablefmt='github'))
    print("\n")
    
    db.commit()
    db.close()

# define the function to check if the id inserted
# is inside the table
def check_id():
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()
    cursor.execute("SELECT id FROM books_stock")
    # create a list of IDs
    ids = cursor.fetchall()
    # create an empty list and populate it to convert
    # tuples in string
    new_ids = []
    for element in ids:
        new_ids.append(element[0])
    db.commit()
    db.close()
    return new_ids

# define the function to edit the column choosen by the user
# and assign to it the new value choosen by the user
def edit_book(id_book, column_name):
    if column_name == 'Title' or column_name == 'Author':
        value = input(f"\nEnter the new {column_name.lower()}: ")
    else:
        while True:
            try:
                value = int(input(f"\nEnter the new {column_name.lower()}: "))
                break
            except ValueError:
                print("\nEnter a number")
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()
    try:
        sql = f'''
UPDATE books_stock
SET {column_name} = ?
WHERE id = {id_book}'''
        cursor.execute(sql, (value,))
        print("\nBook modified successfully")
        db.commit()
        print_table(where=f'WHERE id = {id_book}')
    except Exception as e:
        print(f"\nFailed to edit the book.\n{e}\n")
    finally:
        db.close()

# define the function to delete the row choosen by the user
def delete_book(id_book):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()
    try:
        sql = f'''DELETE FROM books_stock WHERE id = {id_book}'''
        cursor.execute(sql)
        db.commit()
        print("\nBook deleted succesfully")
    except Exception as e:
        print(f"\nFailed to delete the book.\n{e}\n")
    finally:
        db.close()

# define the function to search for books depending on the column choosen
def search_book(column):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()
    if column == 'id':
        while True:
            try:
                choice = int(input("\nEnter the id number: "))
                break
            except ValueError:
                print("\nEnter a number!")
#             print(f"Enter the id number: {choice}")
    else:
        choice = input(f"\nEnter the {column}: ")
    
    sql = f'''SELECT * FROM books_stock WHERE {column} = ?'''
    cursor.execute(sql, (choice,))
    # collect all the rows needed
    rows = cursor.fetchall()
    print("\n")
    # use tabulate to print the table
    print(tabulate(rows, headers=['Id', 'Title', 'Author', 'Quantity'], tablefmt='github'))
    print("\n")
    db.commit()
    db.close()