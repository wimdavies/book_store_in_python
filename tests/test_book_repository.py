from lib.book_repository import BookRepository

def test_all_gets_all_books(db_connection):
    repository = BookRepository(db_connection)
    books = repository.all()

    assert len(books) == 5

    assert books[0].id == 1
    assert books[0].title == 'Nineteen Eighty-Four'
    assert books[0].author_name == 'George Orwell'

    assert books[1].id == 2
    assert books[1].title == 'Mrs Dalloway'
    assert books[1].author_name == 'Virginia Woolf'
