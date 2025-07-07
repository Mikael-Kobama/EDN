def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor, porcentagem)
print("Valor da gorjeta: R$", round(gorjeta, 2))
