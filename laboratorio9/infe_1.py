import itertools
import numpy as np
import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cargar_datos(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        lineas = f.readlines()
    
    dimensiones = tuple(map(int, lineas[0].strip().replace(',', ' ').split()))
    filas, columnas = dimensiones
    
    matriz = np.array([list(map(int, linea.strip().split())) for linea in lineas[1:]])
    return matriz

def calcular_error_absoluto(matriz, target, predictores):
    """Calcular error absoluto según la guía de laboratorio."""
    f_total = {}
    
    # Contar frecuencias para cada combinación de predictores
    for fila in matriz:
        estado_predictores = tuple(fila[p] for p in predictores)
        estado_target = fila[target]
        
        f_total.setdefault(estado_predictores, {0: 0, 1: 0})
        f_total[estado_predictores][estado_target] += 1
    
    # Calcular suma de errores absolutos
    error_total = 0
    for combinacion, frecuencias in f_total.items():
        error_total += abs(frecuencias[0] - frecuencias[1])
    
    return error_total

def inferir_red_booleana(matriz, max_dim=3):
    filas, columnas = matriz.shape
    red_inferida = {}
    
    for target in range(columnas):
        mejor_error = float('inf')
        mejor_predictores = None
        candidatos_empatados = []
        
        # Explorar combinaciones de predictores
        for dim in range(1, max_dim + 1):
            for predictores in itertools.combinations(
                [gen for gen in range(columnas) if gen != target], 
                dim
            ):
                error = calcular_error_absoluto(matriz, target, predictores)
                
                # Criterios de selección según laboratorio
                if error < mejor_error:
                    mejor_error = error
                    mejor_predictores = predictores
                    candidatos_empatados = [predictores]
                elif error == mejor_error:
                    if len(predictores) < len(mejor_predictores or []):
                        mejor_predictores = predictores
                        candidatos_empatados = [predictores]
                    elif len(predictores) == len(mejor_predictores or []):
                        candidatos_empatados.append(predictores)
        
        # Selección aleatoria en caso de empate final
        if candidatos_empatados:
            mejor_predictores = random.choice(candidatos_empatados)
        
        red_inferida[target] = mejor_predictores or ()
        logger.info(f"Gen {target}: Predictores -> {mejor_predictores}")
    
    return red_inferida

def main(ruta_archivo):
    try:
        matriz = cargar_datos(ruta_archivo)
        red_inferida = inferir_red_booleana(matriz)
        
        print("\nRed Booleana Inferida:")
        for gen, predictores in red_inferida.items():
            print(f"Gen {gen}: Predictores -> {predictores}")
    
    except Exception as e:
        logger.error(f"Error en inferencia de red: {e}")

if __name__ == "__main__":
    ruta_archivo = "datos.txt"
    main(ruta_archivo)