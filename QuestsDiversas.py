"""print("ANALISADOR DE NOMES\n")
nome = str(input("Digite seu nome: \n"))
print(f"Seu nome em maiúsculas é: {nome.upper()}")
print(f"Seu nome em minúsculas é: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(" ")} letras")
primeiro = nome.split()
print(f"Seu primeiro nome é {primeiro[0]} e ele tem {nome.find(" ")} letras") """

#separador de casas decimais

"""numero = int(input("Informe um número: "))
u = numero % 10 
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"milhar: {m}")"""

#procurando string dentro de outra

"""nome = input("Seu nome completo: ")
nome_novo = nome.lower()
print("Seu nome tem Silva ?")
if(nome_novo.find("silva") != -1 ) : print("Sim")
else : print("Não")"""

#Primeiro e ultimo nome

"""nome = input("Digite seu nome completo: ")
separado = nome.split()
print(f"Seu primeiro nome é {separado[0]}")
print(f"Seu último nome é {separado[len(separado) - 1]}")"""

#advinhando numero
"""import random
from time import sleep
print("=-" * 27)
print("Vou pensar em um número entre 0 e 5, tente adivinhar !")
print("=-" * 27)
numero = int(input("em que número eu pensei ? \n"))
print("PROCESSANDO...")
sleep(2)
lista = (0, 1, 2, 3, 4, 5)
random = random.choice(lista)
if random == numero :
     print(f"eu pensei em {random} e você disse {numero} ! Parabéns, você acertou !")
else :
     print(f"eu pensei em {random} e você disse {numero} ! Você errou !")"""


#par ou ímpar
""" numero = int(input("Diga um número "))
if numero % 2 == 0 :
    print(f"o número {numero} é par !")
else :
    print(f"o número {numero} é ímpar !")"""

#Triangulo possivel

lado_a = float(input("Insira o lado A do triângulo: "))
lado_b = float(input("Insira o lado B do triângulo: "))
lado_c = float(input("Insira o lado C do triângulo: "))

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a :
    print("Esse triângulo é possível")
else :
    print("Esse triângulo não é possível")



