# 📊 RESUMEN - ANÁLISIS DE DIABETES GESTACIONAL (GDM)
**Equipo Alma de Litio: Pablo, Emmanuel, Diego**  
**Fecha:** 14 de Noviembre de 2025

---

## 🎯 CONTEXTO DEL PROYECTO

Se realizó un **análisis exploratorio de datos (EDA)** sobre un dataset sintético de **~1500 pacientes gestantes**, con el objetivo de identificar diferencias estadísticas entre casos con GDM positivo (17%) y GDM negativo (83%). El análisis es **univariado y bivariado**, sin modelos predictivos multivariados.

---

## 📋 METODOLOGÍA GENERAL

### Estructura del Análisis (6 Fases)

```
1. Preparación de Datos    → Exploración inicial, caracterización
2. Detección de Outliers   → 4 métodos + sistema de votación
3. Intervalos de Confianza → IC 95% para medias y varianzas
4. Pruebas de Hipótesis    → Comparación GDM+ vs GDM-
5. Análisis Bivariado      → Correlaciones Pearson y Spearman
6. Síntesis e Interpretación → Hallazgos y limitaciones
```

---

## 🔍 DETECCIÓN Y LIMPIEZA DE OUTLIERS

### Sistema de Votación (Decisión Clave #1)

**Métodos Utilizados:**
- **IQR (univariado):** Rango intercuartílico clásico [Q1-1.5×IQR, Q3+1.5×IQR]
- **Isolation Forest Categóricas:** Detecta combinaciones raras de factores de riesgo
- **Isolation Forest Continuas:** Aísla valores extremos en mediciones clínicas
- **Isolation Forest Todas:** Enfoque integral multidimensional

**Criterio de Eliminación:**
- Se eliminan registros con **vote_outlier ≥ 3** (concordancia de 3 o 4 métodos)
- Se conservan registros con vote 0, 1 o 2

**Justificación:** Equilibrio conservador entre limpieza de datos y preservación de variabilidad biológica natural. La alternativa vote ≥ 1 sería demasiado agresiva (~25% eliminación).

**Resultado:** Dataset filtrado (`df_filter`) usado en todos los análisis posteriores

---

## 📊 INTERVALOS DE CONFIANZA (IC 95%)

### Cambio Metodológico Importante (Decisión Clave #2)

**Antes:** Submuestras aleatorias (n=10 a 100) para calcular IC
- ❌ Introduce variabilidad artificial por remuestreo repetido
- ❌ Afecta reproducibilidad

**Ahora:** Muestra completa (n≈1500) para IC
- ✅ Estimaciones más robustas
- ✅ Mejora reproducibilidad

### Métodos Complementarios

| Tipo | Método | Cuándo Usar |
|------|--------|-----------|
| **Paramétrico** | Distribución t de Student | Si datos normales |
| **Robusto** | IC percentílico (bootstrap) | Si datos no normales |
| **Combinado** | Ambos juntos | Máxima confianza |

**Interpretación correcta:** "El IC 95% [a, b] significa que tenemos 95% confianza de que el parámetro poblacional µ está en este rango" (NO es "95% de los datos")

---

## 🧪 PRUEBAS DE HIPÓTESIS

### Hallazgo Crítico: Mayoría de Variables NO Normales

Se aplicó prueba de **Shapiro-Wilk** a todas las variables continuas:
- **Resultado:** ~80% de variables rechazan normalidad (p < 0.05)
- **Implicación:** Requiere uso sistemático de pruebas no paramétricas

### Árbol de Decisión para Seleccionar Prueba (Decisión Clave #3)

```
¿Datos normales? (Shapiro-Wilk, p ≥ 0.05)
├─ SÍ → ¿Varianzas iguales? (Levene, p ≥ 0.05)
│       ├─ SÍ → t-test de Student
│       └─ NO → Welch t-test
└─ NO → Mann-Whitney U (usado aquí mayormente)
```

### Pruebas Aplicadas

**Variables Continuas:**
- **Mann-Whitney U:** Compara medianas entre GDM+ y GDM- (no paramétrica)
  - Ventaja: Robusta a no normalidad
  - Base: Rangos, no valores originales

**Variables Binarias (Proporciones):**
- **Chi-cuadrado:** Si todos valores esperados ≥ 5
- **Fisher exacto:** Si algún valor esperado < 5

**Comparación Múltiples Grupos (k > 2):**
- **Kruskal-Wallis:** Alternativa no paramétrica a ANOVA

---

