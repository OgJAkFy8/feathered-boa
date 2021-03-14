# Assignments
file_name = 'happold77-email.txt'
searchfor_what = input('Search String: ')  # "dotandbo"


def check_if_string_in_file(file_name, searchfor_what):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if searchfor_what in line:
                return True
    return False


def search_string_in_file(file_name, searchfor_what):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if searchfor_what in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results


print(search_string_in_file(file_name, searchfor_what))
