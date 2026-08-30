from Database import Database
#  /  @  > < [] {}
class InventoryManager():
    def __init__(self):
        self.db = Database()
        self.db.create_db(self.db.command_create)

                        # PRODUCTS
    def select_products(self):
        return self.db.select_db(self.db.command_SelectProducts)

    def select_productsByID(self,id):
        return self.db.select_dbBYID(self.db.command_SelectProductBYID,id)

    def insert_product(self,product):
        return self.db.insert_product(self.db.command_insert_product,product)

    def update_product(self,product,id):
        return self.db.update_db(self.db.command_update_product,product,id)

    def delete_product(self,id):
         self.db.delete_product(self.db.command_delete_product,id)

                        # CUSTOMER

    def insert_customer(self,customer):
        return self.db.insert_customer(self.db.command_insert_customer,customer)

    def select_customers(self):
        return self.db.select_db(self.db.command_SelectCustomers)

    def select_customerByID(self,id):
        return self.db.select_dbBYID(self.db.command_SelectCustomerByID,id)

                        # CATEGORY
    
    def select_categories(self):
        return self.db.select_db(self.db.command_SelectCategories)

    def insert_category(self,category):
        return self.db.insert_category(self.db.command_insert_category,category)


                         # ORDERS
    
    def insert_orders(self,order):
        print("COOKED")
        self.db.insert_order_items(order)

    def selct_orders(self):
        
        return self.db.select_orders(self.db.command_SelectOrders)
    

    


    