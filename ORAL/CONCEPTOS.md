# Glosario y Explicación de Métodos Utilizados en el Informe

Este documento preliminar recopila los conceptos, métodos y decisiones metodológicas aplicadas en el análisis exploratorio del dataset de diabetes gestacional. Organizado por orden de aparición en el informe.

---

## 1. CONCEPTOS FUNDAMENTALES DEL DATASET

### 1.1 Dataset Sintético vs Real
- **Concepto:** Se utilizó un dataset sintético (simulado) diseñado para reflejar patrones clínicos reales
- **Justificación:** Permite controlar completamente variables conocidas sin sesgos no controlados
- **Limitación:** Los hallazgos deben validarse en poblaciones reales antes de aplicación clínica

### 1.2 Prevalencia de GDM - Desbalance de Clases
- **Concepto:** El dataset presenta ~17% de casos positivos de GDM y ~83% negativos
- **Justificación:** Refleja la prevalencia real de GDM en poblaciones de riesgo moderado
- **Relevancia:** Afecta el diseño de análisis comparativos (no es balance 50-50)

### 1.3 Datos Faltantes (Missing Data)
- **MCAR (Missing Completely At Random):** Ausencia de datos sin relación con otras variables
- **MAR (Missing At Random):** Valores faltantes relacionados con variables observadas
- **Decisión tomada:** Se utilizó exclusión por lista (listwise deletion) en análisis posteriores
- **Consideración:** La imputación múltiple no fue explorada en este trabajo

---

## 2. ANÁLISIS EXPLORATORIO - ESTADÍSTICA DESCRIPTIVA

### 2.1 Medidas de Tendencia Central y Dispersión
- **Se calcularon:** Media, mediana, desviación estándar, percentiles (25%, 75%)
- **Objetivo:** Caracterizar la distribución de todas las variables continuas
- **Resultado:** Base descriptiva para identificar asimetrías y valores extremos

### 2.2 Rango Intercuartílico (IQR)
- **Fórmula:** IQR = Q75 - Q25
- **Uso:** Identificación inicial de límites para valores atípicos
- **Ventaja:** Método robusto, insensible a valores extremos

---

## 3. DETECCIÓN DE VALORES ATÍPICOS (OUTLIERS)

### 3.1 Método IQR (Rango Intercuartílico)
- **Concepto:** Detecta valores fuera del rango [Q25 - 1.5×IQR, Q75 + 1.5×IQR]
- **Tipo:** Univariado (se aplica a cada variable por separado)
- **Ventaja:** Método clásico, fácil de interpretar
- **Limitación:** No detecta combinaciones anómalas en múltiples dimensiones

### 3.2 Isolation Forest
- **Concepto:** Algoritmo de machine learning no supervisado que aísla observaciones anómalas mediante particiones aleatorias
- **Tipo:** Multivariado (considera relaciones entre múltiples variables)
- **Aplicación 1 - Solo categóricas:** Detecta combinaciones inusuales de factores de riesgo binarios
- **Aplicación 2 - Solo continuas:** Identifica valores extremos en mediciones clínicas
- **Aplicación 3 - Todas las variables:** Enfoque integral combinando información categórica y continua
- **Ventaja:** Efectivo en espacios multidimensionales

### 3.3 Sistema de Votación para Outliers
- **Concepto:** Combina 4 métodos complementarios (IQR + 3 variantes de Isolation Forest)
- **Votación:**
  - 0 votos: Registro normal según todos los métodos
  - 1-2 votos: Posible outlier leve (se conserva)
  - 3 votos: Outlier moderado (se elimina)
  - 4 votos: Outlier extremo (se elimina)
- **Decisión:** Se eliminan registros con vote_outlier ≥ 3
- **Justificación de conservadurismo:** Preserva variabilidad biológica natural, elimina solo casos extremos

### 3.4 Rationale de Múltiples Métodos
- **Razón:** Un método solo podría sesgar la detección (sensibilidad/especificidad variable)
- **Ventaja de votación:** Mayor robustez y consenso entre métodos
- **Tradeoff:** Balance entre eliminar verdaderos outliers y conservar datos legítimos pero inusuales