## 🎯 PRINCIPALES HALLAZGOS

### Variables con Diferencias Significativas (p < 0.05)

**Continuas (Mann-Whitney U):**
| Variable | GDM- | GDM+ | Significancia |
|----------|------|------|---------------|
| IMC pregestacional | ~23 | ~24 | ✅ Sí |
| Glucosa en ayunas (FPG) | ~5.2 | ~5.5 mmol/L | ✅ Sí |
| HbA1c | ~5.1 | ~5.3 % | ✅ Sí |
| Edad | ~29 | ~32 años | ✅ Sí |
| HOMA-IR | ~1.8 | ~2.2 | ✅ Sí |

**Binarias (Chi-cuadrado/Fisher):**
- **GDM previa:** MÁS importante en GDM+ (muy significativa)
- **PCOS:** Factor de riesgo moderado en GDM+
- **Tabaco 1er trimestre:** Presente en GDM+

**No significativas:**
- Presión diastólica
- Insulina sérica directa (variable cruda)
- Antecedentes familiares de T2D

### Interpretación Clínica

1. **Variables metabólicas** (IMC, FPG, HbA1c, HOMA-IR) diferencian grupos → predictores importantes
2. **Factores reproductivos** (GDM previa, PCOS) son factores de riesgo muy fuertes
3. **Insulina directa** no diferencia (probablemente por variabilidad individual) pero HOMA-IR sí (combina con glucosa)

---

## 🔗 ANÁLISIS BIVARIADO - CORRELACIONES

### Métodos Complementarios

**Correlación de Pearson (r):**
- Mide asociación **lineal** entre variables
- Paramétrica, sensible a outliers
- Rango: -1 (negativa perfecta) a +1 (positiva perfecta)

**Correlación de Spearman (ρ):**
- Mide asociación **monotónica** entre variables
- No paramétrica, basada en rangos
- Robusta a outliers y no normalidad

**Por qué ambas:** Se usan juntas para confirmación. Si coinciden, confianza en hallazgo.

### Correlaciones Fuertes Encontradas

| Variables | r Pearson | Causa |
|-----------|-----------|-------|
| Insulina vs HOMA-IR | 0.85 | **Relación matemática:** HOMA-IR = (I × G)/22.5 |
| PAD vs PAM | 0.82 | **Fisiológica:** PAM = PAD + 1/3(PAS-PAD) |
| FPG vs HOMA-IR | 0.72 | **Ambas metabólicas** (control glucémico) |

**Interpretación:** No son problemas de colinealidad, sino relaciones esperadas (matemáticas o fisiológicas).

### Estructura por Grupo

- **Correlaciones en GDM+:** Matriz similar a GDM-
- **Máxima diferencia:** < 0.16 entre grupos
- **Conclusión:** Los mecanismos fisiológicos subyacentes son similares entre grupos

---

## 📚 TÉCNICAS Y HERRAMIENTAS

### Librerías Python Utilizadas

| Librería | Uso Principal |
|----------|---------------|
| **pandas** | Manipulación de datos |
| **numpy** | Operaciones numéricas |
| **scipy.stats** | Pruebas estadísticas (Shapiro-Wilk, Mann-Whitney, etc.) |
| **scikit-learn** | Isolation Forest para detección de outliers |
| **matplotlib / seaborn** | Visualizaciones (heatmaps, histogramas, boxplots) |
| **statsmodels** | IC, regresión, ANOVA |

### Funciones Clave de Auxiliar

```python
df_filter()          # Filtra outliers según criterio de votación
calculate_ic()       # Calcula IC paramétricos y percentílicos
verify_assumptions() # Verifica normalidad y homocedasticidad
```

---

## ⚠️ LIMITACIONES RECONOCIDAS

| Limitación | Impacto | Mitigación |
|-----------|--------|-----------|
| **Dataset sintético** | No generalizable directamente | Validación futura en datos reales |
| **Diseño transversal** | No establece causalidad | Solo asociaciones, no causa-efecto |
| **Análisis univariado/bivariado** | No controla variables confusoras | Próxima etapa: regresión logística |
| **Exclusión por lista** (listwise deletion) | Posible sesgo si no MCAR | Considerar imputación múltiple |
| **No estratificación por edad/IMC** | Podría haber confusión | Análisis estratificado futuro |

---

## 🎓 CONCEPTOS CLAVE PARA DEFENDER

### Los 3 Pilares Metodológicos

