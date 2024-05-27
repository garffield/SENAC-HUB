tipo = str(input("Informe o tipo da carne: "))

if (tipo == 'file duplo'):
    qtd_carne = int(input("Informe em gramas a quantidade de carnes a ser comprada: "))
    if (qtd_carne <= 5):
        pesagem = 4.90
    else:
        pesagem = 5.80

if (tipo == 'alcatra'):
    qtd_carne = int(input("Informe em gramas a quantidade de carnes a ser comprada: "))
    if (qtd_carne <= 5):
        pesagem = 5.90
    else:
        pesagem = 6.80

if (tipo == 'picanha'):
    qtd_carne = int(input("Informe em gramas a quantidade de carnes a ser comprada: "))
    if (qtd_carne <= 5):
        pesagem = 6.90
    else: 
        pesagem = 7.80

pagamento = str(input("Informe o tipo de pagamento: "))
if (pagamento == 'cartao tabajara'):
    desconto = 0.05
else: 
    desconto = 0


total = (qtd_carne / 1000) * pesagem
final = total - desconto

print("Tipo de carne: ", tipo)
print("Quantidade de carne compradas: ", qtd_carne)
print("Preço total: ", total)
print("Tipo de pagamento: ", pagamento)
print("Valor do desconto: ", total * desconto)
print("Valor a pagar: ", final)