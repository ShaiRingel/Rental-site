import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_base = declarative_base()
connection_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\shair\OneDrive\שולחן העבודה\Program\Rental-site\RentalServicesproject.accdb;"
)
tableName = "Request"

class Request(_base):
    __tablename__ = tableName

    id = sa.Column("ID", sa.Integer, primary_key=True)
    renterID = sa.Column("RenterID", sa.Integer)
    desired_price = sa.Column("Desired_price", sa.Integer)
    request_status = sa.Column("Request_status", sa.String)

    def __init__(self, renterID, desired_price, request_status):
        self.renterID = renterID
        self.desired_price = desired_price
        self.request_status = request_status

def createNewRequest(renterID, desired_price, request_status):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        id = (session.query(Request).all()[-1]).id + 1
    except:
        id = 1
    
    transaction = Request(id, renterID, desired_price, request_status)
    session.add(transaction)
    session.commit()
    print(f"Request with ID {id} has been created.")
    session.close()


def updateExistingRequestByID(id, renterID=None, desired_price=None, request_status=None):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Request).filter(Request.id == id).first()

    if transaction:
        if transaction.renterID != renterID and renterID != None:
            transaction.renterID = renterID
        if transaction.desired_price != desired_price and desired_price != None:
            transaction.desired_price = desired_price
        if transaction.request_status != request_status and request_status != None:
            transaction.request_status = request_status
        
        session.commit()
        print(f"Request with ID {id} has been updated.")
    else:
        print(f"Request with ID {id} does not exist.")
    session.close()


def removeExistingRequestByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Request).filter(Request.id == id).first()

    if transaction:
        # If transaction exists, delete the transaction
        session.delete(transaction)
        session.commit()
        print(f"Request with ID {id} has been removed.")
    else:
        print(f"Request with ID {id} does not exist.")
    
    session.close()


def getAllRequest():
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Request).all()