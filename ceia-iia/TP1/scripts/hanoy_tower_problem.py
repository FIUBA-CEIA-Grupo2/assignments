import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

src_path = project_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

src_path = project_root / "libs"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils import compare_heuristics, get_execution_time_and_memory_usage

if __name__ == "__main__":
    solution, stats = compare_heuristics(disks_num=5, debug=True)
    output_dir = Path(__file__).resolve().parent / "data/output"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    if hasattr(solution, 'generate_solution_for_simulator'):
        solution.generate_solution_for_simulator(initial_state_file=output_dir / "initial_state.json",
                                        sequence_file=output_dir / "sequence.json")

    print("\nResumen de ejecución:")
    print(f"Algoritmo: A* con heurística {stats.get('heuristica_usada', 'miltifactorial')}")
    print(f"Tiempo de ejecución: {stats.get('tiempo_ejecucion', 0):.4f} segundos")
    print(f"Nodos explorados: {stats.get('nodos_explorados', 0)}")

    print("\n== Medición de tiempo y memoria ==")
    t_stats, m_stats, movs = get_execution_time_and_memory_usage()
    print(f"Tiempo promedio: {t_stats[0]:.4f}s ± {t_stats[1]:.4f}")
    print(f"Memoria promedio: {m_stats[0]:.4f}MB ± {m_stats[1]:.4f}")
    print(f"Promedio de movimientos: {movs}")
