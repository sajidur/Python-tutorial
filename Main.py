import sys
import mysql.connector

# Connect to MySQL
cnx = mysql.connector.connect(
    host="mysql5044.site4now.net",
    user="a66689_python",
    password="Root@pass1",
    database="db_a66689_python"
)

# Create a cursor
cursor = cnx.cursor()

# Execute a query
query = "SELECT * FROM test"
cursor.execute(query)

# Fetch rows
rows = cursor.fetchall()

# Process rows
for row in rows:
    print(row[0])


# Close cursor and connection
cursor.close()
cnx.close()
