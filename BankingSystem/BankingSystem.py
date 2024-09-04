menu = """
[d] deposit
[w] withdraw
[s] statement
[q] quit

=> """

balance = 0 
limit = 500 
statement = ""
number_withdraw = 0 
LIMIT_WITHDRAWS = 3   # isso é uma constante

while True:
    
     option = input(menu) #opção = menu 
    
     if option == "d": # se a opção escolhida for = d (Depósito)
        value = float(input("Inform the deposit value")) #retorne a pergunta qual o valor do depósito? 
        
        if value > 0: #Se o valor for maior que zero 
          balance += value #some o valor do depósito com o valor do saldo 
          statement += f"Deposit: R$ {value:.2f}\n" #extrato vai acrescentar "Depósito: R$____"
        
        else:
            print("the operation failed! the informed value is insuficient")  #Se o depósito não seguir o padrão retorne "o valor informado é suficiente"
        
     elif option == "w": #se a opção for s 
        value = float(input("inform the withdraw value:")) #Informe o valor do saque
        
        exceeded_balance = value > balance #ultrapassou o limite do saldo se o valor for maior que o saldo
        
        exceeded_limit = value > limit #ultrapassa o limite disponível se o valor for maior que o limite disponível
        
        exceeded_withdraw = number_withdraw >= LIMIT_WITHDRAWS #ultrapassa o limite de saques se o valor for maior que o limite de saques 
        
        if exceeded_balance:
            print("Operation Failed! Your balance is insuficient") # se o limite do saldo for excedido retorne "o seu saldo é insuficiente"
            
        elif exceeded_limit:
            print("Operation Failed! The balance value exceeded the limit") #se o limite for ultrapassado retorne "O valor do saque ultrapassou o limite"
            
        elif exceeded_withdraw:
            print("Operation failed!The maximum number of withdraws was exceeded") #se o limite de saques for ultrapassado retorne "o número máximo de saques foi ultrapassado"
            
        else:
            print("Operation failed! The informed value is invalid") #caso contrário o valor informado é inválido
            
     elif option == "s": #exemplo de extrato
         print("\n============== Extrato=============")
         print("No movements were made." if not statement else statement)
         print(f"\nSaldo: R$ {balance:.2f}")
         print("====================================")
         
     elif option == "q": # se a opção escolhida for sair, o código para de rodar
       break
   
     else:
         print("Invalid Operation, please select again the desired operation") # caso contrário retorna a seguinte mensagem "operação inválida, por favor selecione novamente a operação desejada"