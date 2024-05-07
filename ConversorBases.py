import time
numero = int(input("Digite um número inteiro: "))
print("Escolha para qual base você quer converter !")
option = int(input("[ 1 ] Converter para binário\n[ 2 ] Converter para octal\n[ 3 ] Converter para hexadecimal\n"))
if option == 1 :
    print("Convertendo para binário...")
    print(f"{numero} em binário é igual a {bin(numero)[2:]}")
elif option == 2 :
    print("Convertendo para octal...")
    print(f"{numero} em octal é igual a {oct(numero)[2:]}")
elif option == 3 :
    print("Convertendo para hexadecimal...")
    print(f"{numero} em hexadecimal é igual a {hex(numero)[2:]}")

    