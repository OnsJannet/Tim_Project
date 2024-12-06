#!/usr/bin/python3

from datetime import datetime
from pymongo import MongoClient
from uuid import uuid4
import os
from Bleuprints.db_routes import db, client, get_current_db

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = get_current_db()
#db = client["TIM_Demo"]
"""
get_form_to_dict:
"""
def get_form_to_dict(form): 
    """ make a dictionary with unique idif no id are provided from html post form """
    dic = {}
    """if "_id" not in form:
        dic["_id"] = str(uuid4())"""
    for key, value in form.items():
        dic[key] = value
    dic["created_at"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    dic["updated_at"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    return dic

"""
save_to_mongo:
args[dict] : dictionary : dictionary to be saved
args[collection] : string : the collection to be saved to
args[ref] : list :  list of referances objects/dictionarys
args[ref][ref_collection] : string : the collection of the referance
args[ref][ref_id] : string : id of the object to referance
"""
def save_to_mongo(**args):
    """ save/update object/dictionary to mongo """
    if (args["dict"]):
        if("_id" in args["dict"]):
            found = db[args["collection"]].find_one({"_id": args["dict"]["_id"]})
            if found:
                db[args["collection"]].update_one({"_id": args["dict"]["_id"]},
                            {"$set": args["dict"]})
                found["ref"],args["ref"] = [i for i in found["ref"] if i not in args["ref"]],[j for j in args["ref"] if j not in found["ref"]]
                add_ref_mongo(dict = args["dict"], collection = args["collection"], ref = args["ref"])
                return
            db[args["collection"]].insert_one( args["dict"] )
    if (args["ref"]):
        add_ref_mongo(dict = args["dict"], collection = args["collection"], ref = args["ref"])

def add_ref_mongo(**args):
        for ref in args["ref"]:
            db[args["collection"]].update_one(
                    {"_id": args["dict"]["_id"]},
                    {"$push": {"ref_to_" + ref["ref_collection"]: ref["ref_id"]}}
                )
            args["collection"] = ref["ref_collection"]
            db[args["collection"]].update_one(
                    {"_id": ref["ref_id"]},
                    {"$push": {"ref_from_" + args["collection"]: args["dict"]["_id"]}}
                )

def remove_ref_mongo(**args):
        for ref in args["ref"]:
            db[args["collection"]].update_one(
                    {"_id": args["dict"]["_id"]},
                    {"$pull": {"ref_to_" + ref["ref_collection"]: ref["ref_id"]}}
                )
            args["collection"] = ref["ref_collection"]
            db[args["collection"]].update_one(
                    {"_id": ref["ref_id"]},
                    {"$pull": {"ref_from_" + args["collection"]: args["dict"]["_id"]}}
                )
def get_record(**args):
    found = db[args["collection"]].find_one({"_id": args["dict"]["_id"]})
    return found

"""
remove_from_mongo:
args[collection] : string : the collection of the object/dictionary to be removed
args[id] : string : the id of the object to be removed 
"""
def remove_from_mongo(**args):
    remove_ref_mongo(dict = args["dict"], collection = args["collection"], ref = args["ref"])
    db[args["collection"]].delete_one({"_id": args["dict"]["_id"]})
