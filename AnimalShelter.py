from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
#         self.username = username
#         self.password = password
        self.client = MongoClient('mongodb://%s:%s@localhost:54513' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data=dict()):
        if data is not None:
            self.database.animals.insert_one(data) #data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to return, because data parameter is empty")

# Create method to implement the U in CRUD
    def update(self, find = dict(), replace = dict()):
        if find is not None:
            x = self.database.animals.update_many(find, {"$set":replace}) #data should be dictionary
            return json.dumps(str(x.modified_count) + ' records updated')
        else:
            raise Exception("Nothing to update, because data parameter is empty")

# Create method to implement the D in CRUD
    def delete(self, data = dict()):
        if data is not None:
            return json.dumps(self.database.animals.remove(data), indent = 4)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")

