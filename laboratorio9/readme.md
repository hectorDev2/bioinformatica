# Inferencia de Redes Booleanas 🧬

Este repositorio contiene un script en Python diseñado para inferir redes booleanas a partir de datos de estados genéticos. Este proceso se basa en el cálculo del error absoluto para identificar predictores que mejor expliquen el estado de cada gen en función de otros genes en el sistema.  

## Descripción del Código  

### Funciones Principales  

1. **`cargar_datos(ruta_archivo)`**  
   Lee un archivo de texto que contiene los datos genéticos.  
   - La primera línea debe especificar las dimensiones de la matriz (filas y columnas).  
   - Las líneas siguientes representan la matriz de datos donde cada fila corresponde a un estado del sistema.  

2. **`calcular_error_absoluto(matriz, target, predictores)`**  
   Calcula el error absoluto entre los estados predichos y los reales de un gen objetivo (`target`) basado en un conjunto de predictores.  

3. **`inferir_red_booleana(matriz, max_dim=3)`**  
   Infere una red booleana identificando los mejores predictores para cada gen. Utiliza combinaciones de genes como posibles predictores y selecciona la combinación que minimice el error absoluto.  

4. **`main(ruta_archivo)`**  
   Orquesta la ejecución del script:
   - Carga los datos.
   - Llama a la función de inferencia de red.
   - Imprime la red booleana inferida.  

### Log de Información  
El script utiliza la biblioteca `logging` para mostrar información durante la ejecución, como los predictores seleccionados para cada gen.  

## Estructura del Repositorio  

```plaintext
📂 inferencia-red-booleanas/
├── inferencia_red.py    # Código principal
├── datos.txt            # Archivo de datos de ejemplo
└── README.md            # Este archivo
