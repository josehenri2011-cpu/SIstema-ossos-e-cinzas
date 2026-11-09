saida=False

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

def calculo_vida(vigor,constituiçao,sobrevivencia):
     vida_total =(vigor + constituiçao + sobrevivencia)* 5
     return vida_total


def ler_inteligencia(inteligencia):
    if inteligencia>=10:
       return True
    else:
        return False  



def calculo_sanidade(vontade):   
    # calculos
     vontade=vontade*5
     return vontade
      

    #Relatorio da ficha

     print(f"Dado base de Ataque/ Força:1d20+{força}")
     print(f"Dado base de Ataque/ Destreza:1d20+{destreza}")
     print(f"esquivar/velocidade atual: {destreza}")
            
     if percepçao>=10:
              print("percepçao alta, você é capaz de perceber coisas com maior facilidade")
              print(f"**percepçao**={percepçao}")
     else:
        print(f"inteligencia={inteligencia}")  


def ler_nome_personagem(dicionario_fichas):
    while True:
          print("Qual o nome do personagem ? ")
          nome=input()
          if nome not in dicionario_fichas:
             return nome
          else:     
            print("esse personagem já esta cadastrado")

def buscar_ficha(buscar,dicionario_fichas):
    if buscar in dicionario_fichas:
       return True
    else:
        return False
    

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

def cadastro(dicionario_fichas):
    
    while True:
          print("=== GERADOR DE FICHA ===")

          nome=ler_nome_personagem(dicionario_fichas)

          print("Origem:")
          origem=input()

          print("idade")
          idade=(input())

          print("classe:")
          classe=input()

          print("Arma:")
          arma=input()

          print("descrição")
          descrição=input()
          
          print("Lore")
          lore=input()
          
          print("=== ATRIBUTOS===")
          
          força=int(input("força:"))
          destreza=int(input("destreza:"))
          inteligencia=int(input("inteligencia:"))
          percepçao=int(input("Percepçao:"))
          Educaçao=int(input("Educação:"))
          retorica=int(input("Retorica:"))
          vigor=int(input("vigor:"))     
          constituiçao=int(input("constituiçao:"))    
          sobrevivencia=int(input("sobrevivencia:"))
          carisma=int(input("Carisma:"))       
          vontade=int(input("Força de Vontade:"))
          pontos_habilidade=vigor


          #calculos
          vida_total=calculo_vida(vigor,constituiçao,sobrevivencia)
          sanidade=calculo_sanidade(vontade)
          dados_fichas={
               "origem: ":origem,
               "idade: ":idade,
               "classe:":classe,
               "arma :":arma,
               "descrição :":descrição,
               "lore :":lore,
                "atributos":{
                           "força":força,
                           "destreza":destreza,
                           "inteligencia":inteligencia,
                           "percepçao":percepçao,
                           "Educaçao":Educaçao,
                           "retorica":retorica,
                           "vigor":vigor,
                           "constituiçao":constituiçao,    
                           "sobrevivencia":sobrevivencia,
                           "carisma":carisma,
                           "vontade":vontade,
                            },
                 "valores_derivados":{  
                     "Pontos de Habilidade":pontos_habilidade,
                      "vida_total": vida_total,
                      "sanidade": sanidade,}
          
          
          } 
          resultado_int=ler_inteligencia(inteligencia)                    
          if resultado_int:
             print("Inteligencia acima de 10")
             dados_fichas["inteligencia alta"]="Sua inteligencia é acima da media"
          
          
          dicionario_fichas[nome]=dados_fichas
         
          
          
                    




          print("FICHA REGISTRADA COM SUCESSO")
          print(f"Informaçoes sobre: {nome}" )
          for chave, informaçoes in dicionario_fichas[nome].items():
              if chave=="atributos":
                 print("(=== ATRIBUTOS===)")
                 for atributos, valores in dicionario_fichas[nome]["atributos"].items():  
                     print(atributos,valores)
              elif chave=="valores_derivados":
                   print("=== STATUS ===")
                   for chave, valor in dicionario_fichas[nome]["valores_derivados"].items():
                      print(chave,valor)


              else:
                  print(chave, informaçoes)   
                 
                    
                     
                
          
          

          
          
          
                    
          
          while True:
               print("Deseja cadastrar outra ficha ? ")
               resposta=input()
          
               if resposta=="sim":
                  sair=False
                  break
               
               elif resposta=="nao":
                    sair=True
                    break
               else:
                   print("opçao invalida")
          if sair:
            print("voltando ao menu")
            return


#menu

while True:
     opcao=menu()
     
     if opcao==1:
        cadastro(dicionario_fichas)

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

          