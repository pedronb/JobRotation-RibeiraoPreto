# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

n = int(input('Digite um número: '))
sequencia_fibo = [0,1]
cont = 3
a = 0
b = 1

print(a, end = ' ')
print(b, end = ' ')

while cont <= n:
    f = a + b

    if cont == n:
        print(f)
        break
    
    print(f, end = ' ')
    a = b
    b = f
    cont += 1
    sequencia_fibo.append(f)

if (n in sequencia_fibo): 
    print('O número informado pertence a sequência.') 
else: 
    print('O número informado não pertence a sequência.')