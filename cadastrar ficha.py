class FichaPersonagem:
    def __init__(self, nome, origem, idade, classe, arma, descricao, lore):
        self.nome = nome
        self.origem = origem
        self.idade = idade
        self.classe = classe
        self.arma = arma
        self.descricao = descricao
        self.lore = lore

class Atributos:
    def __init__(self,força, destreza, inteligencia, percepçao, Educaçao, retorica, vigor, constituiçao, sobrevivencia, carisma, vontade):
        self.força = força
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.percepçao = percepçao
        self.Educaçao = Educaçao
        self.retorica = retorica
        self.vigor = vigor
        self.constituiçao = constituiçao
        self.sobrevivencia = sobrevivencia
        self.carisma = carisma
        self.vontade = vontade
        self.pontos_habilidade = vigor
        self.vida_total = self.calcular_vida()
        self.sanidade = self.calcular_sanidade()


    def calcular_vida(self):
        vida_total = (self.vigor + self.constituiçao + self.sobrevivencia) * 5
        return vida_total

    def calcular_sanidade(self):
        sanidade = self.vontade * 5
        return sanidade




def cadastro(dicionario_fichas):
    
    while True:
          print("=== GERADOR DE FICHA ===")
          while True:
                nome=input("Insira o nome:")
                
                if nome in dicionario_fichas:
                    print("Esse nome já esta registrado")
                
                else:
                    break
                    
          print("Origem:")
          origem=input()

          print("idade")
          idade=(input())

          print("classe:")
          classe=input()

          print("Arma:")
          arma=input()

          print("descrição")
          descricao=input()
          
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

