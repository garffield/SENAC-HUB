import math

area_a_ser_pintada = float(input("Digite o tamanh da area a ser pintaad: "))

area_a_ser_pintada_com_folga = area_a_ser_pintada * 1.1

litros_de_tinta = area_a_ser_pintada_com_folga / 6
quantidade_latas_18 = math.ceil(litros_de_tinta / 18)
quantidade_latas_36 = math.ceil(litros_de_tinta / 3.6)
preco_lata_18 = quantidade_latas_18 * 80.00
preco_galoes_36 = quantidade_latas_36 * 25.00

quantidade_latas_mix = quantidade_latas_18
quantidade_galoes_mix = math.ceil((litros_de_tinta - quantidade_latas_18 * 18) / 3.6)
