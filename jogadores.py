import time 
import random

pessoa_diferente = ["Neymar", "Messi", "Cristiano Ronaldo", "Lamine Yamal", "Coutinho", "Pelé", "Maradona", "Marcos Rocha",
                    "Marcelo Lomba", "Weverton"]

pessoa_aleatoria = random.choice(pessoa_diferente)

resposta = str
resposta2 = str
meusjogadores = []

menu2 = """
Neymar 
Messi
Cristiano Ronaldo
Lamine Yamal
Coutinho 
Pelé 
Maradona Marcos
Rocha Marcelo 
Lomba Weverton
"""

menu1 = """

[1] Roleta de Jogadores
[2] Jogar contra outro jogador
[3] Mercado de Jogadores
[4] Ver seus jogadores
[5] Sair

"""

resposta = input(menu1)
if resposta == "1":
    time.sleep(1)
    print("Sorteando jogador..")
    print(pessoa_aleatoria)
    meusjogadores.append(pessoa_aleatoria)
    time.sleep(0.7)
    print("Agora esses são seus jogadores:", meusjogadores)
    time.sleep(5)

    resposta2 = input(str("Você deseja voltar ao menu? (S/N)"))
    if resposta2 == "S":
        resposta = input(menu1)