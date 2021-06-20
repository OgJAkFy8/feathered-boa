# Assignments
import time
from tkinter import *


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x150")
        self.master.title("Search and Replace")
        self.grid(row=0, column=1)

        self.prompt = Label(self, text="Filename")
        self.prompt.grid(row=1, column=0)
        self.input = Entry(self)
        self.input.grid(row=1, column=1)

        self.prompt1 = Label(self, text="Search for")
        self.prompt1.grid(row=3, column=0)
        self.input1 = Entry(self)
        self.input1.grid(row=3, column=1)

        self.prompt2 = Label(self, text="Replace with")
        self.prompt2.grid(row=4, column=0)
        self.input2 = Entry(self)
        self.input2.grid(row=4, column=1)

        self.prompt3 = Label(self, text="Example: file.txt or full path")
        self.prompt3.grid(row=2, column=1)

        self.button_submit = Button(self, text="Submit",
                                    command=self.submit_click)
        self.button_submit.grid(row=6, column=0)

        self.button_exit = Button(self, text="Exit",
                                  command=self.exit_click)
        self.button_exit.grid(row=6, column=2)

        self.my_text = StringVar()
        self.message = Label(self, textvariable=self.my_text)
        self.message.grid()

    def submit_click(self):
        # global input_file, replace_what, replace_with
        input_file = self.input.get()
        if '"' in input_file:
            input_file = input_file.replace('"', '')
        replace_what = self.input1.get()
        replace_with = self.input2.get()
        print('Searching for: "{0}" in file "{1}" and replacing it with "{2}".'.format(replace_what, input_file,
                                                                                       replace_with))
        # Open the file
        readfile = open(input_file, 'r')
        original_data = readfile.read()
        readfile.close()

        edited_data = original_data.replace(replace_what, replace_with)

        # File Name
        timestamp = time.strftime("%d%M%S")
        name = '-' + timestamp + 'x.'
        filename = input_file.replace('.', name)

        print('\nNew file: {0}'.format(filename))
        outfile = open(filename, 'w')
        outfile.write(edited_data)
        outfile.close()

        # self.master.destroy()

    def exit_click(self):
        self.master.destroy()
        exit()


frame04 = MyFrame()
frame04.mainloop()
