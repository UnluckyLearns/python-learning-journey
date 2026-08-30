from fastapi import APIRouter
from fastapi import FastAPI
from Inventory_mana import InventoryManager
from Models import Product,UpdateProduct,Customer,Category,Order
#  /  @  > < [] {}

router = APIRouter()
inv_manager = InventoryManager()    
        # PRODUCT ROUTES
@router.get('/products')
def display_products():
    return inv_manager.select_products()


@router.get('/products/{product_id}')
def display_product(product_id : int):
    return inv_manager.select_productsByID(product_id)

@router.post('/products')
def ins_product(product : Product):
    return inv_manager.insert_product(product)


@router.put('/products/{product_id}')
def  up_product(product_id : int ,product : UpdateProduct):
    return inv_manager.update_product(product,product_id)

@router.delete('/products/{product_id}')
def del_product(product_id:int):
    inv_manager.delete_product(product_id)


            # CUSTOMER ROUTES 
@router.get('/customers')
def display_customers():
    return inv_manager.select_customers()

@router.post('/customers')
def ins_customer(customer : Customer):
    return inv_manager.insert_customer(customer)

@router.get('/customers/{customer_id}')
def display_customer(customer_id : int):
    return inv_manager.select_customerByID(customer_id)

            # CATEGORY ROUTES

@router.get('/categories')
def display_categories():
    return inv_manager.select_categories()

@router.post('/categories')
def ins_category(category : Category):
    return inv_manager.insert_category(category)

            # ORDER ROUTES

@router.get('/orders')
def display_orders():
    return inv_manager.selct_orders()

@router.post('/orders')
def ins_orders(order:Order):
    return inv_manager.insert_orders(order)
