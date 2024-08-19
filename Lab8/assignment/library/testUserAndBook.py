# Lab8 - Integration testing
# Unit test -> class User,Book in main.py
# นายชนินทร์ ธัญสิริพัฒนธาดา 653380125-2 sec.1
import pytest
from main import User
from main import Book

# uses the db_session fixture inside conftest.py
def test_add_user(db_session):
    # Create a new user instance
    new_user = User(username="test_newuser1",fullname="test_newuser111")
    db_session.add(new_user)
    db_session.commit()

    # Query the test_newuser1 to see if it is there
    user = db_session.query(User).filter_by(username="test_newuser1").first()
    assert user is not None
    assert user.username == "test_newuser1"
    assert user.fullname== "test_newuser111"

# uses the db_session fixture inside conftest.py
def test_delete_user(db_session):
    # Add a user, then remove this new user from the db
    user = User(username="test_newuser2",fullname="test_newuser222")
    db_session.add(user)
    db_session.commit()

    # Delete the test_newuser2
    db_session.delete(user)
    db_session.commit()

    # Query the test_newuser2 to check if it is removed from the db
    deleted_user = db_session.query(User).filter_by(username="test_newuser2").first()
    assert deleted_user is None
    

# uses the db_session fixture inside conftest.py
def test_add_book(db_session):
    # Create a new book instance
    new_book = Book(title="test_newbook1",firstauthor="aomsin chanin",isbn="1234567891234")
    db_session.add(new_book)
    db_session.commit()

    # Query the test_newbook1 to see if it is there
    book = db_session.query(Book).filter_by(title="test_newbook1").first()
    assert book is not None
    assert book.title == "test_newbook1"
    assert book.firstauthor == "aomsin chanin"
    assert book.isbn == "1234567891234"

# uses the db_session fixture inside conftest.py
def test_delete_book(db_session):
    # Add a book, then remove this new user from the db
    book = Book(title="test_newbook2",firstauthor="aomsin chanin",isbn="1234567891234")
    db_session.add(book)
    db_session.commit()

    # Delete the test_newbook2
    db_session.delete(book)
    db_session.commit()

    # Query the test_newbook2 to check if it is removed from the db
    deleted_book = db_session.query(Book).filter_by(title="test_newbook2").first()
    assert deleted_book is None