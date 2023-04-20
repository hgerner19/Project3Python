#Import ForeignKey
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime, ForeignKey)

# import relationship and backref from sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import ipdb;

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key=True)
    book_name = Column(String())
    book_author = Column(String())
    book_genre = Column(String())
    book_pages = Column(Integer())
    book_sales = Column(Integer())
    book_price = Column(Float())
    book_rating = Column(Float())
    book_inventory = Column(Integer())
    
    #1.a✅ Add  ForeignKey('owners.id', 'libraries.id') 
    # The book BELONGS_TO the owner 
    # The book BELONGS_TO the library
    owner_id = Column(Integer(), ForeignKey("owners.id"))
    library_id = Column(Integer(), ForeignKey("libraries.id"))
   
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Book name:{self.book_name}, " \
            + f"Book author: {self.book_author}, "\
            + f"Book genre: {self.book_genre}, "\
            + f"Book pages: {self.book_pages}, "\
            + f"Book sales: {self.book_sales}, "\
            + f"Book price: {self.book_price}, "\
            + f"Book rating: {self.book_rating}, "\
            + f"Book inventory: {self.book_inventory}, "\
            
    
    


# ? Review
#2.✅ Migrations 
# In the app directory run `alembic init migrations`

#2.b Configuration
    # In alembic.ini, find `sqlalchemy.url`` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. Next, set target_metadata to `target_metadata = Base.metadata`

#2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added  model"`
    # pet_app.db should have been added to your file structure


#1.b✅ Add an Owners table 

class Owner(Base):
    __tablename__  = "owners"

    # def __init__(self, ....):

    id = Column(Integer(), primary_key=True)
    owner_name = Column(String())
    owner_email = Column(String())
    owner_phone = Column(String())
    owner_address = Column(String())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Owner name: {self.owner_name}" \
            + f"Owner email: {self.owner_email}" \
            + f"Owner phone: {self.owner_phone}" \
            + f"Owner address: {self.owner_address}"
    
    books = relationship("Book", backref=backref("owner"))

class Library(Base):
    __tablename__  = "libraries"

    # def __init__(self, ....):

    id = Column(Integer(), primary_key=True)
    library_name = Column(String())
    libray_address = Column(String())
    library_city = Column(String())
    library_state = Column(String())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Name: {self.library_name}" \
            + f"Library address: {self.libray_address}" \
            + f"Library city: {self.library_city}" \
            + f"Library state: {self.library_state}"\
            
    books = relationship("Book", backref=backref("library"))



# #5.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

# #After running your migrations, go build out some seeds and test your many to many