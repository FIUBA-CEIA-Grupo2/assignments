## 🧠 Ejecución de la notebook

Para ejecutar el notebook `notebooks/california_housing_regression.ipynb`, siga los siguientes pasos:

1. **Asegurese de tener instalado Python 3.11 o superior**:

   ```bash
   python3 --version
   ```

2. **Clone el repositorio**:

   ```bash
   git clone https://github.com/FIUBA-CEIA-Grupo2/assignments.git
   cd assignments/ceia-iia/TP2

   ```

3. **Instale `uv` si aun no lo tiene instalado**:

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

6. **Inicie Jupyter Notebook**:

   ```bash
   uv run jupyter notebook
   ```

7. **Abra el archivo** `notebooks/california_housing_regression.ipynb`.

8. **Ejecute todas las celdas en orden** para correr el algoritmo.
