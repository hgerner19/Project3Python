
# 3.✅ CRUD practice
# To run the file run `python3 debug.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Book, Owner, Library)
from ipdb import set_trace

from models import (Base)

if __name__ == '__main__':
    # CONN
    engine = create_engine('sqlite:///models.db')
    Base.metadata.create_all(engine)
   
    # CURSOR
    Session = sessionmaker(bind=engine)
    session = Session()
    


    
