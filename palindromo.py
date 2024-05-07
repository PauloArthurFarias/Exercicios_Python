nome = str(input("Insira uma frase: ")).strip().upper()
cortado = str.split(nome)
junto = ''.join(cortado)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
   inverso += junto[i]
print(f"O inverso de {junto} é {inverso}")
if junto == inverso:
    print("A frase é um palíndromo !")
else:
    print("A frase não é um palíndromo !")


