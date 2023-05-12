from connection.connection import MongoConnectionHandler
from repositories.sessions_repo import SessionsRepository
from datetime import datetime
from os import listdir
import json


def pretty_print(iterable):
    for item in iterable:
        print(item)
        print("\n\n")

connection_handler = MongoConnectionHandler()
connection_handler.connect()
connection = connection_handler.get_connection()

sessions_repo = SessionsRepository(connection)



""" list_of_documents = []
for file in listdir("Jsonalizer/exported"):
    filename = f"Jsonalizer/exported/{file}"
    with open(filename, "r") as f:
        list_of_documents.append(json.load(f))

sessions_repo.insert_list_of_documents(list_of_documents) """

data = sessions_repo.find_max("XP Gain")


pretty_print(data)
#sessions_repo.find_if_date("From 2022-04-14")
