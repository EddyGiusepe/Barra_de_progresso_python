"""
Data Scientist Jr.: Dr. Eddy Giusepe Chirinos Isidro

"""
import requests
from tqdm import tqdm  # tqdm significa progresso
#import time

"""
link = "https://cep.awesomeapi.com.br/json/05424020"

requisicao = requests.get(link)
print("")
resposta = requisicao.json()


# Se quiser rodar esta parte sõ descomentar.
print("")
print(resposta)
print("")
cidade = resposta['city']
bairro = resposta["district"]
print(cidade)
print(bairro)
print("")
"""

# Passo 1: pegar a lista de ceps
with open("ceps.txt", "r") as arquivo:    # r --> read (leitura) e arquivo --> apenas um nome (pode ser outro nome)
    ceps = arquivo.read()

#print(ceps) 
print("Vamos separar o texto (cada cep) com um enter: ")
ceps = ceps.split("\n") # Isso vai gerar uma lista em Python
#print(ceps)

# Passo 2: pegar as informações de cada cep
for cep in tqdm(ceps):
    link = f"https://cep.awesomeapi.com.br/json/{cep}"

# Passo 3: verificar se a cidade é Rio de Janeiro
    requisicao = requests.get(link)
    print("")
    resposta = requisicao.json()
    print("")
    print(resposta)
    print("")
    cidade = resposta['city']
    bairro = resposta["district"]
    #print(cidade)
    #print(bairro)


# Passo 4: printar o cep e o bairro
    print("#######################")
    if cidade == "Rio de Janeiro":
        print(cep, bairro)

