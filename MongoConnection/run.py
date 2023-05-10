from connection.connection import MongoConnectionHandler
from repositories.sessions_repo import SessionsRepository
from os import listdir
import json

connection_handler = MongoConnectionHandler()
connection_handler.connect()
connection = connection_handler.get_connection()

sessions_repo = SessionsRepository(connection)

# list_of_documents = []
# for file in listdir("Jsonalizer/exported"):
#     filename = f"Jsonalizer/exported/{file}"
#     with open(filename, "r") as f:
#         list_of_documents.append(json.load(f))

# sessions_repo.insert_list_of_documents(list_of_documents)

#sessions_repo.read_all()
sessions_repo.find_if_date("From 2022-04-14")