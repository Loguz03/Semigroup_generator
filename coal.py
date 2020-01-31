from sem_g import *
import time
from itertools import product


class CM:
    @staticmethod
    def al_semigrupo(n_base, t_set): 
        start=time.time()        
        base=rg_base(n_base,t_set)
        S=smg_gen(base)
        end = time.time()
        S.printer()
        print("El calculo demoró:", end - start)
        return(S)  
    @staticmethod
    def n_semigrupo(n_base, t_set, n): 
        assert n >= n_base
        start=time.time()
        base=rg_base(n_base,t_set)
        S=smg_gen_n(base,n)
        while S == False:
            base=rg_base(n_base,t_set)
            S=smg_gen_n(base,n)
        end = time.time()
        S.printer()
        print("El calculo demoró:", end - start)
        return(S)
    @staticmethod
    def conmutativo(n_base, t_set): # limite 3, 5// (4,4) demora 30seg
        start=time.time()     
        cah=set()
        while True:
                base=frozenset(rg_base(n_base,t_set))
                erro_r=0
                while base in cah:
                    erro_r += 1
                    base=frozenset(rg_base(n_base,t_set))
                    if erro_r >= 1000: 
                        return False
                cah.add(base)
                if conmutativo_simple(base) == True:
                    end = time.time()
                    S=smg_gen(base)
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod
    def monoide(n_base, t_set): # limite 4, 4
        start=time.time()        
        base=rg_base(n_base,t_set)
        S=smg_gen(base)
        cah=set()
        while True:
                cah.add(S)
                base=rg_base(n_base,t_set)
                S=smg_gen(base)
                erro_r=0
                while S in cah:
                    erro_r += 1
                    base=rg_base(n_base,t_set)
                    S=smg_gen(base)
                    if erro_r >= 1000: 
                        return False
                if S.monoide() == True:
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod
    def semigrupo_regular(n_base, t_set): # limite 4, 4
        start=time.time()        
        base=rg_base(n_base,t_set)
        S=smg_gen(base)
        cah=set()
        while True:
                cah.add(S)
                base=rg_base(n_base,t_set)
                S=smg_gen(base)
                erro_r=0
                while S in cah:
                    erro_r += 1
                    base=rg_base(n_base,t_set)
                    S=smg_gen(base)
                    if erro_r >= 1000: 
                        return False
                if S.semigrupo_regular() == True:
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod
    def semigrupo_inverso(n_base, t_set): # limite 3, 4 
        start=time.time()        
        base=rg_base(n_base,t_set)
        S=smg_gen(base)
        cah=set()
        while True:
                cah.add(S)
                base=rg_base(n_base,t_set)
                S=smg_gen(base)
                erro_r=0
                while S in cah:
                    erro_r += 1
                    base=rg_base(n_base,t_set)
                    S=smg_gen(base)
                    if erro_r >= 1000: 
                        return False
                if S.semigrupo_inverso() == True:
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod
    def semigrupo_regular_no_inverso(n_base, t_set): # limite 4,4 
        start=time.time()        
        base=rg_base(n_base,t_set)
        S=smg_gen(base)
        cah=set()
        while True:
                cah.add(S)
                base=rg_base(n_base,t_set)
                S=smg_gen(base)
                erro_r=0
                while S in cah:
                    erro_r += 1
                    base=rg_base(n_base,t_set)
                    S=smg_gen(base)
                    if erro_r >= 1000: 
                        return False
                if S.semigrupo_inverso() == False and S.semigrupo_regular() == True:
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod           
    def n_conmutativo(n_base, t_set, n): # limite 3,4,6 
        start=time.time()
        cah=set()
        while True:        
                base=rg_base(n_base,t_set)
                S=smg_gen_n(base,n)
                while S == False:
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                erro_r=0
                while S in cah:
                    erro_r += 1
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    while S == False:
                        base=rg_base(n_base,t_set)
                        S=smg_gen_n(base,n)  
                    if erro_r >= 1000: 
                        return False
                cah.add(S)
                if conmutativo_simple(base):
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod           
    def n_monoide(n_base, t_set, n): # limite 3,5,7
        
        start=time.time()
        cah=set()
        while True:        
                base=rg_base(n_base,t_set)
                S=smg_gen_n(base,n)
                while S == False:
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                erro_r=0
                while S in cah:
                    erro_r += 1
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    while S == False:
                        base=rg_base(n_base,t_set)
                        S=smg_gen_n(base,n)  
                    if erro_r >= 1000: 
                        return False
                cah.add(S)
                if S.monoide():
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)   
    @staticmethod           
    def n_semigrupo_regular(n_base, t_set ,n): # limite 3,5,20 // 4,5,10 demora 30seg
        cah=set()
        cout = 0
        while True:        
                base=rg_base(n_base,t_set)
                S=smg_gen_n(base,n)
                error_b = 0
                cout += 1
                while S == False:
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    if error_b > 1000: return False
                    error_b += 1
                erro_r=0
                while S in cah:
                    erro_r += 1
                    error_b = 0
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    while S == False:
                        if error_b > 1000: return False
                        error_b += 1
                        base=rg_base(n_base,t_set)
                        S=smg_gen_n(base,n)  
                        
                    if erro_r >= 1000: 
                        return False
                cah.add(S)
                if S.semigrupo_regular():
                    print(" Objeto encontrado, analizando e imprimiendo: ")
                    S.printer()
                    print("Se analizaron", cout, "bases y", len(cah), "semigrupos.")
                    return(S)
    @staticmethod           
    def n_semigrupo_inverso(n_base, t_set, n):# limite? 4,4,8 // 2,3,5 // 2,5,10 //si t_set | n se obtienen mejores resultados comparar 4,3,6 y 4,4,6
        cah=set()
        cout = 0
        while True:        
                base=rg_base(n_base,t_set)
                S=smg_gen_n(base,n)
                error_b = 0
                cout += 1
                while S == False:
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    if error_b > 1000: return False
                    error_b += 1
                erro_r=0
                while S in cah:
                    erro_r += 1
                    error_b = 0
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    while S == False:
                        if error_b > 1000: return False
                        error_b += 1
                        base=rg_base(n_base,t_set)
                        S=smg_gen_n(base,n)  
                        
                    if erro_r >= 1000: 
                        return False
                cah.add(S)
                if S.semigrupo_inverso():
                    print(" Objeto encontrado, analizando e imprimiendo: ")
                    S.printer()
                    print("Se analizaron", cout, "bases y", len(cah), "semigrupos.")
                    return(S)   
    @staticmethod           
    def n_semigrupo_regular_no_inverso(n_base, t_set, n): # limite 3,5,20 // 4,5,10 demora 30seg
        cah=set()
        cout = 0
        while True:        
                base=rg_base(n_base,t_set)
                S=smg_gen_n(base,n)
                error_b = 0
                cout += 1
                while S == False:
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    if error_b > 1000: return False
                    error_b += 1
                erro_r=0
                while S in cah:
                    erro_r += 1
                    error_b = 0
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    while S == False:
                        if error_b > 1000: return False
                        error_b += 1
                        base=rg_base(n_base,t_set)
                        S=smg_gen_n(base,n)  
                        
                    if erro_r >= 1000: 
                        return False
                cah.add(S)
                if S.semigrupo_regular() == True and S.semigrupo_inverso() == False:
                    print(" Objeto encontrado, analizando e imprimiendo: ")
                    S.printer()
                    print("Se analizaron", cout, "bases y", len(cah), "semigrupos.")
                    return(S)
        
    @staticmethod           
    def t_semigrupo(n_base, t_set, n):
        cah=set()
        cout = 0
        while True:        
                base=rg_base(n_base,t_set)
                S=smg_gen_n(base,n)
                error_b = 0
                cout += 1
                while S == False:
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    if error_b > 1000: return False
                    error_b += 1
                erro_r=0
                while S in cah:
                    erro_r += 1
                    error_b = 0
                    base=rg_base(n_base,t_set)
                    S=smg_gen_n(base,n)
                    cout += 1
                    while S == False:
                        if error_b > 1000: return False
                        error_b += 1
                        base=rg_base(n_base,t_set)
                        S=smg_gen_n(base,n)  
                        
                    if erro_r >= 1000: 
                        return False
                cah.add(S)
                if S.monoide():
                    print(" Objeto encontrado, analizando e imprimiendo: ")
                    S.printer()
                    print("Se analizaron", cout, "bases y", len(cah), "semigrupos.")
                    return(S)



