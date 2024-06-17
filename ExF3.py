import random

def embaralha(valor):
    
    y = len(valor)
    x = random.sample(valor, y) #embaralha palavra
    x = ''.join(x) #junta palavra
    print(x)

embaralha('python')