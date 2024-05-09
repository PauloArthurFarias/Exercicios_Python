from time import sleep
from random import randint
print("Sou seu computador...")
sleep(0.4)
print("Acabei de pensar em um número entre 1 e 10. Advinhe em qual número eu pensei !")
pc = randint(1,10)
palpite = int(input("Qual o seu palpite ? "))
while palpite != pc:
    if(pc > palpite):
        print("Pensei em um número mais alto... Tente mais uma vez.")
    else:
        print("Pensei em um número mais baixo... Tente mais uma vez.")  
    palpite = int(input("Qual o seu palpite ? "))    
if palpite == pc:
    print(f"Parabéns !!! você acertou, eu pensei em {pc}")  
