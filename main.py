from ControleRemoto import *

controle_remoto_x = ControleRemoto('azul', 30, 3, 5)
controle_remoto_y = ControleRemoto('preto', 35, 2, 5)

print(controle_remoto_x.cor)
print(controle_remoto_y.cor)
print(type(controle_remoto_x))
controle_remoto_x.mudar_canal("+")
