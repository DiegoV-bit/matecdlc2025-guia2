================================================================================
  ANÁLISIS EXPLORATORIO DE DATOS: DIABETES GESTACIONAL (GDM)
================================================================================

UNIVERSIDAD DE MAGALLANES
Facultad de Ingeniería, Departamento de Ingeniería en Computación
Asignatura: Matemática para Ciencias de la Computación
Profesor: David Medina Ortiz

================================================================================
  EQUIPO DE DESARROLLO
================================================================================

Equipo: Alma de Litio

Integrantes:
  • Pablo Gómez (Líder)
  • Emmanuel Velásquez
  • Diego Vidal

Fecha de Entrega: 12 de noviembre de 2025

================================================================================
  DESCRIPCIÓN DEL PROYECTO
================================================================================

Análisis exploratorio exhaustivo de un dataset sintético del primer trimestre
del embarazo para caracterizar estadísticamente el riesgo de diabetes 
gestacional (GDM).

ANÁLISIS INCLUIDOS:
  • Estadística descriptiva y detección de outliers (IQR, Isolation Forest)
  • Intervalos de confianza para variables clave
  • Pruebas de hipótesis (t-test, Mann-Whitney, ANOVA, Chi-cuadrado)
  • Análisis de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov)
  • Análisis bivariado (correlaciones de Pearson y Spearman)
  • Visualizaciones comparativas y interpretación clínica

ARCHIVOS:
  Entregable.ipynb                              - Notebook principal
  auxiliar_functions.py                         - Funciones auxiliares
  gdm_first_trimester_ml_dataset.csv           - Dataset (1500 registros)
  gdm_first_trimester_ml_dataset_metadata.json - Metadatos

================================================================================
  REQUISITOS PREVIOS
================================================================================

SOFTWARE NECESARIO:
  ✓ Visual Studio Code
  ✓ Python 3.8 o superior
  ✓ Extensión: Python (Microsoft)
  ✓ Extensión: Jupyter (Microsoft)

SISTEMAS SOPORTADOS:
  • Windows 10/11
  • Linux (Ubuntu 20.04+, Debian 11+, Fedora 35+)
  • macOS 11+ (Big Sur o superior)

================================================================================
  CONFIGURACIÓN RÁPIDA
================================================================================

------------------------------------------------------------------------
WINDOWS - Configuración Completa (PowerShell)
------------------------------------------------------------------------

# Copiar y ejecutar todo el bloque en PowerShell:

cd D:\CopilotWS\matecdlc2025-guia2
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel


------------------------------------------------------------------------
LINUX - Configuración Completa (Bash)
------------------------------------------------------------------------

# Copiar y ejecutar todo el bloque en terminal:

cd ~/matecdlc2025-guia2
python3 -m pip install --upgrade pip
pip3 install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel


================================================================================
  CONFIGURACIÓN CON ENTORNO VIRTUAL (RECOMENDADO)
================================================================================

------------------------------------------------------------------------
WINDOWS - Entorno Virtual (PowerShell)
------------------------------------------------------------------------

# Copiar y ejecutar todo el bloque:

cd D:\CopilotWS\matecdlc2025-guia2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
python -m ipykernel install --user --name=venv_gdm --display-name "Python (GDM)"


# Para activar el entorno en sesiones futuras:
.\.venv\Scripts\Activate.ps1


------------------------------------------------------------------------
LINUX/macOS - Entorno Virtual (Bash/Zsh)
------------------------------------------------------------------------

# Copiar y ejecutar todo el bloque:

cd ~/matecdlc2025-guia2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
python -m ipykernel install --user --name=venv_gdm --display-name "Python (GDM)"


# Para activar el entorno en sesiones futuras:
source .venv/bin/activate


================================================================================
  USO EN VISUAL STUDIO CODE
================================================================================

1. ABRIR EL PROYECTO:
   
   File → Open Folder → Seleccionar carpeta del proyecto


2. ABRIR EL NOTEBOOK:
   
   Click en Entregable.ipynb desde el explorador de archivos


3. SELECCIONAR KERNEL:
   
   • Click en "Select Kernel" (esquina superior derecha)
   • Elegir "Python (GDM)" si usaste entorno virtual
   • O elegir tu instalación de Python global


4. EJECUTAR EL ANÁLISIS:
   
   Opciones:
   • Run All: Click en el botón ⏩ en la barra superior
   • Celda por celda: Shift + Enter en cada celda
   • Ejecutar hasta cursor: Ctrl + Alt + Enter (Cmd + Alt + Enter en Mac)


5. TIEMPO DE EJECUCIÓN:
   
   • Completo: ~2-3 minutos
   • Por secciones: 20-30 segundos cada una


ESTRUCTURA DEL NOTEBOOK:

  1. Descripción General del Dataset
  2. Desarrollo del Análisis
     ├── 2.1 Análisis Exploratorio (EDA)
     ├── 2.2 Intervalos de Confianza
     ├── 2.3 Pruebas de Hipótesis
     ├── 2.4 Evaluación de Normalidad
     └── 2.5 Análisis Bivariado
  3. Finalización y Resumen de Método
     ├── 3.1 Interpretación Clínica y Conclusiones
     └── 3.2 Declaración de Método

================================================================================
  SOLUCIÓN DE PROBLEMAS
================================================================================

PROBLEMA: No se puede seleccionar kernel / "ipykernel not found"
SOLUCIÓN: Ejecutar en terminal:
          Windows: pip install ipykernel
          Linux:   pip3 install ipykernel


PROBLEMA: ModuleNotFoundError al ejecutar celdas
SOLUCIÓN: Reinstalar dependencias (ejecutar bloque de configuración completo)


PROBLEMA: Gráficos no se visualizan en VSCode
SOLUCIÓN: Verificar que la primera celda de código tenga:
          import matplotlib.pyplot as plt
          %matplotlib inline


PROBLEMA: Errores de permisos en Linux
SOLUCIÓN: Agregar --user a pip install:
          pip3 install --user <paquete>


PROBLEMA: Kernel se desconecta o no responde
SOLUCIÓN: En VSCode:
          • Click en "Restart" en barra superior del notebook
          • O Command Palette (Ctrl+Shift+P) → "Restart Kernel"

================================================================================
  LIBRERÍAS UTILIZADAS
================================================================================

pandas       >= 1.3.0    - Manipulación de datos tabulares
numpy        >= 1.21.0   - Operaciones numéricas y álgebra lineal
matplotlib   >= 3.4.0    - Visualización de gráficos base
seaborn      >= 0.11.0   - Visualización estadística avanzada
scipy        >= 1.7.0    - Análisis estadístico y pruebas
scikit-learn >= 0.24.0   - Algoritmos de machine learning
ipykernel    >= 6.0.0    - Kernel de Jupyter para VSCode

================================================================================
  INFORMACIÓN ADICIONAL
================================================================================

• Dataset sintético generado con fines educativos
• Análisis estadísticos implementados completamente por el equipo
• IA utilizada solo para asistencia editorial (ver notebook sección 3.2.2)
• Código reproducible y completamente documentado
• Funciones auxiliares reutilizables en auxiliar_functions.py

CONTACTO:
  Profesor: David Medina Ortiz (david.medina@umag.cl)
  Equipo: Alma de Litio
  Universidad: Universidad de Magallanes

CONTROL DE VERSIONES:
  Sistema: Git + GitHub
  Herramientas: VSCode + extensiones de Git

================================================================================
© 2025 - Equipo Alma de Litio - Universidad de Magallanes
Uso exclusivo para evaluación académica
================================================================================
