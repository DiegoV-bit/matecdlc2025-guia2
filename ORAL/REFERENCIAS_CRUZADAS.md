# REFERENCIAS CRUZADAS - Dónde Encontrar Cada Concepto en el Informe

Documento de navegación rápida que indica en qué sección exacta del notebook se encuentran los conceptos, métodos y resultados.

---

## BUSCAR POR CONCEPTO → UBICACIÓN EN INFORME

### A - ANÁLISIS BIVARIADO
- **Correlación de Pearson** → Sección 2.5.1, celdas 95-96
- **Correlación de Spearman** → Sección 2.5.1, celdas 95-96
- **Heatmap de Correlaciones** → Sección 2.5.1, celda 95
- **Pairplot Estratificado** → Sección 2.5.3, celda 3e6654a6

### B - BOXPLOT
- **Visualización Boxplot** → Sección 2.1.6, celda b067c09e

### C - CHI-CUADRADO
- **Prueba Chi-cuadrado** → Sección 2.3.2, celda 2b71faaf
- **vs Fisher Exacto** → Sección 2.3.2, celda 2b71faaf

### D - DETECCIÓN DE OUTLIERS
- **IQR Método** → Sección 2.1.5, celda 4fc22d1d
- **Isolation Forest** → Sección 2.1.5.2, celdas 65bbb1ff, 1e1e15f5, b0fa89e6, 96ead88e
- **Sistema de Votación** → Sección 2.1.5.3, celdas ad74bf5c - d20dc0ab
- **Filtrado de Outliers** → Sección 2.1.5.4, celda 2961687b

### E - ESTADÍSTICA DESCRIPTIVA
- **Medidas de Tendencia Central** → Sección 2.1.4, celdas 266c31b0, 06fdfeba
- **IQR Calculation** → Sección 2.1.4, celda 06fdfeba

### F - FISHER EXACTO
- **Prueba exacta de Fisher** → Sección 2.3.2, celda 2b71faaf

### G - GRÁFICOS / VISUALIZACIONES
- **Histogramas con KDE** → Sección 2.1.6, celda e0c422c9
- **Boxplots** → Sección 2.1.6, celda 70889ece
- **Violinplots** → Sección 2.1.6, celda 8fb002b1
- **Intervalos de Confianza (Gráfico)** → Sección 2.2.2, celda 0560fe91
- **Heatmaps de Correlación** → Sección 2.5.2, celdas 95cd96ee, a990970b, 836c0fb1

### H - HISTOGRAMA
- **Histograma con KDE** → Sección 2.1.6, celda e0c422c9

### I - INTERVALOS DE CONFIANZA
- **Cambio Metodológico** → Sección 2.2.1, celda a715fa15
- **IC Muestra Completa** → Sección 2.2.2, celda 554d4d5d
- **IC Media (Paramétrico)** → Sección 2.2, celda calculate_ic_mean (auxiliar)
- **IC Varianza** → Sección 2.2, celda calculate_ic_std (auxiliar)
- **IC Percentílicos** → Sección 2.2.2, celda 629aff4f

### J - JUSTIFICACIÓN DE DECISIONES
- **IQR vs Isolation Forest** → Sección 2.1.5, markdown celda 2761a981
- **Cambio Submuestras → Muestra Completa** → Sección 2.2.1, celda a715fa15
- **Criterio vote ≥ 3** → Sección 2.1.5.3, celda 5df60f89
- **Uso de Métodos Complementarios** → Sección 2.3.4, markdown celda efbfd268

### K - KRUSKAL-WALLIS
- **Prueba Kruskal-Wallis** → Sección 2.3.3, celda 1aa1662e
- **vs ANOVA** → Sección 2.3.3, markdown celda 96302b8f

### L - LEVENE
- **Prueba de Levene** → En todas las comparaciones de dos grupos
- **Función en código** → Celda a0967d3c, línea con stats.levene()

### M - MANN-WHITNEY U
- **Prueba Mann-Whitney U** → Sección 2.3.1, celda a0967d3c
- **Uso en mayoria de variables** → Sección 2.3.4, markdown celda 8e1d9040

### N - NORMALIDAD
- **Prueba Shapiro-Wilk** → Sección 2.4, celdas a6307771
- **Prueba Kolmogorov-Smirnov** → Sección 2.4, celdas a6307771
- **Hallazgo: No Normalidad** → Sección 2.4.2, markdown celda 6e310d09

### O - OUTLIERS
- Ver sección D (Detección de Outliers)

