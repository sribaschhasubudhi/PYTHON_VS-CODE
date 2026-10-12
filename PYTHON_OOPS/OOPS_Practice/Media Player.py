# Write a Python program that defines a Media base class, then creates Book, Magazine, and DVD subclasses, each with type-specific attributes and a describe() method.

class Media:
    def __init__(self):
        pass

class Book(Media):
    def __init__(self,name,author):
        super().__init__()
        self.name=name
        self.author=author

    def describe(self):
        print(f"Book:{self.name}, Author:{self.author}")

class Magazine(Media):
    def __init__(self,name,issue):
        super().__init__()
        self.name=name
        self.issue=issue

    def describe(self):
        print(f"Magazine:{self.name}, {self.issue} issue")

class DVD(Media):
    def __init__(self,name,duration):
        super().__init__()
        self.name=name
        self.duration=duration

    def describe(self):
        print(f"Movie:{self.name}, duration:{self.duration} mins")

book=Book("Deep Work","Cal Newport")
book.describe()
magaz=Magazine("TIMES","August")
magaz.describe()
dvd=DVD("Troy",163)
dvd.describe()