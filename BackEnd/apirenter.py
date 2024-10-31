from pydantic import BaseModel
import renter

class APIRenter(BaseModel):
    id: int
    username: str
    password: str
    group_number: int
    unique_code: str
    productID: int
    

def getRenterByID(id):
    filtered_renter = renter.getRenterByID(id)
    return APIRenter(id=id, username=filtered_renter.username, password=filtered_renter.password,
                   group_number=filtered_renter.group_number, unique_code=filtered_renter.unique_code)

def createNewRenter(username, password, group_number, unique_code, productID):
    renter.createNewRenter(username, password, group_number, unique_code, productID)