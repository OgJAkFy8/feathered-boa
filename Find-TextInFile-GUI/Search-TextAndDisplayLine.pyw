# Assignments
import time
from tkinter import *


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("250x100")
        self.master.title("Search for Text")
        self.grid(row=0, column=1)

        self.prompt = Label(self, text="Filename and path")
        self.prompt.grid(row=1, column=0)
        self.input = Entry(self)
        self.input.grid(row=1, column=1)

        self.prompt1 = Label(self, text="Search for")
        self.prompt1.grid(row=2, column=0)
        self.input1 = Entry(self)
        self.input1.grid(row=2, column=1)

        self.button_submit = Button(self, text="Search",
                                    command=self.submit_click)
        self.button_submit.grid()

        self.my_text = StringVar()
        self.message = Label(self, textvariable=self.my_text)
        self.message.grid()

    def submit_click(self):
        # global Input_file, search_for, replace_with
        Input_file = self.input.get()
        if '"' in Input_file:
            Input_file = Input_file.replace('"','')
        search_for = self.input1.get()
        print('Searching for: "{0}" in file "{1}".'.format(search_for, Input_file))

        line_number = 0
        list_of_results = []
        # Open the file in read only mode
        with open(Input_file, 'r') as read_obj:
            # Read all lines in the file one by one
            for line in read_obj:
                # For each line, check if line contains the string
                line_number += 1
                if search_for in line:
                    # If yes, then add the line number & line as a tuple in the list
                    list_of_results.append((line_number, line.rstrip()))
        # Return list of tuples containing line numbers and lines where string is found
        # return list_of_results
        read_obj.close()
        
        # File Name
        timestamp = time.strftime("%d%M%S")
        name = '-' + timestamp + 'x.'
        filename = Input_file.replace('.', name)


        print('\nNew file: {0}'.format(filename))
        Outfile = open(filename, 'a')

        for result in list_of_results:
            Outfile.write(str(result)+'\n')
        Outfile.close()

        self.master.destroy()

frame04 = MyFrame()
frame04.mainloop()
