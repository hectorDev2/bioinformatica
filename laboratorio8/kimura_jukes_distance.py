import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

def distancia_jukes_cantor(seq1, seq2):
    """Calcula la distancia JC69 entre dos secuencias con manejo de precisión."""
    p = sum(c1 != c2 for c1, c2 in zip(seq1, seq2)) / len(seq1)

    # Asegurar que el argumento del logaritmo esté en un rango válido
    if p >= 0.75:
        raise ValueError("JC69 no es válido con p >= 0.75 (saturación de mutaciones)")
    
    # Evitar log(0) o log de valores muy cercanos a 1
    try:
        return -3/4 * np.log(max(1e-10, 1 - (4/3) * p))
    except ValueError:
        return float('inf')  # Si hay demasiadas mutaciones (caso teórico extremo)

def distancia_kimura(seq1, seq2):
    """Calcula la distancia K2P entre dos secuencias."""
    transiciones, transversiones = transiciones_transversiones(seq1, seq2)
    p = transiciones / len(seq1)
    q = transversiones / len(seq1)

    try:
        return -0.5 * np.log(max(1e-10, 1 - 2*p - q)) - 0.25 * np.log(max(1e-10, 1 - 2*q))
    except ValueError:
        return float('inf')

def transiciones_transversiones(seq1, seq2):
    """Cuenta transiciones y transversiones entre dos secuencias."""
    transiciones = 0
    transversiones = 0
    purinas = {'A', 'G'}
    pirimidinas = {'C', 'T'}

    for a, b in zip(seq1, seq2):
        if a != b:
            if (a in purinas and b in purinas) or (a in pirimidinas and b in pirimidinas):
                transiciones += 1
            else:
                transversiones += 1

    return transiciones, transversiones

# Prueba rápida para evitar errores de saturación o log(0)
secuencias = ["AGCT", "AGGT", "ACCT", "TCCT"]

print("Distancia JC69:", distancia_jukes_cantor(secuencias[0], secuencias[1]))
print("Distancia K2P:", distancia_kimura(secuencias[0], secuencias[1]))
