valor_hora = float(input("Informe o valor da sua hora: "))
qtd_hora = int(input("Informe a quantidade de horas trabalhadas no mês: "))

sal_bruto = qtd_hora * valor_hora

sind = 0.03
fgts = 0.15
inss = 0.10

if (sal_bruto <= 900):
    imposto = 0

elif (sal_bruto <= 1500):
    imposto = 0.05

elif (sal_bruto <= 2500):
    imposto = 0.10

elif (sal_bruto > 2500):
    imposto = 0.20

descontos = (sal_bruto * sind) + (sal_bruto * inss) + (sal_bruto * imposto)

print(f'Salário Bruto: {sal_bruto}')
print(f'IR: {sal_bruto * imposto}')
print(f'INSS: {sal_bruto * inss}')
print(f'FGTS: {sal_bruto * fgts}')
print(f'Valor a ser pago para o Sindicato: {sal_bruto * sind}')
print(f'Total de descontos: {descontos}')
print(f'Salário Líquido: {sal_bruto - descontos}')