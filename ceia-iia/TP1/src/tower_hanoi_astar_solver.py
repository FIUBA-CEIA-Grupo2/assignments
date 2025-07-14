import time
import logging
from typing import Tuple

from aima.hanoi_states import ProblemHanoi, StatesHanoi
from aima.tree_hanoi import NodeHanoi
from aima.aima import PriorityQueue as AimaPriorityQueue

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

class TowerHanoiAStar:
    """
    Implementación del algoritmo A* para resolver la Torre de Hanoi.
    """

    def __init__(self, initial_state: StatesHanoi, goal_state: StatesHanoi, problem: ProblemHanoi, disks_num: int = 5):
        self.disks_num = disks_num
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.problem = problem
        self.explored_nodes = 0
        self.expanded_nodes = 0

    def multifactorial_heuristic(self, node: NodeHanoi) -> int:
        """
        Heurística multifactorial: Combinación de múltiples factores

        Fundamentación:
        1. Discos mal ubicados: Penaliza discos que no están en la varilla objetivo
        2. Discos bloqueados: Penaliza discos que tienen otros encima en varillas incorrectas
        3. Orden incorrecto: Penaliza cuando los discos no están en orden correcto
        4. Distancia de movimiento: Considera qué tan lejos están los discos de su destino

        Esta heurística es admisible porque nunca sobreestima el costo real,
        ya que cada factor representa movimientos mínimos necesarios.
        """
        # Factor 1: Discos que no están en la varilla objetivo (C)
        misplaced_disks = 0
        for i in range(2):  # Varillas A y B
            misplaced_disks += len(node.state.rods[i])

        # Factor 2: Discos bloqueados en varillas incorrectas
        locked_disks = 0
        for i in range(2):  # Solo varillas A y B
            rod = node.state.rods[i]
            for j, _ in enumerate(rod):
                # Si hay discos encima, está bloqueado
                if j < len(rod) - 1:
                    locked_disks += 1

        # Factor 3: Verificar orden en varilla objetivo
        incorrect_order = 0
        rod_c = node.state.rods[2]
        for i in range(len(rod_c)):
            if rod_c[i] != self.disks_num - i:
                incorrect_order += 1

        # Factor 4: Peso por tamaño de disco (discos más grandes son más costosos de mover)
        disks_weight = 0
        for i in range(2):
            for disk in node.state.rods[i]:
                disks_weight += disk * 0.1  # Pequeño peso adicional

        # Combinación de factores
        h = misplaced_disks * 2 + locked_disks + incorrect_order + disks_weight

        return int(h)

    def simple_heuristic(self, node: NodeHanoi) -> int:
        """
        Heurística simple propuesta: -1 por cada disco en posición correcta
        (Convertida a positiva para A*)
        """
        correct_disks = len(node.state.rods[2])  # Discos en varilla C
        return self.disks_num - correct_disks

    def a_star(self, use_multifactorial_heuristic: bool = True, debug: bool = False) -> Tuple[NodeHanoi, dict]:
        """
        Implementación del algoritmo A*.

        Returns:
            - Nodo final alcanzado
            - Diccionario con estadísticas del algoritmo
        """
        if debug:
            logger.info(f"Iniciando A* con heurística {'multifactorial' if use_multifactorial_heuristic else 'simple'}...")
            logger.info(f"Estado inicial: {self.initial_state}")
            logger.info(f"Estado objetivo: {self.goal_state}")
            logger.info("-" * 60)

        start_time = time.time()

        # Inicialización
        heuristic = self.multifactorial_heuristic if use_multifactorial_heuristic else self.simple_heuristic
        root = NodeHanoi(state=self.initial_state)
        priority_queue = AimaPriorityQueue(order='min', f=lambda node: (node.path_cost + heuristic(node)))

        priority_queue.append(root)
        open_states = {root.state} # Usamos un set para estados en la lista abierta
        closed_set = set()  # Usamos set en lugar de list para closed
        state_costs = {root.state: root.path_cost} # Diccionario para mantener track del mejor costo para cada estado
        self.explored_nodes = 0
        self.expanded_nodes = 0

        while len(priority_queue) != 0:

            # Seleccionar nodo con menor f
            priority_value, current_node = priority_queue.pop()
            current_state = current_node.state

            # Si este nodo tiene un costo peor que el que ya conocemos, lo saltamos
            if current_state in state_costs and current_node.path_cost > state_costs[current_state]:
                continue

            # Removemos el estado de open_states
            open_states.remove(current_state)

            self.explored_nodes += 1

            # Verificar si alcanzamos el objetivo
            if current_state == self.goal_state:
                total_time = time.time() - start_time

                # Reconstruir camino
                stats = {
                    'movimientos': len(current_node.path()) - 1,
                    'nodos_explorados': self.explored_nodes,
                    'nodos_expandidos': self.expanded_nodes,
                    'tiempo_ejecucion': total_time,
                    'costo_solucion': current_node.path_cost,
                    'heuristica_usada': 'multifactorial' if use_multifactorial_heuristic else 'simple'
                }

                return current_node, stats

            # Agregamos a closed_set el estado, no el nodo
            closed_set.add(current_state)

            # Expandir nodos sucesores
            self.expanded_nodes += 1

            for next_node in current_node.expand(problem=self.problem):
                next_state = next_node.state

                # Si el estado está cerrado y no encontramos un mejor camino, lo saltamos
                if next_state in closed_set and next_node.path_cost >= state_costs.get(next_state, float('inf')):
                    continue

                # Si encontramos un mejor camino a un estado
                if next_state not in state_costs or next_node.path_cost < state_costs[next_state]:
                    # Actualizamos el mejor costo conocido
                    state_costs[next_state] = next_node.path_cost
                    # Agregamos el nodo a la cola con la nueva prioridad
                    priority_queue.append(next_node)
                    open_states.add(next_state)
                    # Si estaba en closed_set, lo removemos para reconsiderarlo
                    if next_state in closed_set:
                        closed_set.remove(next_state)

        return None, {'error': 'No se encontró solución'}
