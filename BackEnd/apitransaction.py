from pydantic import BaseModel
import transaction

class APITransaction(BaseModel):
    id: int
    renterID: int
    start_date: str
    end_date: str
    status: str
    

def getTransactionByID(id):
    filtered_transaction = transaction.getTransactionByID(id)
    return APITransaction(id=id, renterID=filtered_transaction.renterID,
                          start_date=filtered_transaction.start_date, 
                          end_date=filtered_transaction.end_date, status=filtered_transaction.status)

def createNewTransaction(renterID, start_date, end_date, status):
    transaction.createNewTransaction(renterID, start_date, end_date, status)