---

## 4. PREPARACIÓN DE DATOS PARA ANÁLISIS POSTERIORES

### 4.1 Dataset Filtrado (df_filter)
- **Concepto:** Dataset de trabajo después de eliminar outliers extremos
- **Criterio:** Se mantienen registros con vote_outlier < 3
- **Uso:** Todos los análisis estadísticos posteriores (pruebas de hipótesis, correlaciones, etc.)
- **Ventaja:** Mejora la estabilidad de estimadores estadísticos

---

## 5. INTERVALOS DE CONFIANZA

### 5.1 Intervalo de Confianza para la Media
- **Concepto:** Rango de valores que probablemente contiene el parámetro poblacional μ con cierto nivel de confianza
- **Nivel utilizado:** 95% (α = 0.05)
- **Método paramétrico:** Utiliza distribución t de Student
- **Supuesto:** Normalidad de los datos (o n grande por Teorema del Límite Central)

### 5.2 Intervalo de Confianza para la Varianza
- **Concepto:** Rango de valores para el parámetro poblacional σ²
- **Método:** Utiliza distribución chi-cuadrado
- **Uso:** Menos frecuente en interpretación clínica que IC de la media

### 5.3 Cambio Metodológico: De Submuestras a Muestra Completa
- **Fase inicial:** Se calculaban IC variando tamaño muestral (n = 10 a 100)
- **Problema identificado:** Introduce sesgos de muestreo repetido que afecta reproducibilidad
- **Decisión tomada:** Calcular IC sobre la muestra completa (n ≈ 1500)
- **Ventaja:** Estimaciones más robustas y representativas de parámetros poblacionales
- **Lección metodológica:** Se evitó sesgo por submuestreo aleatorio repetido

### 5.4 IC Paramétricos vs Percentílicos
- **Paramétricos:** Basados en distribución t, requieren normalidad (o n grande)
- **Percentílicos:** Basados en bootstrap, robustos sin asumir distribución
- **Decisión:** Se utilizan ambos cuando normalidad es dudosa
- **Complementariedad:** Aumenta confianza en hallazgos

---

## 6. PRUEBAS DE HIPÓTESIS

### 6.1 Estructura General de Prueba de Hipótesis
1. **Formulación:** H₀ (hipótesis nula) y H₁ (alternativa)
2. **Verificación de supuestos:** Normalidad, homocedasticidad, independencia
3. **Selección de prueba:** Según cumplimiento de supuestos
4. **Cálculo e interpretación:** Estadístico, p-valor, decisión

### 6.2 Prueba de Normalidad - Shapiro-Wilk
- **Concepto:** Prueba H₀: "los datos provienen de distribución normal"
- **Estadístico:** W (varía entre 0 y 1)
- **Criterio de rechazo:** p-valor < 0.05 → distribución no normal
- **Ventaja:** Mayor potencia que Kolmogorov-Smirnov en muestras pequeñas
- **Hallazgo:** Mayoría de variables no cumplieron normalidad (p < 0.05)

### 6.3 Prueba de Normalidad - Kolmogorov-Smirnov (KS)
- **Concepto:** Compara distribución empírica con normal teórica
- **Uso:** Confirmación adicional de Shapiro-Wilk
- **Ventaja:** Complementaria, no depende solo de Shapiro-Wilk

### 6.4 Prueba de Homogeneidad de Varianzas - Levene
- **Concepto:** H₀: "Las varianzas de los grupos son iguales" (homocedasticidad)
- **Uso:** Antes de seleccionar entre t-test clásico vs Welch
- **Criterio:** p < 0.05 → varianzas desiguales (heterocedasticidad)
- **Decisión:** Si se detecta heterocedasticidad, usar Welch t-test

### 6.5 Comparación de Dos Grupos - Variables Continuas

