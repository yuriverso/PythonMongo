from data_and_types import set_data_and_types
from os import listdir

print("Bem vindo!")

path = input("Digite o caminho para os arquivos com os dados registrados em .txt: ")
path = path.replace(r'"\"', "/")
for file in listdir(path):
    set_data_and_types(f"{path}/{file}")
    