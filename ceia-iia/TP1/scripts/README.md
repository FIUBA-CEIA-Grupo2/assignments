## 🧠 Ejecución del script

Para ejecutar el script `scripts/hanoi_tower_problem.py`, siga los siguientes pasos:

1. **Asegurese de tener instalado Python 3.11 o superior**:

   ```bash
   python3 --version
   ```

2. **Clone este repositorio**:

   ```bash
   git clone https://github.com/FIUBA-CEIA-Grupo2/assignments.git
   cd assignments
   ```

3. **Instale `uv` si no lo tiene aun instalado**:

   ```bash
   curl -Ls https://astral.sh/uv/install.sh | bash
   ```

4. **Instale las dependencias y cree el entorno virtual**:

   ```bash
   uv venv
   uv sync
   ```

5. **Active el entorno virtual**:

   - En Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - En Windows:
     ```powershell
     .\.venv\Scripts\activate
     ```

6. **Ejecute el Script**:

   ```bash
   python3 ./scripts/hanoi_tower_problem.py
   ```