#### 6.5.1 Árbol de Decisión para Seleccionar Prueba
```
¿Normalidad en ambos grupos? (Shapiro-Wilk, p ≥ 0.05)
├─ SÍ → ¿Homocedasticidad? (Levene, p ≥ 0.05)
│       ├─ SÍ → t-test de Student (paramétrico)
│       └─ NO → Welch t-test (paramétrico, varianzas desiguales)
└─ NO → Mann-Whitney U (no paramétrico)
```

#### 6.5.2 t-test de Student (paramétrico, varianzas iguales)
- **Concepto:** Compara medias de dos grupos independientes
- **Supuestos:** Normalidad + homocedasticidad
- **Aplicación:** Pocas variables en este dataset cumplieron supuestos

#### 6.5.3 Welch t-test (paramétrico, varianzas desiguales)
- **Concepto:** Versión robusta del t-test
- **Supuestos:** Solo normalidad (no requiere homocedasticidad)
- **Ventaja:** Mejor para datos con varianzas diferentes entre grupos

#### 6.5.4 Mann-Whitney U (no paramétrico)
- **Concepto:** Compara medianas (o distribuciones) de dos grupos independientes
- **Supuestos:** Mínimos (distribución libre)
- **Uso en este informe:** Mayoría de variables continuas
- **Ventaja:** Robusta a no normalidad y outliers

### 6.6 Comparación de Proporciones - Variables Binarias

#### 6.6.1 Tabla de Contingencia
- **Concepto:** Tabla 2×2 que resume frecuencias de co-ocurrencia de dos variables binarias
- **Datos almacenados:** n11, n10, n01, n00 (frecuencias por celda)

#### 6.6.2 Prueba Chi-cuadrado (χ²)
- **Concepto:** Prueba H₀: "Las variables son independientes" (no hay asociación)
- **Supuesto:** Todos los valores esperados ≥ 5
- **Uso:** Cuando supuesto se cumple

#### 6.6.3 Prueba Exacta de Fisher
- **Concepto:** Alternativa a Chi-cuadrado para muestras pequeñas
- **Supuesto:** No requiere mínimos en frecuencias esperadas
- **Uso:** Cuando algún valor esperado < 5

### 6.7 Comparación de Múltiples Grupos (k > 2)

#### 6.7.1 ANOVA de Un Factor (paramétrico)
- **Concepto:** Compara medias de k grupos
- **Supuestos:** Normalidad en todos los grupos + homocedasticidad
- **Hipótesis:** H₀: μ₁ = μ₂ = ... = μₖ

#### 6.7.2 Kruskal-Wallis (no paramétrico)
- **Concepto:** Alternativa no paramétrica a ANOVA
- **Supuestos:** Distribución libre
- **Uso:** Cuando ANOVA no es aplicable

### 6.8 Decisión Estadística e Interpretación
- **Nivel de significancia:** α = 0.05 (estándar biomédico)
- **Criterio de rechazo:** p-valor < α
- **Rechazo de H₀:** Evidencia de diferencia/asociación significativa
- **No rechazo de H₀:** Insuficiente evidencia de diferencia (NO significa que H₀ es verdadera)

### 6.9 Impacto de la Falta de Normalidad en Pruebas
- **Hallazgo:** Mayoría de variables no normales
- **Implicación:** Validez de pruebas paramétricas cuestionable
- **Mitigación implementada:**
  1. Verificación automática de supuestos antes de cada prueba
  2. Uso de alternativas no paramétricas cuando supuestos fallan
  3. Confirmación con IC percentílicos

---

## 7. ANÁLISIS BIVARIADO - CORRELACIONES

### 7.1 Correlación de Pearson
- **Concepto:** Mide fuerza de asociación lineal entre dos variables continuas
- **Rango:** r ∈ [-1, 1]
  - r ≈ 1: Correlación lineal positiva perfecta
  - r ≈ 0: Sin correlación lineal
  - r ≈ -1: Correlación lineal negativa perfecta
- **Supuesto:** Linealidad (relación lineal entre variables)
- **Sensibilidad:** Afectada por outliers y datos no normales

