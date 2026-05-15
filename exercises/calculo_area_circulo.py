
# Exercício 
   # Calcule a área de um círculo a partir de um input de raio

# A biblioteca math possibilita precisão maior ao usar constantes
import math

PI = math.pi # <-- Crio a variável PI e já adiciono a constante correspondente.

raio = float(input("Digite o raio do círculo: "))
area = PI * raio ** 2
print(f"A área do círculo é de: {area:.2f}") # <-- Aqui eu formatei de maneira que apareça apenas 2 casas decimais.
