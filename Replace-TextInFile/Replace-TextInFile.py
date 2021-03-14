import time

# Assignments
Input_file = 'ABV.txt'
replace_what = "\t"
replace_with = "\n WHERE BeverageId "

# Open the file
readfile = open(Input_file, 'r')
original_data = readfile.read()
readfile.close()

edited_data = original_data.replace(replace_what, replace_with)

# File Name
timestamp = time.strftime("%d%M%S")
name = '-' + timestamp + '.txt'
filename = Input_file.replace('.txt', name)

# print (filename)
Outfile = open(filename, 'w')
Outfile.write(edited_data)
Outfile.close()

print('\n')
print(edited_data)