### 7.2 Correlación de Spearman
- **Concepto:** Mide fuerza de asociación monotónica entre variables
- **Método:** Basada en rangos (ordinal), no valores originales
- **Ventaja:** Robusta a outliers y no normalidad
- **Uso:** Complementaria a Pearson cuando datos no son normales

### 7.3 Matrices de Correlación
- **Concepto:** Tabla donde cada entrada (i,j) es la correlación entre variable i y j
- **Simetría:** Matriz simétrica alrededor de diagonal principal
- **Diagonal:** Siempre = 1 (cada variable correlaciona perfectamente consigo misma)

### 7.4 Análisis Estratificado por Grupo GDM
- **Concepto:** Se calculan correlaciones separadas para GDM+ y GDM-
- **Objetivo:** Detectar si la estructura de relaciones cambia entre grupos
- **Hallazgo:** Estructura similar entre grupos (diferencias máximas < 0.16)
- **Implicación:** No se requieren modelos de correlación distintos por grupo

### 7.5 Visualización - Heatmaps
- **Concepto:** Mapa de calor donde color indica magnitud de correlación
- **Convención:** Azul = correlación positiva, Rojo = negativa
- **Utilidad:** Identificación rápida de patrones y asociaciones fuertes

### 7.6 Visualización - Pairplot
- **Concepto:** Matriz de gráficos mostrando todas las relaciones bivariadas
- **Diagonal:** Distribución marginal (univariada) de cada variable
- **Resto:** Scatterplots entre pares de variables
- **Estratificación:** Colores diferentes para GDM+ vs GDM-
- **Utilidad:** Detección de clusters, separabilidad entre grupos

### 7.7 Colinealidad
- **Concepto:** Cuando dos variables predictoras están fuertemente correlacionadas (r > 0.7)
- **Problema:** En modelos multivariados, dificulta estimación de efectos individuales
- **Detección:** Inspeccionar matriz de correlación para |r| > 0.7
- **Hallazgo:** Pocas variables con colinealidad severa (excepto relaciones matemáticas)
- **Ejemplo de relación matemática:** Insulina vs HOMA-IR (r ≈ 0.85) porque HOMA-IR se calcula con insulina

---

## 8. DECISIONES SOBRE SESGOS Y LIMPIEZA DE DATOS

### 8.1 Evitar Sesgo de Submuestreo Repetido
- **Problema identificado:** Submuestreo aleatorio repetido introduce variabilidad artificial
- **Solución:** Usar muestra completa para cálculos de IC y parámetros
- **Justificación:** "Se decidió usar el grupo completo en vez de submuestras para evitar sesgos de muestreo"

### 8.2 Criterio Conservador de Eliminación de Outliers
- **Decisión:** Eliminar solo records con vote_outlier ≥ 3 (acordancia de 3 o 4 métodos)
- **Justificación:** Balance entre datos limpios y preservación de variabilidad biológica
- **Alternativa rechazada:** Eliminar con vote_outlier ≥ 1 (demasiado agresivo)

### 8.3 Selección de Pruebas Estadísticas según Supuestos
- **Regla:** Verificar supuestos ANTES de elegir prueba
- **Transparencia:** Reportar resultado de verificación junto con prueba utilizada
- **Robustez:** Usar alternativas no paramétricas cuando supuestos fallan

---

## 9. VARIABLES Y MEDIDAS CLÍNICAS

### 9.1 Medidas Demográficas
- **age_years:** Edad de la paciente (años)
- **gestational_weeks:** Semanas de gestación al momento de medición

### 9.2 Medidas Antropométricas
- **bmi_prepreg_kg_m2:** Índice de masa corporal pregestacional (kg/m²)
- **Importancia clínica:** Factor de riesgo establecido para GDM

### 9.3 Medidas Hemodinámicas
- **systolic_bp_mmHg:** Presión arterial sistólica (mmHg)
- **diastolic_bp_mmHg:** Presión arterial diastólica (mmHg)
- **map_mmHg:** Presión arterial media (mmHg) - calculada como PAD + 1/3(PAS - PAD)

