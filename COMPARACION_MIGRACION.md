# Comparación de Migración: 1_check_data.ipynb → Entregable.ipynb

**Fecha de análisis:** 11 de noviembre de 2025  
**Analista:** GitHub Copilot  
**Objetivo:** Verificar integridad de la migración asistida por IA

---

## Resumen Ejecutivo

### Estadísticas Generales

| Métrica | `1_check_data.ipynb` | `Entregable.ipynb` | Diferencia |
|---------|---------------------|-------------------|------------|
| **Total de celdas** | 62 | 32 | -30 (-48%) |
| **Celdas de código** | 57 | 11 | -46 (-81%) |
| **Celdas markdown** | 5 | 21 | +16 (+320%) |
| **Líneas de código** | ~495 | ~670 | +175 (+35%) |

### Veredicto Global

🟡 **MIGRACIÓN INCOMPLETA CON PÉRDIDAS SIGNIFICATIVAS**

**Nivel de completitud:** ~40-50%

---

## Análisis Detallado por Sección

### 1. ✅ Importaciones y Configuración Inicial

#### `1_check_data.ipynb` (Celda #VSC-a068ee5a)
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from auxiliar_functions import *
from sklearn.ensemble import IsolationForest
from scipy import stats  # Para intervalos de confianza
```

#### `Entregable.ipynb` (Celda #VSC-ae26b6d9)
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from auxiliar_functions import *
from sklearn.ensemble import IsolationForest
from scipy import stats

# Configuración de visualización
plt.style.use('default')
sns.set_palette("husl")
%matplotlib inline
```

**Resultado:** ✅ **COMPLETO Y MEJORADO**
- Todas las librerías migradas correctamente
- **Añadido:** Configuración de visualización (mejora)
- **Añadido:** `%matplotlib inline` para notebooks

---

### 2. ✅ Carga y Exploración Básica del Dataset

#### Código Original (1_check_data.ipynb)
**Celdas 3-10:** 
- Carga de datos (`df_data.head()`)
- Dimensiones (`df_data.shape`)
- Conteo de clases (`label_gdm.value_counts()`)
- Tipos de datos (`df_data.dtypes`)
- Exploración de variables únicas
- Análisis de nulos (`isna().astype(int)`)
- Resumen de nulos con `generate_df_counts()`

#### Código Migrado (Entregable.ipynb)
**Celdas 8-13:**
- ✅ Carga con mensajes descriptivos
- ✅ Dimensiones con print formateado
- ✅ Distribución GDM con **proporción añadida** (mejora)
- ✅ Tipos de datos
- ✅ Resumen de valores faltantes

**Resultado:** ✅ **COMPLETO Y MEJORADO**
- Todo el código esencial migrado
- Añadidos prints descriptivos
- **Añadido:** Cálculo de proporción de casos positivos

**Código faltante no crítico:**
- ❌ `df_data["pcos"].unique().shape` (exploración menor)
- ❌ `df_nulls` completo sin resumen (redundante)

---

### 3. ✅ Estadística Descriptiva

#### Código Original (1_check_data.ipynb)
**Celdas 12-14:**
- Definición de `columns_to_ignore`
- `df_data.describe()`
- Cálculo de estadísticas con IQR y umbrales para outliers

#### Código Migrado (Entregable.ipynb)
**Celdas 15-17:**
- ✅ `columns_to_ignore` con print explicativo
- ✅ `df_data.describe()` con mensaje
- ✅ Estadísticas con IQR y umbrales (idéntico)

**Resultado:** ✅ **COMPLETO**
- Toda la lógica de cálculo estadístico migrada correctamente
- Estructura de `df_statistical` preservada

---

### 4. 🔴 Detección de Outliers - **CRÍTICO: INCOMPLETO**

#### Código Original (1_check_data.ipynb)
**Celdas 16-36:**
1. ✅ Detección por IQR (`df_outliers` con `check_is_outlier`)
2. ❌ **FALTANTE:** Resumen de outliers (`df_summary_outlier`)
3. ❌ **FALTANTE:** Exploración de columnas de outliers
4. ❌ **FALTANTE:** Análisis de proporciones categóricas
5. ❌ **FALTANTE:** Isolation Forest en 3 variantes:
   - Solo categóricas (`data_categorical`)
   - Solo valores continuos (`df_values`)
   - Todas las variables (`df_values_cat`)
