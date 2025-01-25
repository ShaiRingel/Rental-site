from pydantic import BaseModel
import Request

class APIRequest(BaseModel):
    id: int
    renterID: str
    desired_price: int
    request_status: bool
    

def getRequestByID(id):
    filtered_request = Request.getRequestByID(id)
    return APIRequest(id=id, renterID=filtered_request.renterID, 
                      desired_price=filtered_request.desired_price, 
                      request_status=filtered_request.request_status)

def createNewRequest(renterID, desired_price, request_status):
    Request.createNewRequest(renterID, desired_price, request_status)