1. **Verificación de Supuestos:** Se verifican explícitamente ANTES de cada prueba (Shapiro-Wilk, Levene)
2. **Complementariedad de Métodos:** Paramétricos + no paramétricos juntos aumenta robustez
3. **Transparencia Total:** Cada decisión justificada y reportada

### Las 3 Decisiones Más Importantes

1. **Sistema de votación para outliers:** Preserva datos (–1-2% eliminación) mientras elimina extremos (vote ≥ 3)
2. **Muestra completa para IC:** Evita sesgos de submuestreo, mejora reproducibilidad
3. **Árbol de decisión para pruebas:** Rigor en selección basada en supuestos verificados

### Los 3 Hallazgos Principales

1. **Variables metabólicas diferencian grupos:** IMC, FPG, HOMA-IR significativos (p < 0.05)
2. **Factores obstétricos son predictores fuertes:** GDM previa es el factor más importante
3. **Mayoría de variables no normales:** Requiere métodos robusto, bien aplicados aquí

---

## 🛡️ RESPUESTAS A CRÍTICAS POTENCIALES

| Crítica | Respuesta |
|---------|-----------|
| "¿Por qué eliminar datos?" | Criterio conservador (vote ≥ 3) preserva 98%+. Mejora calidad estadística de estimadores |
| "¿Por qué no paramétricos?" | Shapiro-Wilk demostró no normalidad. Necesario por rigor, no capricho |
| "¿Dataset sintético es válido?" | Válido para demostrar metodología rigurosa. Limitación reconocida. Requiere validación futura |
| "¿Por qué IC percentílicos?" | Robustos cuando normalidad falla. Complementan paramétricos, aumentan confianza |
| "¿Cómo saben que no es suerte estadística?" | IC 95% + múltiples pruebas confirmatorias. Bajo riesgo de falso positivo |

---

## 📝 FRASES CLAVE PARA USAR EN LA ORAL

> **Sobre Outliers:** "El sistema de votación es un enfoque conservador que equilibra la limpieza de datos con la preservación de variabilidad biológica natural."

> **Sobre Cambio en IC:** "Se reconoció que el remuestreo repetido introduce sesgos metodológicos, por eso se optó por la muestra completa para estimaciones más robustas."

> **Sobre No Normalidad:** "La mayoría de variables no cumplieron el supuesto de normalidad (Shapiro-Wilk, p < 0.05), por ello utilizamos pruebas no paramétricas como Mann-Whitney U."

> **Sobre Selección de Pruebas:** "Antes de cada prueba se verificaban sistemáticamente los supuestos. La prueba se seleccionaba según el resultado de estas verificaciones."

> **Sobre Correlaciones Altas:** "Las correlaciones fuertes (Insulina-HOMA r=0.85) son esperadas porque HOMA-IR se calcula directamente con insulina. No son problemas de colinealidad, sino relaciones matemáticas esperadas."

---

## ✅ CHECKLIST DE COMPETENCIAS DEMOSTRADAS

- [x] Definir cada técnica estadística utilizada (IQR, IF, Shapiro-Wilk, Mann-Whitney, etc.)
- [x] Explicar por qué se eligió cada método (árbol de decisión, verificación de supuestos)
- [x] Conectar decisiones metodológicas con objetivos del análisis
- [x] Reconocer limitaciones y sesgos potenciales
- [x] Interpretar resultados en contexto clínico (IMC, FPG, HOMA-IR como predictores)
- [x] Comparar métodos alternativos y justificar elecciones
- [x] Evaluar validez y robustez de hallazgos

---

## 🚀 PRÓXIMOS PASOS (No Realizados)

1. **Regresión logística:** Control multivariado de confusoras
2. **Validación cruzada:** Evaluar poder predictivo
3. **Imputación múltiple:** Mejor manejo de datos faltantes
4. **Análisis en cohortes reales:** Validación externa del modelo
5. **Estratificación:** Por edad, BMI, grupo étnico

---

## 📊 CONCLUSIÓN

Este análisis demuestra:
- ✅ Comprensión profunda de métodos estadísticos
- ✅ Rigor metodológico (verificación de supuestos, transparencia)
- ✅ Interpretación clínica de hallazgos
- ✅ Reconocimiento de limitaciones
- ✅ Decisiones basadas en evidencia, no en intuición

**El objetivo fue ENSEÑAR estadística rigurosa, no solo reportar números.**

---

**Hora de la evaluación:** 1 hora desde ahora  
**Última revisión:** 14 de Noviembre de 2025, 11:45 PM  
**Estado:** ✅ LISTO PARA ORAL
