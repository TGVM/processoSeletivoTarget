# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
# próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
# se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada 
# de sua preferência ou pode ser previamente definido no código;


# Uma função recebendo como parâmetro o número a ser conferido
# Ela vai realizar a função de fibonacci e checar se o novo valor é 
# parte da sequência ou não 
def Fibonacci(valorParaChecar):
    valorA = 0
    valorB = 1
    # uma primeira checagem para ver se o valor inserido é 0 ou 1 
    if valorParaChecar == valorA or valorParaChecar == valorB: return True

    # enquanto o valor for maior que o maior dos 2 valores atuais da
    # sequência, a sequência será incrementada
    while(valorParaChecar > valorB):
        # soma os valores
        aux = valorA + valorB
        # se for o valor inserido retorna true
        if(valorParaChecar == aux): return True
        # senão, atualiza os valores para a próxima soma
        # sempre mantendo o valor B como o maior
        valorA = valorB
        valorB = aux

    # se o valor mais alto da sequência for maior que o valor para 
    # checagem, retorna falso
    return False

# prints para inserir o valor e mostrar o resultado
valor = int(input("Digite um valor para saber se está presente na sequência de Fibonacci: "))
if(Fibonacci(valor)):
    print("O número "+str(valor)+" está presente na sequência")
else:
    print("O número "+str(valor)+" não está presente na sequência")
