class SessionsRepository:
    def __init__(self, connection) -> None:
        self.__collection = connection.get_collection("sessions")
    
    def read_all(self):
        print([x for x in self.__collection.find()])

    def read_document(self, filter, options={}):
        return self.__collection.find(filter, options)
    
    def find_max(self, field):
        return self.__collection.find().sort(field, -1).limit(1)

    def insert_document(self, document):
        self.__collection.insert_one(document)
        print("Documento inserido")

    def insert_list_of_documents(self, documents_list):
        self.__collection.insert_many(documents_list)
        print(f"{len(documents_list)} documentos foram inseridos")

    def modify_document(self, filter, properties):
        data = self.__collection.update_one(filter, properties)
        print(str(data.modified_count) + " documento foi alterado")

    def delete_documents(self, filter={}):
        data = self.__collection.delete_many(filter)
        print(str(data.deleted_count) + " documentos foram removidos")

    def find_if_date(self, date):
        filter = {"Session data": {"$regex": "From 2022-04-14"}}
        data = self.__collection.find(filter, {"Session Data": 1, "Session": 1})
        print([x for x in data])

    def aggregate_quick(self):
        data = self.__collection.aggregate([{"$match": {"XP Gain": {"$lt": 1000000}}},
                                            {"$project": {"_id": 0, "XP Gain": 1, "Balance": 1, "Killed Monsters": "$Killed Monsters.Name"}},
                                            {"$group": {"_id": "XP Gain", "XP Gain": {"$sum": "XP Gain"}}}])
        return data

    def aggregate_like(self, filter):
        data = self.__collection.aggregate(filter)
        return data
