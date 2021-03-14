import os


def search_files(directory='.', extension=''):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        for name in files:
            if extension and name.lower().endswith(extension):
                print(os.path.join(dirpath, name))
            elif not extension:
                print(os.path.join(dirpath, name))


search_files('.', 'py')

# .idea
# examples
# inputs
# outputs
# programs
# sketchpad
# .gitattributes
# .gitignore
# findBizName.py
# main.py
# phoneAndemail.pyw
# README.md
