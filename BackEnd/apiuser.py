from pydantic import BaseModel
import User

class APIUser(BaseModel):
    id: int
    username: str
    password: str
    group_number: int
    unique_code: str


def getUserByID(id):
    filtered_user = User.getUserByID(id)
    return APIUser(id=id, username=filtered_user.username, password=filtered_user.password,
                   group_number=filtered_user.group_number, unique_code=filtered_user.unique_code)

def createNewUser(username, password, group_number, unique_code):
    User.createNewUser(username, password, group_number, unique_code)