### P - PROPORCIONES
- **Comparación de Proporciones** → Sección 2.3.2, celda 2b71faaf
- **Tabla de Contingencia** → Sección 2.3.2, celda 2b71faaf

### R - REGRESIÓN / MULTIVARIADO
- **Limitación (no realizado)** → Sección 3.1.3, markdown celda a76f42aa
- **Próximos pasos** → Sección 3.1.4, markdown celda a76f42aa

### S - SHAPIRO-WILK
- **Prueba Shapiro-Wilk** → Sección 2.4.1, celda a6307771
- **Interpretación** → Sección 2.4.2, markdown celda 6e310d09

### T - T-TEST
- **t-test de Student** → Sección 2.3.1, celda a0967d3c (si hay normalidad + homocedasticidad)
- **Welch t-test** → Sección 2.3.1, celda a0967d3c (si hay normalidad - homocedasticidad)

### V - VALORES FALTANTES
- **Análisis Valores Faltantes** → Sección 2.1.3, celdas cb9b3e2b, 325fb21b
- **Cuantificación** → Sección 2.1.3, celda cb9b3e2b

### W - WELCH
- Ver sección T (Welch t-test)

---

## BUSCAR POR VARIABLE CLÍNICA → DÓNDE APARECE

### age_years (Edad)
- Distribución descriptiva → Sección 2.1, descriptive statistics
- Comparación GDM+/GDM- → Sección 2.3.1, celda a0967d3c
- Diferencia significativa → Sección 2.3.4, tabla resumen
- Correlación con otras → Sección 2.5, matrices de correlación

### bmi_prepreg_kg_m2 (IMC)
- **Destacada:** Variable clave diferenciadora
- IC 95% → Sección 2.2.2, celda 554d4d5d
- Comparación GDM+/GDM- → Sección 2.3.1, celda a0967d3c
- Diferencia significativa → Sección 2.3.4, tabla resumen
- Interpretación clínica → Sección 3.1.1, markdown celda 41c87e42

### diastolic_bp_mmHg (Presión Diastólica)
- Comparación → Sección 2.3.1, celda a0967d3c
- **Sin diferencia significativa** → Sección 2.3.4

### diet_score_0_100
- Comparación por actividad física → Sección 2.3.3, celda 1aa1662e

### family_history_t2d (Antecedentes Familiares)
- Comparación proporciones → Sección 2.3.2, celda 2b71faaf
- **Sin diferencia significativa** → Sección 2.3.4

### fpg_mmol_l (Glucosa en Ayunas)
- **Destacada:** Variable diferenciadora
- IC 95% → Sección 2.2.2, celda 554d4d5d
- Comparación → Sección 2.3.1, celda a0967d3c
- Diferencia significativa → Sección 2.3.4, tabla resumen
- Interpretación clínica → Sección 3.1.1, markdown

### gestational_weeks
- Exploración inicial → Sección 2.1

### hba1c_percent (Hemoglobina Glicosilada)
- IC 95% → Sección 2.2.2, celda 554d4d5d
- Comparación → Sección 2.3.1, celda a0967d3c
- Diferencia pequeña pero significativa → Sección 2.3.4

### hdl_mmol_l (Colesterol HDL)
- Correlación negativa con triglicéridos → Sección 2.5
- Descriptiva → Sección 2.1

### homa_ir (Resistencia a Insulina)
- Correlación alta con insulina → Sección 2.5.4, markdown
- Comparación GDM+/GDM- → Sección 2.3.1, celda a0967d3c
- Diferencia significativa → Sección 2.3.4, tabla resumen

### insulin_uIU_ml (Insulina)
- **Sin diferencia significativa** → Sección 2.3.4
- Correlación fuerte con HOMA-IR → Sección 2.5.4

### map_mmHg (Presión Arterial Media)
- Correlación con PAD (esperada) → Sección 2.5.4

### parity (Paridad)
- Exploración de casos extremos → Sección 2.1.5.2, celda dfb40a5e

### physical_activity_level (Actividad Física)
- ANOVA/Kruskal-Wallis con diet_score → Sección 2.3.3, celda 1aa1662e

### pcos (Síndrome Ovario Poliquístico)
- Distribución → Sección 2.1.5.1, celda 4a31f542
- Comparación proporciones → Sección 2.3.2, celda 2b71faaf
- **Diferencia significativa** → Sección 2.3.4, tabla resumen
- Interpretación clínica → Sección 3.1.1, markdown

