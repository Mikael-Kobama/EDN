senha = input("Digite uma senha: ")
tem_numero = any(caractere.isdigit() for caractere in senha)

if len(senha) >= 8 and tem_numero:
    print("Senha válida.")
else:
    print("Senha inválida.")
