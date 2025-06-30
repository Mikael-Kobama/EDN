valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em reais: R$", round(valor_reais, 2))
print("Convertido para dólares: US$", round(valor_dolar, 2))
print("Convertido para euros: €", round(valor_euro, 2))
