a = "EdErsOn"
b = "Ederson Roberto"
s = 'Olá, Mundo'
print(a.capitalize())                       # DEIXAR A PRIMEIRA LETRA EM MAIUSCULO
print(a.casefold())                         # DEIXAR TUDO MINUSCULO
print(a.lower())                            # DEIXAR TUDO MINUSCULO
print(a.upper())                            # DEIXAR TUDO MAIUSCULO
print(a.islower())                          # CONDIÇÃO: SE FOR VERDADEIRA, RETORNA TRUE, SE NÃO, FALSE
print(a.isupper())                          # CONDIÇÃO: SE FOR VERDADEIRA, RETORNA TRUE, SE NÃO, FALSE
print(a.isdigit())                          # CONDIÇÃO: SE FOR VERDADEIRA, RETORNA TRUE, SE NÃO, FALSE
print(len(a))                               # CONTAR QUANTAS LETRA TEM DENTRO DA VARIAVEL


print(b.replace("Roberto", "Costa"))        # TROCA AS OCORRENCIAS DE UMA SUBSTRING POR OUTRA STRING
print(b.find("Roberto"))                    # ENCONTRAR UMA STRING
print("Roberto" in b)                       # PESQUISA DENTRO DE UMA STRING
print(b.count("e"))
print(s[0])                                 # P | H | Y | T | O | N
print(s[1])                                 # 0 | 1 | 2 | 3 | 4 | 5 
print(s[2])                                 # -6|-5 |-4 |-3 |-2 |-1