from pymongo import MongoClient

# Replace with your MongoDB connection string
# Make sure to replace "<password>" with the actual password for the user
# and "<dbname>" with the name of your database
connection_string = "mongodb+srv://<username>:<password>@<cluster-address>/<dbname>?retryWrites=true&w=majority"

# Initialize the MongoClient
client = MongoClient(connection_string)

# Access the specified database
db = client.get_database('<dbname>')

# Access the specified collection
collection = db.get_collection('<collection_name>')

# Query to retrieve documents (change this query as per your collection's structure)
query = {}

# Retrieve data from the collection based on the query
cursor = collection.find(query)

# Iterate over the cursor to print each document
for document in cursor:
    print(document)

# Close the connection to MongoDB
client.close()
