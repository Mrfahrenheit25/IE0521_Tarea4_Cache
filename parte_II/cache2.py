from math import log2, floor
import random

class cache:
    def __init__(self, cache_capacity, cache_assoc, block_size, repl_policy):
        #Escriba aquí el init de la clase

        self.total_access = 0
        self.total_misses = 0
        self.cache_capacity = int(cache_capacity)*1024
        self.cache_assoc = int(cache_assoc)
        self.block_size = int(block_size)
        self.repl_policy = repl_policy
        self.sets = int(self.cache_capacity/(self.block_size*self.cache_assoc))
        # bits para índice
        self.index_bits = (self.sets-1).bit_length()    
        # bits para offset     
        self.offset_bits = (self.block_size-1).bit_length()      

        # Comenzar buffer con tag de bloques, tags[index][way] = tag de bloque:'index', way: 'way'
        self.tags = []
        for i in range(0, self.sets):
            sets = []
            for i in range(0, self.cache_assoc):
                sets.append(None)
            self.tags.append(sets)


        # Comenzar buffer con novedad de bloques
        self.recency = []
        for i in range(0, self.sets):
            sets = []
            for i in range(0, self.cache_assoc):
                sets.append(0)
            self.recency.append(sets)

    def print_info(self):
        print("Parámetros caché:")
        if self.repl_policy == 'l':
            print("Política: LRU")
        elif self.repl_policy == 'r':
            print("Política: Random")
        print("\tCapacidad:\t\t\t"+str(self.cache_capacity)+"kB")
        print("\tAssociatividad:\t\t\t"+str(self.cache_assoc))
        print("\tTamaño de Bloque:\t\t\t"+str(self.block_size)+"B")
        print("\tPolítica de Reemplazo:\t\t\t"+str(self.repl_policy))

    def print_stats(self):
        print("Resultados de la simulación")
        print("Total accesos: "+str(self.total_access))
        print("# Cantidad total de misses: "+str(self.total_misses))
        miss_rate = (100.0*self.total_misses) / self.total_access
        print(str(miss_rate))
        
        

    def access(self, access_type, address):
        hit = False
        way = 0
        # quita bits de offset (no se necesita)
        address = address >> self.offset_bits  
        #  valor de índice del bloque
        index = address % 2**(self.index_bits) 
        # valor de tag del bloque
        tag = address >> self.index_bits  
        
        # Actualizar novedad de todos los ways del set a comparar
        for via in range(0, self.cache_assoc):
            self.recency[index][via]+=1

        # revisar si esta en la cache
        for etiqueta in self.tags[index]:
            if tag == etiqueta:
                hit = True
                # elige ruta cuando hubo hit
                way = self.tags[index].index(etiqueta)  
        # Miss
        if hit is False:
            # Politica LRU
            if (self.repl_policy == "l"):
                lru = -1
                for novedad in self.recency[index]:
                    if novedad > lru:
                        lru = novedad
                        # elige ruta del más viejo  
                        way = self.recency[index].index(novedad)      
            # Politica aleatoria
            elif (self.repl_policy == 'r'):
                way = random.randint(0, self.cache_assoc-1)
            
            # si hubo miss, actualizar tags[]
            self.tags[index][way] = tag

         # actualizar recency a más reciente
        self.recency[index][way] = 0

        self.total_access+= 1
        if hit is False:
                self.total_misses+=1
        
        return hit