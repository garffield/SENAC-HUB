pesopeixe = float(input("Digite o peso dos peixes: "))

if pesopeixe > 50:
    limite = pesopeixe - 50
    multa = limite * 4
print ("Quantidade de peixes: ", pesopeixe)
print ("Quantidade de peixes acima do limite: ", limite)
print ("Multa a ser pagada: ", multa)