
# 3.✅ CRUD practice
# To run the file run `python3 debug.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ipdb import set_trace

from models import (Base)

if __name__ == '__main__':
    # CONN
    engine = create_engine('sqlite:///models.db')
    Base.metadata.create_all(engine)
   
    # CURSOR
    Session = sessionmaker(bind=engine)
    session = Session()
 
    #3✅ One to Many
    #Getting an owners pets
    #Use session.query and first to grab the first owner
    # all_owners = session.query(Owner).all()
    # first_owner = session.query(Owner).first()
    # first_owners_pets = first_owner.pets

    #use session.query and filter_by to get the owners pets from Pet
    
    # first_pet = session.query(Pet).first()
    # pet_owner = session.query(Owner).filter_by(id = first_pet.owner_id)
    #print out your owners pets
  

    #Getting a pets owner
    #Use session.query and first to grab the first pet
    
    #Use session.query and filter_by to get the owner associated with this pet
 

    #4✅ Head back to models to build out a Many to Many 
#--------------------------------------------

#6.✅ Many to Many 
    #Use session.query and .first to get the first handler
   
    #Use session.query and the .filter_by to grab the jobs
    
    #Print the jobs
 
    #Use the handler_jobs to query pets for the associated pet to each job.




    # optional Break point for debugging and testing
    set_trace()