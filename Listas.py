lista1 = [1, 2, 3]                         # EXEMPLO DE LISTA 
lista2 = ['Olá' , 'Mundo']                 # EXEMPLO DE LISTA 
print (lista1, lista2)

lista3 = ['oi', 2.0, 5, [10, 20]]          # EXEMPLO DE LISTA 
print(lista3)
print(len(lista3))                         # CONTAR QUANTOS ELEMENTOS TEM DENTRO DE UMA LISTA

print (lista3[3])                          # PRINT DE UM ELENMENTO DE UMA LISTA

print("Olá" in lista2)
print("ola" in lista2)

a = [1, 2, 3, 4, 5]
print(min(a))
print(max(a))
print(sum(a))

frutas = ['maça', 'pera', 'abacaxi', 'goiaba']
frutas [1:3] = ['banana', 'mamao']
print(frutas)

z = [2, 3, 7, 10, 6]
z.sort()                                   # ORDENA OS ELEMENTOS
print(z)

print(z.index(7))                          # INFORMA A POSIÇÃO DO ELEMENTO DENTRO DA VARIAVEL

b = [88, 81, 90, 90, 92, 784, 12, 90]
print(b.count(90))
print(b)
b.pop(0)                                   # POP DELETA UM ELEMENTO
print(b)

t = [[1, 2], [3], [4, 5, 6]]               # SOMA DE TODOS OS ELEMENTOS
print(sum (t[0] + t[1] + t[2]))            # SOMA DE TODOS OS ELEMENTOS

i = [1, 2, 3]                                   
print([i[0], i[0] + i[1], i[2] + i[1] + i[0]]) # SOMA DO ATUAL COM O ANTERIOR