### previous_gdm (GDM Previa)
- Comparación proporciones → Sección 2.3.2, celda 2b71faaf
- **Factor de riesgo más fuerte** → Sección 2.3.4
- Interpretación clínica → Sección 3.1.1, markdown

### smoking_first_trimester (Tabaquismo)
- Comparación proporciones → Sección 2.3.2, celda 2b71faaf
- **Diferencia significativa** → Sección 2.3.4
- Implicación clínica → Sección 3.1.1, markdown

### systolic_bp_mmHg (Presión Sistólica)
- Comparación → Sección 2.3.1, celda a0967d3c
- **Diferencia significativa** → Sección 2.3.4

### triglycerides_mmol_l (Triglicéridos)
- Ejemplo detección outliers → Sección 2.1.5.2, celda 7aa59928
- Correlación con HDL → Sección 2.5.4

### label_gdm (Objetivo)
- Distribución (17% positivo) → Sección 1.2
- Uso en todas las comparaciones → Celdas 46fded49 (distribución)

---

## BUSCAR POR FUNCIÓN/MÉTODO → UBICACIÓN Y DEFINICIÓN

### Árbol de Decisión para Pruebas
- **Gráfico:** Sección 6.1, CONCEPTOS.md
- **Aplicación en código:** Celda a0967d3c (compare_two_groups_numeric)
- **Explicación:** Sección 2.3, markdown celdas múltiples

### Bootstrap
- **Concepto:** RESUMEN_EJECUTIVO.md, sección 5.4
- **IC percentílicos:** Sección 2.2.2, celda 629aff4f

### Chi-Cuadrado
- **Función:** stats.chi2_contingency() en celda 2b71faaf
- **Criterio:** valores esperados ≥ 5
- **Uso:** Sección 2.3.2

### Colinealidad
- **Definición:** CONCEPTOS.md, sección 7.7
- **Detección:** Matriz de correlación > 0.7, Sección 2.5
- **Ejemplos:** Insulina-HOMA (0.85), PAD-PAM (0.82)

### Exclusión por Lista (Listwise Deletion)
- **Concepto:** CONCEPTOS.md, sección 1.3
- **Limitación:** RESUMEN_EJECUTIVO.md, tabla de limitaciones
- **Alternativa:** Imputación múltiple (mencionada pero no realizada)

### Fisher Exacto
- **Función:** stats.fisher_exact() en celda 2b71faaf
- **Criterio:** Cuando chi-cuadrado falla (valores esperados < 5)

### Heatmap
- **Visualización:** seaborn.heatmap() celdas 95cd96ee, a990970b, 836c0fb1
- **Utilidad:** Ver patrones rápidamente

### Histograma + KDE
- **Función:** seaborn.histplot() celda e0c422c9
- **Parámetros:** kde=True, stat="count", hue="label_gdm"

### Isolation Forest
- **Librería:** sklearn.ensemble.IsolationForest
- **Parámetros:** random_state=42
- **Aplicaciones:** 3 versiones (categóricas, continuas, todas)
- **Celdas:** 65bbb1ff, 1e1e15f5, b0fa89e6, 96ead88e

### Kruskal-Wallis
- **Función:** stats.kruskal() en celda 1aa1662e
- **Supuesto:** Mínimos (distribución libre)
- **Uso:** Cuando ANOVA falla (no normalidad)

### Levene (Homocedasticidad)
- **Función:** stats.levene() en celdas a0967d3c, 629aff4f
- **Criterio:** p ≥ 0.05 para igualdad de varianzas

### Mann-Whitney U
- **Función:** stats.mannwhitneyu() en celda a0967d3c
- **Supuesto:** Mínimos (distribución libre)
- **Uso:** Cuando t-test no aplica (no normalidad)

### Matriz de Correlación
- **Pearson:** df_corr_pearson, celda 95883a1d
- **Spearman:** df_corr_spearman, celda 95883a1d
- **Por grupo:** df_corr_pearson_pos, df_corr_pearson_neg, celdas 95cd96ee

### Pairplot
- **Función:** seaborn.pairplot() celda 3e6654a6
- **Parámetros:** hue="label_gdm", palette diferente para grupos

### Percentiles
- **Cálculo:** np.percentile() en celda 629aff4f
- **Uso:** IC percentílicos (2.5 y 97.5 para 95% CI)

### Shapiro-Wilk
- **Función:** stats.shapiro() en celdas a6307771, a0967d3c
- **Criterio:** p < 0.05 rechazo normalidad

### Tabla de Contingencia
- **Función:** pd.crosstab() en celda 2b71faaf
- **Estructura:** 2x2 con etiquetas binarias

