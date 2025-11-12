# Makefile para crear el entregable según INSTRUCCIONES.md
# Creará: guia2-alma.de.litio.tar.gz
# Funciona en Linux/macOS y en Windows (PowerShell). Usa Python como backend

PY :=
ifeq ($(OS),Windows_NT)
    # En Windows, asumimos que 'python' está disponible en PATH (PowerShell)
    PY := python
else
    # En sistemas Unix preferir python3 si existe
    PY := $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null)
endif

TAR_NAME := guia2-alma.de.litio.tar.gz
PY_SCRIPT := tools/package.py

.PHONY: all dist clean help

all: dist

help:
	@echo "Make targets:"
	@echo "  make dist   - Crear $(TAR_NAME) (usa Python script)"
	@echo "  make clean  - Eliminar $(TAR_NAME) si existe"
	@echo "Nota: en Windows ejecute desde PowerShell si usa 'make' proporcionado por MSYS/MinGW o "
	@echo "      use 'nmake'/'mage' alternativos. Este Makefile intenta localizar 'python3' o 'python'."

dist:
	@if [ -z "$(PY)" ]; then \
		echo "ERROR: no se encontró 'python3' ni 'python' en PATH"; exit 1; \
	fi
	@echo "Usando intérprete: $(PY)"
	@$(PY) $(PY_SCRIPT) --output "$(TAR_NAME)"
	@echo "Creado: $(TAR_NAME)"

clean:
	@echo "Eliminando $(TAR_NAME) si existe..."
	@rm -f $(TAR_NAME) || powershell Remove-Item -Force -ErrorAction SilentlyContinue $(TAR_NAME)
