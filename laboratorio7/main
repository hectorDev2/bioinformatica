import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple, Set, Dict
from collections import defaultdict
import random
import time

def generar_kmers_tuplas(secuencia: str, k: int) -> List[Tuple[str, ...]]:
    """
    Genera k-mers como tuplas a partir de una secuencia.
    """
    return [tuple(secuencia[i:i+k]) for i in range(len(secuencia) - k + 1)]

def grafo_de_bruijn_tuplas(kmers_tuplas: List[Tuple[str, ...]]) -> nx.MultiDiGraph:
    """
    Construye el grafo de Bruijn a partir de k-mers representados como tuplas.
    """
    G = nx.MultiDiGraph()
    
    for kmer in kmers_tuplas:
        prefijo = kmer[:-1]  
        sufijo = kmer[1:]
        G.add_edge(prefijo, sufijo)
    
    return G

def encontrar_todos_caminos_eulerianos(G: nx.MultiDiGraph, 
                                     nodo_actual: Tuple[str, ...], 
                                     camino_actual: List[Tuple], 
                                     caminos: List[List[Tuple]], 
                                     num_aristas: int, 
                                     tiempo_limite: float,
                                     tiempo_inicio: float,
                                     max_caminos: int = 1000) -> bool:
    """
    Encuentra caminos eulerianos con límite de tiempo y número máximo de caminos.
    """
    # Verificar límite de tiempo
    if time.time() - tiempo_inicio > tiempo_limite:
        return True
        
    if len(camino_actual) == num_aristas:
        caminos.append(camino_actual[:])
        if len(caminos) >= max_caminos:
            return True
        return False
    
    # Obtener las aristas disponibles y mezclarlas aleatoriamente
    aristas_disponibles = list(G.edges(nodo_actual, keys=True))
    random.shuffle(aristas_disponibles)
    
    for _, destino, clave in aristas_disponibles:
        G.remove_edge(nodo_actual, destino, key=clave)
        camino_actual.append((nodo_actual, destino))
        
        if encontrar_todos_caminos_eulerianos(G, destino, camino_actual, caminos, 
                                            num_aristas, tiempo_limite, tiempo_inicio, max_caminos):
            return True
        
        camino_actual.pop()
        G.add_edge(nodo_actual, destino, key=clave)
    
    return False

def obtener_caminos_eulerianos(G: nx.MultiDiGraph, 
                              tiempo_limite: float = 10.0,
                              max_caminos: int = 1000) -> List[List[Tuple]]:
    """
    Obtiene caminos eulerianos con límites de tiempo y cantidad.
    """
    caminos = []
    if nx.has_eulerian_path(G):
        nodos_grado_impar = [n for n in G.nodes() if G.in_degree(n) != G.out_degree(n)]
        nodo_inicio = nodos_grado_impar[0] if nodos_grado_impar else list(G.nodes())[0]
        num_aristas = G.number_of_edges()
        
        tiempo_inicio = time.time()
        encontrar_todos_caminos_eulerianos(G.copy(), nodo_inicio, [], caminos, 
                                         num_aristas, tiempo_limite, tiempo_inicio, max_caminos)
    
    return caminos

def reconstruir_secuencia(camino: List[Tuple]) -> str:
    """
    Reconstruye la secuencia a partir de un camino euleriano.
    """
    if not camino:
        return ""
    
    secuencia = ''.join(camino[0][0])
    for _, nodo in camino:
        secuencia += nodo[-1]
    return secuencia

def analizar_caminos(caminos: List[List[Tuple]]) -> Dict:
    """
    Analiza los caminos encontrados y genera estadísticas.
    """
    analisis = {
        'total_caminos': len(caminos),
        'secuencias_unicas': set(),
        'frecuencias_nucleotidos': defaultdict(int),
        'longitudes': set()
    }
    
    for camino in caminos:
        secuencia = reconstruir_secuencia(camino)
        analisis['secuencias_unicas'].add(secuencia)
        analisis['longitudes'].add(len(secuencia))
        
        for nucleotido in secuencia:
            analisis['frecuencias_nucleotidos'][nucleotido] += 1
    
    return analisis