### 9.4 Medidas de Control Glucémico
- **fpg_mmol_l:** Glucosa plasmática en ayunas (mmol/L)
- **hba1c_percent:** Hemoglobina glicosilada (%) - refleja control glucémico de últimos 2-3 meses
- **Importancia clínica:** Indicadores tempranos de disfunción glucémica

### 9.5 Medidas de Resistencia a la Insulina
- **insulin_uIU_ml:** Insulina sérica (μIU/mL)
- **homa_ir:** Índice HOMA-IR (Homeostasis Model Assessment - Insulin Resistance)
  - **Fórmula:** HOMA-IR = (Insulina × Glucosa) / 22.5
  - **Interpretación:** Estima resistencia a la insulina basal
  - **Correlación con insulina:** r ≈ 0.85 (por definición matemática)

### 9.6 Medidas de Perfil Lipídico
- **triglycerides_mmol_l:** Triglicéridos séricos (mmol/L)
- **hdl_mmol_l:** Colesterol HDL (mmol/L)
- **Importancia clínica:** Componentes del síndrome metabólico

### 9.7 Variables de Antecedentes Obstétricos
- **parity:** Paridad (número de embarazos previos)
- **previous_gdm:** Antecedente de GDM previa (0/1) - Factor de riesgo fuerte
- **family_history_t2d:** Antecedentes familiares de diabetes tipo 2 (0/1)

### 9.8 Variables de Comorbilidades
- **pcos:** Síndrome de ovario poliquístico (0/1)
- **Relevancia:** Comparte mecanismo de resistencia a insulina con GDM

### 9.9 Variables de Estilo de Vida
- **smoking_first_trimester:** Tabaquismo durante primer trimestre (0/1)
- **physical_activity_level:** Nivel de actividad física (escala ordinal)
- **diet_score_0_100:** Puntuación de calidad dietética (0-100)

### 9.10 Variable Objetivo
- **label_gdm:** Diagnóstico de diabetes gestacional (0 = No GDM, 1 = GDM)

---

## 10. TÉCNICAS DE VISUALIZACIÓN

### 10.1 Histograma con KDE (Kernel Density Estimation)
- **Concepto:** Histograma que muestra frecuencias + curva suave de densidad
- **KDE:** Estimación no paramétrica de función de densidad de probabilidad
- **Uso:** Comparar distribuciones entre dos grupos
- **Estratificación:** Colores diferentes para GDM+ y GDM-

### 10.2 Boxplot
- **Concepto:** Visualiza 5 números (min, Q1, mediana, Q3, max)
- **Caja:** Representa IQR (contiene 50% de datos)
- **Línea interior:** Mediana
- **Bigotes:** Típicamente 1.5×IQR
- **Puntos:** Valores extremos (outliers)
- **Uso:** Detectar asimetría, outliers, y comparar distribuciones entre grupos

### 10.3 Violinplot
- **Concepto:** Combinación de boxplot + KDE reflejo (forma de violín)
- **Ventaja:** Muestra forma completa de distribución
- **Uso:** Mejor que boxplot cuando distribuciones tienen formas inusuales

---

## 11. HERRAMIENTAS Y LIBRERÍAS UTILIZADAS

### 11.1 Pandas
- **Concepto:** Librería Python para manipulación y análisis de datos
- **Estructuras:** DataFrames (tablas 2D) y Series (vectores 1D)
- **Uso:** Carga, transformación y consultas de datos

### 11.2 NumPy
- **Concepto:** Librería para computación numérica y álgebra lineal
- **Uso:** Operaciones vectorizadas, generación de números aleatorios, funciones matemáticas

### 11.3 SciPy (Stats)
- **Concepto:** Librería para computación científica, incluye funciones estadísticas
- **Módulo stats:** Contiene pruebas estadísticas (Shapiro, Levene, t-test, Mann-Whitney, etc.)
- **Uso:** Principal para análisis estadísticos

### 11.4 Scikit-learn
- **Concepto:** Librería de machine learning
- **Uso en informe:** IsolationForest para detección de anomalías

