import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_base = declarative_base()
connection_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\shair\OneDrive\שולחן העבודה\Program\Rental-site\RentalServicesproject.accdb;"
)

class Transaction(_base):
    __tablename__ = "Transaction"

    id = sa.Column("ID", sa.Integer, primary_key=True)
    renterID = sa.Column("RenterID", sa.Integer)
    start_date = sa.Column("Start_date", sa.Date)
    end_date = sa.Column("End_date", sa.Date)
    status = sa.Column("Status", sa.String)

    def __init__(self, renterID, start_date, end_date, status):
        self.renterID = renterID
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
    
    def __repr__(self):
        return f"ID:{self.id}\renterID:{self.renterID}\nStart_Date:{self.start_date}\nEnd_Date:{self.end_date}\nStatus:{self.status}"

def createNewTransaction(renterID, start_date, end_date, status):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        id = (session.query(Transaction).all()[-1]).id + 1
    except:
        id = 1
    
    transaction = Transaction(id, renterID, start_date, end_date, status)
    session.add(transaction)
    session.commit()
    print(f"Tranction with ID {id} has been created.")
    session.close()


def updateExistingTransactionByID(id, renterID=None, start_date=None, end_date=None, status=None):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Transaction).filter(Transaction.id == id).first()

    if transaction:
        fields_to_update = {
            'renterID': renterID,
            'start_date': start_date,
            'end_date': end_date,
            'status': status
        }

        for field, value in fields_to_update.items():
            if getattr(transaction, field) != value and value is not None:
                setattr(transaction, field, value)
        
        session.commit()
        print(f"Tranction with ID {id} has been updated.")
    else:
        print(f"Tranction with ID {id} does not exist.")
    session.close()


def removeExistingTransactionByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Transaction).filter(Transaction.id == id).first()

    if transaction:
        # If transaction exists, delete the transaction
        session.delete(transaction)
        session.commit()
        print(f"Tranction with ID {id} has been removed.")
    else:
        print(f"Tranction with ID {id} does not exist.")
    
    session.close()


def getAllTransaction():
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Transaction).all()

def getTransactionByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Transaction).filter(Transaction.id == id).first()