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
import math



listaFaturamento = []
menorFaturamento = math.inf
diaMenorFat = ""
maiorFaturamento = -math.inf
diaMaiorFat = ""
mediaMensal = 0
contagemDias = 0


def LeituraDoJSON():

    arquivo = open ('dados.json')
    jsonVetor = json.load(arquivo)
    for item in jsonVetor:
        dia = {"dia":None, "valor":None}
        dia['dia'] = item['dia']
        dia['valor'] = item['valor']
        listaFaturamento.append(dia)

def RealizarOperacoes():
    global maiorFaturamento
    global menorFaturamento
    global diaMaiorFat
    global diaMenorFat
    global mediaMensal
    global contagemDias
    
    for item in listaFaturamento:
        if(item['valor']>0.0):
            if(item['valor'] > maiorFaturamento):
                maiorFaturamento = item['valor']
                diaMaiorFat = item['dia']
            if(item['valor'] < menorFaturamento):
                menorFaturamento = item['valor']
                diaMenorFat = item['dia']
            mediaMensal += item['valor']
    mediaMensal = mediaMensal/len(listaFaturamento)

    for item in listaFaturamento:
        if(item['valor'] > mediaMensal):
            contagemDias+=1


LeituraDoJSON()
RealizarOperacoes()
print("O menor valor de faturamento foi no dia "+str(diaMenorFat)+", com "+str(menorFaturamento)+"R$, sem contar finais de semana e feriados.")
print("O maior valor de faturamento foi no dia "+str(diaMaiorFat)+", com "+str(maiorFaturamento)+"R$")
print("Número de dias em que a média de faturamento mensal ("+str(mediaMensal)+") foi superada: "+str(contagemDias))
