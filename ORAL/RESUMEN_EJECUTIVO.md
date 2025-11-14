# Resumen Ejecutivo - Decisiones Metodológicas Clave

Documento de referencia rápida para los puntos estratégicos del análisis. Usa este documento para recordar rápidamente el "por qué" de cada decisión importante.

---

## DECISIONES CLAVE POR SECCIÓN

### 1. DETECCIÓN Y ELIMINACIÓN DE OUTLIERS

**Decisión:** Sistema de votación de 4 métodos con umbral ≥ 3

| Método | Tipo | Razón Inclusión |
|--------|------|-----------------|
| IQR | Univariado clásico | Base estatutaria de outliers |
| IF Categóricas | Multivariado | Detecta combinaciones raras de factores de riesgo |
| IF Continuas | Multivariado | Detecta valores extremos en mediciones |
| IF Todas | Multivariado integral | Visión holística multidimensional |

**Umbral elegido:** Eliminar si vote ≥ 3 (acordancia de 3 o más métodos)

**Alternativa rechazada:** vote ≥ 1 (demasiado agresivo, eliminaría variabilidad legítima)

**Justificación:** Balance entre datos limpios y preservación de variabilidad biológica natural

---

### 2. INTERVALOS DE CONFIANZA

**Cambio Metodológico:**
- ❌ Inicialmente: Submuestras aleatorias (n = 10 a 100)
- ✅ Finalmente: Muestra completa (n ≈ 1500)

**Razón del cambio:**
- Submuestreo repetido introduce variabilidad artificial y afecta reproducibilidad
- Muestra completa proporciona estimaciones más robustas

**Nivel de confianza:** 95% (α = 0.05, estándar en biomedicina)

**Métodos complementarios:**
- Paramétricos: Basados en distribución t de Student
- Percentílicos: Basados en bootstrap (robustos a no normalidad)
- **Uso:** Ambos cuando normalidad es dudosa

---

### 3. VERIFICACIÓN DE SUPUESTOS Y SELECCIÓN DE PRUEBAS

**Hallazgo crítico:** Mayoría de variables NO son normales (p < 0.05, Shapiro-Wilk)

**Respuesta adoptada:**

```
┌─ ¿Normalidad? (Shapiro-Wilk, p ≥ 0.05)
├─ SÍ → ¿Varianzas iguales? (Levene, p ≥ 0.05)
│       ├─ SÍ → t-test Student
│       └─ NO → Welch t-test
└─ NO → Mann-Whitney U (no paramétrico)
```

**Impacto:** La mayoría de pruebas fueron no paramétricas

**Transparencia:** Se reportó resultado de supuestos junto con prueba utilizada

---

### 4. ANÁLISIS BIVARIADO - CORRELACIONES

**Correlaciones fuertes encontradas (|r| > 0.7):**

| Pares de Variables | r | Explicación |
|-------------------|---|-------------|
| Insulina vs HOMA-IR | 0.85 | Por definición matemática: HOMA-IR = (I × G)/22.5 |
| PAD vs PAM | 0.82 | Fisiológico: PAM = PAD + 1/3(PAS - PAD) |
| FPG vs HOMA-IR | 0.72 | Ambos indicadores de metabolismo glucídico |

**Interpretación:** Colinealidad baja (excepto relaciones matemáticas). Variables son complementarias.

**Estructura por grupo:** Similar entre GDM+ y GDM- (diferencias máximas < 0.16)

---

### 5. VARIABLES CON DIFERENCIAS SIGNIFICATIVAS

#### Variables Continuas (p < 0.05)

| Variable | Prueba Usada | Razón |
|----------|-------------|--------|
| bmi_prepreg_kg_m2 | Mann-Whitney U | No normalidad |
| fpg_mmol_l | Mann-Whitney U | No normalidad |
| hba1c_percent | Mann-Whitney U | No normalidad |
| age_years | Mann-Whitney U | No normalidad |
| homa_ir | Mann-Whitney U | No normalidad |

#### Variables Binarias (p < 0.05)

| Variable | Prueba Usada | Magnitud Efecto |
|----------|-------------|-----------------|
| previous_gdm | Chi-cuadrado/Fisher | Mayor en GDM+ (muy significativo) |
| pcos | Chi-cuadrado/Fisher | Mayor en GDM+ |
| smoking_first_trimester | Chi-cuadrado/Fisher | Mayor en GDM+ |

---

### 6. VARIABLES SIN DIFERENCIAS SIGNIFICATIVAS

- diastolic_bp_mmHg (presión diastólica)
- insulin_uIU_ml (insulina sérica directa)
- family_history_t2d (antecedentes familiares)
- diet_score × physical_activity (sin diferencias entre grupos de actividad)

