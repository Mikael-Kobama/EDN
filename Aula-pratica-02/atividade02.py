nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", round(preco_original, 2))
print("Desconto:", porcentagem_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço com desconto: R$", round(preco_final, 2))