### 11.5 Matplotlib
- **Concepto:** Librería para creación de gráficos estáticos
- **Uso:** Crear figuras con múltiples subplots

### 11.6 Seaborn
- **Concepto:** Librería de visualización estadística (construida sobre Matplotlib)
- **Funciones utilizadas:**
  - histplot: Histogramas
  - boxplot: Diagramas de caja
  - violinplot: Diagramas de violín
  - heatmap: Mapas de calor
  - pairplot: Matrices de scatterplots
- **Ventaja:** Sintaxis más intuitiva y estética mejorada

---

## 12. FUNCIONES AUXILIARES PERSONALIZADAS

### 12.1 calculate_ic_mean()
- **Concepto:** Calcula intervalo de confianza para la media
- **Parámetros:** media, desviación estándar, tamaño muestral, nivel de confianza
- **Método:** Distribución t de Student
- **Retorna:** Tupla (límite inferior, límite superior)

### 12.2 calculate_ic_std()
- **Concepto:** Calcula intervalo de confianza para la varianza
- **Método:** Distribución chi-cuadrado
- **Retorna:** Tupla (límite inferior, límite superior)

### 12.3 get_range_outlier()
- **Concepto:** Calcula límites de outliers basado en IQR
- **Fórmula:** [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
- **Retorna:** Tupla (límite inferior, límite superior)

### 12.4 check_is_outlier()
- **Concepto:** Determina si un valor está fuera del rango de outliers
- **Retorna:** 1 si es outlier, 0 si es normal

### 12.5 categorize_iqr()
- **Concepto:** Convierte conteo de outliers a binario
- **Lógica:** Si cuenta > 0 → outlier (1), si no → normal (0)

### 12.6 generate_df_counts()
- **Concepto:** Genera resumen de conteos de 0s y 1s por columna
- **Uso:** Crear tablas resumen de valores faltantes u outliers detectados

---

## 13. CONTROL DE CALIDAD Y VALIDACIÓN

### 13.1 Exploración Iterativa de Datos
- **Patrón:** Para cada operación importante, se ejecutan verificaciones exploratorias
- **Objetivo:** Confirmar que las transformaciones se realizaron correctamente
- **Ejemplo:** Después de crear df_filter, se verifica tamaño, columnas, y valores faltantes

### 13.2 Transparencia de Decisiones
- **Regla:** Documentar toda decisión metodológica con su justificación
- **Ejemplo:** "Se eliminan registros con vote_outlier ≥ 3 por razones de balance entre limpieza y preservación"

### 13.3 Reporteo de Supuestos
- **Práctica:** Siempre reportar resultado de verificación de supuestos junto con prueba utilizada
- **Ejemplo:** "Normalidad: ✗ No (p-Shapiro = 0.002) → Mann-Whitney U aplicado"

---

## 14. LIMITACIONES METODOLÓGICAS RECONOCIDAS

### 14.1 Datos Sintéticos
- **Limitación:** No hay variabilidad biológica genuina
- **Implicación:** Patrones pueden no generalizarse a datos reales

### 14.2 Diseño Transversal
- **Limitación:** No se puede establecer causalidad, solo asociación
- **Implicación:** Dirección de efectos es incierta

### 14.3 Análisis Univariado y Bivariado
- **Limitación:** No se realizó análisis multivariado (regresión logística)
- **Implicación:** No se pueden cuantificar efectos independientes ni controlar variables confusoras

### 14.4 Exclusión por Lista en Datos Faltantes
- **Limitación:** Puede introducir sesgos si datos no son MCAR
- **Alternativa no explorada:** Imputación múltiple

---

## NOTAS FINALES

Este documento preliminar establece la base conceptual y metodológica del informe. Cada sección puede expandirse con:
- Ejemplos numéricos específicos
- Referencias a secciones del informe donde se aplicó
- Detalles computacionales adicionales
- Justificaciones más profundas de elecciones metodológicas

**Próximo paso recomendado:** Reorganizar secciones según orden de importancia clínica o necesidades de la oral, completando con valores y contextos específicos conforme se requiera.
