from models import Library, Owner, Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace
from helper import main_menu
# from helpers import ...

engine = create_engine('sqlite:///models.db')
session = sessionmaker(bind=engine)()

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

