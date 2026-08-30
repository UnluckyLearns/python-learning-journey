import sqlite3
from Settings import *
#  /  @  > < [] {}
class Database():
    def __init__(self): 
        self.command_create = ["""CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY,name TEXT)""",
                               """CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY,name TEXT,email TEXT)""",
                                """CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY,name TEXT,price REAL,stock INTEGER CHECK(stock >= 0),category_id INTEGER,FOREIGN KEY (category_id) REFERENCES categories(id))""",
                                """CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY,customer_id INTEGER,created_at TEXT,FOREIGN KEY(customer_id) REFERENCES customers(id))""",
                               """CREATE TABLE IF NOT EXISTS order_items (id INTEGER PRIMARY KEY, order_id INTEGER,product_id INTEGER, quantity INTEGER,FOREIGN KEY(order_id) REFERENCES orders(id),FOREIGN KEY(product_id) REFERENCES products(id))"""
                               ] 
        self.command_insert_category = "INSERT INTO categories (name) VALUES (?) RETURNING name"
        self.command_insert_product = "INSERT INTO products (name,price,stock,category_id) VALUES (?,?,?,?) RETURNING name,price,stock,category_id"
        self.command_insert_customer = "INSERT INTO customers(name,email) VALUES (?,?) RETURNING name,email"
        self.command_insert_order = "INSERT INTO orders(customer_id) VALUES (?) RETURNING id"
        self.command_insert_order_items = "INSERT INTO order_items(order_id,product_id,quantity) VALUES (?,?,?)"

        self.command_remove_stock = "UPDATE products SET stock = stock - ? WHERE id = ?"

        self.command_update_product = "UPDATE products SET name = COALESCE(?,name),price = COALESCE(?,price),stock = COALESCE(?,stock),category_id = COALESCE(?,category_id) WHERE id = ? RETURNING name,price,stock,category_id "


        self.command_delete_product = "DELETE FROM products WHERE id = ?"


        self.command_SelectProducts = "SELECT t1.name,t1.price,t1.stock,t2.name FROM products AS t1 JOIN categories AS t2 ON t2.id = t1.category_id"
        self.command_SelectProductBYID = "SELECT t1.name,t1.price,t1.stock,t2.name FROM products AS t1 JOIN categories AS t2 ON t2.id = t1.category_id WHERE t1.id = ?"

        self.command_SelectCustomers = "SELECT name,email FROM customers"
        self.command_SelectCustomerByID = "SELECT name,email FROM customers WHERE id = ? "

        self.command_SelectCategories = "SELECT name FROM categories"

        self.command_SelectOrders = "SELECT t1.name,t4.id,t3.price,t2.quantity,t3.name FROM customers as t1 JOIN orders AS t4 ON t1.id = t4.customer_id JOIN order_items AS t2 ON t4.id = t2.order_id JOIN products AS t3 ON t3.id = t2.product_id  "

        self.command_select_prodCate = "SELECT table1.name , table2.name FROM products AS table1 JOIN categories AS table2 ON table1.category_id = table2.id  "
        self.command_select_prodCate2 = "SELECT table1.name , table2.name FROM products AS table1 JOIN categories AS table2 ON table1.category_id = table2.id  WHERE table2.name = 'Books'"

        self.command_select_productCost  = "SELECT name,price FROM products WHERE price > 50 "
        self.command_select_productCostMax  = "SELECT name,MAX(price) FROM products"
        self.command_select_productStock = "SELECT name,stock FROM products WHERE stock < 33 "

        self.command_select_CountProdCate = "SELECT COUNT(table1.name),table2.name FROM products AS table1 JOIN categories AS table2 ON table1.category_id = table2.id GROUP BY table2.name"
        self.command_select_AVGPriceProdCate = "SELECT AVG(table1.price),table2.name FROM products AS table1 JOIN categories AS table2 ON table1.category_id = table2.id GROUP BY table2.name"

        self.command_select_CustomerOrder = "SELECT table1.name , COUNT(table2.id) FROM customers AS table1 JOIN orders AS table2 ON table1.id = table2.customer_id GROUP BY table1.name"
        self.command_select_OrderDetails = "SELECT table1.name ,table2.id,table2.created FROM customers AS table1 JOIN orders AS table2 ON table1.id = table2.customer_id "
        self.command_select_OrderProductDetails = "SELECT table1.name ,table2.id,table4.name FROM customers AS table1 JOIN orders AS table2 ON table1.id = table2.customer_id  JOIN order_items AS table3 ON table3.order_id = table2.id JOIN products AS table4 ON table3.product_id = table4.id"
        self.command_select_SumProducts = "SELECT table1.name,SUM(table3.quantity) FROM customers AS table1 JOIN orders AS table2 ON table1.id = table2.customer_id JOIN order_items AS table3 ON table3.order_id = table2.id GROUP BY table1.name"
        self.command_select_TotalPriceByOrder = "SELECT table1.id,(table2.quantity * table3.price) FROM orders AS table1 JOIN order_items AS table2 ON table1.id = table2.order_id JOIN products AS table3 ON table3.id = table2.product_id "
        self.command_select_BiggestSpender = "SELECT table1.name,SUM(table3.quantity*table4.price) FROM customers as table1 JOIN orders AS table2 ON table1.id = table2.customer_id JOIN order_items as table3 ON table3.order_id = table2.id JOIN products AS table4 ON table3.product_id = table4.id GROUP BY table1.name ORDER BY SUM(table3.quantity*table4.price) desc  LIMIT 1"
        self.command_select_BadProducts = "SELECT table1.name FROM products AS table1 LEFT JOIN order_items AS table2 ON table2.product_id = table1.id WHERE table2.product_id IS NULL"
        self.command_select_BadCustomers = "SELECT table1.name FROM customers AS table1 LEFT JOIN orders AS table2 on table2.customer_id = table1.id WHERE table2.customer_id IS NULL"

        self.inser1 = "INSERT INTO orders (customer_id, created) VALUES (1, '2026-08-20'),(1, '2026-08-21'),(2, '2026-08-22'),(3, '2026-08-23')"
        self.inser2 = "INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 1, 1),(1, 3, 2),(2, 2, 1),(2, 4, 2),(3, 1, 1),(4, 3, 3)"

                # CREATING TABLES
    def create_db(self,commands):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            for command in commands:
                cursor.execute(command)
            connection.commit()

                # INSERTION
    def insert_category(self,command,category):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(command,(category.name,))
            l = cursor.fetchone()
            connection.commit()
            return l

    def insert_product(self,command,product):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(command,(product.name,product.price,product.stock,product.category_id))
            l = cursor.fetchone()
            connection.commit()
            return l

    def insert_customer(self,command,customer):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(command,(customer.name,customer.email))
            l = cursor.fetchone()
            connection.commit()
            return l

    def insert_db(self,command):
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            cursor.execute(command)
            connection.commit()


    def insert_order_items(self,order):
        print(order.customer_id)
        for item in order.items:
            print(item.product_id)
            print(item.quantity)
        with sqlite3.connect(DB_PATH) as connection :    
            try:        
                cursor = connection.cursor()
                cursor.execute(self.command_insert_order,(order.customer_id,))
                order_id = cursor.fetchone()[0]
                print(order_id)
                for item in order.items:
                    print(item.product_id)
                    cursor.execute(self.command_insert_order_items,(order_id,item.product_id,item.quantity))
                    cursor.execute(self.command_remove_stock,(item.quantity,item.product_id))
                connection.commit()
            except sqlite3.Error:
                print("FAILED")
                connection.rollback()
            # SELECTION

    def select_db(self,command):
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            cursor.execute(command)
            return cursor.fetchall()

    def select_dbBYID(self,command,id):
        with sqlite3.connect(DB_PATH) as connection :
            cursor = connection.cursor()
            cursor.execute(command,(id,))
            return cursor.fetchone()

    def select_orders(self,command):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(command)
            l = cursor.fetchall()
            return l


            # UPDATE
    def update_db(self,command,product,id):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(command,(product.name,product.price,product.stock,product.category_id,id))
            l = cursor.fetchone()
            connection.commit()
            return l 
        
            # DELETE
    def delete_product(self,command,id):
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute(command,(id,))
            connection.commit()