6. ❌ **FALTANTE:** Creación de columnas de outliers en `df_data`:
   - `is_outlier_by_IQR`
   - `is_outlier_by_IF_all`
   - `is_outlier_by_IF_just_values`
   - `is_outlier_by_IF_just_cat`
7. ❌ **FALTANTE:** Transformación con `categorize_iqr()`
8. ❌ **FALTANTE:** Remapeo de valores Isolation Forest (1→0, -1→1)
9. ❌ **FALTANTE:** Sistema de votación (`vote_outlier`)
10. ❌ **FALTANTE:** Filtrado por votación (`df_filter = df_data[df_data["vote_outlier"]<3]`)

#### Código Migrado (Entregable.ipynb)
**Celda 18:** Solo markdown "### Detección de outliers"

**Resultado:** 🔴 **PÉRDIDA CRÍTICA DEL 95% DEL CÓDIGO**
- **Impacto:** El dataset filtrado `df_filter` NO SE CREA
- **Consecuencia:** Todas las visualizaciones y análisis posteriores que usen `df_filter` FALLARÁN
- **Código migrado:** 0% (solo nota markdown)

---

### 5. 🔴 Visualización de Datos - **FALTANTE COMPLETO**

#### Código Original (1_check_data.ipynb)
**Celdas 40-43:**
1. ❌ Histogramas con KDE por grupo GDM (3x5 subplots)
2. ❌ Boxplots por grupo GDM (3x5 subplots)
3. ❌ Violinplots por grupo GDM (3x5 subplots)

#### Código Migrado (Entregable.ipynb)
**Ninguna celda correspondiente**

**Resultado:** 🔴 **PÉRDIDA TOTAL**
- 0% del código de visualización migrado
- 3 gráficos complejos con subplots perdidos

---

### 6. 🔴 Análisis Bivariado - **PARCIAL CON PÉRDIDAS**

#### Código Original (1_check_data.ipynb)
**Celdas 45-54:**
1. ❌ Exploración de columnas (`df_filter.columns`)
2. ❌ Drop de columnas de outliers para análisis limpio
3. ✅ Correlación de Pearson (migrado)
4. ❌ **FALTANTE:** Correlación de Spearman
5. ✅ Heatmap de Pearson (migrado)
6. ❌ **FALTANTE:** Correlaciones separadas por grupo (GDM+ vs GDM-)
7. ❌ **FALTANTE:** Heatmap de diferencias entre grupos
8. ❌ **FALTANTE:** Pairplot con `hue="label_gdm"`

#### Código Migrado (Entregable.ipynb)
**Celda 30:**
- ✅ Cálculo de correlación de Pearson
- ✅ Heatmap básico con mejoras estéticas
- ✅ **AÑADIDO:** Identificación de correlaciones fuertes (|r| > 0.7)

**Resultado:** 🟡 **PARCIAL (40% migrado)**
- Correlación básica presente
- **Pérdidas importantes:**
  - Correlación de Spearman
  - Análisis por grupos separados (GDM+ vs GDM-)
  - Heatmap de diferencias
  - Pairplot completo
- **Nota crítica:** Comentario indica que requiere `df_filter` que NO EXISTE

---

### 7. ✅ Intervalos de Confianza

#### Código Original (1_check_data.ipynb)
**Celdas 56-57:**
- Generación de tamaños de muestra (`np.linspace(10, 100, 10)`)
- Bucle de muestreo con semilla aleatoria
- Cálculo de IC para media y varianza en 3 variables

#### Código Migrado (Entregable.ipynb)
**Celda 21:**
- ✅ Código idéntico migrado
- ✅ Comentarios explicativos preservados

**Resultado:** ✅ **COMPLETO (100%)**
- Toda la lógica migrada sin cambios
- Estructura de bucles preservada

