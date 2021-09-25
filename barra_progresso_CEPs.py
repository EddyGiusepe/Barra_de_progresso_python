"""
Data Scientist Jr.: Dr. Eddy Giusepe Chirinos Isidro

"""
import requests
#from tqdm import tqdm  # tqdm significa progresso
#import time


link = "https://cep.awesomeapi.com.br/json/05424020"

requisicao = requests.get(link)
print("")
resposta = requisicao.json()

"""
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

print(ceps)    
# Passo 2: pegar as informações de cada cep


# Passo 3: verificar se a cidade é Rio de Janeiro


# Passo 4: printar o cep e o bairro
























