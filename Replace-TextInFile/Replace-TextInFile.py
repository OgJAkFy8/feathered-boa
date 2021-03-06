import time

# Assignments
Input_file = 'ExampleABV.txt'
replace_what = "\t"
replace_with = "\n WHERE BeverageId "
print('Searching for: "{0}" in file "{1}" and replacing it with "{2}".'.format(replace_what, Input_file, replace_with))


# Open the file
readfile = open(Input_file, 'r')
original_data = readfile.read()
readfile.close()

edited_data = original_data.replace(replace_what, replace_with)

# File Name
timestamp = time.strftime("%d%M%S")
name = '-' + timestamp + 'x.txt'
filename = Input_file.replace('.txt', name)


print('\nNew file: {0}'.format(filename))
Outfile = open(filename, 'w')
Outfile.write(edited_data)
Outfile.close()