---

### 8. ✅ Pruebas de Normalidad

#### Código Original (1_check_data.ipynb)
**Celda 59:**
- Definición de `continuous_variables`
- Limpieza de NaN por variable
- Pruebas de Shapiro-Wilk y KS-Lilliefors
- Decisiones sobre normalidad
- Almacenamiento en `normality_results`

#### Código Migrado (Entregable.ipynb)
**Celda 27:**
- ✅ Código idéntico migrado
- ✅ Lógica completa preservada
- ✅ **MEJORADO:** Formato de salida más claro

**Resultado:** ✅ **COMPLETO (100%)**
- Toda la lógica estadística migrada
- Estructura de datos preservada

---

### 9. ✅ Pruebas de Hipótesis (Comparación de Grupos)

#### Código Original (1_check_data.ipynb)
**Celda 60:**
- Función `compare_two_groups_numeric()` completa
- Verificación de supuestos (normalidad, homogeneidad)
- Selección automática de test (t-test/Welch/Mann-Whitney)
- Aplicación a presión arterial (3 variables)

#### Código Migrado (Entregable.ipynb)
**Celda 24:**
- ✅ Función completa migrada
- ✅ Lógica de decisión preservada
- ✅ Ejemplos aplicados
- ✅ **MEJORADO:** Formato de salida con separadores

**Resultado:** ✅ **COMPLETO (100%)**
- Función estadística crítica migrada sin pérdidas
- Todos los casos de uso incluidos

---

### 10. 🔴 Código de Exploración Adicional - **FALTANTE**

#### Código Original (1_check_data.ipynb)
**Celdas 23-27, 61-62:**
- ❌ Exploración de casos `parity == 5`
- ❌ Value counts de variables categóricas
- ❌ Verificación de `df_filter` final
- ❌ Celda vacía al final

#### Código Migrado (Entregable.ipynb)
**Ninguna celda correspondiente**

**Resultado:** 🟡 **FALTANTE (Código exploratorio no crítico)**
- Código de exploración ad-hoc no migrado
- No afecta análisis principal

---

## Análisis de Pérdidas Críticas

### 🔴 Pérdida Crítica #1: Sistema de Detección de Outliers
**Ubicación original:** Celdas 16-36 (21 celdas)  
**Código migrado:** 0%  
**Impacto:** CRÍTICO

#### Código faltante esencial:
```python
# 1. Detección por IQR
df_outliers = pd.DataFrame()
for column in df_data.columns:
    if column not in columns_to_ignore:
        df_filter = df_statistical[df_statistical["descriptor"] == column]
        df_filter.reset_index(inplace=True)
        min_value, max_value = df_filter["min_value_for_outlier"][0], df_filter["max_value_for_outlier"][0]
        df_outliers[column] = df_data[column].apply(lambda x: check_is_outlier(x, min_value, max_value))

df_outliers = df_outliers.astype(int)
df_summary_outlier = generate_df_counts(df_outliers, columns_name=["descriptor", "count_Outlier", "count_NotOutlier"])

# 2. Isolation Forest (3 variantes)
data_categorical = df_data[columns_to_ignore].drop(columns=["label_gdm"])
isolation_instance = IsolationForest(random_state=42)
isolation_instance.fit(data_categorical)
data_categorical["is_isolated"] = isolation_instance.predict(data_categorical)

df_values = df_data.drop(columns=columns_to_ignore)
isolation_instance = IsolationForest(random_state=42)
isolation_instance.fit(df_values)
df_values["is_isolated"] = isolation_instance.predict(df_values)

df_values_cat = df_data.drop(columns=["label_gdm"])
isolation_instance = IsolationForest(random_state=42)
isolation_instance.fit(df_values_cat)
df_values_cat["is_isolated"] = isolation_instance.predict(df_values_cat)

# 3. Agregación de resultados
df_data["is_outlier_by_IQR"] = df_outliers["outlier_by_IQR"].values
df_data["is_outlier_by_IF_all"] = df_values_cat["is_isolated"].values
df_data["is_outlier_by_IF_just_values"] = df_values["is_isolated"].values
df_data["is_outlier_by_IF_just_cat"] = data_categorical["is_isolated"].values

# 4. Categorización y votación
df_data["is_outlier_by_IQR"] = df_data["is_outlier_by_IQR"].apply(categorize_iqr)
for column in ["is_outlier_by_IF_all", "is_outlier_by_IF_just_values", "is_outlier_by_IF_just_cat"]:
    df_data[column] = df_data[column].replace({1:0, -1:1})

df_data["vote_outlier"] = df_data[["is_outlier_by_IF_all", "is_outlier_by_IF_just_values", 
                                     "is_outlier_by_IF_just_cat", "is_outlier_by_IQR"]].sum(axis=1)

# 5. FILTRADO FINAL (CRÍTICO)
df_filter = df_data[df_data["vote_outlier"]<3]
```

