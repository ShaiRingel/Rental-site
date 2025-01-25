import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_base = declarative_base()
connection_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\shair\Rental-site\RentalServicesproject.accdb;"
)

class Product(_base):
    __tablename__ = "Product"

    id = sa.Column("ID", sa.Integer, primary_key=True)
    userID = sa.Column("UserID", sa.String)
    name = sa.Column("Name", sa.String)
    description = sa.Column("Description", sa.String)
    condition = sa.Column("Condition", sa.String)
    price = sa.Column("Price", sa.Integer)
    image_url = sa.Column("Image_url", sa.String)
    availability = sa.Column("Availability", sa.String)

    def __init__(self, id, userID, name, description, condition, price, image_url, availability):
        self.id = id
        self.userID = userID
        self.name = name
        self.description = description
        self.condition = condition
        self.price = price
        self.image_url = image_url
        self.availability = availability

def createNewProduct(userID, name, description, condition, price, image_url, availability):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        id = (session.query(Product).all()[-1]).id + 1
    except:
        id = 1
    
    transaction = Product(id, userID, name, description, condition, price, image_url, availability)
    session.add(transaction)
    session.commit()
    print(f"Product with ID {id} has been created.")
    session.close()


def updateExistingProductByID(id, userID=None, name=None, description=None, condition=None,
                            price=None, image_url=None, availability=None):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Product).filter(Product.id == id).first()

    if transaction:
        fields_to_update = {
            'userID': userID,
            'name': name,
            'description': description,
            'condition': condition,
            'price': price,
            'image_url': image_url,
            'availability': availability
        }

        for field, value in fields_to_update.items():
            if getattr(transaction, field) != value and value is not None:
                setattr(transaction, field, value)
        
        session.commit()
        print(f"Product with ID {id} has been updated.")
    else:
        print(f"Product with ID {id} does not exist.")
    session.close()


def removeExistingProductByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    transaction = session.query(Product).filter(Product.id == id).first()

    if transaction:
        # If transaction exists, delete the transaction
        session.delete(transaction)
        session.commit()
        print(f"Product with ID {id} has been removed.")
    else:
        print(f"Product with ID {id} does not exist.")
    
    session.close()

def getAllProduct():
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Product).all()

def getProductByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Product).filter(Product.id == id).first()