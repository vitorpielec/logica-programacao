
# Exercício
   # Faça um programa que converta metros para centímetros:

print("====== SEJA BEM VINDO AO CONVERSOR METROS/CENTIMETROS ======")

# O Try é uma função usada para tratar exceções, caso o usuário não responda da maneira correta(neste caso), somente números, será invalidado

while True:
   try:
      entrada = input("\nQuantos metros? (ou digite 'sair' para encerrar): ").lower()

      if entrada == 'sair':
         print("Encerrando programa.")
         print("Encerrando programa..")
         print("Encerrando programa...")
         break

      metros = float(entrada)
      centimetros = metros * 100
      print(f"{metros} metros, são {centimetros}, centímetros!")

   except ValueError:
      print("Ops! Formato inválido, digite apenas números.")