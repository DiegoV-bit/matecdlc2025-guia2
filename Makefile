# Makefile para crear el entregable según INSTRUCCIONES.md
# Creará: guia2-alma.de.litio.tar.gz
# Funciona en Linux/macOS y en Windows (PowerShell). Usa Python como backend

PY :=
PIP :=
ifeq ($(OS),Windows_NT)
    # En Windows, asumimos que 'python' está disponible en PATH (PowerShell)
    PY := python
    PIP := pip
else
    # En sistemas Unix preferir python3 si existe
    PY := $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)
    PIP := $(shell command -v pip3 2>/dev/null || command -v pip 2>/dev/null)
endif

TAR_NAME := guia2-alma.de.litio.tar.gz
PY_SCRIPT := tools/package.py
VENV_NAME := .venv

.PHONY: all dist clean help setup setup-venv install-deps install-kernel

all: dist

help:
	@echo "====================================================================================="
	@echo "  Makefile - Proyecto GDM (Análisis Exploratorio de Datos)"
	@echo "====================================================================================="
	@echo ""
	@echo "TARGET PRINCIPAL:"
	@echo "  make         o  make dist    - Crear $(TAR_NAME)"
	@echo ""
	@echo "CONFIGURACIÓN DE AMBIENTE:"
	@echo "  make setup                   - Instalación rápida (sin entorno virtual)"
	@echo "  make setup-venv              - Crear entorno virtual e instalar dependencias"
	@echo "  make install-deps            - Solo instalar/actualizar dependencias"
	@echo "  make install-kernel          - Registrar kernel Jupyter (requiere deps instaladas)"
	@echo ""
	@echo "UTILIDADES:"
	@echo "  make clean                   - Eliminar $(TAR_NAME) si existe"
	@echo "  make clean-venv              - Eliminar entorno virtual"
	@echo ""
	@echo "NOTAS:"
	@echo "  - En Windows ejecute desde PowerShell"
	@echo "  - En Linux/macOS use bash/zsh"
	@echo "  - El target principal siempre es 'dist' (crear tar.gz)"
	@echo ""
	@echo "====================================================================================="

# Instalación rápida sin entorno virtual
setup: install-deps
	@echo "✓ Configuración rápida completada"
	@echo "  Ahora puede abrir Informe.ipynb en VSCode"

# Crear entorno virtual e instalar todo
setup-venv:
	@echo "Creando entorno virtual en $(VENV_NAME)..."
	@$(PY) -m venv $(VENV_NAME)
ifeq ($(OS),Windows_NT)
	@echo "Activando entorno e instalando dependencias (Windows)..."
	@powershell -Command "& { . .\$(VENV_NAME)\Scripts\Activate.ps1; python -m pip install --upgrade pip; pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel; python -m ipykernel install --user --name=venv_gdm --display-name 'Python (GDM)' }"
	@echo ""
	@echo "✓ Entorno virtual creado exitosamente"
	@echo "  Para activar: .\$(VENV_NAME)\Scripts\Activate.ps1"
else
	@echo "Activando entorno e instalando dependencias (Unix)..."
	@bash -c "source $(VENV_NAME)/bin/activate && python -m pip install --upgrade pip && pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel && python -m ipykernel install --user --name=venv_gdm --display-name 'Python (GDM)'"
	@echo ""
	@echo "✓ Entorno virtual creado exitosamente"
	@echo "  Para activar: source $(VENV_NAME)/bin/activate"
endif

# Solo instalar dependencias (en el ambiente activo actual)
install-deps:
	@echo "Actualizando pip e instalando dependencias..."
	@$(PY) -m pip install --upgrade pip
	@$(PIP) install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
	@echo "✓ Dependencias instaladas"

# Registrar kernel de Jupyter
install-kernel:
	@echo "Registrando kernel Jupyter..."
	@$(PY) -m ipykernel install --user --name=venv_gdm --display-name "Python (GDM)"
	@echo "✓ Kernel 'Python (GDM)' registrado"

# Crear el archivo tar.gz
dist:
	@if [ -z "$(PY)" ]; then \
		echo "ERROR: no se encontró 'python3' ni 'python' en PATH"; exit 1; \
	fi
	@echo "Usando intérprete: $(PY)"
	@$(PY) $(PY_SCRIPT) --output "$(TAR_NAME)"
	@echo "✓ Creado: $(TAR_NAME)"

# Limpiar archivos generados
clean:
	@echo "Eliminando $(TAR_NAME) si existe..."
ifeq ($(OS),Windows_NT)
	@powershell -Command "Remove-Item -Force -ErrorAction SilentlyContinue $(TAR_NAME)"
else
	@rm -f $(TAR_NAME)
endif
	@echo "✓ Limpieza completada"

# Eliminar entorno virtual
clean-venv:
	@echo "Eliminando entorno virtual $(VENV_NAME)..."
ifeq ($(OS),Windows_NT)
	@powershell -Command "Remove-Item -Recurse -Force -ErrorAction SilentlyContinue $(VENV_NAME)"
else
	@rm -rf $(VENV_NAME)
endif
	@echo "✓ Entorno virtual eliminado"