---

## FRASES CLAVE PARA RECORDAR (Para Usar en la Oral)

### Sobre Outliers
> "Se utilizó un sistema de votación entre 4 métodos complementarios, eliminando solo registros acordes en 3 o más métodos. Esto es un enfoque conservador que preserva la variabilidad biológica mientras elimina casos extremos."

### Sobre Cambio de Metodología en IC
> "Inicialmente se consideró usar submuestras aleatorias, pero se reconoció que el remuestreo repetido introduce sesgos metodológicos. Se optó por la muestra completa para estimaciones más robustas."

### Sobre No Normalidad
> "La mayoría de las variables continuas no cumplieron el supuesto de normalidad (Shapiro-Wilk, p < 0.05). Por ello, se utilizaron principalmente pruebas no paramétricas como Mann-Whitney U, complementadas con intervalos de confianza percentílicos."

### Sobre Selección de Pruebas
> "Antes de cada prueba de hipótesis, se verificaron sistemáticamente los supuestos (normalidad con Shapiro-Wilk, homocedasticidad con Levene). La prueba se seleccionaba según resultado de estas verificaciones."

### Sobre Correlaciones Altas
> "Las correlaciones fuertes (Insulina-HOMA-IR, r = 0.85) eran esperadas porque HOMA-IR se calcula directamente usando insulina. Esto no es un problema de colinealidad problemática, sino relaciones matemáticas o fisiológicamente vinculadas."

### Sobre Estructura Similar en Grupos
> "Aunque hubo diferencias significativas en variables individuales entre GDM+ y GDM-, la estructura de correlación fue similar entre grupos (diferencias máximas < 0.16), sugiriendo que los mecanismos fisiológicos subyacentes son similares."

### Sobre Limitaciones
> "Este es un dataset sintético con diseño transversal. Aunque los hallazgos son consistentes con literatura, no pueden establecerse relaciones causales y se requiere validación en cohortes reales."

---

## ÁRBOL DE DECISIONES - QUICK REFERENCE

```
DECISIÓN 1: ¿Tengo datos faltantes?
├─ SÍ (MCAR/MAR) → Usar exclusión por lista (análisis actual)
└─ Alternativa futura: Imputación múltiple

DECISIÓN 2: ¿Tengo outliers potenciales?
├─ SÍ → Votación de 4 métodos, eliminar vote ≥ 3
└─ Crear df_filter para análisis posteriores

DECISIÓN 3: ¿Calcular IC para parámetro?
├─ Media → Usar muestra completa + dist. t (no submuestras)
├─ Complementar: IC percentílicos si no normalidad
└─ Nivel: 95% (α = 0.05)

DECISIÓN 4: ¿Comparar dos grupos?
├─ Variables continuas:
│   ├─ ¿Normal en ambos? (Shapiro-Wilk)
│   │   ├─ SÍ → ¿Varianzas iguales? (Levene)
│   │   │       ├─ SÍ → t-test Student
│   │   │       └─ NO → Welch t-test
│   │   └─ NO → Mann-Whitney U
│
├─ Variables binarias:
│   ├─ Valores esperados ≥ 5? → Chi-cuadrado
│   └─ Algunos < 5? → Fisher exacto

DECISIÓN 5: ¿Analizar correlaciones?
├─ Pearson + Spearman (complementarias)
├─ Crear matrices separadas por grupo GDM
└─ Heatmaps + pairplot para visualización
```

---

## MÉTRICAS REPORTADAS - DÓNDE ENCONTRARLAS

| Métrica | Sección | Uso |
|---------|---------|-----|
| Prevalencia GDM | 1.1 | 17% casos positivos |
| Valores faltantes | 1.1 | Cuantificación por variable |
| Outliers detectados | 3.3 | Vote count distribución |
| IC 95% (media) | 5.2 | Rangos para variables clave |
| p-valores pruebas | 6.5-6.7 | Comparaciones univariadas |
| r Pearson/Spearman | 7.1-7.2 | Correlaciones bivariadas |

---

## LIMITACIONES RECONOCIDAS

| Limitación | Implicación | Mitigación Futura |
|-----------|-----------|-------------------|
| Dataset sintético | Patrones pueden no generalizarse | Validación en datos reales |
| Diseño transversal | No establece causalidad | Estudios longitudinales |
| Análisis univariado/bivariado | No controla confusoras | Regresión logística multivariada |
| Exclusión por lista | Posible sesgo si no MCAR | Imputación múltiple |

---

## RESULTADOS EN UNA LÍNEA POR VARIABLE

