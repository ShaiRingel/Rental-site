from User import User
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\shair\OneDrive\שולחן העבודה\Program\Rental-site\RentalServicesproject.accdb;"
)

class Renter(User):
    __tablename__ = "Renter"

    id = sa.Column(sa.Integer, sa.ForeignKey('User.ID'), primary_key = True)
    username = sa.Column(sa.String, sa.ForeignKey('User.Username'))
    password = sa.Column(sa.String, sa.ForeignKey('User.Password'))
    group_number = sa.Column(sa.Integer, sa.ForeignKey('User.Group_number'))
    unique_code = sa.Column(sa.String, sa.ForeignKey('User.Unique_code'))
    productID = sa.Column("ProductID", sa.Integer)

    __mapper_args__ = {
        'inherit_condition': id == User.id,  # Define the inheritance condition
        'inherit_condition': username == User.username,  # Define the inheritance condition
        'inherit_condition': password == User.password,  # Define the inheritance condition
        'inherit_condition': group_number == User.group_number,  # Define the inheritance condition
        'inherit_condition': unique_code == User.unique_code  # Define the inheritance condition
    }
    
    def __init__(self, id, username, password, group_number, unique_code, productID):
        super().__init__(id, username, password, group_number, unique_code)
        self.productID = productID


def createNewRenter(renterID, desired_price, request_status):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        id = (session.query(Renter).all()[-1]).id + 1
    except:
        id = 1
    
    transaction = Renter(id, renterID, desired_price, request_status)
    session.add(transaction)
    session.commit()
    print(f"Renter with ID {id} has been created.")
    session.close()


def updateExistingRenterByID(id, renterID=None, desired_price=None, request_status=None):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Renter).filter(Renter.id == id).first()

    if transaction:
        if transaction.renterID != renterID and renterID != None:
            transaction.renterID = renterID
        if transaction.desired_price != desired_price and desired_price != None:
            transaction.desired_price = desired_price
        if transaction.request_status != request_status and request_status != None:
            transaction.request_status = request_status
        
        session.commit()
        print(f"Renter with ID {id} has been updated.")
    else:
        print(f"Renter with ID {id} does not exist.")
    session.close()


def removeExistingRenterByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Renter).filter(Renter.id == id).first()

    if transaction:
        # If transaction exists, delete the transaction
        session.delete(transaction)
        session.commit()
        print(f"Renter with ID {id} has been removed.")
    else:
        print(f"Renter with ID {id} does not exist.")
    
    session.close()

def getAllRenter():
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Renter).all()