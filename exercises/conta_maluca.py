
# Exercício
   # Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
      # O produto do dobro do primeiro com metade do segundo .
      # A soma do triplo do primeiro com o terceiro.
      # O terceiro elevado ao cubo.

num_int1 =  int(input("Digite um número inteiro: "))
num_int2 = int(input("Digite outro número inteiro: "))
num_real3 = float(input("Digite um número real: "))

primeira_conta = ((num_int1 * 2) * (num_int2 / 2))
print(f"O resultado do produto entre o dobro do primeiro(Inteiro) e a metade do segundo(Inteiro) é de : {primeira_conta:.2f}")

segunda_conta = (num_int1 * 3) + num_real3
print(f"O resultado da soma entre o triplo do primeiro número(Inteiro) com o terceiro(Real), é de : {segunda_conta:.2f}")

terceira_conta = num_real3 ** 3
print(f"O resultado do terceiro(Real) número elevado ao cubo, é de: {terceira_conta}")
