class Assento():

    def __init__(self,numero,preco,disponivel):
        self.__numero = numero
        self.__preco = preco
        self.__disponivel = disponivel

    def get_numero(self):
        return self.__numero

    def get_preco(self):
        return self.__preco

    def get_disponivel(self):
        return self.__disponivel

    def set_numero(self,numero):
        self.__numero = numero

    def set_preco(self,novonumero):
        self.__preco = novonumero

    def set_disponivel(self,novonumero2):
        self.__disponivel = novonumero2
