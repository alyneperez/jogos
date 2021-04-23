#CALCULADORA #

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
op = input("Digite um operador (+, -, *, /): ")
if op == "+":
    total = n1 + n2
elif op == "-":
    total = n1 - n2
elif op == "*":
    total = n1 * n2
elif op == "/":
    total = n1 / n2
print("O resultado é: " +str(total))