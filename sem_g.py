# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 12:51:02 2020

@author: Emmanuel Jerez
"""

import random
from itertools import product



class tran:
    
    @staticmethod
    def f_domain(rule):
        domain=set()
        for w in rule:
            domain.add(w[0])
        return domain
    
    @staticmethod
    def f_image(rule):
        image=set()
        for w in rule:
            image.add(w[1])
        return image
    
    @staticmethod
    def rg_tran(n):
        tr=set()
        for i in range(n):
            tr.add((i, random.choice(range(n))))
        return tran(tr)

    @staticmethod
    def TS_base(n):
        pass
    



    __cache = {}
    def __new__(cls, rule): # si dos transformaciones tienen la misma regla, son almacenadas en el mismo espacio de memoria, es decir, son el mismo objeto
        # assert tran.f_image(rule) <= tran.f_domain(rule) and len(rule) == len(tran.f_domain(rule))
        rule=frozenset(rule)
        if rule in tran.__cache:
            return tran.__cache[rule]
        else:
            o = object.__new__(cls)
            o.rule = rule
            tran.__cache[rule] = o
            return o
        
    def __init__(self, rule):
        self.op = dict(rule)
        self.domain = self.c_domain()
        self.image = self.c_image()
   
    def __lt__(self, other):  
        return self.rule < other.rule
     
           
    def c_domain(self):
        return set(self.op.keys())
    
    def c_image(self):
        return set(self.op.values())

    @classmethod   
    def com(cls, A, B):
        # assert A.domain == B.domain
        n_rule=set()
        for x in A.domain:
            y=A.op[B.op[x]]
            n_rule.add((x,y))
        return tran(n_rule)
    
    @classmethod
    def c_asoc(cls, A,B,C):
        # assert C.domain == B.domain and B.domain == A.domain
        if tran.com(tran.com(A,B),C) == tran.com(A, tran.com(B,C)):
            return True
        else:
            return False
      
    
class semigroup:
        
    __cache = {}
    def __new__(cls, elements):
        elements=frozenset(elements)
        if elements in semigroup.__cache:
            return semigroup.__cache[elements]
        else:
            smg=object.__new__(cls)
            semigroup.__cache[elements]=smg
            return smg
        
 
    
    def __init__(self, elements):
        self.elements = elements
        
    def checker_s(self):
        for x in self.elements:
            for y in self.elements:
                if tran.com(x,y) not in self.elements:
                    return False
        return True
        
    
    def conmutativo(self):
        for A in self.elements:
            for B in self.elements:
                if tran.com(A, B) != tran.com(B, A):
                    return False
        return True
    
    def unidad_i(self):
        ui=set()
        for E in self.elements:
            neu = True
            for T in self.elements:
                if tran.com(E,T) != T:
                    neu = False
                    break
            if neu == True: ui.add(E)
        if ui == set():
            return False
        else:
            return ui
        
        
    def unidad_d(self):
        ui=set()
        for E in self.elements:
            neu = True
            for T in self.elements:
                if tran.com(T,E) != T:
                    neu = False
                    break
            if neu == True: ui.add(E)
        if ui == set():
            return False
        else:
            return ui

    def unidad(self):
        A = self.unidad_d()
        B = self.unidad_i()
        if A == False or B == False:
            return False
        else:
            (u,) = set.intersection(A, B)
            return u 
        
    def inverso_i(self, g):
        # assert g in self.elements
        if self.unidad == False:
            return False
        else:
            i_i=set()
            e=self.unidad()
            for h in self.elements:
                if tran.com(h,g)==e:
                    i_i.add(h)
            if i_i == set():
                return False
            else: 
                return i_i
            
    def inverso_d(self, g):
        assert g in self.elements
        if self.unidad == False:
            return False
        else:
            i_i=set()
            e=self.unidad()
            for h in self.elements:
                if tran.com(g,h)==e:
                    i_i.add(h)
            if i_i == set():
                return False
            else: 
                return i_i
            
                
    def inverso(self, g):
        assert g in self.elements
        if self.unidad == False or self.inverso_d(g) == False or self.inverso_i(g) == False:
            return False
        else:
            i_d = self.inverso_d(g)
            i_i = self.inverso_i(g)
            W=set.intersection(i_d, i_i)
            if W == set():
                return False
            else:
                (w,) = set.intersection(i_d, i_i)
                return w
            
    def idempotentes(self):
        EG=set()
        for e in self.elements:
            if tran.com(e,e)==e:
                EG.add(e)
        if EG == set():
            return False
        else:
            return EG


    def monoide(self):
        if self.unidad() != False:
            return True
        else:
            return False
    
    def grupo(self):
        if self.monoide:
            for g in self.elements:
                if self.inverso(g) == False:
                        return False
            return True
        else:
            return False
        
    def inverso_regular(self, g):
        inv_re = set()
        for h in self.elements:
            if tran.com(tran.com(g,h),g) == g and tran.com(tran.com(h,g),h) == h:
                    inv_re.add(h)
        if inv_re == set():
            return False
        else:            
            return inv_re
        
    def semigrupo_regular(self):
        for g in self.elements:
            if self.inverso_regular(g) == False:
                return False      
        return True
    
    def semigrupo_inverso(self):
            for g in self.elements:
                i_r = self.inverso_regular(g)
                if i_r == False:
                    return False
                else:
                    if len(i_r) != 1:
                        return False
            return True
    
    def translate(self):
        lista=list(self.elements)
        lista.sort()
        n=len(lista)
        table=[]
        for i in range(n):
            row=[]
            for j in range(n):
                P=tran.com(lista[i], lista[j])
                row.append(str(lista.index(P)))
            table.append(row)
        return list(map(str,range(n))), table
       
    def e_translate(self, T):
        lista=list(self.elements)
        lista.sort()
        im = lista.index(T)
        return im
     
    def r_e_translate(self, n):
        lista=list(self.elements)
        lista.sort() 
        return(lista[n])
    
    def t_op(self, a, b):
        x=self.r_e_translate(a)
        y=self.r_e_translate(b)
        z=tran.com(x,y)
        return self.e_translate(z)

    def smg_print(self):
        elementos, operacion = self.translate()
        print("•",end='\t')
        for e in elementos:
            print(e, end='\t')
        for y in elementos:
            print('\n')
            print(y, end='\t')
            pos=elementos.index(y)
            for w in operacion[pos]:
                print(w, end='\t')
                
    def printer(self):
        self.smg_print()
        print("\n\n# # #   sg   # # #\n")
                            
        print("Unidad izquierda:", end=' ')
            
        if self.unidad_i() != False:
            for w in self.unidad_i():
                print(self.e_translate(w), end='')
        else:
            print(False, end=' ')
            
        print("\nUnidad derecha:", end=' ')
            
        if self.unidad_d() != False:
            for w in self.unidad_d():
                print(self.e_translate(w), end=' ')
        else:
            print(False, end='')
                            
        print("\nUnidad:", end=' ')
        if self.unidad() != False:
            print(self.e_translate(w))
        else: 
            print(False)
                            
        print("Comnutativo:", self.conmutativo())
                            
        print("Idempotentes:",  end=' ')
            
        if self.idempotentes() != set():
            for w in self.idempotentes():
                print(self.e_translate(w), end=' ')
                             
        print("\nSemigrupo regular:", self.semigrupo_regular())
                            
        print("Semigrupo inverso:", self.semigrupo_inverso())
                            
        print("Monoide:", self.monoide())
                            
        print("Grupo:", self.grupo())
                        
        print("\n#   #   #\n")

    def fun_printer(self):
        for w in self.elements:
            print(w.op)

    @staticmethod
    def TS(n):
        list(range(n))
        seto = [ list(range(n))]*n
        cartesian = product(*seto)
        elements=set()
        for W in cartesian:
            T=set()
            for i in range(n):
                T.add((i,W[i]))
            elements.add(tran(T))
        return semigroup(elements)

def rg_base(n, X): # n numero de funciones, X tamaño del dominio
    assert n <= X**X
    bass=set()
    while len(bass) < n:
        bass.add(tran.rg_tran(X))
    return frozenset(bass)
 
def smg_gen(base):
    smg=list(base) # es necesario que sea lista para realizar este tipo de algoritmo
    for A in smg:
        for B in base:
            C=tran.com(A,B)
            if C not in smg: smg.append(C)
    return semigroup(set(smg))

def smg_gen_n(base,n):
    if len(base)>n:
        return False
    else:
        smg=list(base)
        for A in smg:
            for B in base:
                C=tran.com(A,B)
                if C not in smg: 
                    smg.append(C)
                    if len(smg)>n: 
                        return False
        if len(smg)==n:
            return semigroup(set(smg))
        else:
            return False

def conmutativo_simple(base):
    for A in base:
        for B in base:
            if tran.com(A, B) != tran.com(B, A):
                return False
    return True










