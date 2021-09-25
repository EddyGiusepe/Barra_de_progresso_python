"""
Data Scientist Jr.: Dr. Eddy Giusepe Chirinos Isidro

"""

from tqdm import tqdm  # tqdm significa progresso
import time


print("################################################")
print(" # Forma simples de ver uma barra de progresso #")
print("################################################")
for i in tqdm(range(10)):
    time.sleep(1)  # 1 --> representa um segundo

print("")


print("################################################")
print(" # Barra de progresso numa lista#")
print("################################################")

lista = [1, 2, 3, 10, 15, 20 , -4]
for i in tqdm(lista):
    time.sleep(1)

print("")
