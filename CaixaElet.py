print("BANCO")
valor = int(input(("Qual valor você quer sacar ? R$")))
notas_milhar = (valor // 1000) * 20
notas_centena = ((valor % 1000) // 100) * 5
notas_dezena = ((valor % 100) // 10) * 1
notas_unidade = ((valor % 10) // 1) * 1
print(f"Total de {notas_milhar} cédulas de R$50")
print(f"Total de {notas_centena} cédulas de R$20")
print(f"Total de {notas_dezena} cédulas de R$10")
print(f"Total de {notas_unidade} moedas de R$1")

    

