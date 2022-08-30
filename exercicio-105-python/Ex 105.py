"""105) Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
— Quantidade de notas
— A maior nota
— A menor nota
— A média da turma
— A situação (opcional)"""

def notas(*args, sit=False):
    d = {"Total": len(args), "Maior Nota": max(args), "Menor Nota": min(args), "Média": sum(args) / len(args)}
    if sit:
        if d["Média"] > 7:
            d["Situação"] = "Aprovado"
        elif 4 < d["Média"] < 7:
            d["Situação"] = "Recuperação"
        else:
            d["Situação"] = "Reprovado"
    return d


rep = notas(4, 7, 10, 8.0, sit=True)
print(rep)