### t-test Student
- **Función:** stats.ttest_ind(equal_var=True) en celda a0967d3c
- **Supuesto:** Normalidad + homocedasticidad
- **Variante:** igual_var=True

### Welch t-test
- **Función:** stats.ttest_ind(equal_var=False) en celda a0967d3c
- **Supuesto:** Normalidad (sin requerir igualdad de varianzas)
- **Variante:** igual_var=False

---

## BUSCAR POR TEMA → SECCIONES RELEVANTES

### Cambios Metodológicos (Decisiones que Evolucionaron)
1. **Submuestras → Muestra Completa (IC)** 
   - Antes: Sección 2.2.1, celda f3c2f9cc
   - Después: Sección 2.2.2, celda 554d4d5d
   - Justificación: Sección 2.2.1, markdown celda a715fa15

### Control de Calidad
- Exploración iterativa: Celdas 325fb21b, 3b05e782, f1fa8189, 051958cd, 34d84f95, f1a186b4
- Verificación post-operación: Patrón documentado en todo el notebook

### Interpretación Clínica
- Variables metabólicas: Sección 3.1.2, markdown celda 41c87e42
- Antecedentes obstétricos: Sección 3.1.2, markdown
- Factores modificables: Sección 3.1.2, markdown

### Limitaciones Reconocidas
- Datos sintéticos: Sección 3.1.3, markdown celda a76f42aa
- Diseño transversal: Sección 3.1.3, markdown
- Análisis univariado/bivariado: Sección 3.1.3, markdown
- Exclusión por lista: Sección 3.1.3, markdown

### Próximos Pasos
- Validación en datos reales: Sección 3.1.4, markdown
- Análisis multivariado: Sección 3.1.4, markdown
- Modelos predictivos: Sección 3.1.4, markdown

### Robustez Estadística
- Múltiples métodos complementarios: Sección 2.1.5, markdown
- Verificación de supuestos: Sección 2.3.1, markdown
- IC paramétricos + percentílicos: Sección 2.2, explicación general

---

## BÚSQUEDA RÁPIDA - TABLA DE CELDAS CRÍTICAS

| Concepto | Celda ID | Tipo | Sección |
|----------|----------|------|---------|
| Carga datos | f7a56e19 | Code | 2.1.2 |
| Descriptiva | 06fdfeba | Code | 2.1.4 |
| IQR Outliers | 4fc22d1d | Code | 2.1.5 |
| IF Outliers | 65bbb1ff, 1e1e15f5, b0fa89e6 | Code | 2.1.5.2 |
| Votación | ad74bf5c, fa76a54b, d20dc0ab | Code | 2.1.5.3 |
| Filter datos | 2961687b | Code | 2.1.5.4 |
| IC Paramétrico | 554d4d5d | Code | 2.2.2 |
| IC Percentílico | 629aff4f | Code | 2.2.2 |
| Pruebas Hipótesis | a0967d3c | Code | 2.3.1 |
| Proporciones | 2b71faaf | Code | 2.3.2 |
| k Grupos | 1aa1662e | Code | 2.3.3 |
| Tabla Resumen | 60880f6f | Code | 2.3.5 |
| Normalidad | a6307771 | Code | 2.4.1 |
| Correlación | 95883a1d | Code | 2.5.1 |
| Heatmap | 95cd96ee, a990970b, 836c0fb1 | Code | 2.5.2 |
| Pairplot | 3e6654a6 | Code | 2.5.3 |

---

## CAMBIOS CLAVE EXPLICADOS

### 1. Submuestras vs Muestra Completa (IC)
- **Original (celda f3c2f9cc):** Loops sobre n = 10, 20, ..., 100
- **Cambio (celda 554d4d5d):** Usar n ≈ 1500 completo
- **Razón (markdown a715fa15):** "Evitar sesgos de muestreo repetido"

### 2. Eliminación de Outliers
- **Método 1 (IQR): Univariado clásico** → Incorporado
- **Método 2-4 (Isolation Forest):** Tres variantes complementarias → Incorporadas
- **Votación:** Solo eliminar si 3+ métodos concuerdan → Conservador

### 3. Selección de Pruebas
- **Supuesto de normalidad fallado** → Use Mann-Whitney U (mayoría de variables)
- **Documentado:** Se reportan p-valores de Shapiro junto con prueba usada

---

**TIP DE USO:** Ctrl+F en el notebook para buscar por nombre de celda o sección. Los cell IDs (ej: #VSC-a0967d3c) permiten localización exacta.
