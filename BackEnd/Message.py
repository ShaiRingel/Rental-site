import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_base = declarative_base()
connection_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\shair\OneDrive\שולחן העבודה\Program\Rental-site\RentalServicesproject.accdb;"
)

class Message(_base):
    __tablename__ = "Message"

    id = sa.Column("ID", sa.Integer, primary_key=True)
    renterID = sa.Column("RenterID", sa.Integer)
    message = sa.Column("Message", sa.String)
    timestamp = sa.Column("Timestamp", sa.Date)

    def __init__(self, id, renterID, message, timestamp):
        self.id = id
        self.renterID = renterID
        self.message = message
        self.timestamp = timestamp


def createNewMessage(renterID, message, timestamp):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        id = (session.query(Message).all()[-1]).id + 1
    except:
        id = 1
    
    message = Message(id, renterID, message, timestamp)
    session.add(message)
    session.commit()
    print(f"Message with ID {id} has been created.")
    session.close()


def updateExistingMessageByID(id, renterID=None, message=None, timestamp=None):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    message = session.query(Message).filter(Message.id == id).first()

    if message:
        if message.renterID != renterID and renterID != None:
            message.renterID = renterID
        if message.message != message and message != None:
            message.message = message
        if message.timestamp != timestamp and timestamp != None:
            message.timestamp = timestamp
        
        session.commit()
        print(f"Message with ID {id} has been updated.")
    else:
        print(f"Message with ID {id} does not exist.")
    session.close()


def removeExistingMessageByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    message = session.query(Message).filter(Message.id == id).first()

    if message:
        # If message exists, delete the message
        session.delete(message)
        session.commit()
        print(f"Message with ID {id} has been removed.")
    else:
        print(f"Message with ID {id} does not exist.")
    
    session.close()


def getAllMessage():
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Message).all()

def getMessageByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Message).filter(Message.id == id).first()