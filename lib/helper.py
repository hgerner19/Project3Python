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
    print("3\=>\tSee Books in Libraries")
    print("4\=>\tReturn to Main Menu")
    second_input = input()
    print(f"You selected {second_input}")

    if second_input == "1":
        show_all_libraries()
        show_library_options()
        pass
    elif second_input == "2":
        show_all_locations()
        show_library_options()
        pass
    elif second_input == "3":
        show_library_books()
        show_library_options()
        pass
    elif second_input == "4":
        main_menu()
    else:
        print("Invalid Input")

    

def show_book_options():
    print("Choose an option:")
    print("1\=>\tSee all books")
    print("2\=>\tPurchase a book")
    print("3\=>\tReturn a book")
    print("4\=>\tDonate a book")
    print("5\=>\tFilter books")
    print("6\=>\tReturn to Main Menu")
    third_input = input()

    if third_input == "1":
        show_all_books()
        show_book_options()
        pass
    elif third_input == "2":
        buy_book()
        show_book_options()
        pass
    elif third_input == "3":
        return_book()
        show_book_options()
        pass
    elif third_input == "4":
        donate_book()
        show_book_options()
        pass
    elif third_input == "5":
        filter_books()
        show_book_options()
        pass
    elif third_input == "6":
        main_menu()
    else:
        print("Invalid Input")
    
 #Library options
def show_all_libraries():
    for library in libraries:
        print("-" * 50)
        print("Library: ", library.library_name)
        print("-" * 50)
    pass

def show_all_locations():
    for library in libraries:
        print("-" * 50)
        print("Library: ", library.library_name)
        print("Address: ", library.libray_address)
        print("City: ", library.library_city)
        print("State: ", library.library_state)
        print("-" * 50)
    pass

def  show_library_books():
    for book in books:
        for library in libraries:
            print("-" * 50)
            print("Library: ", library.library_name)
            print("Book: ", book.book_name)
            print("Author: ", book.book_author)
            print("-" * 50)

    pass


#Book Options
def show_all_books():
    for book in books:
        print("-" * 50)
        print("Book: ", book.book_name)
        print("Author: ", book.book_author)
        print("Genre: ", book.book_genre)
        print("Pages: ", book.book_pages)
        print("Price: ", book.book_price)
        print("Rating: ", book.book_rating)
        print("Current Inventory: ", book.book_inventory)
        print("-" * 50)
    pass

def buy_book():
    print("-" * 50)
    print("What book what you like to purchase?")
    check_input = input()
    book_found = False
    for book in books:
        if check_input == book.book_name:
            if book.book_inventory > 0:
                print("-" * 50)
                print(f"The price of {book.book_name} is {book.book_price}")
                print("Would you like to checkout (Y/N)")
                print("-" * 50)
                answer = input()
                if answer == "Y":
                    print("Here you go!")
                    print("-" * 50)
                    book.book_inventory -= 1
                elif answer == "N":
                    print("No worries. Thanks for coming in!")
                    print("-" * 50)
            else:
                print("-" * 50)
                print("Sorry, we are all out of that book.")
                print("-" * 50)
            book_found = True
            break
        if not book_found:
            print("-" * 50)
            print("Sorry! We don't have that book!")
            print("-" * 50)
        
    
    pass

def return_book():
    print("What book are you returning?")
    return_input = input()
    book_found = False
    for book in books:
        if book.book_name == return_input:
            print(f"Thank you for returning {book.book_name}")
            book.book_inventory += 1
            book_found = True
            break
        if not book_found:
            print("Woah, that is not one our books.")
        pass
    pass

# def donate_book():
#     print("Which book would you like to donate?")
#     donate_input = input()
#     print("Thanks for donating {donate_input}")

def filter_books():
    print("What would you like to Filter by?")
    print("1\=>\tGenre")
    print("2\=>\tPrice")
    print("3\=>\tRating")
    print("4\=>\tPages")
    print("5\=>\tReturn to Book Options")
    filter_input = input()

    if filter_input == "1":
        filter_genre()
        filter_books()
        
    if filter_input == "2":
        filter_price()
        filter_books()
        
    if filter_input == "3":
        filter_rating()
        filter_books()
        
    if filter_input == "4":
        filter_pages()
        filter_books()
        
    if filter_input == "5":
        show_book_options()
        

# Filter_Book Options
def filter_genre():
    print("-" * 50)
    print("What genre would you like to filter by?")
    print("-" * 50)
    check_genre = input()
    filtered_books = [book for book in books if book.book_genre == check_genre]
    if not filtered_books:
        print(f"No books found for {check_genre} genre")
    else:
        print("-" * 50)
        print(f"Here are the books for {check_genre} genre:")
        for book in filtered_books:
            print("-" * 50)
            print("Book: ", book.book_name)
            print("Author: ", book.book_author)
            print("Genre: ", book.book_genre)
            print("Pages: ", book.book_pages)
            print("Price: ", book.book_price)
            print("Rating: ", book.book_rating)
            print("Current Inventory: ", book.book_inventory)
            print("-" * 50)

def filter_price():
    print("-" * 50)
    print("What price would you like to filter by?")
    print("-" * 50)
    check_price = input()
    filtered_price = [book for book in books if book.book_price == check_price]
    if not filtered_price:
        print(f"No books found for {check_price}")
    else:
        print("-" * 50)
        print(f"Here are the books for {check_price}")
        for book in filtered_price:
            print("-" * 50)
            print("Book: ", book.book_name)
            print("Author: ", book.book_author)
            print("Genre: ", book.book_genre)
            print("Pages: ", book.book_pages)
            print("Price: ", book.book_price)
            print("Rating: ", book.book_rating)
            print("Current Inventory: ", book.book_inventory)
            print("-" * 50)

def filter_rating():
    print("-" * 50)
    print("What rating would you like to filter by?")
    print("-" * 50)
    check_rating = input()
    filtered_rating = [book for book in books if book.book_rating == check_rating]
    if not filtered_rating:
        print(f"No books found for {check_rating}")
    else:
        print("-" * 50)
        print(f"Here are the books for {check_rating}")
        for book in filtered_rating:
            print("-" * 50)
            print("Book: ", book.book_name)
            print("Author: ", book.book_author)
            print("Genre: ", book.book_genre)
            print("Pages: ", book.book_pages)
            print("Price: ", book.book_price)
            print("Rating: ", book.book_rating)
            print("Current Inventory: ", book.book_inventory)
            print("-" * 50)

def filter_pages():
    print("-" * 50)
    print("What number of pages would you like to filter by?")
    print("-" * 50)
    check_pages = input()
    filtered_pages = [book for book in books if book.book_pages == check_pages]
    if not filtered_pages:
        print(f"No books found for {check_pages}")
    else:
        print("-" * 50)
        print(f"Here are the books for {check_pages}")
        for book in filtered_pages:
            print("-" * 50)
            print("Book: ", book.book_name)
            print("Author: ", book.book_author)
            print("Genre: ", book.book_genre)
            print("Pages: ", book.book_pages)
            print("Price: ", book.book_price)
            print("Rating: ", book.book_rating)
            print("Current Inventory: ", book.book_inventory)
            print("-" * 50)

    




    