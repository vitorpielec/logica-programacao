
# Exercício
   # Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
   # Conceito --> Se quiser diminuir faça *1024, se quiser aumentar faça /1024. 
   # Exemplos --> (GB para MB = GB * 1024) ### (KB para MB = KB / 1024)

try:
   
   print("Seja bem-vindo ao conversor de unidades de medidas computacionais")
   valor = float(input("Qual tamanho do seu arquivo?: "))
   origem = input("\nQual a unidade de medida inicial?(B, KB, MB, GB): ").upper()
   destino = input("Qual a unidade de conversão destinatária? (B, KB, MB, GB): ").upper()

   # Usei condicionais para transformar o dado de origem em uma unidade basal
   if origem == 'B':              
      valor_bytes = valor         
   elif origem == 'KB':
      valor_bytes = valor * 1024
   elif origem == 'MB':
      valor_bytes = valor * 1024 * 1024
   elif origem == 'GB':
      valor_bytes = valor * 1024 * 1024 * 1024
   else:
      valor_bytes = None

   if valor_bytes is not None:
      if destino == 'B':
         resultado = valor_bytes
      elif destino == 'KB':
         resultado = valor_bytes / 1024 
      elif destino == 'MB':
         resultado = valor_bytes / (1024 * 1024)
      elif destino == 'GB':
         resultado = valor_bytes / (1024 * 1024 * 1024)
      else:
         resultado = None

      if resultado is not None:
         print(f"\n[SUCESSO] {valor}{origem} equivalem a {resultado:.6f} {destino}")
      else:
         print("\n[ERRO] Unidade de destino inválida.")

except ValueError:
   print("\n[ERRO] Por favor, digite apenas números no valor.")


