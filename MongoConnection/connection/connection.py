from pymongo import MongoClient
from .configs import connection_configs

class MongoConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb+srv://{}:{}@clusterverso.denz94q.mongodb.net/?retryWrites=true&w=majority".format(
            connection_configs["USER"],
            connection_configs["PASSWORD"],
        )
        self.__db_name = connection_configs["DB_NAME"]
        self.__db_client = None
        self.__db_connection = None
    
    def connect(self):
        self.__db_client = MongoClient(self.__connection_string)
        self.__db_connection = self.__db_client[self.__db_name]

    def get_client(self):
        return self.__db_client
    
    def get_connection(self):
        return self.__db_connection
        