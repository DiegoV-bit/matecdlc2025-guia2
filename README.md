# Análisis Exploratorio de Datos: Diabetes Gestacional (GDM)

**Universidad de Magallanes**  
Facultad de Ingeniería, Departamento de Ingeniería en Computación  
**Asignatura:** Matemática para Ciencias de la Computación  
**Profesor:** David Medina Ortiz

---

## 👥 Equipo de Desarrollo

**Equipo:** Alma de Litio

**Integrantes:**
- Pablo Gómez (Líder)
- Emmanuel Velásquez
- Diego Vidal

**Fecha de Entrega:** 12 de noviembre de 2025

---

## 📋 Descripción del Proyecto

Análisis exploratorio exhaustivo de un dataset sintético del primer trimestre del embarazo para caracterizar estadísticamente el riesgo de diabetes gestacional (GDM).

### Análisis Incluidos

- ✅ Estadística descriptiva y detección de outliers (IQR, Isolation Forest)
- ✅ Intervalos de confianza para variables clave
- ✅ Pruebas de hipótesis (t-test, Mann-Whitney, ANOVA, Chi-cuadrado)
- ✅ Análisis de normalidad (Shapiro-Wilk, Kolmogorov-Smirnov)
- ✅ Análisis bivariado (correlaciones de Pearson y Spearman)
- ✅ Visualizaciones comparativas y interpretación clínica

### Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| `Informe.ipynb` | Notebook principal con el análisis completo |
| `auxiliar_functions.py` | Funciones auxiliares reutilizables |
| `gdm_first_trimester_ml_dataset.csv` | Dataset (1500 registros) |
| `gdm_first_trimester_ml_dataset_metadata.json` | Metadatos del dataset |

---

## 🔧 Requisitos Previos

### Software Necesario

- ✓ Visual Studio Code
- ✓ Python 3.8 o superior
- ✓ Extensión: Python (Microsoft)
- ✓ Extensión: Jupyter (Microsoft)

### Sistemas Soportados

- Windows 10/11
- Linux (Ubuntu 20.04+, Debian 11+, Fedora 35+)
- macOS 11+ (Big Sur o superior)

---

## 🚀 Configuración Rápida

### Windows - Configuración Completa (PowerShell)

```powershell
cd D:\CopilotWS\matecdlc2025-guia2
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
```

### Linux - Configuración Completa (Bash)

```bash
cd ~/matecdlc2025-guia2
python3 -m pip install --upgrade pip
pip3 install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
```

---

## 🐍 Configuración con Entorno Virtual (Recomendado)

### Windows - Entorno Virtual (PowerShell)

```powershell
cd D:\CopilotWS\matecdlc2025-guia2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
python -m ipykernel install --user --name=venv_gdm --display-name "Python (GDM)"
```

**Para activar el entorno en sesiones futuras:**
```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS - Entorno Virtual (Bash/Zsh)

```bash
cd ~/matecdlc2025-guia2
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install pandas numpy matplotlib seaborn scipy scikit-learn ipykernel
python -m ipykernel install --user --name=venv_gdm --display-name "Python (GDM)"
```

**Para activar el entorno en sesiones futuras:**
```bash
source .venv/bin/activate
```

---

## 💻 Uso en Visual Studio Code

### 1. Abrir el Proyecto

```
File → Open Folder → Seleccionar carpeta del proyecto
```

### 2. Abrir el Notebook

Click en `Informe.ipynb` desde el explorador de archivos de VSCode

### 3. Seleccionar Kernel

- Click en **"Select Kernel"** (esquina superior derecha)
- Elegir **"Python (GDM)"** si usaste entorno virtual
- O elegir tu instalación de Python global

### 4. Ejecutar el Análisis

**Opciones:**
- **Run All:** Click en el botón ⏩ en la barra superior
- **Celda por celda:** `Shift + Enter` en cada celda
- **Ejecutar hasta cursor:** `Ctrl + Alt + Enter` (`Cmd + Alt + Enter` en Mac)

### 5. Tiempo de Ejecución

- **Completo:** ~2-3 minutos
- **Por secciones:** 20-30 segundos cada una

---

## 📚 Estructura del Notebook

```
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
```

---

## 🔧 Solución de Problemas

### ❌ No se puede seleccionar kernel / "ipykernel not found"

**Solución:**
```bash
# Windows
pip install ipykernel

# Linux
pip3 install ipykernel
```

### ❌ ModuleNotFoundError al ejecutar celdas

**Solución:** Reinstalar dependencias (ejecutar bloque de configuración completo arriba)

### ❌ Gráficos no se visualizan en VSCode

**Solución:** Verificar que la primera celda de código tenga:
```python
import matplotlib.pyplot as plt
%matplotlib inline
```

### ❌ Errores de permisos en Linux

**Solución:** Agregar `--user` a pip install:
```bash
pip3 install --user <paquete>
```

### ❌ Kernel se desconecta o no responde

**Solución:** En VSCode:
- Click en **"Restart"** en barra superior del notebook
- O Command Palette (`Ctrl+Shift+P`) → **"Restart Kernel"**

---

## 📦 Librerías Utilizadas

| Librería | Versión | Descripción |
|----------|---------|-------------|
| `pandas` | >= 1.3.0 | Manipulación de datos tabulares |
| `numpy` | >= 1.21.0 | Operaciones numéricas y álgebra lineal |
| `matplotlib` | >= 3.4.0 | Visualización de gráficos base |
| `seaborn` | >= 0.11.0 | Visualización estadística avanzada |
| `scipy` | >= 1.7.0 | Análisis estadístico y pruebas |
| `scikit-learn` | >= 0.24.0 | Algoritmos de machine learning |
| `ipykernel` | >= 6.0.0 | Kernel de Jupyter para VSCode |

---

## ℹ️ Información Adicional

- Dataset sintético generado con fines educativos
- Análisis estadísticos implementados completamente por el equipo
- IA utilizada solo para asistencia editorial (ver notebook sección 3.2.2)
- Código reproducible y completamente documentado
- Funciones auxiliares reutilizables en `auxiliar_functions.py`

### Contacto

- **Profesor:** David Medina Ortiz ([david.medina@umag.cl](mailto:david.medina@umag.cl))
- **Equipo:** Alma de Litio
- **Universidad:** Universidad de Magallanes

### Control de Versiones

- **Sistema:** Git + GitHub
- **Herramientas:** VSCode + extensiones de Git

---

<sub>© 2025 - Equipo Alma de Litio - Universidad de Magallanes  
Uso exclusivo para evaluación académica</sub>
