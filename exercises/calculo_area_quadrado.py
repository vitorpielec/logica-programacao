
# Exercício
   # Calcule a área de um quadrado, a partir de um lado fornecido pelo usuário, depois apresente o dobro dessa área para ele

lado_quadrado = float(input("Digite o lado do quadrado: "))
area_quadrado = lado_quadrado ** 2
dobro_area = area_quadrado * 2

print(f"O resultado de {lado_quadrado} elevado ao quadrado é de {area_quadrado:.2f} consequentemente, também sua área.")
print(f"E o dobro da área é {dobro_area:.2f}")