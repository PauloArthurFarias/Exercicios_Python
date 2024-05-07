from datetime import date
from time import sleep
ano_atual = int(date.today().year)
nascimento = int(input("Ano de nascimento: "))
if ano_atual - nascimento > 18 :
    print("Seu alistamento já passou !")
    print(f"Você deveria ter se alistado a {ano_atual - (nascimento + 18)} anos atrás")
elif ano_atual - nascimento == 18 :
    print(f"Você deve se alistar neste ano de {ano_atual}!")
else :
    sleep(0.2)
    print(f"Quem nasceu em {nascimento} tem {ano_atual - nascimento} anos de idade em {ano_atual}")
    sleep(0.2)
    print(f"Ainda faltam {18 - (ano_atual - nascimento)} anos para o alistamento")
    sleep(0.2)
    print(f"Seu alistamento será em {nascimento + 18}")