from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///models.db', echo = True)

Session = sessionmaker(bind = engine)

session = Session()



# creating librarys
library1 = Library(id = 1, library_name = "Denver Public Library", libray_address = "10 W. Fourteenth Ave Pkwy, 80204",
library_city = "Denver", library_state = "CO")

library2 = Library(id = 2, library_name = "Boston Public Library", libray_address = "700 Boylston St., 02116",
library_city = "Boston", library_state = "MA")

library3 = Library(id = 3, library_name = "Seattle Public Library", libray_address = "1000 Fourth Ave., 98104",
library_city = "Seattle", library_state = "WA")

session.add(library1)
session.add(library2)
session.add(library3)



owner1 = Owner(id = 1, owner_name = "Holden Gerner", owner_email= "holdeng@hotmail.com",
owner_phone="123-456-7890",owner_address="130 Peterson Rd, Libertyville,Indiana")

owner2 = Owner(id = 2, owner_name = "Cole Perry", owner_email = "colep@hotmail.com",
owner_phone="234-432-8679", owner_address = "124 S Forrest Ave, Liberty, Mississippi")

owner3 = Owner(id = 3, owner_name = "Joe Smoo", owner_email = "Joes@hotmail.com",
owner_phone = "732-0932-8888", owner_address = "500 Sand Dune Dr, Kitty Hawk Nebraska")

session.add(owner1)
session.add(owner2)
session.add(owner3)

book1 = Book(id = 1)
