
"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente 
definido no código
"""


#Funcao para calcular a sequencia de fibonacci

def pertence_fibonacci(num):
  a, b = 0, 1
  while b < num:
    a, b = b, a + b
    print(a,b)
  return b == num

# Entrada do usuário
numero = int(input("Digite um número: "))

# Verifica se o número pertence à sequência e imprime o resultado
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")



###############################################################################################


"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de 
informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código"""


# Entrada pré definida
frase_exemplo = "Escreva um programa que verifique, em uma string, a existência da letra ‘a’"

# Verifica se a existencia da letra e a quantidade de vezez que aparece na frase
if "a" in frase_exemplo:
  print(f'A frase possui a letra "a", ela ocorre {frase_exemplo.count('a')} vezes.')



##############################################################################################


"""
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE 
faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?"""

#variaveis
indice = 12
soma = 0
k = 1
#Loop de condição, vai parar quando k for maior que o indice
while k < indice:
  k += 1
  soma = soma + k 
print(soma)



#################################################################################################


"""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____ 
"""


# Descobrindo o próximo elemento de cada sequência

# a) 
a = [1, 3, 5, 7]
proximo_a = a[-1] + 2

# b) 
b = [2, 4, 8, 16, 32, 64]
proximo_b = b[-1] * 2

# c) 
c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = (len(c))**2

# d) 
d = [4, 16, 36, 64]
proximo_d = (len(d) * 2)**2

# e) 
e = [1, 1, 2, 3, 5, 8]
proximo_e = e[-1] + e[-2]

# f) 
f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = f[-1] + 1

#imprimindo os resultados
print(f'a) 1, 3, 5, 7, {proximo_a}')
print(f'b) 2, 4, 8, 16, 32, 64, {proximo_b}')
print(f'c) 0, 1, 4, 9, 16, 25, 36, {proximo_c}')
print(f'd) 4, 16, 36, 64, {proximo_d}')
print(f'e) 1, 1, 2, 3, 5, 8, {proximo_e}')
print(f'f) 2,10, 12, 16, 17, 18, 19, {proximo_f}')



##########################################################################################



""" 
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as
lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, 
usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? """


import time

# Iniciando o estado das lampadas 
# 0 = apagada e fria 
# 1 = ligada
# 2 = apagada e quente

lampadas = [0, 0, 0]  # Todas começam apagadas e frias

# Ligando o primeiro interruptor (lampada 1)
lampadas[0] = 2  # Lampada 1 esquenta
time.sleep(5) # simulando tempo ligado

# Desligando o primeiro interruptor e ligando o segundo (lampada 2)
lampadas[0] = 1  # Lampada 1 apagada mas quente
lampadas[1] = 2  # Lampada 2 ligada

print(f'Lampadas{lampadas}')

# Verificando o estado das lâmpadas
def verificar_lampadas(lampadas):
    for i, lamp in enumerate(lampadas):
        if lamp == 0:
            status = "apagada e fria"
        elif lamp == 1:
            status = "Ligada"
        else:
            status = "apagada e quente"
        print(f"Lampada {i + 1}: {status}")

verificar_lampadas(lampadas)
