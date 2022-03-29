import random
import os
print("~~" * 40)
print("\n---- Pedra, Papel e Tesoura ----\n")

escolha = int(input("Escolha uma opção \n 1- Pedra \n 2- Papel \n 3- Tesoura\n"))

if escolha == 1:
    print("Sua escolha foi Pedra")

elif escolha == 2:
    print("Sua escolha foi Papel")

elif escolha == 3:
    print("Sua escolha foi Tesoura\n")

while escolha >= 4:
    print("Opção inválida, tente novamente") 
    escolha = int(input("Escolha uma opção \n 1- Pedra \n 2- Papel \n 3- Tesoura\n"))
    if escolha == 1:
        print("Sua escolha foi Pedra")

    elif escolha == 2:
        print("Sua escolha foi Papel")

    else:
        print("Sua escolha foi Tesoura\n")

print("\nAgora é a vez da maquina escolher\n")    
os.system("Pause")

print("~~" * 40)

maquina = random.randrange(1,100)

if maquina < 33:
    print("\nMaquinha escolheu Pedra")
    if escolha == 1:
            print("Empate")
    elif escolha == 2:
        print("Voce ganhou")
    else:
        print("Você perdeu")

elif maquina >= 34 and maquina <= 63:
    print("Maquina escolheu Papel")
    if escolha == 2:
            print("Empate")
    elif escolha == 1:
        print("Voce perdeu")
    else:
        print("Você ganhou")
    
elif maquina >= 64 and maquina <= 100:
    print("Maquina escolheu tesoura")
    if escolha == 3:
        print("Empate")
    elif escolha == 2:
        print("Você perdeu")
    elif escolha == 3:
        print("Você ganhou")


print("~~" * 40)
print("\n")



