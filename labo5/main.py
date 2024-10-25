from enum import IntEnum
import numpy as np

# Definimos los puntajes según el ejemplo
class Score(IntEnum):
    MATCH = 1       # Coincidencia (Match)
    MISMATCH = -1   # Desajuste (Mismatch)
    GAP = -2        # Gap

# Constantes para el trazado (traceback)
class Trace(IntEnum):
    STOP = 0
    LEFT = 1
    UP = 2
    DIAGONAL = 3

def smith_waterman(seq1, seq2):
    # Inicialización de matrices de puntajes y trazado
    rows, cols = len(seq1) + 1, len(seq2) + 1
    matrix = np.zeros((rows, cols), dtype=int)
    trace_matrix = np.zeros((rows, cols), dtype=int)

    max_score = 0
    max_pos = None

    # Llenado de la matriz con los puntajes
    for i in range(1, rows):
        for j in range(1, cols):
            match = Score.MATCH if seq1[i - 1] == seq2[j - 1] else Score.MISMATCH
            diagonal = matrix[i - 1, j - 1] + match
            up = matrix[i - 1, j] + Score.GAP
            left = matrix[i, j - 1] + Score.GAP

            # Escogemos el máximo puntaje (o 0 si es negativo)
            matrix[i, j] = max(0, diagonal, up, left)

            # Rastrear de dónde viene el puntaje máximo
            if matrix[i, j] == 0:
                trace_matrix[i, j] = Trace.STOP
            elif matrix[i, j] == diagonal:
                trace_matrix[i, j] = Trace.DIAGONAL
            elif matrix[i, j] == up:
                trace_matrix[i, j] = Trace.UP
            elif matrix[i, j] == left:
                trace_matrix[i, j] = Trace.LEFT

            # Guardar la posición con el puntaje máximo
            if matrix[i, j] >= max_score:
                max_score = matrix[i, j]
                max_pos = (i, j)

    # Backtracking para obtener el alineamiento
    aligned_seq1, aligned_seq2 = "", ""
    i, j = max_pos

    while trace_matrix[i, j] != Trace.STOP:
        if trace_matrix[i, j] == Trace.DIAGONAL:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1
        elif trace_matrix[i, j] == Trace.UP:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        elif trace_matrix[i, j] == Trace.LEFT:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2, max_score

if __name__ == "__main__":
    # Ejemplo de secuencias
    s = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
    t = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"

    # Ejecutar el algoritmo Smith-Waterman
    aligned_s, aligned_t, score = smith_waterman(s, t)

    # Mostrar los resultados
    print("Alineamiento Local:")
    print(f"Secuencia 1 alineada: {aligned_s}")
    print(f"Secuencia 2 alineada: {aligned_t}")
    print(f"Puntaje máximo: {score}")

