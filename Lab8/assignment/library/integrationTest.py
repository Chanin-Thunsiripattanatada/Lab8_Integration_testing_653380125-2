import pytest
from fastapi.testclient import TestClient
from main import app, get_db, User, Book, Borrowlist
# นายชนินทร์ ธัญสิริพัฒนธาดา 653380125-2 sec.1
# create a test client to interact with the api
@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.mark.parametrize("userdata,bookdata", [({"username" : "test_user1","fullname" : "test_newuser111"},{"title":"test_newbook1","firstauthor":"aomsin chanin","isbn":"12345"}),
                                               ({"username" : "test_user2","fullname" : "test_newuser222"},{"title":"test_newbook2","firstauthor":"aomsin chanin","isbn":"12345"}),
                                               ({"username" : "test_user3","fullname" : "test_newuser333"},{"title":"test_newbook3","firstauthor":"aomsin chanin","isbn":"12345"})])
def test_create_borrowlist(client, db_session,userdata,bookdata):
    
    # create the user to borrow book
    user = User(username=userdata["username"],fullname=userdata["fullname"])
    db_session.add(user)
    db_session.commit()
    
    # Create a new book instance
    book = Book(title=bookdata["title"],firstauthor=bookdata["firstauthor"],isbn=bookdata["isbn"])
    db_session.add(book)
    db_session.commit()

     # makes a POST request to the /users/ endpoint
    response = client.post(f"/borrowlist/?user_id={user.id}&book_id={book.id}")

    # checks that the api request was successful
    assert response.status_code == 200

    # checks the content returned by the api matches the one we sent
    assert response.json()["user_id"] == user.id
    assert response.json()["book_id"] == book.id

    # checks that the borrowlist was succesfully added to the database
    assert db_session.query(Borrowlist).filter_by(user_id=user.id,book_id=book.id).first()


@pytest.mark.parametrize("userdata,bookdata", [({"username" : "test_user1","fullname" : "test_newuser111"},{"title":"test_newbook1","firstauthor":"aomsin chanin","isbn":"12345"}),
                                               ({"username" : "test_user2","fullname" : "test_newuser222"},{"title":"test_newbook2","firstauthor":"aomsin chanin","isbn":"12345"}),
                                               ({"username" : "test_user3","fullname" : "test_newuser333"},{"title":"test_newbook3","firstauthor":"aomsin chanin","isbn":"12345"})])   
def test_read_borrowlist(client, db_session,userdata,bookdata):
    
    # create the user to borrow book
    user = User(username=userdata["username"],fullname=userdata["fullname"])
    db_session.add(user)
    db_session.commit()
    
    # Create a new book instance
    book = Book(title=bookdata["title"],firstauthor=bookdata["firstauthor"],isbn=bookdata["isbn"])
    db_session.add(book)
    db_session.commit()

    response = client.post(f"/borrowlist/?user_id={user.id}&book_id={book.id}")
    response = client.get(f"/borrowlist/{user.id}")

    # checks that the api request was successful
    assert response.status_code == 200

    # checks number of row data
    assert len(response.json()) == 1
    # check same data 
    assert response.json()[0]["user_id"] == user.id
    assert response.json()[0]["book_id"] == book.id

     
    