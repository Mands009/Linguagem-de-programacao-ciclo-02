#conferindo se os valores formam um triangulo e calculando a area.
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c))
    print("A area é: ", area)

else:
    print("Os valores não formam um triangulo: ", a, b, c)