from c_magma import *
from l_mix import *
from sem_g import *
import time

class RM:
    @staticmethod
    def magma_aleatorio(elet):
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
                elementos, operacion = random_magma_generator(element)
                while operacion in ops:
                    random_error += 1
                    elementos, operacion = random_magma_generator(element)            
                
                ops.append(operacion)
                M=magma(elementos, operacion)
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
    @staticmethod
    def conmutativo(elet): # limite de 4 elementos
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
                elementos, operacion = random_magma_generator(element)
                while operacion in ops:
                    random_error += 1
                    elementos, operacion = random_magma_generator(element)            
                
                ops.append(operacion)
                M=magma(elementos, operacion)
                
                if M.conmutativo():
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
    @staticmethod
    def asociativo(elet): # limite de 3 elementos
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
                elementos, operacion = random_magma_generator(element)
                while operacion in ops:
                    random_error += 1
                    elementos, operacion = random_magma_generator(element)            
                
                ops.append(operacion)
                M=magma(elementos, operacion)
                
                if M.asociativo():
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
    @staticmethod
    def semigrupo_regular(elet): # limite de 3 elementos
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
                elementos, operacion = random_magma_generator(element)
                while operacion in ops:
                    random_error += 1
                    elementos, operacion = random_magma_generator(element)            
                
                ops.append(operacion)
                M=magma(elementos, operacion)
                
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
    @staticmethod
    def semigrupo_inverso(elet): # limite de 3 elementos
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
                elementos, operacion = random_magma_generator(element)
                while operacion in ops:
                    random_error += 1
                    elementos, operacion = random_magma_generator(element)            
                
                ops.append(operacion)
                M=magma(elementos, operacion)
                
                if M.semigrupo_inverso():
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
    @staticmethod
    def semigrupo_regular_no_inverso(elet): # limite de 3 elementos
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
                elementos, operacion = random_magma_generator(element)
                while operacion in ops:
                    random_error += 1
                    elementos, operacion = random_magma_generator(element)            
                
                ops.append(operacion)
                M=magma(elementos, operacion)
                
                if M.semigrupo_regular() and not M.semigrupo_inverso():
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
    def n_semigrupo_regular(n_base, t_set, n): # limite 3,5,20 // 4,5,10 demora 30seg
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
                if S.semigrupo_regular():
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
    @staticmethod           
    def n_semigrupo_inverso(n_base, t_set, n):# limite? 4,4,8 // 2,3,5 // 2,5,10 //si t_set se obtienen mejores resultados comparar 4,3,6 y 4,4,6
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
                if S.semigrupo_inverso():
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)   
    @staticmethod           
    def n_semigrupo_regular_no_inverso(n_base, t_set, n): # limite 3,5,20 // 4,5,10 demora 30seg
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
                if S.semigrupo_regular() == True and S.semigrupo_inverso() == False:
                    end = time.time()
                    S.printer()
                    print("El calculo demoró:", end - start, "y se analizaron", len(cah), "semigrupos.")
                    return(S)
        

CM.n_semigrupo_inverso(2,3,5)