#### Consecuencias:
- ❌ Variable `df_filter` NO SE CREA → Todas las celdas posteriores que la usen FALLARÁN
- ❌ No hay limpieza de outliers aplicada
- ❌ Análisis bivariado opera sobre datos sin filtrar (incorrecto según metodología)
- ❌ Visualizaciones posteriores no funcionarán

---

### 🔴 Pérdida Crítica #2: Visualizaciones Completas
**Ubicación original:** Celdas 40-43  
**Código migrado:** 0%  
**Impacto:** ALTO

#### Código faltante:
1. **Histogramas con KDE (3x5 subplots)**
2. **Boxplots (3x5 subplots)**
3. **Violinplots (3x5 subplots)**

Cada gráfico muestra 15 variables separadas por grupo GDM con:
- Configuración de subplots (3 filas x 5 columnas)
- Iteración sobre `df_statistical["descriptor"].values`
- Separación por `hue="label_gdm"`

---

### 🔴 Pérdida Crítica #3: Análisis Bivariado Avanzado
**Ubicación original:** Celdas 47-54  
**Código migrado:** 30%  
**Impacto:** ALTO

#### Código faltante:
```python
# Correlación de Spearman
df_corr_spearman = df_filter.drop(columns=["label_gdm"]).corr(method="spearman")

# Correlaciones por grupo
df_corr_pearson_pos = df_filter[df_filter["label_gdm"] == 1].corr(method="pearson")
df_corr_pearson_neg = df_filter[df_filter["label_gdm"] == 0].corr(method="pearson")

# Heatmaps separados
sns.heatmap(data=df_corr_pearson_pos, annot=True, fmt=".2f", cmap="Blues")
sns.heatmap(data=df_corr_pearson_neg, annot=True, fmt=".2f", cmap="Blues")

# Heatmap de diferencias
sns.heatmap(data=df_corr_pearson_neg-df_corr_pearson_pos, annot=True, fmt=".2f", cmap="Blues")

# Pairplot
sns.pairplot(data=df_filter, hue="label_gdm")
```

---

## Problemas de Dependencias

### Dependencia Rota: `df_filter`

**Variable crítica NO creada que afecta a:**

1. ✅ Celda 30 (Entregable): Análisis bivariado - **Código presente pero FALLARÁ**
   ```python
   df_corr_pearson = df_filter.drop(columns=["label_gdm"]).corr(method="pearson")
   # NameError: name 'df_filter' is not defined
   ```

2. ❌ Todas las visualizaciones del original (no migradas)

3. ❌ Análisis de correlaciones por grupo (no migrado)

**Solución requerida:** Migrar completamente las celdas 16-38 del original antes de poder ejecutar análisis posteriores.

---

## Mejoras Introducidas en la Migración

A pesar de las pérdidas, se identifican **mejoras** en el notebook destino:

### ✅ Mejoras en Documentación
1. **Estructura clara con secciones markdown detalladas**
   - Tabla de progreso global
   - Descripciones de contexto
   - Estados visuales (🟢🟡🔴)

2. **Comentarios explicativos en código**
   - Prints descriptivos antes de cada operación
   - Mensajes de contexto para el usuario

3. **Formato profesional**
   - Headers jerárquicos
   - Separadores visuales
   - Indicadores de tareas pendientes

