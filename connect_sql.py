from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1810",
        database="connect_api",
        port=3306
    )
    
class user(BaseModel):
    User_Id : int
    Username : str
    Mobile_Number : str
    Entry_Date : str
    
@app.post("/user")
def insert_user(User:user):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO user (User_Id, Username, Mobile_Number, Entry_Date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (User.User_Id, User.Username, User.Mobile_Number, User.Entry_Date))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "User added"}

@app.get("/user")
def view_user():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

class unit(BaseModel):
    Unit_Id : int
    Unit : str

@app.post("/unit")
def insert_unit(Unit:unit):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO unit (Unit_Id, Unit) VALUES (%s, %s)"
    cursor.execute(sql, (Unit.Unit_Id, Unit.Unit))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Unit added"}

@app.get("/unit")
def view_unit():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM unit")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

class product(BaseModel):
    Product_Id : int
    Product_Name : str
    Unit_Id : int
    Per_Price : int
    Expiry_Date : str

@app.post("/products")
def insert_product(Product:product):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO product (Product_Id, Product_Name, Unit_Id, Per_Price, Expiry_Date) VALUES (%s, %s, %s, %s,%s)"
    cursor.execute(sql, (Product.Product_Id, Product.Product_Name, Product.Unit_Id, Product.Per_Price, Product.Expiry_Date))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Product added"}

@app.get("/products")
def view_product():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM product")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

class order_list(BaseModel):
    Order_List_Id : int
    User_Id : int
    Total_Amount : int
    Order_Date : str
    Order_Status : str

@app.post("/order_list")
def insert_order_list(Order_List:order_list):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO order_list (Order_List_Id, User_Id, Total_Amount, Order_Date, Order_Status) VALUES (%s, %s, %s, %s,%s)"
    cursor.execute(sql, (Order_List.Order_List_Id, Order_List.User_Id, Order_List.Total_Amount, Order_List.Order_Date, Order_List.Order_Status))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Order_List added"}

@app.get("/order_list")
def view_order_list():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM order_list")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

class order_items(BaseModel):
    Order_Items_Id : int
    Order_List_Id : int
    Product_Id : int
    Quantity : int

@app.post("/order_items")
def insert_order_items(Order_Items:order_items):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO order_items(Order_Items_Id, Order_List_Id, Product_Id, Quantity) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (Order_Items.Order_Items_Id, Order_Items.Order_List_Id, Order_Items.Product_Id, Order_Items.Quantity))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Order_Items added"}

@app.get("/order_items")
def view_order_items():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM order_items")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

##Join Tables

@app.get("/order")
def view_order():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT order_list.Order_List_Id, user.Username, user.Mobile_Number, product.Product_Name, order_items.Quantity, order_list.Total_Amount, order_list.Order_Date, order_list.Order_Status FROM order_list INNER JOIN user ON user.User_Id=order_list.User_Id INNER JOIN order_items ON order_items.Order_List_Id=order_list.Order_List_Id INNER JOIN product ON product.Product_Id=order_items.Product_Id")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

@app.get("/orderleftjoin")
def view_order_leftjoin():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT order_list.Order_List_Id, user.Username, user.Mobile_Number, product.Product_Name, order_items.Quantity, order_list.Total_Amount, order_list.Order_Date, order_list.Order_Status FROM order_list LEFT JOIN user ON user.User_Id=order_list.User_Id LEFT JOIN order_items ON order_items.Order_List_Id=order_list.Order_List_Id LEFT JOIN product ON product.Product_Id=order_items.Product_Id")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

@app.get("/orderrightjoin")
def view_order_rightjoin():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT order_list.Order_List_Id, user.Username, user.Mobile_Number, product.Product_Name, order_items.Quantity, order_list.Total_Amount, order_list.Order_Date, order_list.Order_Status FROM order_list RIGHT JOIN user ON user.User_Id=order_list.User_Id RIGHT JOIN order_items ON order_items.Order_List_Id=order_list.Order_List_Id RIGHT JOIN product ON product.Product_Id=order_items.Product_Id")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data