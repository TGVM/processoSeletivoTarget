# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?


# Exercício simples, apenas copiei o enunciado e fiz as correções 
# necessárias para python

INDICE = 13
SOMA = 0
K = 0
while(K < INDICE):
    K = K + 1
    SOMA = SOMA + K

# E adicionei um print ao final para exibir o valor na tela
print("o valor da variável SOMA é "+ str(SOMA))