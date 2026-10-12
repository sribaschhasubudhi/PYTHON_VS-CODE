# Write a Python program to create a Notebook class that maintains an internal list of notes. 
# Add an add_note(note) method that appends a new note to the list, and a show_notes() method that prints all stored notes.

class Notebook:
    def __init__(self):
        self.notes=["apple","banana","orange"]

    def add_note(self):
        new_note=input("Enter note:-")
        self.notes.append(new_note)

    def show_notes(self):
        print(self.notes)

fruits=Notebook()
def add_or_show():
    add=input("Do you want to add something to notes? (y/n):-")
    if add in {"y","Y"}:
        fruits.add_note()

    show=input("Do you want to see the notes? (y/n):-")
    if show in {"y","Y"}:
        fruits.show_notes()

add_or_show()