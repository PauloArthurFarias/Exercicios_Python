from random import randint
print("=" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR ")
print("=" * 15) 
ganhei = True

while ganhei:
    numero = int(input("Escolha um número: "))
    computador = randint(0,10)
    escolha = str.upper(input("Par ou Ímpar ? "))
    if (numero + computador) % 2 == 0 and escolha == 'P':
        print(f"Eu joguei {computador} e você {numero}, {numero + computador} é par ! Você venceu !")
        ganhei = True
        print("Vamos novamente...")
    elif (numero + computador) % 2 == 1 and escolha == 'P':
        print(f"Eu joguei {computador} e você {numero}, {numero + computador} é ímpar ! Você perdeu !")
        ganhei = False
        break
    elif (numero + computador) % 2 == 0 and escolha == 'I':
        print(f"Eu joguei {computador} e você {numero}, {numero + computador} é par ! Você perdeu !")
        ganhei = False
        break
    elif (numero + computador) % 2 == 1 and escolha == 'I':
        print(f"Eu joguei {computador} e você {numero}, {numero + computador} é ímpar ! Você venceu !")
        ganhei = True
        print("Vamos novamente...")

print("FIM")