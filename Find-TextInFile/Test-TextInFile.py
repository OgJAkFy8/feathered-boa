# Assignments
file_name = 'Example.txt'
searchfor_what = 'Victory' #input('Search String: ')
print('Searching for: "{0}" in file "{1}".'.format(searchfor_what, file_name))


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


print(check_if_string_in_file(file_name, searchfor_what))
