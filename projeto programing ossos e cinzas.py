saida=False
import cadastrar_ficha

dicionario_fichas={}

def menu():
    print("1 - Cadastrar ficha")
    print("2 - mostrar ficha")
    print("3 - Alterar ficha")
    print("4 - Encerrar")
    print("5 - Defina seu atributo favorito")
    while True:
         try:
           opcao=int(input())
           break
         except ValueError:
             print("digite um numero para selecionar uma das opçoes")
    return opcao




    

def alterar_ficha(dicionario_fichas):
    if dicionario_fichas=={}:
       print("nenhum cadastro registrado")
       return
    while True:
         while True:
               print("qual ficha você deseja alterar ?")
               buscar=input()
               if buscar_ficha(buscar,dicionario_fichas)==True:
                  print(dicionario_fichas[buscar])
                  break
               else:
                  print("ficha nao cadastrada")
                  print("tente novamente")
         while True:   
               print("qual dado vc deseja atualizar  ? ")
               alterar=input()
               if alterar in dicionario_fichas[buscar]:
                  print(f"digite a atualização da {alterar}")
                  novo_registro=input()
                  dicionario_fichas[buscar][alterar]=novo_registro
                  print("Alteração feita com sucesso")
                  break
               else:
                   print("dado inexistente")
            
            
         while True:
                  print("deseja continuar ? sim/nao")
                  continuar=input()
                  if continuar=="sim":
                     sair=False
                     break
                  elif continuar=="nao":
                       sair=True
                       break
                  else:
                    print("opcao invalida")
                    
         if sair==True:
            print("voltando ao menu")
            break
            

def consulta_ficha(dicionario_fichas):
    if dicionario_fichas=={}:
       print("nenhum cadastro registrado")
       return   
    while True:
          print("qual ficha deseja consultar ? ")
          buscar=input()
          if buscar_ficha(buscar,dicionario_fichas)==True:
             print(f"Informaçoes sobre: {buscar}" ) 
             for chave, informaçoes in dicionario_fichas[buscar].items():
                   if chave=="atributos":
                    print("(=== ATRIBUTOS===)")
                    for atributos, valores in dicionario_fichas[buscar]["atributos"].items():  
                        print(atributos,valores)
                   elif chave=="valores_derivados":
                       print("=== STATUS ===")
                       for status, valor in dicionario_fichas[buscar]["valores_derivados"].items():
                           print(status,valor)
                   else:
                      print(chave, informaçoes)   
          else:
              print("Registro nao encontrado")                 
    
          while True:
               print("deseja continuar ? sim/nao")
               continuar=input()
               
               if continuar=="sim":
                  sair= False 
                  break
               elif continuar=="nao":
                    sair= True
                    break
               else:
                   print("resposta invalida")
          
          if sair:
             print("voltando ao menu")
             return


#menu

while True:
     opcao=menu()
     
     if opcao==1:
        cadastrar_ficha.cadastro(dicionario_fichas)

     elif opcao==2:
          consulta_ficha(dicionario_fichas)
     elif opcao==3:
         alterar_ficha(dicionario_fichas)
         
     elif opcao==4:
         
         while True:
              print("tem certeza que dejesa encerrar ? ")
              encerrar=input()
              if encerrar=="sim":
                 saida=True
                 break
              elif encerrar=="nao":
                   print("voltando ao menu")
                   break
              else:
                  print("opçao invalida")
                  print("tente novamente!")

     if saida==True:
        print("Programa finalizado") 
        break

          