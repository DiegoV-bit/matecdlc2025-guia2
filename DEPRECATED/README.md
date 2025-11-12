# matecdlc2025-guia2

Análisis Exploratorio de Datos sobre Diabetes Gestacional (GDM) - Guía 2 del curso Matemáticas para las Ciencias de la Computación.

## Equipo de Trabajo

**Nombre del equipo:** Almas de Litio

**Integrantes:**
- Pablo Gómez (Líder)
- Emmanuel Velásquez
- Diego Vidal

---

## Resumen del Proyecto

Este repositorio contiene el desarrollo de la Guía Práctica 2 enfocada en el **análisis exploratorio estadístico de datos clínicos** para un dataset sintético sobre diabetes gestacional (GDM) del primer trimestre del embarazo.

### 📊 Progreso Global: 39%

| Sección | Estado | Progreso |
|---------|--------|----------|
| 2.1 Exploración Descriptiva | 🟡 | 56% |
| 2.2 Intervalos de Confianza | 🟡 | 54% |
| 2.3 Pruebas de Hipótesis | 🔴 | 8% |
| 2.4 Evaluación de Normalidad | 🟢 | 85% |
| 2.5 Análisis Bivariado | 🔴 | 28% |
| 2.6 Conclusiones | 🔴 | 0% |

---

## 🎯 Características Clave

### Documento Principal: `Entregable.ipynb`

1. **Estructura organizada** por secciones según `INSTRUCCIONES.md`
   - Sección 1: Descripción del dataset (completa ✅)
   - Sección 2: Actividades desarrolladas (2.1 - 2.6)
   - Sección 3: Entregables y archivos adjuntos (completa ✅)

2. **Indicadores de progreso visuales**
   - Emojis de estado: 🔴 (crítico), 🟡 (en progreso), 🟢 (casi completo)
   - Porcentajes de completitud por sección
   - Listas de tareas realizadas y pendientes

3. **Código integrado del prototipo**
   - Importación y exploración de datos
   - Estadística descriptiva con IQR
   - Detección de outliers (IQR + Isolation Forest)
   - Intervalos de confianza para variables clave
   - Pruebas de normalidad (Shapiro-Wilk, KS-Lilliefors)
   - Matriz de correlación y heatmaps
   - Función de comparación de grupos (t-test/Mann-Whitney)

4. **Documentación completa**
   - Lista de todos los archivos a entregar
   - Herramientas y librerías utilizadas
   - Instrucciones de ejecución
   - Referencias a archivos de soporte

### Archivos de Soporte

- **`TASKS.md`**: Lista de tareas organizadas por sección (orden lineal)
- **`auxiliar_functions.py`**: Funciones auxiliares para análisis estadístico
- **`1_check_data.ipynb`**: Prototipo inicial del desarrollo
- **Dataset**: `gdm_first_trimester_ml_dataset.csv` (~1500 registros)

---

## 📋 Próximos Pasos Sugeridos

### Prioridad Alta 🔴 (Completar primero)

1. **Completar Sección 2.3 - Pruebas de Hipótesis (8% → 100%)**
   - Comparar todas las variables continuas entre GDM vs No-GDM
   - Aplicar ANOVA/Kruskal-Wallis para dieta vs actividad física
   - Realizar pruebas de proporciones (chi², z-test)
   - Calcular y reportar tamaño de efecto (d de Cohen)
   - **Tiempo estimado**: 6-8 horas

2. **Completar Sección 2.5 - Análisis Bivariado (28% → 100%)**
   - Crear scatterplots con regresión y R²
   - Generar boxplots comparativos por grupo GDM
   - Interpretar correlaciones fuertes (|r| > 0.7)
   - Relacionar hallazgos con literatura clínica
   - **Tiempo estimado**: 4-5 horas

3. **Crear Sección 2.6 - Conclusiones (0% → 100%)**
   - Sintetizar hallazgos principales
   - Interpretar resultados en contexto clínico
   - Discutir limitaciones del estudio
   - Proponer próximos pasos (modelado predictivo)
   - **Tiempo estimado**: 2-3 horas

### Prioridad Media 🟡 (Mejorar secciones existentes)

4. **Mejorar Sección 2.2 - Intervalos de Confianza (54% → 100%)**
   - Calcular IC para variables faltantes (HDL, presión arterial, triglicéridos)
   - Implementar IC para proporciones (método Wilson/Agresti-Coull)
   - Calcular IC para diferencias de medias entre grupos
   - Interpretar IC en contexto clínico
   - **Tiempo estimado**: 3-4 horas

5. **Mejorar Sección 2.1 - Exploración Descriptiva (56% → 100%)**
   - Generar histogramas individuales con interpretación
   - Añadir gráficos de densidad (KDE)
   - Documentar estrategia de manejo de outliers
   - Interpretar tendencias y dispersiones por variable
   - **Tiempo estimado**: 2-3 horas

### Prioridad Baja 🟢 (Refinamiento)

6. **Completar Sección 2.4 - Evaluación de Normalidad (85% → 100%)**
   - Generar QQ-plots para todas las variables
   - Crear histogramas con curva normal superpuesta
   - Probar transformaciones (log, Box-Cox)
   - Documentar impacto de transformaciones
   - **Tiempo estimado**: 2-3 horas

### Antes de la Entrega

7. **Verificación Final**
   - Ejecutar todo el notebook secuencialmente
   - Verificar que todas las visualizaciones se generen correctamente
   - Completar información del equipo en `Entregable.ipynb`
   - Revisar redacción y ortografía
   - Comprimir archivos (`.tar.gz` o `.zip`)
   - **Tiempo estimado**: 1-2 horas

### ⏰ Tiempo Total Estimado: 21-30 horas

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Jupyter Notebook**
- **pandas, numpy**: Manipulación de datos
- **matplotlib, seaborn**: Visualización
- **scipy.stats**: Pruebas estadísticas
- **scikit-learn**: Detección de outliers (Isolation Forest)
- **Git/GitHub**: Control de versiones

---

## 📅 Información de Entrega

- **Fecha límite**: Viernes 15 de noviembre de 2025, 13:00 hrs (SCL)
- **Formato**: Archivo comprimido (`.tar.gz` o `.zip`)
- **Envío**: david.medina@umag.cl
- **Profesor**: David Medina Ortiz

---

## 📂 Estructura del Repositorio

```
matecdlc2025-guia2/
├── Entregable.ipynb                          # Documento principal de entrega
├── 1_check_data.ipynb                        # Prototipo de desarrollo
├── auxiliar_functions.py                     # Funciones auxiliares
├── gdm_first_trimester_ml_dataset.csv        # Dataset principal
├── gdm_first_trimester_ml_dataset_metadata.json
├── INSTRUCCIONES.md                          # Guía práctica original
├── TASKS.md                                  # Tareas por sección
├── TASK2.md                                  # Tareas por prioridad
├── README.md                                 # Este archivo
├── .gitignore                                # Configuración Git
└── __pycache__/
    └── README.md                             # Evaluación de progreso
```

---

**Universidad de Magallanes**  
**Facultad de Ingeniería - Departamento de Ingeniería en Computación**  
**Asignatura**: Matemática para Ciencias de la Computación
