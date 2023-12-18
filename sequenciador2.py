numero = int(input("Número para ser sequenciado: "))

numero_pretendido = numero + 400


def sequenciador():
    global numero
    arquivo = open("ListadeTelefones.txt", "w")

    while numero <= numero_pretendido:
        print(numero)
        numero += 1


        arquivo.write(str(numero) + "\n")
    arquivo.close()


sequenciador()      
