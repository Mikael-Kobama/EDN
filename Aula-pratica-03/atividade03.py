temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Converter para (C, F ou K): ").upper()

if origem == "C":
    if destino == "F":
        convertida = (temp * 9/5) + 32
    elif destino == "K":
        convertida = temp + 273.15
    else:
        convertida = temp
elif origem == "F":
    if destino == "C":
        convertida = (temp - 32) * 5/9
    elif destino == "K":
        convertida = (temp - 32) * 5/9 + 273.15
    else:
        convertida = temp
elif origem == "K":
    if destino == "C":
        convertida = temp - 273.15
    elif destino == "F":
        convertida = (temp - 273.15) * 9/5 + 32
    else:
        convertida = temp
else:
    convertida = None

if convertida is not None:
    print("Temperatura convertida:", round(convertida, 2), destino)
else:
    print("Unidade inválida.")
