nome = input("Qual seu nome? ")
# print(f"Olá, {nome}!")

# if nome == "Cícero":
#     print("Que legal! Você é meu xará.")

idade = 0
while True:
    try:
        idade = int(input("Qual a sua idade? "))
        break
    except:
        print("Idade inválida!")

print(f"Olá, {nome}!")
if idade >= 18:
    print("Você já é maior!")