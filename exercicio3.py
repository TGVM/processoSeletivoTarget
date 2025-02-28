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


# variáveis globais
# valores de maior/menor faturamento iniciados com infinito
listaFaturamento = []
menorFaturamento = math.inf
diaMenorFat = ""
maiorFaturamento = -math.inf
diaMaiorFat = ""
mediaMensal = 0
contagemDias = 0

#função para fazer a leitura do arquivo json
def LeituraDoJSON():

    arquivo = open ('dados.json')
    jsonVetor = json.load(arquivo)
    #salva os dados no vetor
    for item in jsonVetor:
        dia = {"dia":None, "valor":None}
        dia['dia'] = item['dia']
        dia['valor'] = item['valor']
        listaFaturamento.append(dia)

# função que realiza as operações necessárias
def RealizarOperacoes():
    # define as variáveis globais dentro do escopo da função
    global maiorFaturamento
    global menorFaturamento
    global diaMaiorFat
    global diaMenorFat
    global mediaMensal
    global contagemDias
    
    # passa uma primeira vez no vetor para definir os valores de
    # maior/menor faturamento e incrementar média
    for item in listaFaturamento:
        # condicional para ignorar dias sem faturamento
        if(item['valor']>0.0):
            # confere se valor do item atual é maior que o registrado
            if(item['valor'] > maiorFaturamento):
                maiorFaturamento = item['valor']
                diaMaiorFat = item['dia']
            # confere se valor do item atual é menor que o registrado
            if(item['valor'] < menorFaturamento):
                menorFaturamento = item['valor']
                diaMenorFat = item['dia']
            # adiciona o valor atual na média
            mediaMensal += item['valor']
    # após sair do laço de repetição divide o valor total acumulado
    # pela quantidade de itens no vetor
    mediaMensal = mediaMensal/len(listaFaturamento)

    #passa uma segunda vez no vetor para contar quantos dias 
    # tiveram um faturamento maior que a média
    for item in listaFaturamento:
        if(item['valor'] > mediaMensal):
            contagemDias+=1

# chamada de funções
LeituraDoJSON()
RealizarOperacoes()
# prints para exibir resultados
print("O menor valor de faturamento foi no dia "+str(diaMenorFat)+", com "+str(menorFaturamento)+"R$, sem contar finais de semana e feriados.")
print("O maior valor de faturamento foi no dia "+str(diaMaiorFat)+", com "+str(maiorFaturamento)+"R$")
print("Número de dias em que a média de faturamento mensal ("+str(mediaMensal)+") foi superada: "+str(contagemDias))
