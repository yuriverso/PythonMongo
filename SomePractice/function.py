from pymongo import MongoClient
import pandas as pd

def df_from_db(collection, filter={}, fields=None):
    user = "yurikruk"
    pw = "FvZkECbUjhMvv5MY"
    connection_string = f"mongodb+srv://{user}:{pw}@clusterverso.denz94q.mongodb.net/?retryWrites=true&w=majority"

    connection = MongoClient(connection_string)["Tibia"]

    collection = connection.get_collection(collection)

    if fields is None:
        df = pd.DataFrame(list(collection.find(filter)))
        return df
    else:
        desired_fields = {field: 1 for field in fields}
        df = pd.DataFrame(list(collection.find(filter, desired_fields)))
        return df
    
    #return pd.DataFrame(list(collection.find()))

    