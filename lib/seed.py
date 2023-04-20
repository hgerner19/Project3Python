from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from models import (Base, Book, Owner, Library)
import ipdb;

if __name__ == "__main__":
    print("Seeding 🌱...")
    print("Connecting to DB....")
    engine = create_engine('sqlite:///models.db', echo = True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()
    print("Session Created...")

    session.query(Book).delete()
    session.query(Owner).delete()
    session.query(Library).delete()
    session.commit()
    


    print("CREATING LIBRARIES....")
    denver = Library(id = 1, library_name = "Denver Public Library", libray_address = "10 W. Fourteenth Ave Pkwy, 80204",
    library_city = "Denver", library_state = "CO")
    boston = Library(id = 2, library_name = "Boston Public Library", libray_address = "700 Boylston St., 02116",
    library_city = "Boston", library_state = "MA")
    seattle = Library(id = 3, library_name = "Seattle Public Library", libray_address = "1000 Fourth Ave., 98104",
    library_city = "Seattle", library_state = "WA")



    session.add(denver)
    session.add(boston)
    session.add(seattle)
    session.commit()
    


    print("CREATING OWNERS....")
    holden = Owner(id =1, owner_name = "Holden Gerner", owner_email= "holdeng@hotmail.com",
    owner_phone="123-456-7890", owner_address="130 Peterson Rd, Libertyville,Indiana")
    cole = Owner(id = 2, owner_name = "Cole Perry", owner_email = "colep@hotmail.com",
    owner_phone="234-432-8679", owner_address = "124 S Forrest Ave, Liberty, Mississippi")
    joe = Owner(id = 3, owner_name = "Joe Smoo", owner_email = "Joes@hotmail.com",
    owner_phone = "732-0932-8888", owner_address = "500 Sand Dune Dr, Kitty Hawk Nebraska")

    session.add(holden)
    session.add(cole)
    session.add(joe)
    session.commit()
    

# Genres: Novel, Fiction, Fantasy , Short Story, Drama, Nonfiction 

    print("CREATING BOOKS....")
    a_christmas_carol = Book(book_name="A Christmas Carol", book_author= "Charles Dickens", book_genre="Short Story",
    book_pages= 64, book_sales= 2000000, book_price= 5.99, book_rating= 4.1,owner_id=holden.id, library_id=denver.id)
    animal_farm = Book(book_name="Animal Farm", book_author="George Orwell",book_genre="Fiction",
    book_pages=128, book_sales=250000, book_price=10.99, book_rating=4.0,owner_id=holden.id, library_id=denver.id)
    dracula = Book(book_name="Dracula", book_author= "Bram Stoker",book_genre="Fantasy", 
    book_pages=488, book_sales=4000000, book_price=11.99, book_rating=4.0,owner_id=holden.id, library_id=denver.id)
    farenheit_451 = Book(book_name="Fahrenheit 451", book_author= "Ray Bradbury",book_genre="Fiction",
    book_pages=194, book_sales=10000000, book_price=8.36, book_rating=4.0, owner_id=holden.id, library_id=denver.id)
    jane_eyre = Book(book_name="Jane Eyre", book_author= "Charlote Bronte", book_genre="Fiction",
    book_pages=532, book_sales=2000000, book_price=7.99, book_rating=4.1,owner_id=cole.id, library_id=boston.id)
    little_women = Book(book_name="Little Women", book_author= "Lousia May Alcott",book_genre="Novel",
    book_pages=449, book_sales=1780000, book_price=14.91, book_rating=4.1, owner_id=cole.id, library_id=boston.id)
    moby_dick = Book(book_name="Moby Dick", book_author= "Herman Melville",book_genre="Fiction",
    book_pages=427, book_sales=10000000, book_price=15.72, book_rating=4.3,owner_id=cole.id,library_id=boston.id)
    nineteen_eighty_four = Book(book_name="Nineteen Eighty-Four", book_author= "George Orwell", book_genre="Science Fiction",
    book_pages=328, book_sales=8000000, book_price=7.48, book_rating=4.6,owner_id=cole.id,library_id=boston.id)
    of_mice_and_men = Book(book_name="Of Mice and Men", book_author= "John Steinbeck", book_genre="Fiction",
    book_pages=107, book_sales=7500000, book_price=9.72, book_rating=4.6, owner_id=joe.id, library_id=seattle.id)
    one_hundred_years_of_solitude = Book(book_name="One Hundred Years of Solitude",book_author= "Gabriel Garcia", book_genre="Novel",
    book_pages=448, book_sales=50000000, book_price=8.99, book_rating=4.5, owner_id=joe.id, library_id=seattle.id)
    catcher_in_the_rye = Book(book_name="The Catcher In The Rye", book_author= "J.D. Salinger", book_genre="Novel",
    book_pages=234, book_sales=65000000, book_price=8.93, book_rating=3.8, owner_id=joe.id, library_id=seattle.id)
    great_gatsby = Book(book_name="The Great Gatsby",book_author= "F. Scott Fitzgerald",book_genre="Fiction",
    book_pages=208, book_sales=25000000, book_price=10.99, book_rating=4.6, owner_id=joe.id, library_id=seattle.id)



    session.add(a_christmas_carol)
    session.add(animal_farm)
    session.add(dracula)
    session.add(farenheit_451)
    session.add(jane_eyre)
    session.add(little_women)
    session.add(moby_dick)
    session.add(nineteen_eighty_four)
    session.add(of_mice_and_men)
    session.add(one_hundred_years_of_solitude)
    session.add(catcher_in_the_rye)
    session.add(great_gatsby)
    

    session.commit()
    
    print("DONE!")


# owner_id = holden.id
# library_id = denver.id 