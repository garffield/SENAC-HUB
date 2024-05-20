horas = int(input("Informe quantas horas você trabalha por mês: "))
valor_hora = float(input("Informe quantos você ganha por hora: "))
salario_bruto = horas * valor_hora
sindicato = 0.05
inss = 0.08
imposto = 0.11

IRfinal = salario_bruto * imposto
INSsfinal = salario_bruto * inss
sindicatofinal = salario_bruto * sindicato
descontos = IRfinal + INSsfinal + sindicatofinal
salario_liquido = salario_bruto - descontos

print ("Salario bruto: ", salario_bruto)
print ("Imposto de renda: ", IRfinal)
print ("INSS: ", INSsfinal)
print ("Sindicato: ", sindicatofinal)
print ("Salário liquido: ", salario_liquido)