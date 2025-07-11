# Trabajo Práctico N°1: Algoritmos de búsqueda en Torre de Hanoi. (22Co 2025)

## Integrantes:

- Martín Fernando Andres
- María Belén Cattaneo
- Nicolas Ciarrapico
- Maira Daniela Ferrari
- Gaspar Rivollier <!-- revisemos por las dudas que los saque del usuario del user de github. -->

## Tareas y preguntas a resolver:

### 1. ¿Cuáles son los PEAS de este problema? (Performance, Environment, Actuators, Sensors)

  - **Performance:** Solución hallada (Si/No), Cantidad de movimientos hasta la solución hallada por algoritmo. 
  - **Environment:** Varillas 1,2,3; Discos 1,2,3,4,5. Posición de discos en cada una de las varillas en los distintos estados. 
  - **Actuators:** Movimiento de discos 1,2,3,4,5 en varillas 1,2,3. 
  - **Sensors:** Visualización de estado y posición de todos los discos en las varillas 1,2,3.
### 2. ¿Cuáles son las propiedades del entorno de trabajo?

  - **Totalmente observable vs. parcialmente observable:** Totalmente observable. En todo momento el agente puede verificar la posición de cada uno de los discos en las tres varillas. 
  - **Deterministas vs. Estocástico:** Determinista. Los movimientos de los discos siempre tienen el mismo resultado si la acción y el estado inicial en que se realizan. son iguales. 
  - **Episódico vs. Secuencial:** Episódico. Las partidas son individuales y no se afectan una a la otra. El escensario se resetea cada vez que se inicia una nueva partida. 
  - **Estático vs. Dinámico:** Estático. El entorno no cambia más allá de los cambios generados por la propia acción del agente. 
  - **Discreto vs. Continuo:** Discreto. Las acciones se pueden individualizar de forma discreta en movimientos de discos a varillas. 
  - **Agente individual vs. Multiagente: Agente individual** Agente individual. Solo hay un agente operando en un mismo momento, no hay ni cooperación ni competencia. <!-- me entro la duda si al hacer la comparación de las dos heurísticas no estamos haciendo multiagente. entiendo que no porque no se hacen en el mismo momento digamos. -->
### 3. En el contexto de este problema, defina los siguientes conceptos:

  - **Estado:** Posición de cada uno de los discos 1,2,3,4,5 en las distintas varillas 1,2,3. Ejemplo: Estado inicial. Varilla 1: 5,4,3,2,1; Varilla 2: Vacía; Varilla 3: Vacía. 
  - **Espacio de estados:** Conjunto de todos los posibles estados a los que se puede llegar siguiendo las reglas propuestas. 
  - **Árbol de búsqueda:** Representación de los estados que el algoritmo de búsqueda va explorando y expandiendo durante la operación de búsqueda. Este contiene el registro de el estado explorado, la profundidad, el costo de búsqueda y el camino de como se llego a cierto nodo. <!-- este me quedo medio genérico, no se que mas ponerle que sea especifico del ejercicio -->
  - **Nodo de búsqueda:** Elemento específico del árbol de búsqueda con una combinación única de profundidad, estado, padre y costo del camino.
  - **Objetivo:** Hallar solución al problema, es decir, lograr que los discos 5,4,3,2,1 estén en el respectivo orden en la varilla 3. Partiendo del estado inicial descripto. 
  - **Acción:** Movimiento posible de un disco X (1,2,3,4,5) a una varilla Y (1,2,3). 
  - **Frontera:** Conjunto de nodos generados y pendientes de ser explorados. Estos componen la cola de trabajo del algoritmo. 
### 4. Implemente algún método de búsqueda. Podés elegir cualquiera excepto búsqueda en anchura (breadth-first search), que ya fue desarrollada en clase. Sos libre de utilizar cualquiera de los algoritmos vistos, o incluso explorar nuevos.
Se decide utilizar el método de búsqueda A* con 2 funciones heurísticas (la propuesta por la cátedra y una más exploratoria) para tener un benchmark de ambas. 

### 5. ¿Cuál es la complejidad teórica en tiempo y memoria del algoritmo elegido?

<!-- resultados del notebook, habría que fijarse de que cuando entreguemos quede con los ultimos resultados bien entre esto y el notebook -->

### 6. A nivel de implementación, ¿cuánto tiempo y memoria utiliza el algoritmo? (Se recomienda ejecutarlo 10 veces y calcular el promedio y el desvío estándar de ambas métricas).

<!-- IDEM 5 -->

### 7. Si la solución óptima es de $2^k - 1$ movimientos (siendo *k* el número de discos), ¿qué tan lejos está la solución encontrada por el algoritmo implementado de esa solución óptima? (Se recomienda ejecutar al menos 10 veces y usar el promedio de los trayectos obtenidos).

<!-- IDEM 5 -->

