class Book:
    # Initializing Book attributes like title and author
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
class EBook(Book):
    # Initializing file size and inheriting other attributes of Book
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    # Initializing page count and inheriting other attributes of Book
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library(EBook, PrintBook):
    # Initialize an empty list of books
    def __init__(self):
        self.books = []
    
    # Accept any instance of Book, Ebook, or PrintBook
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")