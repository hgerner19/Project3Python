#Import ForeignKey
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Float,  DateTime, ForeignKey)

# import relationship and backref from sqlalchemy.orm 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    publisher = Column(String())
    genre = Column(String())
    isbn = Column(String())
    edition = Column(Integer())
    pages = Column(Integer())
    sales = Column(Integer())
    price = Column(Integer())
    
    #1.a✅ Add  ForeignKey('owners.id') to owner)id
    # THe pet BELONGS_TO the owner
    owner_id = Column(Integer(), ForeignKey("owners.id"))
   
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Publisher: {self.species}, "\
            + f"Breed {self.breed}, "\
            + f"Species {self.temperament}"
    
    jobs = relationship("Job", backref=backref("pet"))


# ? Review
#2.✅ Migrations 
# In the app directory run `alembic init migrations`

#2.b Configuration
    # In alembic.ini, find `sqlalchemy.url`` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. Next, set target_metadata to `target_metadata = Base.metadata`

#2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added Pet model"`
    # pet_app.db should have been added to your file structure


#1.b✅ Add an Owners table 

class Owner(Base):
    __tablename__  = "owners"

    # def __init__(self, ....):

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())
    address = Column(String())

    def __repr__(self):
        return f"Id: {self.id}" \
            + f"Name: {self.name}" \
            + f"Email: {self.email}" \
            + f"Phone: {self.phone}" \
            + f"Address: {self.address}"