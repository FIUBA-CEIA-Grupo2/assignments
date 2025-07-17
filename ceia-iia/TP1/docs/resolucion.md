# Torre de Hanoi - Algoritmo A\*

### Descripción de la Implementación

Este trabajo práctico implementa una solución al problema clásico de la Torre de Hanoi utilizando el algoritmo de búsqueda A\*.

La implementación se encuentra en la carpeta src y se puede ejecutar tanto desde la notebook `notebooks/hanoi_tower_problem.ipynb` como dede el script `scripts/hanoi_tower_problem.py`.

El desarrollo tiene las siguientes características principales:

- Implementación del algoritmo A\* con dos heurísticas diferentes
- Manejo eficiente de estados y nodos de búsqueda
- Comparación de rendimiento entre heurísticas
- Análisis de tiempo de ejecución y uso de memoria
- Validación de estados y secuencias de movimientos

### Preguntas a Resolver

#### 1. PEAS del problema

- **Performance:** Se obtiene a través de métricas de tiempo de ejecución y uso de memoria.
- **Environment:** Varillas 1,2,3; Discos 1,2,3,4,5. Posición de discos en cada una de las varillas en los distintos estados, restricciones o reglas del juego.
- **Actuators:** Movimiento de discos 1,2,3,4,5 en varillas 1,2,3.
- **Sensors:** Visualización de estado y posición de todos los discos en las varillas 1,2,3.

#### 2. Propiedades del entorno de trabajo

- **Totalmente observable vs. parcialmente observable:** Totalmente observable. En todo momento el agente puede verificar la posición de cada uno de los discos en las tres varillas.
- **Deterministas vs. Estocástico:** Determinista. Los movimientos de los discos siempre tienen el mismo resultado si la acción y el estado inicial en que se realizan son iguales. Las reglas son fijas y sin azar.
- **Episódico vs. Secuencial:** Episódico. Las partidas son individuales y no se afectan una a la otra. El escenario se resetea cada vez que se inicia una nueva partida.
- **Estático vs. Dinámico:** Estático. El entorno no cambia más allá de los cambios generados por la propia acción del agente.
- **Discreto vs. Continuo:** Discreto. Las acciones se pueden individualizar de forma discreta en movimientos de discos a varillas.
- **Agente individual vs. Multiagente: Agente individual** Agente individual. Solo hay un agente operando en un mismo momento, no hay ni cooperación ni competencia.

#### 3. Definición de conceptos

- **Estado:** Posición de cada uno de los discos 1,2,3,4,5 en las distintas varillas 1,2,3.
  Ejemplo: Estado inicial. Varilla 1: 5,4,3,2,1; Varilla 2: Vacía; Varilla 3: Vacía.
- **Espacio de estados:** Conjunto de todos los posibles estados a los que se puede llegar siguiendo las reglas definidas.
- **Árbol de búsqueda:** Representación de los estados que el algoritmo de búsqueda va explorando y expandiendo durante la operación de búsqueda. Este contiene el registro de el estado explorado, la profundidad, el costo de búsqueda y el camino de como se llego a cierto estado de discos en varillas.
- **Nodo de búsqueda:** Elemento específico del árbol de búsqueda con una combinación única de profundidad, estado, padre y costo del camino.
- **Objetivo:** Hallar solución al problema, es decir, lograr que los discos 5,4,3,2,1 estén en el respectivo orden en la varilla 3. Partiendo del estado inicial descripto.
- **Acción:** Movimiento posible de un disco X (1,2,3,4,5) a una varilla Y (1,2,3).
- **Frontera:** Conjunto de nodos generados y pendientes de ser explorados. Estos componen la cola de trabajo del algoritmo.

#### 4. Método de búsqueda implementado

Se implementó el algoritmo de búsqueda A\* (A-estrella) con dos heurísticas diferentes:

1. **Heurística Simple:**

   - Otorga -1 punto por cada disco en posición correcta
   - Admisible: nunca sobreestima el costo real
   - Consistente pero poco informativa

2. **Heurística Multifactorial (implementación elegida):**
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
  - A\* mantiene en memoria la frontera, nodos explorados y el camino actual

#### 6. Métricas de implementación

- Tiempo promedio: 0.0350 segundos
- Desvío estándar tiempo: 0.0009 segundos
- Memoria promedio: 0.1728 MB
- Desvío estándar memoria: 0.0052 MB

#### 7. Análisis de optimalidad

La solución encontrada es optima, generando soluciones de 31 movimientos para una torre de 5 discos lo que coincide con
el valor de 2^k - 1 = 2^5 - 1
