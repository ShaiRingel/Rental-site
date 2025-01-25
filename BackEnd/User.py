import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_base = declarative_base()
connection_string = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\shair\Rental-site\RentalServicesproject.accdb;"
)

class User(_base):
    __tablename__ = "User"

    id = sa.Column("ID", sa.Integer, primary_key=True)
    username = sa.Column("Username", sa.String)
    password = sa.Column("Password", sa.String)
    group_number = sa.Column("Group_number", sa.Integer)
    unique_code = sa.Column("Unique_code", sa.String)

    def __init__(self, id, username, password, group_number, unique_code):
        self.id = id
        self.username = username
        self.password = password
        self.group_number = group_number
        self.unique_code = unique_code

    
    def __repr__(self):
        return f"ID:{self.id}\nUserName:{self.username}\nPassword:{self.password}\ngroup_number:{self.group_number}\nunique code:{self.unique_code}"


def createNewUser(username, password, group_number, unique_code):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        id = (session.query(User).all()[-1]).id + 1
    except:
        id = 1
    
    user = User(id, username, password, group_number, unique_code)
    session.add(user)
    session.commit()
    print(f"User with ID {id} has been created.")
    session.close()


def updateExistingUserByID(id, username=None, password=None, group_number=None, unique_code=None):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter(User.id == id).first()

    if user:
        fields_to_update = {
            'username': username,
            'password': password,
            'group_number': group_number,
            'unique_code': unique_code
        }

        for field, value in fields_to_update.items():
            if getattr(user, field) != value and value is not None:
                setattr(user, field, value)
        
        session.commit()
        print(f"User with ID {id} has been updated.")
    else:
        print(f"User with ID {id} does not exist.")
    session.close()


def removeExistingUserByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter(User.id == id).first()

    if user:
        # If user exists, delete the user
        session.delete(user)
        session.commit()
        print(f"User with ID {id} has been removed.")
    else:
        print(f"User with ID {id} does not exist.")
    
    session.close()


def getAllUsers():
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(User).all()


def getUserByID(id):
    engine = sa.create_engine(f"access+pyodbc:///?odbc_connect={connection_string}")

    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(User).filter(User.id == id).first()