import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB URI from .env
MONGODB_URI = os.getenv("MONGODB_URI")
print(MONGODB_URI)

# Connect to MongoDB
client = MongoClient(MONGODB_URI)

# Select database and collection
db = client["test"]  # Replace with your database name
products_collection = db["product2"]  # Replace with your collection name


def get_product_titles():
    try:
        # Query to get all product titles
        product_titles = products_collection.find({}, {"_id": 0, "title": 1})  # Exclude _id, include title

        # Extract titles into a list
        titles_list = [product["title"] for product in product_titles]

        return titles_list
    except Exception as e:
        print(f"Error fetching product titles: {e}")
        return []

# Function to get product by ID
def get_product_by_id(product_id):
    try:
        # Fetch the product by its ObjectId
        product = products_collection.find_one({"_id": ObjectId(product_id)})
        if not product:
            return None

        return product
    except Exception as e:
        print(f"Error fetching product: {e}")
        return None
    

def delete_all_items():
    try:
        # Delete all documents in the collection
        result = products_collection.delete_many({})
        
        print(f"Deleted {result.deleted_count} documents from the collection.")
        return result.deleted_count  # Return the count of deleted documents

    except Exception as e:
        print(f"Error deleting documents: {e}")
        return None
    