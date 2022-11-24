"""
This is the python script to control the terminal for our database specific Query Language

Started by Dylan Lawrence on 2/2/2022
"""

from parser_test import help, parser
from main import process
from main import load_data
from main import quit

#gets user input
def get_user_input() -> str:
    return input(">")

def main():
    quit_loop = False

    #Main loop
    while quit_loop == False:

        #get input
        user_input = get_user_input().lower()

        #handle potential edge cases
        if user_input == 'help':
            help()
            continue
        
        elif user_input == 'quit':
            quit_loop = True
            continue
        
        elif user_input == 'load data':
            load_data()
            continue

        #else parse input, if invalid statement print an error
        parsed_input = parser(user_input)
        if parsed_input == None:
            print("Invalid statement. Please type 'help' for a list of valid statements.")
        else:
            print(process(parsed_input[0], parsed_input[1], parsed_input[2]))
    quit()

main()