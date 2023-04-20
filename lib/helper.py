from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Library, Owner, Book
from ipdb import set_trace

engine = create_engine('sqlite:///models.db')
session = sessionmaker(bind=engine)()

libraries = session.query(Library).all()
books = session.query(Book).all()
owner = session.query(Owner).all()

 #CLI ACTIONS
    #  1. See all libraries and books in each library
    #  2. Add a book to a library
    #  3. Return a book to a library
    #  4. Donate a book
    #  5. Relocate a library
    #  6. Filter by things such as genre, page numbers, rating

def main_menu():
    print("Choose an option:")
    print("1\=>\tSee all Library options")
    print("2\=>\tSee all book options")
    print("Type 'exit' to leave")
    first_input = input()
    print(f"You selected {first_input}")

    if first_input == "1":
        show_library_options()
    elif first_input == "2":
        show_book_options()
    else:
        print("Invalid Input")

def show_library_options():
    print("Choose an option:")
    print("1\=>\tSee Libraries")
    print("2\=>\tSee Library locations")
    print("3\=>\tSee Owners of Libraries")
    print("4\=>\tSee Books in Libraries")
    print("5\=>\tReturn to Main Menu")
    second_input = input()
    print(f"You selected {second_input}")

    if second_input == "1":
        show_all_libraries(libraries[0])
        show_library_options()
        pass
    elif second_input == "2":
        show_all_locations(libraries)
        show_library_options()
        pass
    elif second_input == "3":
        show_owners(owner)
        show_library_options()
        pass
    elif second_input == "4":
        show_library_books(books)
        show_library_options()
        pass
    elif second_input == "5":
        main_menu()
    else:
        print("Invalid Input")

    

def show_book_options():
    print("Choose an option:")
    print("1\=>\tSee all books")
    print("2\=>\tCheck out a book")
    print("3\=>\tReturn a book")
    print("4\=>\tDonate a book")
    print("5\=>\tFilter books")
    print("6\=>\tReturn to Main Menu")
    third_input = input()

    if third_input == "1":
        show_all_books(books[0])
        show_book_options()
        pass
    elif third_input == "2":
        check_book_out(books)
        show_book_options()
        pass
    elif third_input == "3":
        return_book(books)
        show_book_options()
        pass
    elif third_input == "4":
        donate_book(books)
        show_book_options()
        pass
    elif third_input == "5":
        filter_books(books)
        show_book_options()
        pass
    elif third_input == "6":
        main_menu()
    else:
        print("Invalid Input")
    
 #Library options
def show_all_libraries(libraries):
    for library in libraries:
        print("-" * 50)
        print(library)
        print("-" * 50)
    pass

def show_all_locations(libraries):

    pass

def show_owners(owner):
    pass

def  show_library_books(books):
    pass


#Book Options
def show_all_books(books):
    for book in books:
        print("-" * 50)
        print(book)
        print("-" * 50)
    pass

def check_book_out(books):
    pass

def return_book(books):
    pass

def donate_book(books):
    pass

def filter_books(books):
    pass




    