extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    valor = int(input("Digite um número para escrevê-lo por extenso: "))
    if 0 <= valor <= 10:
        print(f"O número {valor} escrito por extenso é {extenso[valor]}")
        break
    print("Número inválido, tente novamente")