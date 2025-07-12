# Torre de Hanoi - Algoritmo A*
## Introducción a la Inteligencia Artificial - TP1

### Descripción de la Implementación

Este trabajo práctico implementa una solución al problema clásico de la Torre de Hanoi utilizando el algoritmo de búsqueda A*. La implementación se encuentra en el notebook `TP1_hanoi_tower_problem.ipynb` y presenta las siguientes características principales:

- Implementación del algoritmo A* con dos heurísticas diferentes
- Manejo eficiente de estados y nodos de búsqueda
- Comparación de rendimiento entre heurísticas
- Análisis de tiempo de ejecución y uso de memoria
- Validación de estados y secuencias de movimientos

### Preguntas a Resolver

#### 1. PEAS del problema
[Espacio para completar los componentes PEAS]
- Performance:
- Environment:
- Actuators:
- Sensors:

#### 2. Propiedades del entorno de trabajo
[Espacio para completar las propiedades]

#### 3. Definición de conceptos
[Espacio para completar las definiciones]
- Estado:
- Espacio de estados:
- Árbol de búsqueda:
- Nodo de búsqueda:
- Objetivo:
- Acción:
- Frontera:

#### 4. Método de búsqueda implementado
Se implementó el algoritmo de búsqueda A* (A-estrella) con dos heurísticas diferentes:

1. Heurística Simple:
   - Otorga -1 punto por cada disco en posición correcta
   - Admisible: nunca sobreestima el costo real
   - Consistente pero poco informativa

2. Heurística Multifactorial (implementación elegida):
   - Combina cuatro factores relevantes:
     a) Discos mal ubicados: Penaliza por cada disco fuera de la varilla objetivo
     b) Discos bloqueados: Penaliza discos con otros encima en varillas incorrectas
     c) Orden incorrecto: Penaliza cuando los discos no están en orden correcto
     d) Peso por tamaño: Añade peso adicional basado en el tamaño del disco

La heurística multifactorial demostró ser más eficiente, reduciendo en un 13.5% el número de nodos explorados mientras mantiene la optimalidad de la solución. Es admisible (nunca sobreestima el costo real) y consistente (el valor entre nodos adyacentes nunca excede el costo real del movimiento).

El algoritmo utiliza estructuras de datos optimizadas:
- Cola de prioridad para la frontera
- Conjunto (set) para estados explorados
- Diccionario para costos de estados

Esta implementación garantiza encontrar la solución óptima en términos del número mínimo de movimientos necesarios.

#### 5. Complejidad teórica
- Tiempo: O(3^(2^n - 1)), donde n es el número de discos
  - Factor de ramificación b = 3 (máximo 3 movimientos posibles por estado)
  - Profundidad de la solución d = 2^n - 1
- Memoria: O(3^(2^n - 1))
  - A* mantiene en memoria la frontera, nodos explorados y el camino actual

#### 6. Métricas de implementación
[Espacio para completar con los resultados de las ejecuciones]
- Tiempo promedio: 0.0350 segundos
- Desvío estándar tiempo: 0.0009 segundos
- Memoria promedio: 0.1728 MB
- Desvío estándar memoria: 0.0052 MB

#### 7. Análisis de optimalidad
La solución encontrada es optima, generando soluciones de 31 movimientos para una torre de 5 discos.

### Ejecución del Notebook

Para ejecutar el notebook `TP1_hanoi_tower_problem.ipynb`, siga estos pasos:

1. Asegúrese de tener instalado Python 3.11 o superior :
    ```bash
    python3 --version
    ```
2. Clone este repositorio
3. Navegue hasta el directorio del proyecto
4. Instale las dependencias necesarias:
   ```bash
   uv sync
   ```
5. Active el entorno virtual (`source .venv/bin/activate` en Linux/macOS o `.\.venv\Scripts\activate` en Windows).
6. Inicie Jupyter Notebook:
   ```bash
   uv run jupyter notebook
   ```
7. Abra el archivo `TP1_hanoi_tower_problem.ipynb`
8. Ejecute todas las celdas en orden

### Autores
- Martín Fernando Andres
- María Belén Cattaneo
- Nicolas Ciarrapico
- Maira Daniela Ferrari
- Gaspar Rivollier 

<!-- revisemos por las dudas que los saque del usuario del user de github. @gasparrivollier  -->