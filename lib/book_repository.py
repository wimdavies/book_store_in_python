from lib.book import Book

class BookRepository():
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        # Executes the SQL query:
        # SELECT * FROM books;
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        # Returns an array of Books objects.
        return books
