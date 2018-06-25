#!/usr/bin/env python
__author__      = "Leandro de Campos"

class Fila:
    def __init__(self):
        self.items = []
    def inserir(self,n):
        self.items.append(n)
    def remover(self):
        if not self.vazia():
            return self.items.pop(0)
    def tamanho(self):
        return len(self.items)
    def vazia(self):
        return (self.items == [])
    def imprimir(self):
        print("Fila: {}".format(self.items))
