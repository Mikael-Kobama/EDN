def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)

print("Sim" if resultado else "Não")
