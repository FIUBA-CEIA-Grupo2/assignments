import json
from core.logger import logger

def validate_hanoi_simulator_files(output_path: str) -> bool:
    """
    Valida que los archivos generados tengan el formato correcto.
    """

    # 1. Validar initial_state.json
    logger.info("1. Validando initial_state.json...")
    try:
        with open(f'{output_path}/initial_state.json', 'r', encoding='utf-8') as initial_state_file:
            initial_state = json.load(initial_state_file)

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
        all_disks = []
        for peg in ['peg_1', 'peg_2', 'peg_3']:
            all_disks.extend(initial_state[peg])

        # Verificar discos únicos
        if len(all_disks) != len(set(all_disks)):
            logger.error("   ✗ Hay discos duplicados")
            return False

        # Verificar secuencia completa
        if all_disks and (set(all_disks) != set(range(1, max(all_disks) + 1))):
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
        with open(f'{output_path}/sequence.json', 'r', encoding='utf-8') as sequence_file:
            sequence = json.load(sequence_file)

        # Verificar que sea una lista
        if not isinstance(sequence, list):
            logger.error("   ✗ sequence.json debe ser una lista")
            return False

        # Validar cada movimiento
        for idx, move in enumerate(sequence):
            if not isinstance(move, dict):
                logger.error(f"   ✗ Movimiento {idx} debe ser un objeto")
                return False

            required_move_keys = ['type', 'disk', 'peg_start', 'peg_end']
            if not all(key in move for key in required_move_keys):
                logger.error(f"   ✗ Movimiento {idx} incompleto")
                return False

            if move['type'] != 'movement':
                logger.error(f"   ✗ Movimiento {idx} debe tener type='movement'")
                return False

            # Verificar que los números de varilla sean válidos
            if not (1 <= move['peg_start'] <= 3 and 1 <= move['peg_end'] <= 3):
                logger.error(f"   ✗ Movimiento {idx} tiene números de varilla inválidos")
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
