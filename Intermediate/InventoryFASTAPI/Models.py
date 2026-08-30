from pydantic import BaseModel,Field,EmailStr
from typing import Literal
#  /  @  > < [] {}
class Product(BaseModel):
    name : str = Field(min_length = 5 ,max_length = 25)
    price : float
    stock : int
    category_id : Literal [1,2,3,4]  = Field(default = 1,description = "1 = Electronics,2 = Books,3 = Games,4 = Clothing")

class UpdateProduct(BaseModel):
    name : str | None  = Field(default = None,min_length = 5 ,max_length = 25)
    price : float | None = None
    stock : int | None = None
    category_id : Literal [1,2,3,4] | None  = Field(default = None,description = "1 = Electronics,2 = Books,3 = Games,4 = Clothing")


class Customer(BaseModel):
    name : str = Field(min_length= 5,max_length= 25)
    email : EmailStr 

class Category(BaseModel):
    name : str = Field(min_length = 5,max_length = 25)


class OrderProducts(BaseModel):
    product_id : int
    quantity : int


class Order(BaseModel):
    customer_id : int
    items : list[OrderProducts]