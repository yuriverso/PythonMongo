import json
import random
import string
from os import listdir


def read_hunt(filename):
    with open(filename, "r") as f:
        return f.read()

def get_hunting_data(hunt_content, hunt_dict):
    splited_hunt = hunt_content.split("\nKilled Monsters:\n")
    hunt_list1 = splited_hunt[0].split("\n")
    for item in hunt_list1:
        data = item.split(": ")
        hunt_dict[data[0]] = data[1]

def get_killed_monsters(hunt_content, monsters, hunt_dict):
    splited_hunt = hunt_content.split("\nKilled Monsters:\n")
    killed_monsters = splited_hunt[1].split("\nLooted Items:\n")[0].split("\n")

    for item in killed_monsters:
        count = item.split("x ")[0]
        monster = " ".join(item.split(" ")[3:])
        monsters.append({"Count": count, "Name": monster})

    hunt_dict["Killed Monsters"] = monsters

def get_looted_items(hunt_content, loot, hunt_dict):
    splited_hunt = hunt_content.split("\nKilled Monsters:\n")
    looted_items = splited_hunt[1].split("\nLooted Items:\n")[1].split("\n")

    for item in looted_items:
        splited_hunt = hunt_content.split("\nKilled Monsters:\n")
        count = item.split("x ")[0]
        looted = " ".join(item.split(" ")[3:])
        loot.append({"Count": count, "Name": looted})
    
    hunt_dict["Looted Items"] = loot


def jsonalize(filename):
    hunt_content = read_hunt(filename)
    hunt_dict = {}
    monsters = []
    loot = []

    get_hunting_data(hunt_content, hunt_dict)
    get_killed_monsters(hunt_content, monsters, hunt_dict)
    get_looted_items(hunt_content, loot, hunt_dict)
    
    new_filename = "data"+str(len(listdir("Jsonalizer/exported"))+1)
    #new_filename = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    with open(f"Jsonalizer/exported/{new_filename}.json", 'w') as f:
        json.dump(hunt_dict, f)

if __name__ == "__main__":
    print(listdir("Jsonalizer"))
    jsonalize("C:/Users/Yuri/Desktop/♠/JonasSalazarDrive/Data/tibia sessions/1.txt")