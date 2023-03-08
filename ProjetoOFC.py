C = 300000000
print(f"Velocidade da Luz: {C:.2e} m/s")

Opcao = int(input("Escolha uma opção: 1 - Em, 2 - Bm, 3 - I"))

if Opcao == 1:
    Em = float(input("Digite o valor de Em: "))
    Bm = (Em)/C
    print(f"O valor de Bm é: {Bm:.2e} T")
    
elif Opcao == 2:
    Bm = float(input("Digite o valor de Bm: "))
    Em = Bm * C
    print(f"O valor de Em é: {Em:.2e} V/m")