from models import Library, Owner, Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace
from helper import main_menu
# from helpers import ...

engine = create_engine('sqlite:///models.db')
session = sessionmaker(bind=engine)()

#book_to_delete = session.query(Book).filter_by(id = 13). first()

#if book_to_delete:
    #session.delete(book_to_delete)
    #session.commit()
    #print(f"Book {book_to_delete.book_name} has been deleted.")
#else:
  #print("Book not found")
  
if __name__ == '__main__':
    print('''
  _      _  _                              
 | |    (_)| |__   _ __  __ _  _ __  _   _ 
 | |    | || '_ \ | '__|/ _` || '__|| | | |
 | |___ | || |_) || |  | (_| || |   | |_| |
 |_____||_||_.__/ |_|   \__,_||_|    \__, |
                                     |___/   

   ____  _      ___ 
  / ___|| |    |_ _|
 | |    | |     | | 
 | |___ | |___  | | 
  \____||_____||___|                 
    ''')
    print("Hello and welcome to our Library CLI!!")

    main_menu()

