import json
from core.logger import logger

def validate_files(output_path: str) -> bool:
    """
    Valida que los archivos generados tengan el formato correcto.
    """

    # 1. Validar initial_state.json
    logger.info("1. Validando initial_state.json...")
    try:
        with open(f'{output_path}/initial_state.json', 'r', encoding='utf-8') as archivo:
            initial_state = json.load(archivo)

        # Verificar estructura
        required_keys = ['peg_1', 'peg_2', 'peg_3']
        if not all(key in initial_state for key in required_keys):
            logger.error("   ✗ Estructura incorrecta: faltan claves requeridas")
            return False

        # Verificar que todos los valores sean listas
        for key in required_keys:
            if not isinstance(initial_state[key], list):
                logger.error(f"   ✗ {key} debe ser una lista")
                return False

        # Validar discos
        todos_discos = []
        for peg in ['peg_1', 'peg_2', 'peg_3']:
            todos_discos.extend(initial_state[peg])

        # Verificar discos únicos
        if len(todos_discos) != len(set(todos_discos)):
            logger.error("   ✗ Hay discos duplicados")
            return False

        # Verificar secuencia completa
        if todos_discos and (set(todos_discos) != set(range(1, max(todos_discos) + 1))):
            logger.error("   ✗ Secuencia de discos incompleta")
            return False

        logger.info("   ✓ initial_state.json válido")

    except FileNotFoundError:
        logger.error("   ✗ Archivo initial_state.json no encontrado")
        return False
    except json.JSONDecodeError:
        logger.error("   ✗ Error al decodificar initial_state.json")
        return False

    # 2. Validar sequence.json
    logger.info("2. Validando sequence.json...")
    try:
        with open(f'{output_path}/sequence.json', 'r', encoding='utf-8') as archivo:
            sequence = json.load(archivo)

        # Verificar que sea una lista
        if not isinstance(sequence, list):
            logger.error("   ✗ sequence.json debe ser una lista")
            return False

        # Validar cada movimiento
        for i, move in enumerate(sequence):
            if not isinstance(move, dict):
                logger.error(f"   ✗ Movimiento {i} debe ser un objeto")
                return False

            required_move_keys = ['type', 'disk', 'peg_start', 'peg_end']
            if not all(key in move for key in required_move_keys):
                logger.error(f"   ✗ Movimiento {i} incompleto")
                return False

            if move['type'] != 'movement':
                logger.error(f"   ✗ Movimiento {i} debe tener type='movement'")
                return False

            # Verificar que los números de varilla sean válidos
            if not (1 <= move['peg_start'] <= 3 and 1 <= move['peg_end'] <= 3):
                logger.error(f"   ✗ Movimiento {i} tiene números de varilla inválidos")
                return False

        logger.info(f"   ✓ sequence.json válido ({len(sequence)} movimientos)")

    except FileNotFoundError:
        logger.error("   ✗ Archivo sequence.json no encontrado")
        return False
    except json.JSONDecodeError:
        logger.error("   ✗ Error al decodificar sequence.json")
        return False

    logger.info("🎉 Ambos archivos son válidos!")
    return True
