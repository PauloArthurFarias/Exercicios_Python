aluno = {}
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input("Média: "))
if aluno["media"] >= 7:
    aluno["situation"] = str("APROVADO")
elif aluno["media"] >= 5:
    aluno["situation"] = str("RECUPERAÇÃO")  
else:
    aluno["situation"] = str("REPROVADO")
print(aluno["situation"])  