def semigrupo_regular(cardinal, inicio_base = 1):
    start =  time.time()
    for i in range(cardinal + 2):
        if i**i >= cardinal:
            inicio_Tn = i
            print(inicio_Tn)
            break
    
    for w in range(inicio_Tn, cardinal+2):
        print(w, end=' ')
        for j in range(inicio_base, cardinal+1):
            print(j, end=' ')
            S = CM.n_semigrupo_regular(j, w, cardinal)             
            if S != False:
                end = time.time()
                print ("La estructura fue generada por", j, "elementos del semigrupo total de transformaciones", w)
                print ("El calculo demoró:", end - start)
                return S
    return False

def semigrupo_inverso(cardinal, inicio_base = 1):
    start = time.time()
    for i in range(cardinal + 2):
        if i**i >= cardinal:
            inicio_Tn = i
            print(inicio_Tn)
            break
    
    for w in range(inicio_Tn, cardinal+2):
        print(w, end=' ')
        for j in range(inicio_base, cardinal+1):
            print(j, end=' ')
            S = CM.n_semigrupo_inverso(j, w, cardinal)             
            if S != False:
                end = time.time()
                print ("La estructura fue generada por", j, "elementos del semigrupo total de transformaciones", w)
                print ("El calculo demoró:", end - start)
                return S
    return False
    
def semigrupo_regular_no_inverso(cardinal, inicio_base = 1):
    start = time.time()
    for i in range(cardinal + 2):
        if i**i >= cardinal:
            inicio_Tn = i
            print(inicio_Tn)
            break
    
    for w in range(inicio_Tn, cardinal+2):
        print(w, end=' ')
        for j in range(inicio_base, cardinal+1):
            print(j, end=' ')
            S = CM.n_semigrupo_regular_no_inverso(j, w, cardinal)             
            if S != False:
                end = time.time()
                print ("La estructura fue generada por", j, "elementos del semigrupo total de transformaciones", w)
                print ("El calculo demoró:", end - start)
                return S
    return False

def semigrupo(cardinal, inicio_base = 1):
    start = time.time()
    for i in range(cardinal + 2):
        if i**i >= cardinal:
            inicio_Tn = i
            print(inicio_Tn)
            break
    
    for w in range(inicio_Tn, cardinal+2):
        print(w, end=' ')
        for j in range(inicio_base, cardinal+1):
            print(j, end=' ')
            S = CM.t_semigrupo(j, w, cardinal)             
            if S != False:
                end = time.time()
                print ("La estructura fue generada por", j, "elementos del semigrupo total de transformaciones", w)
                print ("El calculo demoró:", end - start)
                return S
    return False



