import numpy as np
from utils.paintMatrix import print_matrix_with_pandas  # Importa la función desde el módulo

# Función para obtener el puntaje
def get_score(a, b):
    """Devuelve el puntaje para el par de caracteres."""
    if a == b:
        return 1  # Match
    elif a == '-' or b == '-':
        return -1  # Gap
    else:
        return -1  # Mismatch

# Inicializa la matriz de puntuación
def initialize_matrix(seq1, seq2, gap_penalty):
    n = len(seq1)
    m = len(seq2)
    score_matrix = np.zeros((n + 1, m + 1))

    # Inicializa la primera fila y columna con penalización de hueco
    for i in range(n + 1):
        score_matrix[i][0] = gap_penalty * i
    for j in range(m + 1):
        score_matrix[0][j] = gap_penalty * j

    return score_matrix

# Llena la matriz de puntuación con los puntajes
def fill_matrix(seq1, seq2, score_matrix, gap_penalty):
    n = len(seq1)
    m = len(seq2)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + get_score(seq1[i - 1], seq2[j - 1])
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty

            score_matrix[i][j] = max(match, delete, insert)

# Retrocede para encontrar el mejor alineamiento
def backtrack(seq1, seq2, score_matrix, gap_penalty):
    alignment_a = []
    alignment_b = []
    i, j = len(seq1), len(seq2)

    while i > 0 and j > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i - 1][j - 1]
        up_score = score_matrix[i - 1][j]
        left_score = score_matrix[i][j - 1]

        # Caso 1: Diagonal (Match o Mismatch)
        if current_score == diagonal_score + (1 if seq1[i - 1] == seq2[j - 1] else -1):
            alignment_a.append(seq1[i - 1])
            alignment_b.append(seq2[j - 1])
            i -= 1
            j -= 1
        # Caso 2: Arriba (Gap en la secuencia 2)
        elif current_score == up_score + gap_penalty:
            alignment_a.append(seq1[i - 1])
            alignment_b.append('-')
            i -= 1
        # Caso 3: Izquierda (Gap en la secuencia 1)
        else:
            alignment_a.append('-')
            alignment_b.append(seq2[j - 1])
            j -= 1

    # Manejo de gaps al final si quedan
    while i > 0:
        alignment_a.append(seq1[i - 1])
        alignment_b.append('-')
        i -= 1

    while j > 0:
        alignment_a.append('-')
        alignment_b.append(seq2[j - 1])
        j -= 1

    # Las alineaciones están al revés, debemos revertirlas
    return ''.join(reversed(alignment_a)), ''.join(reversed(alignment_b))

# Función principal del algoritmo de Needleman-Wunsch
def needleman_wunsch(seq1, seq2, gap_penalty):
    score_matrix = initialize_matrix(seq1, seq2, gap_penalty)
    fill_matrix(seq1, seq2, score_matrix, gap_penalty)
    return backtrack(seq1, seq2, score_matrix,gap_penalty), score_matrix

# Parámetros de ejemplo
gap_penalty = -1



seq1 = "GATTACA"
seq2 = "GCATGCG"

# Ejecuta el algoritmo
alignment, score_matrix = needleman_wunsch(seq1, seq2, gap_penalty)

# Imprimir alineamiento
print("Alineamiento:")
print(alignment[0])
print(alignment[1])

# Mostrar la matriz de puntuación
print("\nMatriz de puntuación:")

print_matrix_with_pandas(score_matrix, seq1, seq2)
