#Import ForeignKey
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime, ForeignKey)

# import relationship and backref from sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key=True)
    books_name = Column(String())
    books_publisher = Column(String())
    books_genre = Column(String())
    books_pages = Column(Integer())
    books_sales = Column(Integer())
    books_price = Column(Integer())
    
    #1.a✅ Add  ForeignKey('owners.id') to owner)id
    # The book BELONGS_TO the owner - ??? - is this in the wrong
    owner_id = Column(Integer(), ForeignKey("owners.id"))
   
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Books name:{self.books_name}, " \
            + f"Books publisher: {self.books_publisher}, "\
            + f"Books genre: {self.books_genre}, "\
            + f"Books pages: {self.books_pages}, "\
            + f"Books sales: {self.books_sales}, "\
            + f"Books price: {self.books_price}, "\
            
    
    
    # jobs = relationship("Job", backref=backref("pet"))


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
    owner_phone = Column(Integer())
    owner_address = Column(String())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Owner name: {self.owner_name}" \
            + f"Owner email: {self.owner_email}" \
            + f"Owner phone: {self.owner_phone}" \
            + f"Owner address: {self.owner_address}"
    
        # jobs = relationship("Job", backref=backref("handler"))

class Library(Base):
    __tablename__  = "libraries"

    # def __init__(self, ....):

    id = Column(Integer(), primary_key=True)
    library_name = Column(String())
    libray_address = Column(String())
    library_city = Column(Integer())
    library_state = Column(Integer())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Name: {self.library_name}" \
            + f"Library address: {self.libray_address}" \
            + f"Library city: {self.library_city}" \
            + f"Library state: {self.library_state}"\
 
#Create a "jobs" table to serve as our join
# class Job(Base):
#     __tablename__ = "jobs"

#     #Create the following columns
#     id = Column(Integer(), primary_key=True)
#     request = Column(String())
#     date = Column(String())
#     fee = Column(Float())

#     pet_id = Column(Integer(), ForeignKey("pets.id"))
#     handler_id = Column(Integer(), ForeignKey("handlers.id"))

#     # pet = relationship("Pet", backref=backref("pets"))
#     # handler = relationship("Handler", backref=backref("handlers"))
    
#     def __repr__(self):
#         return f"Id: {self.id}" \
#             + f"request: {self.request}" \
#             + f"date: {self.date}" \
#             + f"fee: {self.fee}"


#     #Associate the models with relationship(<ModelNameHere>, backref=backref(<TableNameHere>))
   

#     #Add a __repr__ method that returns a string containing the id, request, date, notes, fee, pet_id and handler_id of our class
   
    
# #5.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

# #After running your migrations, go build out some seeds and test your many to many