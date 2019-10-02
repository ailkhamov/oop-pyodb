Connecting SQL to Python using pyodbc 
-

This is an example of us connecting to our SQL server,
using pytodbc

We will look into:
- 
1. Cursor
2. Rows
3. Using While loops for effecient data queries
4. Querying the db 
5. Transactions 

## What is a connection ?
    Read-only attribute returning a reference to the connection object which cursor was created

## What is a cursor ? .cursor()
    Read only attribute describing the result of query.
    It is a sequance of 'column' instances, each one describing one result column in order 
     
    
## cursor().execute() -  
    Execute a database operation (query or command)
    Parameters may be provided as sequence or mapping and will be bound to variables in the operation. Variables are specified either with positional (%s) or named placedholders
    

## .fetchall vs fetchone
    fetchone() - Fetch the next row of query result set, returning a single tuple or None when no more data is avaliable
    fetchall() - Fetch all rows of query results returning them as list of tuples. An Empty list is returend if there is no more records to fetch

## 