### ✅ Mejoras en Código
1. **Configuración de visualización** (celda 6)
   ```python
   plt.style.use('default')
   sns.set_palette("husl")
   %matplotlib inline
   ```

2. **Cálculos adicionales** (celda 10)
   ```python
   print(f"\nProporción de casos positivos: {df_data['label_gdm'].mean():.2%}")
   ```

3. **Identificación automática de correlaciones fuertes** (celda 30)
   ```python
   for i in range(len(df_corr_pearson.columns)):
       for j in range(i+1, len(df_corr_pearson.columns)):
           corr_value = df_corr_pearson.iloc[i, j]
           if abs(corr_value) > 0.7:
               print(f"{...}: r = {corr_value:.3f}")
   ```

4. **Formato de salida mejorado** (celda 24, 27)
   - Separadores visuales (`"=" * 70`)
   - Prints organizados

---

## Resumen de Completitud por Sección

| Sección | Original (celdas) | Migrado (celdas) | % Código | Estado | Crítico |
|---------|------------------|------------------|----------|--------|---------|
| **Importaciones** | 1 | 1 | 100% | ✅ Completo | No |
| **Carga datos** | 8 | 5 | 90% | ✅ Casi completo | No |
| **Estadística descriptiva** | 3 | 3 | 100% | ✅ Completo | No |
| **Detección outliers** | 21 | 0 | 0% | 🔴 Faltante | **SÍ** |
| **Visualizaciones** | 4 | 0 | 0% | 🔴 Faltante | Sí |
| **Análisis bivariado** | 10 | 1 | 30% | 🔴 Incompleto | Sí |
| **Intervalos confianza** | 2 | 1 | 100% | ✅ Completo | No |
| **Pruebas normalidad** | 1 | 1 | 100% | ✅ Completo | No |
| **Pruebas hipótesis** | 1 | 1 | 100% | ✅ Completo | No |
| **Exploración adicional** | 5 | 0 | 0% | 🟡 Faltante | No |
| **TOTAL** | **56 celdas código** | **13 celdas código** | **~45%** | 🟡 **Parcial** | - |

---

## Conclusiones y Recomendaciones

### ❌ Problemas Críticos Identificados

1. **CRÍTICO:** Variable `df_filter` no se crea → Análisis posteriores fallarán
2. **CRÍTICO:** Sistema completo de detección de outliers no migrado (0%)
3. **ALTO:** Todas las visualizaciones principales faltantes (0%)
4. **ALTO:** Análisis bivariado avanzado incompleto (70% faltante)

### ✅ Aspectos Positivos

1. Funciones estadísticas críticas migradas correctamente (IC, normalidad, hipótesis)
2. Estructura documental mejorada significativamente
3. Código base (carga, exploración inicial) completo
4. Mejoras en legibilidad y formato

### 🔧 Acciones Correctivas Requeridas

#### Prioridad CRÍTICA (Bloquea ejecución)

1. **Migrar sistema de detección de outliers completo**
   - Celdas 16-36 del original
   - Asegurar creación de `df_filter`
   - ~150 líneas de código

#### Prioridad ALTA (Funcionalidad incompleta)

2. **Migrar visualizaciones principales**
   - Histogramas con KDE (celda 41)
   - Boxplots (celda 42)
   - Violinplots (celda 43)
   - ~75 líneas de código

3. **Completar análisis bivariado**
   - Correlación de Spearman
   - Correlaciones por grupo (GDM+ vs GDM-)
   - Heatmaps de diferencias
   - Pairplot
   - ~40 líneas de código

#### Prioridad MEDIA (Mejoras opcionales)

4. **Código exploratorio adicional**
   - Exploración de variables categóricas
   - Value counts detallados
   - ~20 líneas de código

### 📊 Estimación de Trabajo Restante

| Tarea | Líneas código | Celdas | Tiempo est. |
|-------|---------------|--------|-------------|
| Detección outliers | ~150 | 20 | 45-60 min |
| Visualizaciones | ~75 | 3 | 20-30 min |
| Análisis bivariado | ~40 | 6 | 15-20 min |
| Exploración adicional | ~20 | 3 | 5-10 min |
| **TOTAL** | **~285** | **32** | **90-120 min** |

