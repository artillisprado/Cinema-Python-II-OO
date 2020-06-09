from assento import Assento
class controladorAssentos():
    PrecoDevolvido = 0
    PessoasNaSala = 0
    cont = 0
    ValorApurado = 0
    PrecoPessoaSala = 0
    def __init__(self):
        self.__linhas = None
        self.__colunas = None
        self.__lista = []
        self.__saldodevolucoes = None


    def criarsala(self):
        qtdCadeiras = int(self.__linhas) * int(self.__colunas)
        cadLinha = 0
        valor = 20
        for i in range(qtdCadeiras):
          a = Assento(i, valor, True)
          self.__lista.append(a)
          cadLinha += 1
          if cadLinha == self.__colunas:
            valor -= 1
            cadLinha = 0

    def set_linhas(self,linhas):
      self.__linhas = linhas

    def set_colunas(self,colunas):
      self.__colunas = colunas

    def get_linhas(self):
      return self.__linhas

    def get_colunas(self):
      return self.__colunas

    def get_lista(self):
      return self.__lista

    def listadeassentos(self,cadeirapronta):
      self.__lista.append(cadeirapronta)        

    def matriz(self): 
        sala = ""
        numCadeira = 0
        v = (int(self.__linhas) * int(self.__colunas) - 1)
        for i in range(int(self.__linhas)):
          for j in range(int(self.__colunas)):
            cadeira = self.__lista[numCadeira]
            if cadeira.get_disponivel():
              sala += str(cadeira.get_numero()).zfill(len(str(v))) + " "
            else:
              sala += "xx".zfill(len(str(v))) + " "          
            numCadeira += 1
          sala += "\n"
        print(sala)

    
    def comprarAssentos(self,cadeiraquero):
      retorno = False
      v = (int(self.__linhas) * int(self.__colunas) - 1)
      temRepetidos = self.saberRepetidos(cadeiraquero)
      if (temRepetidos):
          pass
      else:
        for f in self.__lista:
          for e in cadeiraquero:
            if f.get_numero() == int(e):
              if f.get_disponivel():
                  f.set_disponivel(False)
                  retorno = True
                  f.set_numero = "xx".zfill(len(str(v))) + " "
                  controladorAssentos.ValorApurado += int(f.get_preco())
              else:
                  retorno = False
              break
      return retorno

    def saberRepetidos(self, lista):
        retorno = False
        l = []
        for i in lista:
          if i not in l:
            l.append(i)
          else:
            print('\033[1;31mCompra inválida, Tente novamente !\033[m'.format(i))
            retorno = True
            break
        for l in lista:
          num = int(l)
          a = self.__lista[num]          
          if a.get_disponivel() == False:
            retorno = True
            break          
        return retorno
    
    def saberRepetidosD(self, lista):
        retorno = False
        l = []
        for i in lista:
          if i not in l:
            l.append(i)
          else:
            print('\033[1;31mCompra inválida, Tente novamente !\033[m'.format(i))
            retorno = True
            break
        for l in lista:
          num = int(l)
          a = self.__lista[num]          
          if a.get_disponivel() == True:
            retorno = True
            break          
        return retorno
  
    def devolverAssentos(self,cadeiradevolver):
      retorno = False
      v = (int(self.__linhas) * int(self.__colunas) - 1)
      temRepetidos = self.saberRepetidosD(cadeiradevolver)
      if (temRepetidos):
          pass
      else:
        for f in self.__lista:
          for e in cadeiradevolver:
            if f.get_numero() == int(e):
                if f.get_disponivel():
                  retorno = False
                  f.set_numero = e.zfill(len(str(v))) + " "
                else:
                    f.set_disponivel(True)
                    retorno = True
                    controladorAssentos.cont += 1
                    controladorAssentos.ValorApurado -= 0.9*int(f.get_preco())
                break
      return retorno 
    def salvararquivo(self):
      salvArq = open('arquivo.txt', 'w')
      salvArq.write(str(self.__linhas) + '>')
      salvArq.write(str(self.__colunas) + '>')
      salvArq.write(str(controladorAssentos.PessoasNaSala) + '>')
      salvArq.write(str(controladorAssentos.cont) + '>')
      salvArq.write(str(controladorAssentos.ValorApurado) + '\n')
      for f in self.__lista:
        a = '{}'.format(f.get_numero())
        b = '{}'.format(f.get_preco())
        c = '{}'.format(f.get_disponivel())
        salvArq.write('{}:'.format(a))
        salvArq.write('{}:'.format(b))
        salvArq.write('{}\n'.format(c))
      salvArq.close()  

    def teste(self):
      try:
        a = open('arquivo.txt', 'r')
        return True
      except:
        return False
        
    def carregararquivo(self):
      salvArq = open('arquivo.txt', 'r')
      for c in salvArq.readlines():
        c = c.replace("\n","")
        if '>' in c:
          a = c.split('>')
          self.set_linhas(int(a[0]))
          self.set_colunas(int(a[1]))
          controladorAssentos.PessoasNaSala = int(a[2])
          controladorAssentos.cont = int(a[3])
          controladorAssentos.ValorApurado = float(a[4])
        else:
          b = c.split(':')

          u = int(b[0])
          valor = float(b[1])
          if b[2] == 'True':
            disponibilidade = True
          else:
            disponibilidade = False
          ç = Assento(u, valor, disponibilidade)
          self.__lista.append(ç)





        

