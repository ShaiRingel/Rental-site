from fastapi import FastAPI
from apirenter import *
from apiproduct import *
from apimessage import *
from apirequest import *
from apitransaction import *
from apiuser import *

app = FastAPI()


@app.post("/users")
def post_user(user: APIUser):
    createNewUser(user.username, user.password, user.group_number, user.unique_code)


@app.post("/renter")
def post_renter(renter: APIRenter):
    createNewRenter(renter.username, renter.password, renter.group_number, renter.unique_code,
                    renter.productID)


@app.post("/transaction")
def post_transaction(transaction: APITransaction):
    createNewTransaction(transaction.renterID, transaction.start_date, transaction.end_date, 
                         transaction.status)


@app.post("/request")
def post_request(request: APIRequest):
    createNewRequest(request.renterID, request.desired_price, request.request_status)


@app.post("/message")
def post_message(message: APIMessage):
    createNewMessage(message.renterID, message.message, message.timestamp)


@app.post("/product")
def post_product(product: APIProduct):
    createNewProduct(product.userID, product.name, product.description, product.condition,
                     product.price, product.image_url, product.availability)


@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = getUserByID(user_id)
    print(user.username)
    return {"user_id": user_id, "name": user.username, "password": user.password, 
            "group_number": user.group_number, "unique_code": user.unique_code}


@app.get("/renter/{renter_id}")
def read_user(renter_id: int):
    renter = getRenterByID(renter_id)
    print(renter.username)
    return {"user_id": renter_id, "name": renter.username, "password": renter.password, 
            "group_number": renter.group_number, "unique_code": renter.unique_code, 
            "product_id": renter.productID}


@app.get("/product/{product_id}")
def read_user(product_id: int):
    product = getProductByID(product_id)
    print(product.name)
    return {"product_id": product_id, "userID": product.userID, "name": product.name, 
            "description": product.description, "condition": product.condition, "price": product.price,
            "image_url": product.image_url, "availability": product.availability}


@app.get("/transaction/{transaction_id}")
def read_user(transaction_id: int):
    transaction = getTransactionByID(transaction_id)
    print(transaction.username)
    return {"transaction_id": transaction_id, "renterID": transaction.renterID, 
            "start_id": transaction.start_date, "end_date": transaction.end_date, 
            "status": transaction.status}


@app.get("/request/{request_id}")
def read_user(request_id: int):
    request = getRequestByID(request_id)
    print(request.id)
    return {"request_id": request_id, "renterID": request.renterID, 
            "desired_price": request.desired_price, "request_status": request.request_status}


@app.get("/message/{message_id}")
def read_user(message_id: int):
    message = getMessageByID(message_id)
    print(message.id)
    return {"message_id": message_id, "renter_id": message.renterID, "message": message.message, 
            "timestamp": message.timestamp}