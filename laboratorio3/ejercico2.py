def calcular_gc_contenido(adn):
    # Calcula el contenido de GC de una cadena de ADN
    g_c_contenido = adn.count('G') + adn.count('C')
    return (g_c_contenido / len(adn)) * 100

def parse_fasta(fasta):
    # Procesa las cadenas en formato FASTA
    secuencias = {}
    id_actual = ""
    for linea in fasta:
        linea = linea.strip()
        if linea.startswith(">"):
            id_actual = linea[1:]  # Obtiene el ID sin el '>'
            secuencias[id_actual] = ""
        else:
            secuencias[id_actual] += linea  # Agrega la secuencia de ADN a la ID correspondiente
    return secuencias

def encontrar_gc_maximo(fasta):
    secuencias = parse_fasta(fasta)
    max_gc_id = ""
    max_gc_contenido = 0.0

    # Calcula el contenido de GC para cada secuencia
    for id, adn in secuencias.items():
        gc_contenido = calcular_gc_contenido(adn)
        if gc_contenido > max_gc_contenido:
            max_gc_id = id
            max_gc_contenido = gc_contenido
    
    return max_gc_id, max_gc_contenido

# Ejemplo de uso:
fasta = [
    ">biotype_6404",
    "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG",
    ">biotype_5959",
    "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC",
    ">biotype_0808",
    "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
]

# Encontrar el ID con el mayor contenido de GC y su porcentaje
id_max_gc, gc_contenido = encontrar_gc_maximo(fasta)
print(id_max_gc)
print(f"{gc_contenido:.6f}")
