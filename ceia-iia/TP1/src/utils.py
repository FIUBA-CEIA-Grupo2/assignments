import logging
from typing import List, Tuple
import tracemalloc
import statistics

from aima.hanoi_states import ProblemHanoi, StatesHanoi
from aima.tree_hanoi import NodeHanoi
from tower_hanoi_astar_solver import TowerHanoiAStar

# Setup de logger
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def compare_heuristics(disks_num: int = 5, debug: bool = False) -> Tuple[NodeHanoi, dict]:
    """Inicialización del problema"""
    disks_list = list(range(disks_num, 0, -1))
    initial_state = StatesHanoi(disks_list, [], [], max_disks=disks_num)
    goal_state = StatesHanoi([], [], disks_list, max_disks=disks_num)
    problem = ProblemHanoi(initial=initial_state, goal=goal_state)

    # Probar heurística simple
    tower = TowerHanoiAStar(initial_state, goal_state, problem, disks_num=disks_num)
    solution_simple, stats_simple = tower.a_star(use_multifactorial_heuristic=False)

    if solution_simple and debug:
        logger.info("\n1. HEURÍSTICA SIMPLE (discos fuera de lugar)")
        logger.info(f"✓ Solución encontrada en {stats_simple['movimientos']} movimientos")
        logger.info(f"  - Nodos explorados: {stats_simple['nodos_explorados']}")
        logger.info(f"  - Nodos expandidos: {stats_simple['nodos_expandidos']}")
        logger.info(f"  - Tiempo: {stats_simple['tiempo_ejecucion']:.4f} segundos")

    # Probar heurística multifactorial
    tower = TowerHanoiAStar(initial_state, goal_state, problem, disks_num=disks_num)
    solution_multifactor, stats_multifactor = tower.a_star(use_multifactorial_heuristic=True)

    if solution_multifactor and debug:
        logger.info("\n2. HEURÍSTICA MULTIFACTORIAL")
        logger.info(f"✓ Solución encontrada en {stats_multifactor['movimientos']} movimientos")
        logger.info(f"  - Nodos explorados: {stats_multifactor['nodos_explorados']}")
        logger.info(f"  - Nodos expandidos: {stats_multifactor['nodos_expandidos']}")
        logger.info(f"  - Tiempo: {stats_multifactor['tiempo_ejecucion']:.4f} segundos")

    # Análisis comparativo
    logger.info("\n" + "=" * 50)
    logger.info("ANÁLISIS COMPARATIVO")
    logger.info("=" * 50)

    if solution_simple and solution_multifactor:
        if stats_simple['movimientos'] == stats_multifactor['movimientos'] == (2 ** disks_num - 1):
            logger.info(f"Ambas heurísticas encontraron solución óptima: {stats_simple['movimientos']} movimientos")
        logger.info("Eficiencia en nodos explorados:")
        logger.info(f"  - Simple: {stats_simple['nodos_explorados']} nodos")
        logger.info(f"  - Creativa: {stats_multifactor['nodos_explorados']} nodos")
        mejora = (stats_simple['nodos_explorados'] - stats_multifactor['nodos_explorados']) / stats_simple['nodos_explorados'] * 100
        logger.info(f"  - Mejora: {mejora:.1f}%")

    return solution_multifactor, stats_multifactor


def get_execution_time_and_memory_usage(iterations: int = 10, use_multifactorial_heuristic: bool = True) -> Tuple[List[float], List[float], int]:
    """Cálculo del tiempo de ejecución y el uso de memoria requeridos para la búsqueda de una solución."""

    n = 5  # número de discos
    disks_list = list(range(n, 0, -1))
    initial_state = StatesHanoi(disks_list, [], [], max_disks=n)
    goal_state = StatesHanoi([], [], disks_list, max_disks=n)
    problem = ProblemHanoi(initial=initial_state, goal=goal_state)
    tower = TowerHanoiAStar(initial_state, goal_state, problem, disks_num=n)

    time_data = []
    memory_data = []
    movements = []

    for _ in range(iterations):
        tracemalloc.start()
        solution_multifactor, stats_multifactor = tower.a_star(use_multifactorial_heuristic=use_multifactorial_heuristic)
        _, memory_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        memory_peak /= 1024 * 1024  # Convertir a MB
        time_data.append(stats_multifactor['tiempo_ejecucion'])
        memory_data.append(memory_peak)
        movements.append(stats_multifactor['movimientos'])

    time_list = [statistics.mean(time_data), statistics.stdev(time_data)]
    memory_list = [statistics.mean(memory_data), statistics.stdev(memory_data)]

    return time_list, memory_list, statistics.mean(movements)
