from pymongo import MongoClient
MONGO_URI = "mongodb+srv://rinshadkv20:NkkQ9bUP5FBJGIa8@cluster0.w0i8hsg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# MongoDB database and collection names
DB_NAME = "school"
COLLECTION_NAME = "students"

# MongoDB Atlas client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]