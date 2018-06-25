#!/usr/bin/env python
__author__      = "Leandro de Campos"

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def imprime_sequencia(limite):
     for lim in range(limite+1):
            print fibonacci(lim),
