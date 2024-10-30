from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np
import matplotlib.pyplot as plt

def distancia_hamming(seq1, seq2):
    """Calcula la distancia de Hamming entre dos secuencias de igual longitud."""
    if len(seq1) != len(seq2):
        raise ValueError("Las secuencias deben tener la misma longitud")
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

def generar_matriz_distancias(secuencias):
    """Genera una matriz de distancias a partir de las secuencias."""
    n = len(secuencias)
    matriz = np.zeros((n, n))

    # Rellenar la matriz de distancias (sólo parte superior porque es simétrica)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i, j] = distancia_hamming(secuencias[i], secuencias[j])
            matriz[j, i] = matriz[i, j]  # Simetría

    return matriz

def upgma(secuencias):
    """Aplica el método UPGMA para generar un árbol filogenético."""
    # Generar la matriz de distancias
    matriz = generar_matriz_distancias(secuencias)

    # scipy espera la matriz en formato 'condensed' (parte superior sin duplicar)
    matriz_condensed = matriz[np.triu_indices(len(secuencias), k=1)]

    # Aplicar UPGMA usando el método 'average' (promedio)
    arbol = linkage(matriz_condensed, method='average')

    return arbol

def dibujar_arbol_filogenetico(arbol, etiquetas):
    """Dibuja el  árbol generado por UPGMA."""
    plt.figure(figsize=(10, 5))
    dendrogram(arbol, labels=etiquetas, leaf_rotation=90)
    plt.title("Árbol filogenético (UPGMA)")
    plt.xlabel("Secuencias")
    plt.ylabel("Distancia")
    plt.show()

# Ejemplo de uso
secuencias = [
    "AGCT",
    "AGGT",
    "ACCT",
    "TCCT"
]

# Generar el árbol UPGMA
arbol = upgma(secuencias)

# Dibujar el dendrograma
dibujar_arbol_filogenetico(arbol, etiquetas=[f"Seq{i+1}" for i in range(len(secuencias))])
