#!/usr/bin/env python
__author__      = "Leandro de Campos"

class Pilha:
    def __init__(self):
        self.items = []
    def topo(self):
        if(self.vazia()):
            raise(Exception('Pilha vazia'))
        else:
            return self.items[-1]        
    def vazia(self):
        return (self.items == [])
    def tamanho(self):
        return len(self.items)
    def empilha(self,n):
        self.items.append(n)
    def desempilha(self):
        if(self.vazia()):
            raise(Exception('Pilha vazia')) 
        else:
            return self.items.pop()
    def imprime(self):
        print("Pilha: {}".format(self.items))
