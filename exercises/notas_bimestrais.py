
# Exercício

# Faça um programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

if nota1 > 10 or nota2 > 10 or nota3 > 10 or nota4 > 10:
   print("Formato numérico inválido")
else:
   mediaBimestral = (nota1 + nota2 + nota3 + nota4) / 4
   print(f"A média foi: {mediaBimestral:.2f}")
