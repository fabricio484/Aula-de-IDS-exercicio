def soma (a, b):
    return a + b

a = int(input("Digitre o primeiro valor"))
b = int(input("Digite o segundo valor"))

operacao = input("+: Soma\n-: Subtração\n*: Multiplicaçao\n/: Divisão\n**: Exponenciaçao")
if operacao == '+':
    resultado = soma(a, b)
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b:
elif operacao == '/':
    resultado = a // b
else:
    resultado = a ** b
print (resultado)