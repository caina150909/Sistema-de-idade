print("---------------------VERIFICAÇÃO DE IDADE-----------------------")

while True:
    idade = int(input("\nDIGITE SUA IDADE: "))

    if idade >= 18 and idade <= 120:
        print("Idade permitida: ")
    else:
        print("PROIBIDO IDADE INSUFICIENTE")
        
    