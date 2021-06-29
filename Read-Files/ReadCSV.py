import csv

#filename = "C:\Temp\FastCruise\FastCruiseFile.csv"
#rowview = 5

filename = 'default.txt'
while (filename.endswith('csv') == False):
    filename = input ("CSV filename and path: ")
rowview = int(input("How many rows to view: "))

fields = []
rows = []

# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
  
#  printing first 5 rows 
print('\nFirst %d rows are:\n'%rowview) 
for row in rows[:rowview]: 
    # parsing each column of a row 
    for col in row: 
        print("%10s"%col), 
    print('\n') 
