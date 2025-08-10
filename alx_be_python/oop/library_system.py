class Book:
    def __init__(self, title: str, author: str):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of a generic book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an EBook with title, author, and file size.
        Calls the base class constructor for title and author.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a PrintBook with title, author, and page count.
        Calls the base class constructor for title and author.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty book collection."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book (or subclass) instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print the details of each book in the library."""
        for book in self.books:
            print(book)
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
