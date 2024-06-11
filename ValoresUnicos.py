lista = []
lista.append(input("Digite um número para adicioná-lo à lista: "))
print("Valor adicionado com sucesso...")
while True:
    option = str(str.lower(input("Quer continuar ?[S/N] ")))
    if option == 'n':
        break
    num = input("Digite um número para adicioná-lo à lista: ")
    if num in lista:
        print("Valor não adicionado, já está presente na lista.")
    else:
        lista.append(num)
        print("Valor adicionado com sucesso...")    
print(f"Você digitou os valores {sorted(lista)}")          
print("FIM")