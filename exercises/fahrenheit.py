
# Exercício
   # Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.(RESOLVI FAZER AS DUAS, DE FH PARA CL, E DE CL PARA FH.)

entrada = input("====== BEM-VINDO AO CONVERSOR DE TEMPERATURA, VOCE DESEJA DE FAHRENHEIT PARA CELSIUS, OU DE CELSIUS PARA FARENHEIT? Digite 1 para a primeira opção, ou 2 para a segunda. =============: ")

if entrada == '1':
   temp_graus_fr = float(input("Digite a temperatura em graus Fahreinheit: "))
   fr_celsius = 5 * ((temp_graus_fr - 32) / 9)
   print(f"A conversão de graus Fahrenheit para Celsius, é de: {fr_celsius:.2f}")
elif entrada == '2':
   temp_graus_cl = float(input("Digite a temperatura em graus Celsius: "))
   cl_fahrenheit = (temp_graus_cl * 1.8) + 32 
   print(f"A conversão de graus Celsius para Fahrenheit, é de: {cl_fahrenheit:.2f}")
