# Assignments
import time
from tkinter import *


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("350x150")
        self.master.title("Search and Replace")
        self.grid(row=0, column=1)

        self.prompt = Label(self, text="Filename and path")
        self.prompt.grid(row=1, column=0)
        self.input = Entry(self)
        self.input.grid(row=1, column=1)

        self.prompt1 = Label(self, text="Search for")
        self.prompt1.grid(row=2, column=0)
        self.input1 = Entry(self)
        self.input1.grid(row=2, column=1)

        self.prompt2 = Label(self, text="Replace with")
        self.prompt2.grid(row=3, column=0)
        self.input2 = Entry(self)
        self.input2.grid(row=3, column=1)

        self.button_submit = Button(self, text="Submit",
                                    command=self.submit_click)
        self.button_submit.grid()

        self.my_text = StringVar()
        self.message = Label(self, textvariable=self.my_text)
        self.message.grid()

    def submit_click(self):
        # global Input_file, replace_what, replace_with
        Input_file = self.input.get()
        if '"' in Input_file:
            Input_file = Input_file.replace('"','')
        replace_what = self.input1.get()
        replace_with = self.input2.get()
        print('Searching for: "{0}" in file "{1}" and replacing it with "{2}".'.format(replace_what, Input_file,
                                                                                       replace_with))
        # Open the file
        readfile = open(Input_file, 'r')
        original_data = readfile.read()
        readfile.close()

        edited_data = original_data.replace(replace_what, replace_with)

        # File Name
        timestamp = time.strftime("%d%M%S")
        name = '-' + timestamp + 'x.'
        filename = Input_file.replace('.', name)

        print('\nNew file: {0}'.format(filename))
        Outfile = open(filename, 'w')
        Outfile.write(edited_data)
        Outfile.close()

        self.master.destroy()

frame04 = MyFrame()
frame04.mainloop()
