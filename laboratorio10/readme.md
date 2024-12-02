# Inferencia de Red Booleana Mediante Selección Secuencial hacia Adelante (SFS)

## Descripción del Código

Este script implementa un algoritmo de inferencia de redes booleanas utilizando el método de Selección Secuencial hacia Adelante (SFS - Sequential Forward Selection). El objetivo es descubrir las relaciones predictivas entre genes en un conjunto de datos booleano.

### Funcionalidades Principales

- Carga de datos desde un archivo de texto
- Cálculo de información mutua entre genes
- Selección de predictores para cada gen objetivo
- Registro de información y manejo de errores

## Dependencias

Para ejecutar este script, necesitarás:

- Python 3.7+
- NumPy
- Logging (incluido en la biblioteca estándar de Python)

### Instalación de Dependencias

```bash
pip install numpy
```

## Formato del Archivo de Entrada

El archivo `datos.txt` debe seguir el siguiente formato:
- Primera línea: Dimensiones de la matriz (filas, columnas)
- Líneas siguientes: Datos booleanos (0 o 1) separados por espacios

Ejemplo:
```
5 4
0 1 0 1
1 0 1 0
1 1 1 1
0 0 0 0
1 1 0 1
```

## Ejecución del Código

### Método 1: Ejecución Directa

```bash
python infe_1.py
```

### Método 2: Modificación del Archivo

1. Cambia la ruta del archivo en la línea:
```python
ruta_archivo = "datos.txt"
```

2. Ejecuta el script

## Parámetros Configurables

- `max_dim`: Número máximo de predictores para cada gen (por defecto: 3)
- Niveles de logging configurables

## Funcionamiento del Algoritmo

1. Carga los datos desde el archivo
2. Para cada gen:
   - Selecciona predictores secuencialmente
   - Maximiza la información mutua
3. Genera una red booleana inferida
4. Registra los predictores para cada gen

## Consideraciones

- Funciona mejor con conjuntos de datos pequeños a medianos
- Requiere datos booleanos (0 o 1)
- La complejidad computacional aumenta con el número de genes

## Registro y Errores

El script utiliza logging para:
- Informar predictores seleccionados
- Registrar errores durante la ejecución
