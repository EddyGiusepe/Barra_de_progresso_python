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
print(" # Barra de progresso numa lista #")
print("################################################")

lista = [1, 2, 3, 10, 15, 20 , -4]
for i in tqdm(lista):
    time.sleep(1)

print("")



print("################################################")
print(" # Atualizando a minha barra de progresso #")
print("################################################")


with tqdm(total=100) as barra_progresso:
    for i in range(10): # Ver que só vai rodar 10 vezes
        time.sleep(1)
        barra_progresso.update(10) #ter cuidado. Porque se você colocar 1 a barra papararia em 10% apenas



















