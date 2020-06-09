from controladorassento import controladorAssentos
class interfaceConsole():
    def __init__(self):
      self.linha = None
      self.coluna = None
      self.cadeirascompradas = None
      self.cadeirasdevolvidas = None
      self.controlador = None

    def imprimirmenu(self):
        print('')
        print('''\033[1;32m********\033[m \033[1;97;41m Bem vindo ao sistema de venda de ingressos. \033[m \033[1;32m********\033[m

\033[1;91mEscolha a operação:\033[m

\033[1;32m1- Comprar ingressos \033[1;93m$$$\033[m
\033[1;32m2- Devolver ingressos \033[1;91m(taxa de 10%)\033[m
\033[1;32m3- Resumo das vendas
4- Sair\033[m''')
        print('')
        
    def seguranca(self, l):
      while True:
          try:
              return int(l)
          except:
              l = input('Valor invalido, Informe o numero novamente: ')

    def pop(self):
      linha = input('linhas: ')
      linha = self.seguranca(linha)
      self.linha = linha

      coluna = input('coluna: ')
      coluna = self.seguranca(coluna)
      self.coluna = coluna

      controlador = controladorAssentos()
      controlador.set_linhas(linha)
      controlador.set_colunas(coluna)
      print('')
      controlador.criarsala()
      self.controlador = controlador
      self.menu()
    
    def matriz(self): 
        sala = ""
        numCadeira = 0
        v = (int(self.controlador.get_linhas()) * int(self.controlador.get_colunas()) - 1)
        for i in range(int(self.controlador.get_linhas())):
          for j in range(int(self.controlador.get_colunas())):
            cadeira = self.controlador.get_lista()[numCadeira]
            if cadeira.get_disponivel():
              sala += str(cadeira.get_numero()).zfill(len(str(v))) + " "
            else:
              sala += "xx".zfill(len(str(v))) + " "          
            numCadeira += 1
          sala += "\n"
        print(sala)
    
    def __repr__(self):
      print("\033[1;91mOcupação da sala no momento: {}\033[m".format(controladorAssentos.PessoasNaSala) )
      print('\033[1;91mQuantidade de ingressos devolvidos: {}\033[m'.format(controladorAssentos.cont))
      print('\033[1;91mValor total apurado: R$ {:.2f}\033[m'.format(controladorAssentos.ValorApurado))
     
    def Resumos(self):
      cont = 0
      for f in self.controlador.get_lista():
        if f.get_disponivel() == False:
          cont += 1
      controladorAssentos.PessoasNaSala = cont
            

    def menu(self):
      while True:
        print('')
        self.matriz()
        self.imprimirmenu()
        pergunta = input('\033[1;91mDigite sua escolha: \033[m')
        self.controlador.salvararquivo()
        if pergunta == '1':
          print('')
          self.controlador.matriz()
          cadeiraquero = input('\033[1;91mQuais assentos deseja comprar ? [dígite o número do assento]: \033[m').replace(" ", "").split(",")
          self.cadeirascompradas = cadeiraquero
          self.controlador.comprarAssentos(self.cadeirascompradas)
        elif pergunta == '2':
          print('')
          self.controlador.matriz()
          cadeiradevolver = input('\033[1;91mQuais assentos deseja devolver ? [dígite o número do assento]: \033[m').replace(" ", "").split(",")
          self.cadeirasdevolvidas = cadeiradevolver
          self.controlador.devolverAssentos(self.cadeirasdevolvidas)
        elif pergunta == '3':
          print('')
          self.Resumos()
          self.__repr__()
        elif pergunta == '4':
          print('')
          print('programa finalizado')
          self.controlador.carregararquivo()
          break   

    def inicio(self):
      self.controlador = controladorAssentos()
      if self.controlador.teste() == True:
        self.controlador.carregararquivo()
        self.menu()
      else:
        self.pop()

