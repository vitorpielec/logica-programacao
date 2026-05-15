
# Exercício 
   # Crie um programa, que peça para o usário seu seu salário por hora, horas trabalhadas no mês e depois informe seu salário mensal

try:
   salario_hora = float(input("Quanto você recebe por hora? R$ : "))
   horas_mes = float(input("Quantos horas por mês você trabalha?: "))
   
   total_salario = salario_hora * horas_mes
   
   print(f"O seu salário mensal é de: R$ {total_salario:.2f}")
except ValueError:
   print("Erro, digite apenas números.")

