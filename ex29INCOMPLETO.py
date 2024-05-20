salario = float(input("Informe seu salário: "))

if salario > 0 and salario <= 280:
    aumento = 0.20
elif salario > 280 and salario <= 700:
    aumento = 0.15
elif salario > 700 and salario <= 1500:
    aumento = 0.10
elif salario > 1500:
    aumento = 0.05

print(f'Seu salário antes era de: {salario}')
print(f'Percentual de aumento aplicado: {salario * aumento}')
print(f'Aumento aplicado: {salario * aumento}')