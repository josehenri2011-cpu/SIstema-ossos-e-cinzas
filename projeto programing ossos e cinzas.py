saida=False
import cadastrar_ficha

dicionario_fichas={}



campos_editaveis = {
    "origem", "idade", "classe", "arma", "descricao", "lore",
    "força", "destreza", "inteligencia", "percepçao",
    "Educaçao", "retorica", "vigor", "constituiçao",
    "sobrevivencia", "carisma", "vontade"
}


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



#menu

while True:
     opcao=menu()
     
     if opcao==1:
        cadastrar_ficha.cadastro(dicionario_fichas)

     elif opcao==2:
        cadastrar_ficha.consulta_ficha(dicionario_fichas)
     elif opcao==3:
         cadastrar_ficha.alterar_ficha(dicionario_fichas,campos_editaveis)
         
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

          