import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Eukaliptus1'
)

#create a cursor object
cursorObject = dataBase.cursor()

try:
    # Execute the SQL statement to create a new database
    cursorObject.execute("CREATE DATABASE sashadb")
    print("Database created successfully!")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
finally:
    # Close the cursor and connection
    cursorObject.close()
    dataBase.close()