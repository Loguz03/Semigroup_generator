# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:11:29 2020

@author: Emmanuel Jerez
"""
import l_mix
import c_magma
import time
import sem_g

def ejecutor(elet):
    element=list(elet)
    cantidad_elementos=len(element)
    ops=[]
    i=0
    random_error=0
    
    while True:
        
        if len(ops) >= cantidad_elementos**(cantidad_elementos**2):
               print("Todos los elementos ya fueron evaluados.")
               break
        else:
            i += 1
            elementos, operacion = l_mix.random_magma_generator(element)
            while operacion in ops:
                random_error += 1
                elementos, operacion = l_mix.random_magma_generator(element)            
            
            ops.append(operacion)
            M=c_magma.magma(elementos, operacion)
            M.imprimir_op()
            
            print("\n\n# # #       # # #\n")
            
            print("Asociativo:", M.asociativo())
                
            print("Unidad izquierda:", M.unidad_i())
                
            print("Unidad derecha:", M.unidad_d())
                
            print("Unidad:", M.unidad())
                
            print("Comnutativo:", M.conmutativo())
                
            print("Idempotentes:", M.idempotentes())
                
            print("Semigrupo:", M.semigrupo())
                 
            print("Semigrupo regular:", M.semigrupo_regular())
                
            print("Semigrupo inverso:", M.semigrupo_inverso())
                
            print("Monoide:", M.monoide())
                
            print("Grupo:", M.grupo())
            
            print("\n#   #   #\n")
                         
            cont=input("Evaluar un magma más? (1 = si, 0 = no): ")
            if cont != '1': 
                break
    
    
    print( "Se evaluaron", i,"magmas"," y ocurrieron", random_error, "errores de random")
    
def buscador(elet):
    element=list(elet)
    cantidad_elementos=len(element)
    ops=[]
    i=0
    random_error=0
    
    start=time.time()   
    
    while True:
        if time.time() - start > 30:
            break
        if len(ops) >= cantidad_elementos**(cantidad_elementos**2):
               print("Todos los elementos ya fueron evaluados y no se encontro el objeto deseado.")
               break
        else:
            i += 1
            elementos, operacion = l_mix.random_magma_generator(element)
            while operacion in ops:
                random_error += 1
                elementos, operacion = l_mix.random_magma_generator(element)            
            
            ops.append(operacion)
            M=c_magma.magma(elementos, operacion)
            
            if M.semigrupo_regular():
                print("\n#   #   #\n")
                M.imprimir_op()
                
                print("\n\n# # #       # # #\n")
                 
                print("Asociativo:", M.asociativo())
                    
                print("Unidad izquierda:", M.unidad_i())
                    
                print("Unidad derecha:", M.unidad_d())
                    
                print("Unidad:", M.unidad())
                    
                print("Comnutativo:", M.conmutativo())
                    
                print("Idempotentes:", M.idempotentes())
                    
                print("Semigrupo:", M.semigrupo())
                     
                print("Semigrupo regular:", M.semigrupo_regular())
                    
                print("Semigrupo inverso:", M.semigrupo_inverso())
                    
                print("Monoide:", M.monoide())
                    
                print("Grupo:", M.grupo())
                
                print("\n#   #   #\n")
                
                break
            
                          
    end=time.time()
    
    
    print("El calculo demoró", end - start, "se evaluaron", i,"magmas"," y ocurrieron", random_error, "errores objeto random")
   
    
def test():
    base=sem_g.rg_base(2,3)
    S=sem_g.smg_gen(base)
    
    compara(S)
    
def compara(S):
    SS=S.translate()
    SM=c_magma.magma(*SS)
    SM.imprimir_op()
    
    print("\n\n# # #   cm / sg  # # #\n")
                    
    print("Asociativo:", SM.asociativo())
                    
    print("Unidad izquierda:", SM.unidad_i(), end=' ')
    
    if S.unidad_i() != False:
        for w in S.unidad_i():
            print(S.e_translate(w))
    else:
        print(False)
                    
    print("Unidad derecha:", SM.unidad_d(), end=' ')
    
    if S.unidad_d() != False:
        for w in S.unidad_d():
            print(S.e_translate(w))
    else:
        print(False)
                    
    print("Unidad:", SM.unidad(), end=' ')
    if S.unidad() != False:
        print(S.e_translate(w))
    else: 
        print(False)
                    
    print("Comnutativo:", SM.conmutativo(), S.conmutativo())
                    
    print("Idempotentes:", SM.idempotentes(), end=' ')
    
    if S.idempotentes() != set():
        for w in S.idempotentes():
            print(S.e_translate(w), end=' ')
                    
    print("\nSemigrupo:", SM.semigrupo())
                     
    print("Semigrupo regular:", SM.semigrupo_regular(), S.semigrupo_regular())
                    
    print("Semigrupo inverso:", SM.semigrupo_inverso(), S.semigrupo_inverso())
                    
    print("Monoide:", SM.monoide(), S.monoide())
                    
    print("Grupo:", SM.grupo(), S.grupo())
                
    print("\n#   #   #\n")
        

def localizador(n_base, t_set):
       
    start=time.time()
    
    base=sem_g.rg_base(n_base,t_set)
    S=sem_g.smg_gen(base)
    cah=set()
    while True:
            cah.add(S)
            base=sem_g.rg_base(n_base,t_set)
            S=sem_g.smg_gen(base)
            erro_r=0
            while S in cah:
                erro_r += 1
                base=sem_g.rg_base(n_base,t_set)
                S=sem_g.smg_gen(base)
                if erro_r >= 1000: 
                    return False
            if S.semigrupo_regular() == True and S.semigrupo_inverso() == False:
                end = time.time()
                S.printer()
                print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                return(S)
            
def n_localizador(n_base, t_set, n):
    start=time.time()
    cah=set()
    while True:        
            base=sem_g.rg_base(n_base,t_set)
            S=sem_g.smg_gen_n(base,n)
            while S == False:
                base=sem_g.rg_base(n_base,t_set)
                S=sem_g.smg_gen_n(base,n)
            erro_r=0
            while S in cah:
                erro_r += 1
                base=sem_g.rg_base(n_base,t_set)
                S=sem_g.smg_gen_n(base,n)
                while S == False:
                    base=sem_g.rg_base(n_base,t_set)
                    S=sem_g.smg_gen_n(base,n)  
                if erro_r >= 1000: 
                    return False
            cah.add(S)
            if S.semigrupo_regular() == True and S.semigrupo_inverso() == True:
                end = time.time()
                S.printer()
                print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                return(S)
    

