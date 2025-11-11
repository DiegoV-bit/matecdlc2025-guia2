# Lista de Tareas Pendientes - Análisis Exploratorio GDM
## Organizado por orden de secciones de la guía

**Progreso Global Actual: 39%**

Basado en la evaluación detallada del profesor David Medina. Las tareas están organizadas en el orden de las secciones de la guía práctica.

---

## 2.1 Exploración Descriptiva (56% completado)

**Estado actual**: Datos cargados, outliers detectados, estadísticos calculados. Faltan visualizaciones e interpretación.

### Visualizaciones faltantes

- [ ] Generar histogramas para: `bmi_prepreg_kg_m2`, `fpg_mmol_l`, `hba1c_percent`, `hdl_mmol_l`
- [ ] Generar boxplots para: `systolic_bp_mmHg`, `diastolic_bp_mmHg`, `map_mmHg`
- [ ] Generar gráficos de densidad (KDE) para variables clave
- [ ] Superponer curva normal en histogramas para evaluar normalidad visual

### Interpretación textual de cada variable

- [ ] `bmi_prepreg_kg_m2`: comentar media, dispersión, asimetría
- [ ] `fpg_mmol_l`: describir distribución y presencia de valores extremos
- [ ] `hba1c_percent`: analizar tendencia central y dispersión
- [ ] `systolic_bp_mmHg` / `diastolic_bp_mmHg` / `map_mmHg`: comentar patrones

### Estrategia para outliers

- [ ] Documentar decisión sobre outliers (mantener/eliminar/transformar)
- [ ] Si se mantienen: justificar uso de métodos robustos
- [ ] Si se transforman: documentar transformación aplicada
- [ ] Verificar impacto en análisis posteriores

---

## 2.2 Intervalos de Confianza (54% completado)

**Estado actual**: Funciones correctas y algunos IC calculados (IMC), pero faltan variables y tipos de IC.

### IC para medias de variables continuas faltantes

- [ ] `fpg_mmol_l`: IC95% para la media
- [ ] `hba1c_percent`: IC95% para la media
- [ ] `hdl_mmol_l`: IC95% para la media
- [ ] `systolic_bp_mmHg`: IC95% para la media
- [ ] `diastolic_bp_mmHg`: IC95% para la media
- [ ] `map_mmHg`: IC95% para la media
- [ ] `triglycerides_mmol_l`: IC95% para la media

### IC para proporciones

- [ ] Proporción de `smoking_first_trimester=1`: usar método Wilson o Agresti-Coull
- [ ] Proporción de `family_history_t2d=1`: IC95%
- [ ] Proporción de `previous_gdm=1`: IC95%
- [ ] Proporción de `pcos=1`: IC95%
- [ ] Proporción de `label_gdm=1`: IC95%

### IC para diferencia de medias entre grupos

- [ ] `bmi_prepreg_kg_m2`: IC95% para diferencia GDM vs No-GDM
- [ ] `fpg_mmol_l`: IC95% para diferencia GDM vs No-GDM
- [ ] `hba1c_percent`: IC95% para diferencia GDM vs No-GDM
- [ ] `map_mmHg`: IC95% para diferencia GDM vs No-GDM
- [ ] Usar fórmulas apropiadas (varianzas iguales vs desiguales)

### Interpretación clínica de IC

- [ ] Comparar IC de `hba1c_percent` con rangos de referencia clínicos
- [ ] Comparar IC de `fpg_mmol_l` con umbrales diagnósticos
- [ ] Interpretar amplitud de IC (precisión de estimaciones)
- [ ] Comentar implicancia clínica de cada IC

---

## 2.3 Pruebas de Hipótesis (8% completado) 🔴 CRÍTICO

**Estado actual**: Casi sin empezar. Solo hay preparación de datos.

### Comparación GDM vs No-GDM en variables continuas

- [ ] Formular H₀ y H₁ para cada comparación
- [ ] `map_mmHg`: aplicar t-test o Mann-Whitney según normalidad
- [ ] `bmi_prepreg_kg_m2`: aplicar t-test o Mann-Whitney según normalidad
- [ ] `fpg_mmol_l`: comparación entre grupos
- [ ] `hba1c_percent`: comparación entre grupos
- [ ] `systolic_bp_mmHg`: comparación entre grupos
- [ ] `diastolic_bp_mmHg`: comparación entre grupos
- [ ] Reportar: estadístico, p-valor, decisión y **tamaño de efecto** (d de Cohen o r)

### Comparación de dieta según nivel de actividad física

- [ ] Discretizar `physical_activity_level` en 3 niveles (bajo/medio/alto)
- [ ] Aplicar ANOVA o Kruskal-Wallis según normalidad de `diet_score_0_100`
- [ ] Post-hoc si hay diferencias significativas (Tukey o Dunn)

### Comparación de proporciones

- [ ] Test chi² 2×2 o z de 2 proporciones: `family_history_t2d` vs `label_gdm`
- [ ] Test chi² 2×2 o z de 2 proporciones: `previous_gdm` vs `label_gdm`
- [ ] Test chi² 2×2 o z de 2 proporciones: `pcos` vs `label_gdm`
- [ ] Test chi² 2×2 o z de 2 proporciones: `smoking_first_trimester` vs `label_gdm`

### Documentación de cada test

- [ ] Justificar elección del test (paramétrico vs no paramétrico)
- [ ] Verificar supuestos (normalidad con Shapiro, homogeneidad con Levene)
- [ ] Interpretar resultados en contexto clínico

---

## 2.4 Evaluación de Normalidad (85% completado) ✅ CASI COMPLETO

**Estado actual**: Shapiro-Wilk y KS-Lilliefors correctos. Faltan solo visualizaciones y transformaciones.

### QQ-plots