| Variable | GDM- Media | GDM+ Media | Prueba | p-valor | Conclusión |
|----------|-----------|-----------|--------|---------|-----------|
| bmi_prepreg_kg_m2 | ~23.1 | ~24.1 | M-W | <0.05 | **Significativo** |
| fpg_mmol_l | ~5.2 | ~5.5 | M-W | <0.05 | **Significativo** |
| age_years | ~29.3 | ~31.5 | M-W | <0.05 | **Significativo** |
| homa_ir | ~1.8 | ~2.2 | M-W | <0.05 | **Significativo** |
| diastolic_bp_mmHg | ~71 | ~72 | M-W | >0.05 | No significativo |

*M-W = Mann-Whitney U, debido a no normalidad*

---

## CRONOLOGÍA DE DECISIONES

```
FASE 1: Exploración
  └─ Cargar datos → Exploración inicial → Identificar características

FASE 2: Limpieza
  └─ Detectar outliers (4 métodos) → Votación → Crear df_filter

FASE 3: Estadística Descriptiva
  └─ Medidas centrales/dispersión → Distribuciones → Visualizaciones

FASE 4: Intervalos de Confianza
  └─ Decisión: muestra completa, no submuestras
  └─ Paramétricos + percentílicos

FASE 5: Pruebas de Hipótesis
  └─ Verificar supuestos → Seleccionar prueba → Ejecutar e interpretar

FASE 6: Análisis Bivariado
  └─ Correlaciones Pearson + Spearman
  └─ Estratificar por grupo GDM
  └─ Visualizaciones (heatmaps, pairplot)

FASE 7: Síntesis e Interpretación
  └─ Integrar hallazgos → Implicaciones clínicas → Limitaciones
```

---

## PUNTOS FUERTES DEL ANÁLISIS (Para Defender)

✅ **Verificación sistemática de supuestos** antes de cada prueba
✅ **Múltiples métodos complementarios** (no depende de un único enfoque)
✅ **Conservadurismo en eliminación de datos** (preserva representatividad)
✅ **Transparencia completa** en decisiones y justificaciones
✅ **Métodos paramétricos y no paramétricos** juntos (robustez)
✅ **Exploración iterativa** validando cada transformación
✅ **Visualizaciones estratificadas** por grupo GDM

---

## PUNTOS A DEFENDER ANTE CRÍTICAS

| Crítica Potencial | Respuesta |
|------------------|-----------|
| "¿Por qué eliminar datos?" | Criterio conservador (vote ≥ 3) preserva 98%+ de datos. Mejora calidad estadística |
| "¿Por qué no usar submuestras?" | Submuestreo repetido introduce sesgos. Muestra completa es más robusta |
| "¿Por qué usar no paramétricos?" | Mayoría de variables no normales (demostrado con Shapiro-Wilk). Necesario por rigidez |
| "¿Por qué IC percentílicos?" | Robustos cuando normalidad falla. Complementan paramétricos. Aumentan confianza |
| "¿Y si los outliers son reales?" | Posible. Sistema de votación es conservador. Vote 1-2 se conservan |
| "¿Dataset sintético es válido?" | Válido para demostrar metodología. Requiere validación futura en reales |

---

## PARA MEMORIZAR (ANTES DE LA ORAL)

**Los 3 pilares metodológicos:**
1. **Verificación:** Supuestos antes de pruebas
2. **Complementariedad:** Paramétrico + no paramétrico
3. **Transparencia:** Justificar cada decisión

**Las 3 decisiones más importantes:**
1. Sistema de votación para outliers (preserva datos, elimina extremos)
2. Muestra completa para IC (evita sesgos de submuestreo)
3. Árbol de decisión para pruebas (rigor en selección)

**Los 3 hallazgos principales:**
1. Variables metabólicas (IMC, FPG, HOMA-IR) diferencian grupos
2. Factores obstétricos (GDM previa, PCOS) son factores de riesgo fuertes
3. Mayoría de variables no normales, requiriendo métodos robustos

---

## ESTRUCTURA DE RESPUESTA ANTE PREGUNTAS DIFÍCILES

1. **"Entiendo que..." [reformular la pregunta en términos simples]**
2. **"La decisión fue..." [nombrar la decisión]**
3. **"Porque..." [justificación del por qué]**
4. **"Esto resultó en..." [consecuencia o resultado]**
5. **"La validez se asegura mediante..." [cómo se verificó]**

---

**Última nota:** Este análisis demuestra comprensión de estadística rigurosa. No es memorizar valores, es demostrar que entiendes POR QUÉ cada método se eligió y QUÉ hace cada decision para mejorar la calidad del análisis.

¡Éxito en la oral! 📊📈
