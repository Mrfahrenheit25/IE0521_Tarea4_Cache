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
        self.sets = int(self.cache_capacity/(block_size*cache_assoc))
        # bits para índice
        self.index_bits = (self.sets-1).bit_length()    
        # bits para offset     
        self.offset_bits = (block_size-1).bit_length()      

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
        print("Total accesos: ")
        print(self.total_access)
        print("# Cantidad total de misses: ")
        print(self.total_misses)
        miss_rate = (100.0*self.total_misses) / self.total_access
        print("Missrate: ")
        print(str(miss_rate))
        
    """
    Accede a la cache para verificar si una dirección está presente y maneja los hits y misses.

    Esta función simula el acceso a un caché multinivel para una dirección de memoria específica,
    verificando si la dirección resulta en un hit o miss, y actualiza el estado del caché
    de acuerdo con la política de reemplazo especificada.

    Args:
        access_type (str): Tipo de acceso; puede ser 'read' o 'write'.
        address (int): Dirección de memoria que se está accediendo.

    Returns:
        Nothing.

    Detalles:
        - Se desplaza la dirección para remover los bits de offset.
        - Calcula el índice del set y el tag basado en los bits restantes.
        - Se incrementa la recencia de todos los elementos en el set.
        - Verifica la presencia del tag en el caché:
          - Si está presente, se actualiza la recencia a más reciente.
          - Si no está, se selecciona un way basado en la política de reemplazo (LRU o aleatoria),
            se actualizan los tags y la recencia.
        - Contabiliza los accesos totales y los misses.
    """
    def access(self, access_type, address):
        hit = False
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
        
