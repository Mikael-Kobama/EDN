pares = 0
impares = 0

while True:
    entrada = input("Digite um número ou 'sair' para encerrar: ")
    if entrada.lower() == "sair":
        break
    numero = int(entrada)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
