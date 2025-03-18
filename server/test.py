

# utils.py

from mongo import products_collection
from utils import ai_tasks

def get_all_product():
    """Retrieve all product IDs from the database."""
    return [str(product["_id"]) for product in products_collection.find({}, {"_id": 1})]

x= get_all_product()
i = 0
for product in x:
    
    ai_tasks(product_id=product)
    i+=1
    if (i%5==0):
        print(i)
