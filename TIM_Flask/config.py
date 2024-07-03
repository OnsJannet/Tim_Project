#!/usr/bin/python3
"""python script that initialize the database
with defaults values """
from pymongo import MongoClient


DEFAULT_VALUES = 0.0
db = MongoClient().TIM

def set_default_values():
    """function that set the default values"""
    # get all collections in the database
    collections = db.list_collection_names()
    for collection in collections:
        if collection != "users":
        # get all documents in the collection
            documents = db[collection].find()
            for document in documents:
                for key in document:
                    if key != "GlobalId" and key != "_id" and key != "updated_at" and key != "created_at":
                        db[collection].update_one(
                            {"_id": document["_id"]},
                            {"$set": {key: DEFAULT_VALUES}})
                        print("{} updated".format(key))
        
                    
if __name__ == "__main__":
    set_default_values()