### 🎯 Nivel de Completitud Final

**Actual:** 45% del código migrado  
**Con acciones críticas:** 75% funcional  
**Con todas las acciones:** 95% completo

---

## Anexo: Mapeo Detallado de Celdas

### Celdas Migradas Correctamente

| Original (ID) | Original (Líneas) | Migrado (ID) | Migrado (Líneas) | Contenido |
|---------------|------------------|--------------|-----------------|-----------|
| #VSC-a068ee5a | 2-8 | #VSC-ae26b6d9 | 102-113 | Importaciones + config |
| #VSC-860a2909 | 14-15 | #VSC-9beaf152 | 119-124 | Carga dataset |
| #VSC-948c08fe | 18 | #VSC-8996a9be | 127-131 | Dimensiones |
| #VSC-d0b907d2 | 21 | #VSC-6d79bfb7 | 134-137 | Distribución GDM |
| #VSC-462854e5 | 24 | #VSC-f0a6fba4 | 140-142 | Tipos de datos |
| #VSC-c384178a | 33-36 | #VSC-7fb0cee5 | 148-151 | Resumen nulos |
| #VSC-12f73fd9 | 45-53 | #VSC-9c95b2ce | 159-170 | columns_to_ignore |
| #VSC-f3269bbe | 56 | #VSC-4ac33a2f | 173-175 | describe() |
| #VSC-73f843b9 | 59-86 | #VSC-89733963 | 178-206 | Estadísticas + IQR |
| #VSC-90875e10 | 331-359 | #VSC-d3f26649 | 237-268 | Intervalos confianza |
| #VSC-ed0b60d3 | 365-428 | #VSC-e37c4c5e | 381-441 | Pruebas normalidad |
| #VSC-16294833 | 431-488 | #VSC-bebb1ae0 | 296-353 | compare_two_groups |

### Celdas NO Migradas (Pérdidas)

| Original (ID) | Líneas | Tipo | Contenido | Impacto |
|---------------|--------|------|-----------|---------|
| #VSC-b8dcf804 | 27 | Código | unique() de pcos | Bajo |
| #VSC-2c5cf950 | 30 | Código | df_nulls sin resumen | Bajo |
| #VSC-cf3d377a | 39 | Código | Mostrar df_nulls | Bajo |
| **#VSC-b7dfc0af** | **92-102** | **Código** | **Detección outliers IQR** | **CRÍTICO** |
| **#VSC-6668fed0** | **105-107** | **Código** | **Resumen outliers** | **CRÍTICO** |
| **#VSC-c081b2c3 - #VSC-60df1e51** | **110-193** | **Código** | **Sistema outliers completo** | **CRÍTICO** |
| **#VSC-7e8113f9 - #VSC-0658ae10** | **199-276** | **Código** | **Visualizaciones (3 tipos)** | **Alto** |
| #VSC-5554f36a | 282 | Código | df_filter.columns | Bajo |
| #VSC-d88ac6eb | 285 | Código | Ver columns_to_ignore | Bajo |
| **#VSC-a9aa374d** | **288-296** | **Código** | **Drop columnas para bivariado** | **Alto** |
| **#VSC-d949d500** | **299-300** | **Código** | **Correlación Spearman** | **Alto** |
| #VSC-dbe8c96d | 303 | Código | Heatmap básico | Medio |
| **#VSC-1f10d5e3 - #VSC-9e6ce3f8** | **306-320** | **Código** | **Análisis por grupo + pairplot** | **Alto** |
| #VSC-c1170c4a | 126 | Código | Filtro parity==5 | Bajo |
| #VSC-584282c3 | 129-130 | Código | Value counts categóricas | Bajo |
| #VSC-4c91ae42 | 491 | Código | Mostrar df_filter | Bajo |

---

**Documento generado por:** GitHub Copilot  
**Fecha:** 11 de noviembre de 2025  
**Versión:** 1.0
