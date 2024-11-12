#lendo 3 numeros e mostrando o menor deles

primeiro = int(input("Numero 1: "))
segundo = int(input("Numero 2: "))
terceiro = int(input("Numero 3: "))

menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print("O menor numero é: ", menor)