import  pyodbc # package used to connect to our database

# In this file we will make our connection

# Parameters/variables for connection

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


# Establish a connection to North Wind database
conn_northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE='+ database +';UID='+username+';PWD='+ password)

print(conn_northwind)

# Create a curso - in order to execute sql quires we need to create a curser
# Allows us to execute readonly queries of our database
cursor = conn_northwind.cursor()

# cursor.execute("SELECT * FROM Customers;")
# # Fetch rows from cursor - Fetch one
# row = cursor.fetchone()
#
# print(row)
# # Fetch all
# # This is bad MM'kay
# # We dont' you this mm'kay...
# rows = cursor.execute("SELECT * FROM Customers;").fetchall()
# for row in rows:
#     print(row)

# Fetch some data using for loops
# rows = cursor.execute("SELECT * FROM Products").fetchall()
# count = 0
#for row in rows:
  #  print(row.UnitPrice) # We can access the column of a specific record

# However, this is dangerous as we said
# Because we can clog our machine with too much date
    # We can use While Loop to be more effiecent

rows = cursor.execute('SELECT *  FROM Orders').fetchall()
print("Question1")
print(len(rows))
# while True:
#     record = rows.fetchone()
#     if record is None:
#         break
#     print(len(record))

print("Question2")
question2 = cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro'").fetchall()
print(len(question2))

print("Question3")
question3 = cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro' OR ShipCity = 'Reims'").fetchall()
for row in question3:
    print(row)
print("Number of orders for Question 3")
print(len(row))