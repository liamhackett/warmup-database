import time

TIME_DOT = .5
HELP_KEYWORD = "help"
ORDER_BY_KEYWORD = "order by"



# EDIT def help()
def help() -> str:
    """ Prints help instructions: format, query structure etc.

    """

    # TODO: Edit the print statement
    
    # load, help, exit all standalone statements
    # format select_query table_query query_identifier
    print('\nFormat your search: ARTIST [then the rest of the keywords]\n' \
        'Make sure to put any double words (e.g. "Johnny Cash") in quotes\n')

def parser(user_input) -> str:
    """ Parse and format the user query for the query search

    :param user_input: the user input
    :type user_input: str

    """
    user_input = user_input.lower()

    # if the user would like to access the help function
    if user_input in HELP_KEYWORD:
        help()
    
   
# attempted to add how many to function
    # if the user would like to know the total number of elemenets in either list
    elif "how" in user_input:
        if "artists" in user_input:
            return "SELECT COUNT(*) as amount FROM artist", "", ""
        elif "songs" in user_input:
             return "SELECT COUNT(*) as amount FROM song", "", ""

    # TODO: add more functionality for different query formats

    else:
        # split the string on the first white space to seperate column name
        user_input_split = user_input.split(" ", 1)

        # if "order by" is in the second half of the user input split on "order by" to get the order
        if "order by" in user_input_split[1]:

            user_input_split1 = user_input_split[1].split(" order by ")  

            return(user_input_split[0], user_input_split1[0], user_input_split1[1])

        # else return a blank order
        else:

            return user_input_split[0], user_input_split[1], ""

    
def parser_tester() -> str:
    """ Tests the parser function

    """
    test_string_2 = "'Johhny Cash' Pop 117"
    test_string_3 = "length song ransom"
    test_string_4 = "rank song 'Ol Town Road'"
    test_string = "country artist Drake"
    test_string_6 = "how many artists"

    # print(type(test_string))

    print("\nTesting!")
    print('.', end="", flush=True), time.sleep(TIME_DOT), print('.', end="", flush=True), \
                                    time.sleep(TIME_DOT), print('.', end="", flush=True), time.sleep(TIME_DOT), \
                                    print('.', end="", flush=True), time.sleep(TIME_DOT), print('.\n'), \
                                    time.sleep(TIME_DOT)
    
    return test_string

def main():

    # Gets user_input
    # user_input = input("Input: ")
    # parser(user_input)

    # tester
    test_string = parser_tester()
    parser(test_string)

if __name__ == "__main__":
    main()