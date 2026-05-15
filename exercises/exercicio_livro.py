
# Exercício 
   # Esse é um algoritmo do livro Python Crash Course, usei-o para estudar sobre as tomadas de decisão.

from random import randint # A biblioteca randint permite uso de números aleatórios no seu algoritmo

print("I'm thinking of a number!")
secret_number = randint(1, 100) # Gera o número aleatório
active = True # Usando uma 'Flag' para controle

while active:
   # Recebe a entrada e converte para inteiro para evitar o erro TypeError
   guess = int(input("Try to guess the number I'm thinking of: "))
   
   # Lógica de Decisão
   if guess < secret_number:
      print("Too low! Guess again.")
   elif guess > secret_number: 
      print("Too high! Guess again.") 
   else:
      print("That's it, correct!")

      # Pergunta se quer continuar e limpa a string com lower()
      play_again = input("Would you like to play again? (yes/no) ").lower()
      if play_again == 'no':
         active = False # Encerra o loop através da Flag

print("Thanks for playing!")


