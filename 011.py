sal = float(input("Informe seu salário: "))

if (sal >= 0 and sal <= 280):
    aumento = 0.20
    aumento2 = '20%'
if (sal > 280 and sal <= 700):
    aumento = 0.15
    aumento2 = '15%'
if (sal > 700 and sal < 1500):
    aumento = 0.10
    aumento2 = '10%'
if (sal >= 1500):
    aumento = 0.05
    aumento2 = '5%'

print(f'Seu salário antes do reajuste: {sal}')
print(f'Percentual de aumento aplicado {aumento2}')
print(f'Valor do aumento: {sal*aumento}')
print(f'Novo salário: {sal + (sal*aumento)}')