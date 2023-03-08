pi = 3.1416
C = 300000000
micro0 = 4 * pi * 10**-7
print(f"Velocidade da Luz: {C:.2e} m/s")

Opcao = int(input("Escolha uma opção: 1 - Em, 2 - Bm, 3 - I"))

if Opcao == 1:
    Em = float(input("Digite o valor de Em: "))
    Bm = (Em)/C
    print(f"O valor de Bm é: {Bm:.2e} T")
    I = (1/(2* micro0 * C)) * (Em ** 2)
    print(f"O valor de I é: {I:.2e} W/m²")
elif Opcao == 2:
    Bm = float(input("Digite o valor de Bm: "))
    Em = Bm * C
    print(f"O valor de Em é: {Em:.2e} V/m")
    I = (1/(2* micro0)) * (Bm ** 2)
    print(f"O valor de I é: {I:.2e} W/m²")
elif Opcao == 3:
    I = float(input("Digite o valor de I: "))
    Em = (2 * micro0 * C * I)**(1/2)
    print(f"O valor de Em é: {Em:.2e} V/m")
    Bm = (2 * micro0 * I)**(1/2)
    print(f"O valor de Bm é: {Bm:.2e} T")
