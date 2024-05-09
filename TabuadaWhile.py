c = 1
while c != 0:
    numero = int(input("Digite um número para consultar sua tabuada ou digite '0' para finalizar: "))
    if numero == 0:
        print("FIM")
        break
    else:
        print("=" * 12)
        for i in range(1,11):
            produto = int(i * numero)
            print(f"{numero} x {i} = {produto}")
        print("=" * 12)    