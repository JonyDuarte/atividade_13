import math

def exibir_menu():
    print(''' 
              [0] - Sair do programa
              [1] - Calcular potencia
              [2] - Calcular raiz quadrada.\n''')
    
potencia = lambda base, expoente: base ** expoente
raiz_quadrada = lambda numero: math.sqrt(numero)