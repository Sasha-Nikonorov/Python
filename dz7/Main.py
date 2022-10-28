from os.path import exists
from CSV_creating import creating
from File_writing import writing_scv

file = 'Phonebook.csv'
valid = exists(file)
if not valid:
    creating()

writing_scv()
