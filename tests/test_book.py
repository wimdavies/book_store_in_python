from lib.book import Book

def test_init():
    book = Book(1, "One Flew Over The Cuckoo's Nest", "Ken Kesey")
    book = Book(1, "One Flew Over The Cuckoo's Nest", "Ken Kesey")
    assert book.id == 1
    assert book.title == "One Flew Over The Cuckoo's Nest"
    assert book.author_name == "Ken Kesey"
