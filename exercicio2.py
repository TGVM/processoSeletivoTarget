# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
# próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
# se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada 
# de sua preferência ou pode ser previamente definido no código;

def Fibonacci(valorParaChecar):
    valorA = 0
    valorB = 1
    if valorParaChecar == valorA or valorParaChecar == valorB: return True

    while(valorParaChecar > valorB):
        aux = valorA + valorB
        if(valorParaChecar == aux): return True
        valorA = valorB
        valorB = aux
    return False

valor = int(input("Digite um valor para saber se está presente na sequência de Fibonacci: "))
if(Fibonacci(valor)):
    print("O número "+str(valor)+" está presente na sequência")
else:
    print("O número "+str(valor)+" não está presente na sequência")
