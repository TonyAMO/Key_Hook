from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging
from keys import keys
from access import access
from building import building
from door_formats import door_formats
from doors import doors
from employees import employees
from hooks import hooks
from issued_key import issued_key
from key_issues import key_issues
from lost_key import lost_key
from returned_key import returned_key
from room_requests import room_requests
from rooms import rooms

if __name__=='__main__':
    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)
    
    metadata.drop_all(bind=engine)  # start with a clean slate while in development
    
    # Create whatever tables are called for by our "Entity" classes.  The simple fact that
    # your classes that are subtypes of Base have been loaded by Python has populated
    # the metadata object with their definition.  So now we tell SQLAlchemy to create
    # those tables for us.
    metadata.create_all(bind=engine)

    k1: keys = keys(serial_number=12345)

    with Session() as sess:
        sess.begin()
        sess.add(k1)
        sess.commit()
    