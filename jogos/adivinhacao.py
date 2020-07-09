print("***************")
print("Olá, bem-vindo!")
print("***************")

numero_secreto = 42

chute_str = input("Digite um número=> ")
chute = int(chute_str)

if(chute == numero_secreto):
    print("Você acertou!! => ", chute)
else:
    print("Você errou!! => ", chute)

print("Fim do Jogo")