- [ ] Generar QQ-plot para cada variable continua
- [ ] Destacar variables con desviación marcada de normalidad
- [ ] Comentar patrones visuales (colas pesadas, asimetría, etc.)

### Histogramas con curva normal superpuesta

- [ ] Graficar histograma + curva normal teórica para variables no normales
- [ ] Facilitar comparación visual con distribución normal

### Transformaciones de variables

- [ ] Probar transformación logarítmica en variables asimétricas positivas
- [ ] Probar Box-Cox en variables con asimetría moderada
- [ ] Re-evaluar normalidad post-transformación (Shapiro-Wilk)
- [ ] Documentar si transformación mejora ajuste a normalidad
- [ ] Decidir si usar variable transformada en análisis posteriores

---

## 2.5 Análisis Bivariado (28% completado) 🔴 CRÍTICO

**Estado actual**: Datos preparados pero sin análisis ni visualizaciones completas.

### Matriz de correlación

- [ ] Calcular correlación de Pearson para todas las variables continuas
- [ ] Generar heatmap con anotaciones de valores
- [ ] Identificar correlaciones fuertes (|r| > 0.7) y discutir multicolinealidad

### Scatterplots con regresión

- [ ] `fpg_mmol_l` vs `hba1c_percent` + línea de regresión
- [ ] `insulin_uIU_ml` vs `homa_ir` + línea de regresión
- [ ] `bmi_prepreg_kg_m2` vs `map_mmHg` + línea de regresión
- [ ] `triglycerides_mmol_l` vs `hdl_mmol_l` + línea de regresión
- [ ] Incluir ecuación de regresión y R² en cada gráfico

### Boxplots comparativos por grupo GDM

- [ ] Boxplot de `bmi_prepreg_kg_m2` por `label_gdm`
- [ ] Boxplot de `fpg_mmol_l` por `label_gdm`
- [ ] Boxplot de `hba1c_percent` por `label_gdm`
- [ ] Boxplot de `map_mmHg` por `label_gdm`
- [ ] Comentar diferencias visuales entre grupos

### Interpretación clínica

- [ ] Discutir asociaciones relevantes encontradas
- [ ] Explicar implicancias clínicas de correlaciones fuertes
- [ ] Relacionar hallazgos con literatura sobre GDM

---

## 2.6 Conclusiones e Interpretación Clínica (0% completado) 🔴 CRÍTICO

**Estado actual**: Sección inexistente.

### Resumen de hallazgos

- [ ] Síntesis de variables con distribución no normal y consecuencias
- [ ] Resumen de diferencias significativas entre grupos (GDM vs No-GDM)
- [ ] Destacar dirección de diferencias (qué grupo tiene valores más altos/bajos)

### Correlaciones clínicamente relevantes

- [ ] Listar correlaciones fuertes encontradas
- [ ] Explicar significado clínico de cada asociación
- [ ] Discutir posibles relaciones causales vs correlación espuria

### Limitaciones del estudio

- [ ] Comentar sobre datos faltantes y su posible impacto
- [ ] Discutir sesgos potenciales en la muestra
- [ ] Mencionar variables confusoras no controladas

### Próximos pasos

- [ ] Proponer análisis multivariado (regresión logística)
- [ ] Sugerir validación cruzada de modelos predictivos
- [ ] Recomendar estudios adicionales

---

## 📊 Resumen de Progreso por Sección

| Sección | Progreso Efectivo | Tareas Pendientes | Urgencia |
|---------|-------------------|-------------------|----------|
| 2.1 Exploración descriptiva | 56% | ~12 tareas | 🟡 Media |
| 2.2 Intervalos de confianza | 54% | ~17 tareas | 🟡 Media |
| 2.3 Pruebas de hipótesis | 8% | ~18 tareas | 🔴 Alta |
| 2.4 Evaluación de normalidad | 85% | ~8 tareas | 🟢 Baja |
| 2.5 Análisis bivariado | 28% | ~13 tareas | 🔴 Alta |
| 2.6 Conclusiones | 0% | ~11 tareas | 🔴 Alta |
| **GLOBAL** | **39%** | **~79 tareas** | |

---

## 📝 Notas de Trabajo

### Orden sugerido de ejecución

1. **Completar 2.4** (85% → 100%): Agregar QQ-plots y transformaciones (2-3 horas)
2. **Avanzar 2.5** (28% → 80%): Correlaciones y gráficos bivariados (4-5 horas)
3. **Completar 2.3** (8% → 100%): Todas las pruebas de hipótesis (6-8 horas)
4. **Completar 2.2** (54% → 100%): IC faltantes (3-4 horas)
5. **Mejorar 2.1** (56% → 100%): Visualizaciones e interpretaciones (2-3 horas)
6. **Redactar 2.6** (0% → 100%): Conclusiones finales (2-3 horas)

**Tiempo estimado total**: 19-26 horas de trabajo

### Integración de tareas

- Los IC para diferencias de medias (2.2) se relacionan con las pruebas de hipótesis (2.3)
- Las visualizaciones de 2.1 pueden reutilizarse para interpretación en 2.6
- Los resultados de normalidad (2.4) determinan qué tests usar en 2.3
- El análisis bivariado (2.5) alimenta las conclusiones de 2.6

### Recursos necesarios

- `auxiliar_functions.py`: verificar que tenga todas las funciones necesarias
- Librerías: scipy.stats, statsmodels (para pruebas adicionales si es necesario)
- Referencias clínicas: rangos normales de HbA1c, FPG, presión arterial

---

**Última actualización**: 11 de noviembre de 2025  
**Fuente**: Evaluación del profesor David Medina (ver `__pycache__/README.md`)  
**Archivo complementario**: `TASKS.md` (organizado por prioridad)
