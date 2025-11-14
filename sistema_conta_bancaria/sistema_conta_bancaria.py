class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
        self.__limite = 500

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Não é possivel definir saldo negativo!')
        else:
            self.__saldo = valor

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito feito com sucesso! | Saldo: €{self.__saldo}")

    def sacar(self, valor):
        if valor <= self.__saldo and valor <= self.__limite:
            self.saldo -= valor
            print(f"Saque feito com sucesso! | Saldo: €{self.__saldo}")
        else:
            print('Saque não autorizado!')
            
    def mostrar_info(self):
        print(f"Titular: {self.__titular} | Saldo: €{self.__saldo}")
    
p1 = ContaBancaria('Matheus')
p2 = ContaBancaria('Bruna')

p1.depositar(1000)
p2.depositar(2000)
print()

p1.sacar(400)
p2.sacar(500)
print()

p1.sacar(600)
print()

p1.mostrar_info()
p2.mostrar_info()
