altura = float(input("Digite sua altura: "))
sexo = int(input("Digite 1 para Homem e 2 para Mulher: "))

if sexo == 1:
 peso_ideal = (72.7 * altura) - 58
elif sexo == 2:
 peso_ideal = (62.1 * altura) - 44.7

print("Seu peso ideal é: ", peso_ideal)

# SE = IF
# SENAO = ELSE
# SENAO SE = ELIF