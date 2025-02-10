class Book:
    """checks availabilty of books by title and author"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False # initially the book is available
        
    def check_out(self):
        """Check out the book by marking it as not available."""
        if self._is_checked_out:
            return f"The book '{self.title}' is already checked out."
        self._is_checked_out = True
        return f"You have checked out '{self.title}'."
    
    def return_book(self):
        """Return the book by marking it as available."""
        if not self._is_checked_out:
            return f"The book '{self.title}' is available"
        self._is_checked_out = False
        return f"You have returned '{self.title}'."


class Library:
    """stores instances of the book class"""
    def __init__(self):
        self._books = [] # Private list to store books in the librar
    
    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
           if book.title == title and not book._is_checked_out:
               book.check_out()
               return f"Book '{title}' has been checked out."
        return f"Book '{title}' is not available or does not exist."
    
    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return f"Book '{title}' has been returned."
        return f"Book '{title}' was not checked out or does not exist."
   
    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book.title for book in self._books if not book._is_checked_out]
        if not available_books:
            return "No books available."
        return available_books