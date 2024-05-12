import mysql.connector

def list_all():
	c = db.cursor()
	sql = """SELECT * FROM products"""
	c.execute(sql)
	prod_data = c.fetchall()
 
	# print all the data returned by the database
	for p in prod_data:
   	    print(p[0] , " " , p[1] ," " , p[2])
 
	# finally closing the database connection
	db.close()

def insert_data(pname,price):
	c = db.cursor()
	sql = """INSERT INTO products (prod_name,price) VALUES  (%s, %s)"""
	data = [(pname,price),]
	c.executemany(sql, data)
	db.commit()
 
	# finally closing the database connection
	db.close()

def update_data(id,pname,price):
	c = db.cursor()
	sql = "update products set prod_name='" + pname + "',price=" + price + " where id=" + id
	c.execute(sql)
	db.commit()
 
	# finally closing the database connection
	db.close()	
	
def delete_data(id):
	c = db.cursor()
	sql = "delete from products where id = "+ id
	c.execute(sql)
	db.commit()
 
	# finally closing the database connection
	db.close()	
   
def check_selection(input_str):
    if input_str.strip()=="1":
        print("Add product\n")
        prod_name = input("Enter Product Name: ")
        prod_price = input("Enter Price: ")
        insert_data(prod_name,prod_price)
  
    if input_str.strip()=="2":
        print("Delete Product\n")
        prod_id = input("Enter Product Id: ")
        delete_data(prod_id)
        
    if input_str.strip()=="3":
        print("Edit Product\n")
        prod_id = input("Enter Product Id: ")
        prod_name = input("Enter new Name: ")
        prod_price = input("Enter new Price: ")
        update_data(prod_id,prod_name,prod_price)
 
    if input_str.strip()=="4":
        print("Listing Product\n")
        print("Id     Name     Price")
        list_all()
        
    if input_str.strip()=="5":
        print("Bye!!!\n")
    else:
        print("\nInvalid Option !!!")
        
db = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="1234",
  database="mydatabase"
)

user_input = "0"
while user_input != "5":
	print("\nProduct Records Menu\n")

	print(" 1 - Add Product")
	print(" 2 - Delete Product")
	print(" 3 - Edit Product")
	print(" 4 - List All Products")
	print(" 5 - Exit\n")
	user_input = input("Enter Selection: ")
	check_selection(user_input)

 
