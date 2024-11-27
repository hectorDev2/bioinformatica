import numpy as np
import itertools
import math
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def cargar_datos(ruta_archivo):
    with open(ruta_archivo, 'r') as f:
        lineas = f.readlines()
    
    dimensiones = tuple(map(int, lineas[0].strip().replace(',', ' ').split()))
    matriz = np.array([list(map(int, linea.strip().split())) for linea in lineas[1:]])
    return matriz

def calcular_informacion_mutua(matriz, target, predictores):
    """Calcular información mutua entre genes predictores y gen objetivo."""
    filas, _ = matriz.shape
    
    # Contar frecuencias
    freq_conjunta = {}
    freq_target = {0: 0, 1: 0}
    freq_predictores = {}
    
    for fila in matriz:
        estado_target = fila[target]
        estado_predictores = tuple(fila[p] for p in predictores)
        
        # Frecuencia de estados del gen objetivo
        freq_target[estado_target] += 1
        
        # Frecuencia conjunta
        freq_conjunta.setdefault(estado_predictores, {0: 0, 1: 0})
        freq_conjunta[estado_predictores][estado_target] += 1
        
        # Frecuencia de los predictores
        freq_predictores.setdefault(estado_predictores, 0)
        freq_predictores[estado_predictores] += 1
    
    # Calcular información mutua
    im_total = 0
    for estado_pred, conteo_pred in freq_predictores.items():
        prob_pred = conteo_pred / filas
        
        for estado_target in [0, 1]:
            conteo_conj = freq_conjunta[estado_pred].get(estado_target, 0)
            prob_conj = conteo_conj / filas
            prob_target = freq_target[estado_target] / filas
            
            if prob_conj > 0:
                im = prob_conj * math.log2(prob_conj / (prob_pred * prob_target))
                im_total += im
    
    return abs(im_total)

def inferir_red_sfs(matriz, max_dim=3):
    filas, columnas = matriz.shape
    red_inferida = {}
    
    for target in range(columnas):
        # Búsqueda SFS (Secuencial hacia adelante)
        predictores_seleccionados = []
        candidatos = [gen for gen in range(columnas) if gen != target]
        
        while len(predictores_seleccionados) < max_dim and candidatos:
            mejor_im = float('-inf')
            mejor_predictor = None
            
            for predictor in candidatos:
                predictores_prueba = predictores_seleccionados + [predictor]
                im = calcular_informacion_mutua(matriz, target, predictores_prueba)
                
                if im > mejor_im:
                    mejor_im = im
                    mejor_predictor = predictor
            
            if mejor_predictor is not None:
                predictores_seleccionados.append(mejor_predictor)
                candidatos.remove(mejor_predictor)
            else:
                break
        
        red_inferida[target] = tuple(predictores_seleccionados)
        logger.info(f"Gen {target}: Predictores -> {red_inferida[target]}")
    
    return red_inferida

def main(ruta_archivo):
    try:
        matriz = cargar_datos(ruta_archivo)
        red_inferida = inferir_red_sfs(matriz)
        
        print("\nRed Booleana Inferida (SFS):")
        for gen, predictores in red_inferida.items():
            print(f"Gen {gen}: Predictores -> {predictores}")
    
    except Exception as e:
        logger.error(f"Error en inferencia de red: {e}")

if __name__ == "__main__":
    ruta_archivo = "datos.txt"
    main(ruta_archivo)
