from pydantic import BaseModel
import Transaction

class APITransaction(BaseModel):
    id: int
    renterID: int
    start_date: str
    end_date: str
    status: str
    

def getTransactionByID(id):
    filtered_transaction = Transaction.getTransactionByID(id)
    return APITransaction(id=id, renterID=filtered_transaction.renterID,
                          start_date=filtered_transaction.start_date, 
                          end_date=filtered_transaction.end_date, status=filtered_transaction.status)

def createNewTransaction(renterID, start_date, end_date, status):
    Transaction.createNewTransaction(renterID, start_date, end_date, status)