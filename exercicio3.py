# 3) Dado um vetor que guarda o valor de faturamento diário de uma 
# distribuidora, faça um programa, na linguagem que desejar, que calcule 
# e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi 
# superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento 
# mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e 
# feriados. Estes dias devem ser ignorados no cálculo da média;

import json

arquivo = open ('dados.json')
jsonVetor = json.load(arquivo)
listaFaturamento = []

for item in jsonVetor:
    dia = {"dia":None, "valor":None}
    dia['dia'] = item['dia']
    dia['valor'] = item['valor']
    listaFaturamento.append(dia)

print(listaFaturamento)