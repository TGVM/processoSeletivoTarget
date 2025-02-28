# 4) Dado o valor de faturamento mensal de uma distribuidora, 
# detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o 
# percentual de representação que cada estado teve dentro do valor 
# total mensal da distribuidora.  

listaFaturamento = [
    {'estado': "SP", 'valor': 67836.43},
    {'estado': "RJ", 'valor': 36678.66},
    {'estado': "MG", 'valor': 29229.88},
    {'estado': "ES", 'valor': 27165.48},
    {'estado': "Outros", 'valor': 19849.53}
]

def CalculaPorcentagem(total, valor):
    return 100 * valor/total

total = 0
for item in listaFaturamento:
    total += item['valor']

print("Faturamento total: "+str(total))
for item in listaFaturamento:
    print("O estado "+item['estado']+" teve faturamento equivalente a "+str(CalculaPorcentagem(total, item['valor']))+"% do total.")

#print(listaFaturamento)