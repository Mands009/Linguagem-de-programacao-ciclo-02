#Uma função que:
#Receba uma frase como parâmetro.
#Retorne uma nova frase com cada palavra com as letras invertidas.

new_string = " "
frase = str(input("Digite uma frase: "))
print("Você digitou: ", format(frase))
for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
print("A frase invertida fica:", format(new_string))