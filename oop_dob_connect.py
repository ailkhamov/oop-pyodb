import pyodbc

# Concept of 'Strong Params'
    # never EVER, Trust user Input
    # Avoid SQL injections
    # Filter for SQL Injections

class ConnectMicrosoftServer():
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE='+ self.database +';UID='
                                      +self.username+';PWD='+ self.password)
        self.cursor = self.conn_db.cursor()

    def __filter_query(self, query):
        # Doing some filtering for some bad queries
        return self.cursor.execute(query)


    def sql_query(self, query):
        return self.__filter_query(query)

    def sql_query_fetchone(self, query):
        return  self.__filter_query(query).fetchone()

    def print_all_product_records(self, table):
        query_rows = self.__filter_query(f'SELECT * From {table}')
        while True:
            record = query_rows.fetchone
            if record is None:
                break
            print(record)
    def print_average_price_products(self, table):
        query_rows = self.__filter_query(f'SELECT AVG(UnitPrice) FROM {table}')
        record = query_rows.fetchone()
        print(record)

    def return_avg_unitprice_products(self):
        query = self.__filter_query('SELECT * FROM Products')
        prices = []
        while True:
            # get indivudaul prices and eppend to my list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        return print(sum(prices)/len(prices))
from oop_dob_connect import *


server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_now = ConnectMicrosoftServer(server,database,username,password)

question_1 = db_now
question_2 = db_now

question_2.return_avg_unitprice_products()

# CRUD

# Create 1 entry
    # User Insert
    # The cursor cannot make transactions ( got to documantions )
    #

# Read all entreis
    # fetch all record and return as List of Dictionaries

# Read one entry
    # fetch a specific record
    # Get one value using ID
# Update 1 entry
    # The id of the record to update
    # Update the specific record
        # The cursor cannot make transaction (go to documantation)

# Destroy / one entry
    # The id of the specific record
    # Destroy the record
        # The cursur cannot make transaction (got to documantion)








