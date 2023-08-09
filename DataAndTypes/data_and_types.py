import json
from datetime import datetime


def read_json(filename):
    content = None
    with open(filename) as f:
        content = json.load(f)
    return content

def date_setup(content):
    #from_date_string = content["Session data"].split("From")[1].split("to")[0].replace(",", "").strip()
    #to_date_string = content["Session data"].split("From")[1].split("to")[1].replace(",", "").strip()

    #from_date = datetime.strptime(from_date_string, "%Y-%m-%d %H:%M:%S").timestamp()
    #to_date = datetime.strptime(to_date_string, "%Y-%m-%d %H:%M:%S").timestamp()

    #content["From"] = from_date
    #content["To"] = to_date

    from_date_string = content['Session start']
    to_date_string = content['Session end']

    from_date = datetime.strptime(from_date_string, "%Y-%m-%d, %H:%M:%S").timestamp()
    to_date = datetime.strptime(to_date_string, "%Y-%m-%d, %H:%M:%S").timestamp()

    content['From'] = from_date
    content['To'] = to_date

def types_setup(content):
    list_to_update = [
        "Raw XP Gain",
        "XP Gain",
        "Raw XP/h",
        "XP/h",
        "Loot",
        "Supplies",
        "Balance",
        "Damage",
        "Damage/h",
        "Healing",
        "Healing/h"
        ]
    for property in list_to_update:
        if property in content:
            if type(content[property]) == str:
                content[property] = int(content[property].replace(",", ""))
    
    for idx in range(len(content["Killed Monsters"])):
        if type(content["Killed Monsters"][idx]["Count"]) == str and content["Killed Monsters"][idx]["Count"].strip().isnumeric():
            content["Killed Monsters"][idx]["Count"] = int(content["Killed Monsters"][idx]["Count"])
    
    for idx in range(len(content["Looted Items"])):
        if type(content["Looted Items"][idx]["Count"]) == str and content["Looted Items"][idx]["Count"].strip().isnumeric():
            content["Looted Items"][idx]["Count"] = int(content["Looted Items"][idx]["Count"])

def dump_content(filename, content):
    with open(filename, 'w') as f:
        json.dump(content, f)

def set_data_and_types(filename):
    content = read_json(filename)
    date_setup(content)
    types_setup(content)
    dump_content(filename, content)

if __name__ == "__main__":
    name = "Jsonalizer/exported/data2.json"
    set_data_and_types(name)

