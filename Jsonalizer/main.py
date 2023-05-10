from jsonalizer import *
from os import listdir

print("Bem vindo!")

path = input("Digite o caminho para os arquivos com os dados registrados em .txt: ")
path = path.replace(r'"\"', "/")
for file in listdir(path):
    print(file)
    try:
        jsonalize(f"{path}\{file}")
    except:
        print("erro")


