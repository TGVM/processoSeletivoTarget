# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de 
# sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


palavra = str(input("Digite uma palavra para ser invertida: "))

palavraInversa = ""

for i in range(len(palavra)-1, -1, -1):
    palavraInversa = palavraInversa + palavra[i]

print(palavraInversa)