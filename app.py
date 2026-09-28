print("=== PESQUISA DE OPINIÃO - TUDOWEB ===")

excelente = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida.")

print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")