from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from random import randint
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
        
    elif second_input == "2":
        show_all_locations()
        show_library_options()
        
    elif second_input == "3":
        show_library_books()
        show_library_options()
        
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
        
    elif third_input == "2":
        buy_book()
        show_book_options()
        
    elif third_input == "3":
        return_book()
        show_book_options()
        
    elif third_input == "4":
        donate_book()
        show_book_options()
        
    elif third_input == "5":
        filter_books()
        show_book_options()
        
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
    
def show_all_locations():
    for library in libraries:
        print("-" * 50)
        print("Library: ", library.library_name)
        print("Address: ", library.libray_address)
        print("City: ", library.library_city)
        print("State: ", library.library_state)
        print("-" * 50)
    
def  show_library_books():
    for book in books:
        for library in libraries:
            print("-" * 50)
            print("Library: ", library.library_name)
            print("Book: ", book.book_name)
            print("Author: ", book.book_author)
            print("-" * 50)

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
                print("-" * 50
            book_found = True
            break

        if not book_found:
            print("-" * 50)
            print("Sorry! We don't have that book!")
            print("-" * 50)


def return_book():
    print("What book are you returning?")
    return_input = input()

    book_found = False
    
    for book in books:
        if book.book_name == return_input:
            print(f"Thank you for returning {book.book_name}")
            book.book_inventory += 1
            book_found = True # if book is found stop the code
            break

        if not book_found:
            print("Woah, that is not one our books.")

def donate_book():
    # list of all the genres
    genre = ["Short Story", "Fiction", "Fantasy", "Novel", "Science Fiction"]

    print("What Book would you like to donate?")
    book = input()

    print("Who's the Author?")
    author = input()

    # randomizing each value (book_genre will be 
    # assigned a random value from genre list)
    book_price = round(randint(5,15) + randint (0,99) / 100, 2)
    book_rating = round(randint(3,5) + randint (0,99) / 100, 2)
    book_pages = randint(60,600)
    book_sale = randint(1000000,3000000)
    book_genre = random.choice(genre)
    book_inventory = 1
    owner_id = randint(1,3)
    library_id = randint(1,3)

    # Adding new book to database
    new_book = Book(book_name = book,
                    book_author = author,
                    book_genre = book_genre,
                    book_pages = book_pages,
                    book_sales = book_sale,
                    book_price = book_price,
                    book_rating = book_rating,
                    book_inventory = book_inventory,
                    owner_id = owner_id,
                    library_id = library_id)

    session.add(new_book)
    session.commit()
    # Appending new_book to books list
    books.append(new_book)
    
    print(f"Thanks for your donation! {book} has been added to our database.")

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
        
    elif filter_input == "2":
        filter_price()
        filter_books()
        
    elif filter_input == "3":
        filter_rating()
        filter_books()
        
    elif filter_input == "4":
        filter_pages()
        filter_books()
        
    elif filter_input == "5":
        show_book_options()
        

# Filter_Book Options
def filter_genre():
    # genre lists
    short_story = []
    fiction = []
    fantasy = []
    novel = []
    scifi = []

    # Iterating through each books to filter
    for book in books:
        if book.book_genre == "Short Story":
            short_story.append(book.book_name)

        elif book.book_genre == "Fiction":
            fiction.append(book.book_name)

        elif book.book_genre == "Fantasy":
            fantasy.append(book.book_name)

        elif book.book_genre == "Novel":
            novel.append(book.book_name)

        elif book.book_genre == "Science Fiction":
            scifi.append(book.book_name)
    
    #Printing each list
    print("-" * 50)
    print("Short Story:")
    print("")
    for index in short_story:
        print(index)

    print("-" * 50)
    print("Fiction:")
    print("")
    for index in fiction:
        print(index)

    print("-" * 50)
    print("Fantasy:")
    print("")
    for index in fantasy:
        print(index)

    print("-" * 50)
    print("Novels:")
    print("")
    for index in novel:
        print(index)

    print("-" * 50)
    print("Science Fiction:")
    print("")
    for index in scifi:
        print(index)

    print("-" * 50)

def filter_price():
    # Price Lists
    cheap = []
    medium = []
    expensive = []

    # Iterating through books to filter
    for book in books:
        if book.book_price < 6:
            cheap.append(f"{book.book_name} - ${book.book_price}")

        elif book.book_price > 6 and book.book_price < 12:
            medium.append(f"{book.book_name} - ${book.book_price}")

        elif book.book_price > 12:
            expensive.append(f"{book.book_name} - ${book.book_price}")

    # Printing each list 
    print("-" * 50)
    print("Cheap Priced Books:")
    print("")
    for index in cheap:
        print(index)

    print("-" * 50)
    print("Medium Priced Books:")
    print("")
    for index in medium:
        print(index)

    print("-" * 50)
    print("Expensive Priced Books:")
    print("")
    for index in expensive:
        print(index)

    print("-" * 50)

def filter_rating():
    # Lists for ratings
    four = []
    fourthree = []
    foursix = []

    # Iterating through books to filter
    for book in books:
        if book.book_rating < 4.2:
            four.append(f"{book.book_name} - {book.book_rating}")

        elif book.book_rating > 4.2 and book.book_rating < 4.5:
            fourthree.append(f"{book.book_name} - {book.book_rating}")

        elif book.book_rating > 4.5:
            foursix.append(f"{book.book_name} - {book.book_rating}")

    # Printing each rating list
    print("-" * 50)
    print("Good Books:")
    print("")
    for index in four:
        print(index)

    print("-" * 50)
    print("Great Books:")
    print("")
    for index in fourthree:
        print(index)

    print("-" * 50)
    print("Fantastic Books:")
    print("")
    for index in foursix:
        print(index)

    print("-" * 50)

def filter_pages():
    # creating list for page filter
    short = []
    medium = []
    longg = []

    # Iterating through books to filter pages
    for book in books:
        if book.book_pages  < 200:
            short.append(f"{book.book_name} - {book.book_pages}")

        elif book.book_pages > 200 and book.book_pages < 400:
            medium.append(f"{book.book_name} - {book.book_pages}")

        elif book.book_pages > 400:
            longg.append(f"{book.book_name} - {book.book_pages}")

    # Printing each list
    print("-" * 50)
    print("Short Books:")
    print("")
    for index in short:
        print(index)

    print("-" * 50)
    print("Medium Books:")
    print("")
    for index in medium:
        print(index)

    print("-" * 50)
    print("Long Books:")
    print("")
    for index in longg:
        print(index)

    print("-" * 50)
        




    