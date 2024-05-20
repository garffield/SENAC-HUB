lista1 = [10 ,20 ,["spam","bungee","swallow"]] # uma lista dentro de outra lista 
lista2 = ["spam","bungee","swallow"] # apenas uma lista 

print (len(lista1)) # aqui ele vai contar quantos elementos tem dentro da lista , que é 5 elementos "LEMBRANDO QUE " o que está dentro do couchetes não conta exemplo [1,2,3,4,5] nesse caso conta como 1 
print (len(lista2)) # aqui conta 3 elementos 
print (lista1[2][2]) # aqui vai imprimir quero visualizar no caso vou pegar o item "30" da lista 1 . ## começa a contar apartir do zero um dois três quatro ... na posição 2 é o numero "30"
print (lista2[1])# aqui vai imprimir a posição 1 da lista2 , mesma coisa do exemplo acima
lista3 = [10,20,30,40,50,60,70,80,90,100]
lista3[1:4]= [15,16,17] # aqui vou substituir o 20,30,40 por 15,16,17

frutas = ["maça","laranja","banana","cereja"]
del frutas[1] # essa função faz deletar o item selecionado , no caso deletei a laranja da lista

frutas[0] = "salada" # aqui eu altero a palavra que eu quero colocando a posição dela , troquei a palavra maça por salada
frutas[-1] = "teste" # troquei cereja por teste 

print(lista3[1:5]) # aqui ele vai mostra os itens entre a posição 1 a 5 no caso vai imprimir ( 20,30,40,50)
print("maça" in frutas) # essa função mostra se tem maça dentro da lista frutas se tiver é verdadeira 
print("pera" in frutas) # nesse caso vai ser false por que não tem pera na lista 
print("1234567890\n"*2) # aqui vc multiplica quantas vezes quer q apareça a frase

print((frutas + lista1 + lista2)*2)

print(min(lista3)) # aqui ele vai mostrar o menor valor da lista
print(max(lista3)) # aqui ele vai mostrar o maior valor da lista
print(sum(lista3)) # aqui ele vai somar todos os elementos da lista 

frutas.append ("abacaxi ") # ele add um item no final da lista

lista4 = [20,10,30,54,65,25,36,12,22]
lista5 = [21,11,31,53,64,24,37,13,27]
lista4.sort() # aqui ele coloca em ordem crescente
lista5.reverse() # aqui em ordem decrescente
print(lista4)
print(lista5)

a = [1,2,3,4,5,6,7,8,9,10]
print(a.index(3)) # aqui ele busca em qual posição ta na lista 

b = [1,2,3,4,5,6,7,8,9,10,4,4,4,4,4]
b.insert(11,100) # o 11 é a posição que quer q coloca e o 100 é o numero
print(b)
print(b.count(4)) # contador de quantas vezes ele apareceu 
c = [88,81,82,83,88,85,86]

c.pop() # deleta o ultimo item no caso é o 86
print (c)
c.pop(0) # aqui ele vai apagar o primeiro item 
print(c)

d = [1,2]
d.extend([3,4]) # add no final exemplo [1,2,3,4]
print(d)
