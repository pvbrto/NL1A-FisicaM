print()
print("***********NL1A - Ondas Eletromagnéticas***********")
print()

print("Esse programa tem como objetivo calcular os valores de Em, Bm, I, f, lambda, k e omega, a partir de um valor conhecido.")
print()
print("Ondas eletromagnéticas são ondas que se propagam no vácuo, e que são formadas por oscilações de campos elétricos e magnéticos.\nUm exemplo de onda eletromagnética é a luz.")
print()
print("Em = campo elétrico médio\nBm = campo magnético médio\nI = intensidade da onda\nf = frequência\nlambda = comprimento de onda\nk = número de onda\nomega = frequência angular")
print()
print("Integantes da NL1A:\n- Livia Miyabara\n- Luiggi\n- Marcio Forner\n- Paulo Brito")
print()
print("Declaração de constantes: \npi = 3.1416\nC = 300000000\nmicro0 = 4 * pi * 10^-7")
pi = 3.1416
C = 300000000
micro0 = 4 * pi * 10**-7
print()
resposta = 1
while resposta == 1:
    Opcao = int(input("Escolha uma opção:\n1 - Em\n2 - Bm\n3 - I\n4 - f\n5 - Lambda\n6 - k\n7 - Omega\n"))
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
        I = (C/(2* micro0)) * (Bm ** 2)
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
        print(f"O valor de k é: {k:.2e} rad/m")
        omega = 2 * pi * f
        print(f"O valor de omega é: {omega:.2e} rad/s")
    elif Opcao == 5:
        lambdaa = float(input("Digite o valor de lambda: "))
        f = C/lambdaa
        print(f"O valor de f é: {f:.2e} Hz")
        k = 2 * pi/lambdaa
        print(f"O valor de k é: {k:.2e} rad/m")
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
    resposta = int(input("Deseja fazer um outro estudo? 1 - Sim 2 - Não: "))
