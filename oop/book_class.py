# book_class.py

class Book:
    """A class representing a book with magic methods."""

    def __init__(self, title, author, year):
        """Constructor that initializes the book details."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when an object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (for developers)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
