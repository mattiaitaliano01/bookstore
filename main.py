# import db_manager module to connect to database
import db_manager as db
# import running module to run the application
from running import welcome_msg, choice_from_menu, clear

# connect to database and create it if it doesn't exist
db.connect_db()

# display the welcome message
welcome_msg()

# set the default variable for loop
is_running = True
# run the application until the user choice to exit
while is_running:
    # call the choiche_from_menu function
    choice = choice_from_menu()
    # exit if the user choice is 0
    if choice == 0:
        clear()
        print("\nGoodbye!\n")
        is_running = False