def visualizar_grafo_con_peso(G: nx.MultiDiGraph):
    """
    Visualiza el grafo con pesos en las aristas basados en la frecuencia.
    """
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    # Calcular pesos de aristas
    edge_weights = defaultdict(int)
    for u, v in G.edges():
        edge_weights[(u, v)] += 1
    
    # Normalizar pesos para el grosor de las aristas
    max_weight = max(edge_weights.values())
    edge_widths = [2 * edge_weights[(u, v)] / max_weight for u, v in G.edges()]
    
    # Dibujar el grafo
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000)
    nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='gray', 
                          arrowsize=20, arrowstyle='->')
    
    # Añadir etiquetas
    labels = {node: ''.join(node) for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')
    
    plt.title("Grafo de Bruijn con pesos")
    plt.axis('off')
    plt.show()

def analizar_secuencia_adn(secuencia: str, k: int, 
                          tiempo_limite: float = 10.0,
                          max_caminos: int = 1000):
    """
    Analiza una secuencia de ADN usando el grafo de Bruijn con límites ajustables.
    """
    print(f"Analizando secuencia de longitud {len(secuencia)} con k={k}")
    
    # Generar k-mers y construir grafo
    kmers_tuplas = generar_kmers_tuplas(secuencia, k)
    print(f"Número de {k}-mers generados: {len(kmers_tuplas)}")
    
    G = grafo_de_bruijn_tuplas(kmers_tuplas)
    print(f"Número de nodos: {G.number_of_nodes()}")
    print(f"Número de aristas: {G.number_of_edges()}")
    
    # Visualizar grafo
    print("\nVisualizando grafo de Bruijn...")
    visualizar_grafo_con_peso(G)
    
    # Encontrar caminos
    print(f"\nBuscando caminos eulerianos (límite de tiempo: {tiempo_limite}s, máx caminos: {max_caminos})...")
    tiempo_inicio = time.time()
    caminos = obtener_caminos_eulerianos(G, tiempo_limite, max_caminos)
    tiempo_total = time.time() - tiempo_inicio
    
    # Analizar resultados
    if caminos:
        analisis = analizar_caminos(caminos)
        print(f"\nResultados del análisis:")
        print(f"Tiempo de búsqueda: {tiempo_total:.2f} segundos")
        print(f"Total de caminos encontrados: {analisis['total_caminos']}")
        print(f"Número de secuencias únicas: {len(analisis['secuencias_unicas'])}")
        print(f"Longitudes de secuencias encontradas: {sorted(analisis['longitudes'])}")
        
        print("\nFrecuencia de nucleótidos:")
        total_nucleotidos = sum(analisis['frecuencias_nucleotidos'].values())
        for nucleotido, frecuencia in sorted(analisis['frecuencias_nucleotidos'].items()):
            porcentaje = (frecuencia / total_nucleotidos) * 100
            print(f"{nucleotido}: {porcentaje:.2f}%")
        
        # Mostrar algunas secuencias de ejemplo
        print("\nEjemplos de secuencias reconstruidas (primeras 3):")
        for i, secuencia in enumerate(list(analisis['secuencias_unicas'])[:3], 1):
            print(f"Secuencia {i}: {secuencia}")
    else:
        print("\nNo se encontraron caminos eulerianos.")

# Ejemplo de uso
if __name__ == "__main__":
    secuencia = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
    k = 5
    # Ajustar estos parámetros según necesidad
    tiempo_limite = 5.0  # 5 segundos
    max_caminos = 100   # máximo 100 caminos
    
    analizar_secuencia_adn(secuencia, k, tiempo_limite, max_caminos)
