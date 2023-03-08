import time
import os
print("=============NL1A - Ondas Eletromagnéticas=============")
time.sleep(3)
os.system('cls')
print()
print("==================Sumário e Objetivos==================")
print()
print("Esse programa tem como objetivo calcular os valores de Em, Bm, I, f, lambda, k e omega, a partir de um valor conhecido.")
print()
print("Em relação a parte teórica as ondas eletromagnéticas são um tipo de radiação ")
print("que se propaga no espaço sem a necessidade de um meio físico. Elas são compostas por campos elétricos") 
print("e magnéticos oscilantes, que se propagam perpendicularmente um ao outro e à direção de propagação da onda.")
print("A velocidade de propagação dessas ondas no vácuo é de aproximadamente 3x10^8 metros por segundo,")
print("e sua frequência e comprimento de onda podem variar amplamente, desde ondas de rádio de baixa ")
print("frequência até raios gama de alta frequência.")
print()
print("Alguns exemplos de ondas eletromagnéticas são as ondas de rádio, as micro-ondas, a luz visível,") 
print("os raios X e os raios gama. As ondas magnéticas são uma parte importante desse espectro ")
print("eletromagnético, e são geradas pela variação do campo magnético ao longo do tempo. Elas podem ser") 
print("produzidas naturalmente, como no caso das tempestades solares, ou artificialmente, em equipamentos ")
print("como transformadores e motores elétricos. As ondas magnéticas têm várias aplicações práticas, ")
print("incluindo a comunicação sem fio, a produção de imagens médicas, a inspeção de materiais e a geração ")
print("de energia elétrica.")
print()
time.sleep(3)
os.system('cls')
print("==================Integrantes do Grupo=================")
print()
print("- Livia Miyabara\n- Luiggi\n- Marcio Forner\n- Paulo Brito")
print()
time.sleep(3)
os.system('cls')
pi = 3.1416
C = 300000000
micro0 = 4 * pi * 10**-7
print("======================CONSTANTES=======================")
print()
print(f"pi = {pi}\nVelocidade da Luz(C) = {C:.2e}\nConstanteMagnética(micro0) = {micro0:.2e}")
print()
time.sleep(3)
os.system('cls')
print("OBS: O programa só aceita números com ponto, não com vírgula, além disso escreva todos os valores em relação a unidade Ex. 60uT = 60*10^-6T")
resposta = 1
while resposta == 1:
    time.sleep(3)
    print("=======================================================")
    print("==================Legenda de Unidades==================")
    print("=======================================================")
    print()
    print("Em = campo elétrico médio\nBm = campo magnético médio\nI = intensidade da onda\nf = frequência\nlambda = comprimento de onda\nk = número de onda\nomega = frequência angular")
    print()
    print()
    print("===============MENU DE OPÇÕES DE CALCULO===============")
    Opcao = int(input("Escolha uma opção:\n1 - Em\n2 - Bm\n3 - I\n4 - f\n5 - Lambda\n6 - k\n7 - Omega\n=======================================================\nEscolha a opção:"))
    time.sleep(1)
    print()
    
    if Opcao == 1:
        Em = float(input("Digite o valor de Em: "))
        print()
        Bm = (Em)/C
        print(f"O valor de Bm é: {Bm:.2e} T")
        I = (1/(2* micro0 * C)) * (Em ** 2)
        print(f"O valor de I é: {I:.2e} W/m²")
    elif Opcao == 2:
        Bm = float(input("Digite o valor de Bm: "))
        print()
        Em = Bm * C
        print(f"O valor de Em é: {Em:.2e} V/m")
        I = (C/(2* micro0)) * (Bm ** 2)
        print(f"O valor de I é: {I:.2e} W/m²")
    elif Opcao == 3:
        I = float(input("Digite o valor de I: "))
        print()
        Em = (2 * micro0 * C * I)**(1/2)
        print(f"O valor de Em é: {Em:.2e} V/m")
        Bm = ((2 * micro0 * I)/C)**(1/2)
        print(f"O valor de Bm é: {Bm:.2e} T")
    elif Opcao == 4:
        f = float(input("Digite o valor de f: "))
        print()
        lambdaa = C/f
        print(f"O valor de lambda é: {lambdaa:.2e} m")
        k = 2 * pi/lambdaa
        print(f"O valor de k é: {k:.2e} rad/m")
        omega = 2 * pi * f
        print(f"O valor de omega é: {omega:.2e} rad/s")
    elif Opcao == 5:
        lambdaa = float(input("Digite o valor de lambda: "))
        print()
        f = C/lambdaa
        print(f"O valor de f é: {f:.2e} Hz")
        k = 2 * pi/lambdaa
        print(f"O valor de k é: {k:.2e} rad/m")
        omega = 2 * pi * f
        print(f"O valor de omega é: {omega:.2e} rad/s")
    elif Opcao == 6:
        k = float(input("Digite o valor de k: "))
        print()
        lambdaa = 2 * pi/k
        print(f"O valor de lambda é: {lambdaa:.2e} m")
        f = C/lambdaa
        print(f"O valor de f é: {f:.2e} Hz")
        omega = 2 * pi * f
        print(f"O valor de omega é: {omega:.2e} rad/s")
    elif Opcao == 7:
        omega = float(input("Digite o valor de omega: "))
        print()
        f = omega/(2 * pi)
        print(f"O valor de f é: {f:.2e} Hz")
        lambdaa = C/f
        print(f"O valor de lambda é: {lambdaa:.2e} m")
        k = 2 * pi/lambdaa
        print(f"O valor de k é: {k:.2e} m^-1")
    else:
        print("Opção inválida!")
    print()
    resposta = int(input("Deseja fazer um outro estudo? 1 - Sim 2 - Não: "))
    os.system('cls')
    print()
print("Obrigado por usar nosso programa! :D")
