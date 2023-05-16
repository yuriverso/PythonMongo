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


#data = sessions_repo.aggregate_quick()

"""filter = [
            {"$project": {"_id": 1, "XP Gain": 1, "Balance": 1, "Killed Monsters": 1}},
            {"$group": {"_id": "$Killed Monsters.Name", "Count": {"$max": "$Killed Monsters.Count"}, "ID": {"$max": "$_id"}}}
        ]

ag_data = sessions_repo.aggregate_like(filter)

for item in ag_data:
    most_killed_index = item['Count'].index(max(item['Count']))
    most_killed = item['_id'][most_killed_index]
    
    sessions_repo.modify_document({"_id": item["ID"]}, {"$set": {"Hunt": most_killed}})"""

filter = [{"$project": {"_id": 1, "XP Gain": 1, "Balance": 1, "Hunt": 1}},
          {"$match": {"Hunt": None}}
         ]

data = sessions_repo.aggregate_like(filter)

pretty_print(data)

