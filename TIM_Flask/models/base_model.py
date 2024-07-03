#!/usr/bin/python3
import collections
from uuid import uuid4
from services.mongodb_interactions import *

class BaseModel:
    def __init__(self, *args, **kwargs):
        self._id = str(uuid4())
        self.ref = []
        self.collection = ""


    def to_dict(self):
        return(self.__dict__)

    def save(self):
        save_to_mongo(dict = self.__dict__, collection = self.collection, ref = self.ref)
        self.load()

    def add_ref(self, collection, id):
        self.ref.append({"ref_collection": collection, "ref_id": id})
        self.save()
        self.load()

    def remove_ref(self, collection, id):
        self.ref.remove({"ref_collection": collection, "ref_id": id})
        remove_ref_mongo(dict = self.__dict__, collection = self.collection, ref = self.ref)
        self.load()
        self.save()


    def load(self):
        self.__dict__ = get_record(dict = self.__dict__, collection = self.collection, ref = self.ref)

    def delete(self):
        remove_from_mongo(dict = self.__dict__, collection = self.collection, ref = self.ref)
