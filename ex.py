try: 
 a = int(input("DIgite uma palavra: "))
except ValueError:                          # ESPECIFICA OS ERROS
 print("DIgite apenas numeros")
except:                                     # CASO HAJA ALGUM ERRO, IMPRIMA A MENSAGEM
 print("Erro Desconhecido")
finally:                                    # CASO EXISTA UM ERRO OU NÃO, SERÁ EXECUTADO
 print("Fim do ALgoritmo")