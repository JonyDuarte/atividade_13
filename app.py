
from math import sqrt
from calculo import *

while True:
        exibir_menu()
        opcao = input("Opção desejada: ")

        match opcao: 
            case "0":
                print("Saindo do programa")
                break
            case "1":
                base = int(input("Informe o número da base: "))
                expoente = int(input("Informe o número do exponte: "))
                print(f"O valor da potençiação dos números informados é {potencia(base, expoente)}.2
                ")
                continue
            case "2":
                numero = float(input("Informe um número que deseja saber sua raiz: ").replace(",","."))
                print(f" A raiz quadrada de {numero} é: {raiz_quadrada(numero)}")
                continue
            case _: 
                print("Opção Inválida.") 

    