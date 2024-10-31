from pydantic import BaseModel
import message as msg

class APIMessage(BaseModel):
    id: int
    renterID: int
    message: str
    timestamp: str
    

def getMessageByID(id):
    filtered_message = msg.getMessageByID(id)
    return APIMessage(id=id, renterID=filtered_message.renterID, 
                      message=filtered_message.message, 
                      timestamp=filtered_message.timestamp)

def createNewMessage(renterID, message, timestamp):
    msg.createNewMessage(renterID, message, timestamp)