from pydantic import BaseModel
import Product

class APIProduct(BaseModel):
    id: int
    userID: int
    name: str
    description: str
    condition: str
    price: int
    image_url: str
    availability: bool
    

def getProductByID(id):
    filtered_product = Product.getProductByID(id)
    return APIProduct(id=id, userID=filtered_product.userID, name=filtered_product.name,
                   description=filtered_product.description, condition=filtered_product.condition,
                   price=filtered_product.price, image_url=filtered_product.image_url, 
                   availability=filtered_product.availability)

def createNewProduct(userID, name, description, condition, price, image_url, availability):
    Product.createNewProduct(userID, name, description, condition, price, image_url, availability)