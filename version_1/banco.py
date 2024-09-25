
menu="""
    [d]- Depositar
    [s]- Sacar
    [e]- Extrato
    [x]- Sair

"""
LIMITE_SAQUE=3
LIMITE=500
if __name__ == '__main__':
   saldo=0
   extrato=""
   numero_saques=0
   
   while(True):
      opcao= input(menu)

      if opcao=="d":
         print("\nDepositar")
         valor = float(input("Informe o valor do depósito: "))
         if valor > 0:
             saldo=valor
             extrato += f"Depósito: R$ {valor:.2f}\n"
         else:
             print("Operação falhou! O valor informado é inválido.")

      elif opcao=="s":
         print("\nSacar")
         valor = float(input("informe o valor do saque:"))
         if valor > saldo:
             print("Operação falhou"" Você não tem saldo suficiente")
         elif valor > LIMITE:
             print("Operação falhou!! O valor do saque excedeu o limite.")
         elif valor > 0:
             saldo-=valor
             extrato += f"Saque: R$ {valor:.2f} \n" 
             numero_saques += 1   
         else:
             print("Operação falhou! O valor informado é inválido.")
      elif opcao=="e":
         print("\nExtrato")
         print("Não foram realizadas movimentações." if not extrato else extrato)
         print(f"\n Saldo: R$ {saldo:.2f}\n")
         

      elif opcao=="x":
         print("Saindo")
         break
    
      else:
         print("[ERRO]- Opcao invalida!!")
                 