# import pymongo as pymongo
#
#
# class DataBaseExample:
#     def __init__(self):
#         self.db = pymongo.MongoClient(CONNECTION_STRING, ssl=True, tlsCAFile=config.CA_FILE)[config.DB_NAME]
#         self.collection = self.db[config.DB_COL_NAME_STATUS]
#
#     def get_data(self, _id):
#         return self.collection.find_one({'_id': _id})
#
#     def update_data(self, data: dict):
#         try:
#             self.collection.insert_one(data)
#         except DuplicateKeyError:
#             self.collection.update_one({'_id': data['_id']}, {"$set": data})
