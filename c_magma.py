# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:11:58 2020

@author: Emmanuel Jerez
"""

class magma:
    def __init__(self, elementos = [], operacion = []):
        self.elementos=list(elementos)
        self.operacion=operacion
                  
                              
    def d_operacion(self):
        n=len(self.elementos)
        op=[]
        for i in range(n):
            for j in range(n):
                r=input("Digite el producto " + str(self.elementos[i]) + str(self.elementos[j])+ '= ')
                while r not in self.elementos:
                    r=input("Símbolo no definido, digite el producto " + str(self.elementos[i]) + str(self.elementos[j]) + '= ')
                op.append([self.elementos[i],self.elementos[j],r])
        return op
    
    def op(self, a, b):
        assert a in self.elementos and b in self.elementos
        i=self.elementos.index(a)
        j=self.elementos.index(b)
        return self.operacion[i][j]
            
    def asociativo(self):
        for a in self.elementos:
            for b in self.elementos:
                for c in self.elementos:
                    if self.op(self.op(a,b),c) != self.op(a, self.op(b,c)):
                        return False
        return True
    
    def conmutativo(self):
        for a in self.elementos:
            for b in self.elementos:
                if self.op(a,b) != self.op(b,a):
                    return False
        return True
    
    def unidad_i(self):
        ui=[]
        for e in self.elementos:
            neu = True
            for a in self.elementos:
                if self.op(e,a) != a:
                    neu = False
                    break
            if neu == True: ui.append(e)
        if ui == []:
            return False
        else:
            return ui
    
    def unidad_d(self):
        ud=[]
        for e in self.elementos:
            neu = True
            for a in self.elementos:
                if self.op(a,e) != a:
                    neu = False
                    break
            if neu == True: ud.append(e)
        if ud== []:
            return False
        else:
            return ud
        
    def unidad(self):
        if self.unidad_d() == False or self.unidad_i() == False:
            return False
        else:
            for u in self.unidad_d():
                if u in self.unidad_i():
                    return u
    
    def inverso_i(self, g):
        assert g in self.elementos
        if self.unidad == False:
            return False
        else:
            i_i=[]
            e=self.unidad()
            for h in self.elementos:
                if self.op(h,g)==e:
                    i_i.append(h)
            if i_i == []:
                return False
            else: 
                return i_i
    
    def inverso_d(self, g):
        assert g in self.elementos
        if self.unidad == False:
            return False
        else:
            i_d=[]
            e=self.unidad()
            for h in self.elementos:
                if self.op(g,h)==e:
                    i_d.append(h)
            if i_d == []:
                return False
            else: 
                return i_d
        
    def inverso(self, g):
        assert g in self.elementos
        if self.unidad == False or self.inverso_d(g) == False or self.inverso_i(g) == False:
            return False
        else:
            i_d = self.inverso_d(g)
            i_i = self.inverso_i(g)
            for w in i_d:
                if w in i_i:
                    return w
            return False
    
    def idempotentes(self):
        EG=[]
        for e in self.elementos:
            if self.op(e,e)==e:
                EG.append(e)
        if EG == []:
            return False
        else:
            return EG
    
    def semigrupo(self):
        if self.asociativo() != False:
            return True
        else:
            return False
    
    def monoide(self):
        if self.semigrupo() and self.unidad() != False:
            return True
        else:
            return False
    
    def grupo(self):
        if self.monoide:
            for g in self.elementos:
                if self.inverso(g) == False:
                        return False
            return True
        else:
            return False
        
    def inverso_regular(self, g):
        inv_re = []
        if self.asociativo():
            for h in self.elementos:
                if self.op(self.op(g,h),g) == g and self.op(self.op(h,g),h) == h:
                    inv_re.append(h)
            if inv_re == []:
                return False
            else:
                return inv_re
        else:
            return False
        
    def semigrupo_regular(self):
        for g in self.elementos:
            if self.inverso_regular(g) == False:
                return False      
        return True
    
    def semigrupo_inverso(self):
        if self.semigrupo_regular():
            for g in self.elementos:
                if len(self.inverso_regular(g)) != 1:
                    return False
            return True
        else:
            return False
        
    def imprimir_op(self):
        print("•",end='\t')
        for e in self.elementos:
            print(e, end='\t')
        for y in self.elementos:
            print('\n')
            print(y, end='\t')
            pos=self.elementos.index(y)
            for w in self.operacion[pos]:
                print(w, end='\t')
            
    def magma_isomorfo(self, other):
        if self.elementos == other.elementos:
            return 1
    
