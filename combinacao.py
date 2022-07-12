class Mao:
    def __init__ (self, carta1, carta2):
        self.carta1 = carta1
        self.carta2 = carta2
    
    def show_hands(self):
        print(f' A sua mão é: {self.carta1}, {self.carta2}!')


class Repeticao:
    def __init__ (self, par, trinca, quadra):
        self.par = par
        self.trinca = trinca
        self.quadra = quadra

class Combinacao:
    def __init__(self, combinacao):
        self.combinacao = combinacao
    
    def show_combi(self):
        print(f' Você tem {self.combinacao}!')

