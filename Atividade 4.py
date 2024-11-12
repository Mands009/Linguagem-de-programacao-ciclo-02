#uma função que retorne verdadeiro se o número for primo

n = int(input("Digite um numero: "))
divisor = 0
for c in range(1, n + 1):
    if n % c == 0:
        divisor += 1

if divisor == 2:
    print("Verdadeiro, %d é um numero primo."%(n))
else:
    print("Falso, %d não é numero primo."%(n))
