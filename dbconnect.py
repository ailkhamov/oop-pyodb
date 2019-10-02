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

# Create a cursor

#
