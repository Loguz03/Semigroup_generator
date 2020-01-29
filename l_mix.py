# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:20:15 2020

@author: Emmanuel Jerez
"""

import random

def random_magma_generator(elementos):
    elementos=list(elementos)
    n=len(elementos)
    op=[]
    for _ in range(n):
        rest=random.choices(elementos, k=n)
        op.append(rest)
    return elementos, op
        
def printer(matrix, elementos):    
    print("•",end='\t')
    for e in elementos:
        print(e, end='\t')
    for y in elementos:
        print('\n')
        print(y, end='\t')
        pos=elementos.index(y)
        for w in matrix[pos]:
            print(w, end='\t')
