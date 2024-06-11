import random as rd
jogadores = dict()
grupo = list()
for i in range(0,4):
    jogadores["nome"] = str(input(f"Nome {i + 1}ro jogador: "))
    jogadores["numero"] = rd.randint(1,6)
    grupo.append(jogadores.copy())   
maior = 0
for jogadores in grupo:
    if jogadores["numero"] > maior:
        maior = jogadores["numero"]
ganhadores = list()        
for jogadores in grupo:
    if jogadores["numero"] == maior:
        ganhadores.append(jogadores)
for j in ganhadores:  
    print(f"O ganhador foi {j["nome"]} com o número {j["numero"]}")

    
    


