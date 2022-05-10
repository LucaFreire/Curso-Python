    #Jokenpô

from random import randint
print("""[0] Contra a Matrix
[1] Offline 1vs1 """)
jog=int(input("Modo de Jogo: "))
   
if jog==1:   
    aa=str(input("Nome do Primeiro Jogador: "))
    bb=str(input("Nome do Segundo Jogador: "))

    print("""[0]Pedra 
[1]Papel 
[2]Tesoura""")
    a=int(input(f"Jogada do {aa}: "))
    b=int(input(f"Jogada do {bb}: "))
    if a==b:
        print("Empate")
    elif a==0 and b==1:
        print(f"{bb} Ganhou!")    
    elif a==1 and b==0:
        print(f"{aa} Ganhou!")
    elif a==2 and b==0:
        print(f"{bb} Ganhou!")
    elif b==2 and a==0:
        print(f"{aa} Ganhou!")
    elif b==1 and a==2:
        print(f"{aa} Ganhou!")
    elif a==1 and b==2:
        print(f"{bb} Ganhou!")
    else:
        print("Número Inválido!")       

elif jog==0:

    a=str(input("Digite Seu Nome: "))
    print("""[0]Pedra 
[1]Papel 
[2]Tesoura""")
    jog=int(input(f"Digite sua Jogada {a}: "))
    Matrix=randint(0,2)
    if jog==Matrix:
        print("Empataram!")
    elif jog==0 and Matrix==1:
        print("Matrix Ganhou!")
    elif jog==1 and Matrix==0:
        print(f"{a} Ganhou!")
    elif jog==2 and Matrix==1:
        print("Matrix Ganhou!")
    elif jog==1 and Matrix==2:
        print(f"{a} Ganhou!")
    elif jog==0 and Matrix==2:
        print(f"{a} Ganhou!")
    elif jog==2 and Matrix==0:
        print("Matrix Ganhou!")            
    else:
        print("Número Inválido!")
else:
    print("Digite um Número Válido!")             