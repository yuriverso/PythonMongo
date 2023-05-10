class SessionsRepository:
    def __init__(self, connection) -> None:
        self.__collection = connection.get_collection("sessions")
    
    def read_all(self):
        print([x for x in self.__collection.find()])

    def insert_document(self, document):
        self.__collection.insert_one(document)
        print("Documento inserido")

    def insert_list_of_documents(self, documents_list):
        self.__collection.insert_many(documents_list)
        print("Todos os documentos foram inseridos")

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