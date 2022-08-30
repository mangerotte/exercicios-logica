"""83) Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
e fechados na ordem correta."""

expressao = input('Digite a expressão: ')
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.pop()
    else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão não está correta')