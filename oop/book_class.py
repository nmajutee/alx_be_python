class Book:
    
    # initializing Book instance with title, author, and year.
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    # Deleting book title upon object deletion.
    def __del__(self):
        print(f"Deleting {self.title}")
    
    # Returns a string in a user friendly format.
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    # Returns a string that would recreate the Book instance.
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    