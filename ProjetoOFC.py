pi = 3.1416
C = 300000000
micro0 = 4 * pi * 10**-7
print(f"Velocidade da Luz: {C:.2e} m/s")

Opcao = int(input("Escolha uma opção: 1 - Em, 2 - Bm, 3 - I, 4 - f, 5 - lambdaa, 6 - k, 7 - omega: "))

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
    Bm = ((2 * micro0 * I)/C)**(1/2)
    print(f"O valor de Bm é: {Bm:.2e} T")
elif Opcao == 4:
    f = float(input("Digite o valor de f: "))
    lambdaa = C/f
    print(f"O valor de lambda é: {lambdaa:.2e} m")
    k = 2 * pi/lambdaa
    print(f"O valor de k é: {k:.2e} m^-1")
    omega = 2 * pi * f
    print(f"O valor de omega é: {omega:.2e} rad/s")
elif Opcao == 5:
    lambdaa = float(input("Digite o valor de lambdaa: "))
    f = C/lambdaa
    print(f"O valor de f é: {f:.2e} Hz")
    k = 2 * pi/lambdaa
    print(f"O valor de k é: {k:.2e} m^-1")
    omega = 2 * pi * f
    print(f"O valor de omega é: {omega:.2e} rad/s")
elif Opcao == 6:
    k = float(input("Digite o valor de k: "))
    lambdaa = 2 * pi/k
    print(f"O valor de lambda é: {lambdaa:.2e} m")
    f = C/lambdaa
    print(f"O valor de f é: {f:.2e} Hz")
    omega = 2 * pi * f
    print(f"O valor de omega é: {omega:.2e} rad/s")
elif Opcao == 7:
    omega = float(input("Digite o valor de omega: "))
    f = omega/(2 * pi)
    print(f"O valor de f é: {f:.2e} Hz")
    lambdaa = C/f
    print(f"O valor de lambda é: {lambdaa:.2e} m")
    k = 2 * pi/lambdaa
    print(f"O valor de k é: {k:.2e} m^-1")
else:
    print("Opção inválida!")
