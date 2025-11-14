# Preguntas Sugeridas para Examen Oral - Preparación

Este documento contiene preguntas potenciales para el examen oral, organizadas por sección temática del informe. Cada pregunta está diseñada para evaluar comprensión profunda, no solo conocimiento de valores.

---

## SECCIÓN 1: DATASET Y PREPARACIÓN

### Preguntas sobre Dataset y EDA

1. **¿Por qué se utilizó un dataset sintético en lugar de datos reales? ¿Qué ventajas y limitaciones tiene esto?**
   - Espera: Control de variables conocidas, ausencia de sesgos no medidos
   - Limitación: No generalización directa sin validación

2. **¿Qué significa que el dataset tenga una prevalencia de GDM del 17%? ¿Por qué no es 50-50?**
   - Refleja realidad clínica, afecta análisis comparativos
   - Balance de clases: relevancia en modelado futuro

3. **¿Cuál es la diferencia entre MCAR y MAR en términos de datos faltantes?**
   - MCAR: ausencia sin relación con otras variables
   - MAR: valores faltantes relacionados con variables observadas

---

## SECCIÓN 2: DETECCIÓN DE OUTLIERS

### Preguntas sobre Métodos de Outliers

4. **¿Cómo funciona el método IQR para detectar outliers? ¿Cuáles son sus limitaciones?**
   - Fórmula: [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
   - Limitación: Solo univariado, no detecta combinaciones anómalas

5. **¿Por qué se utilizó Isolation Forest además de IQR? ¿Cuál es la principal diferencia?**
   - IF: Multivariado, detecta combinaciones inusuales
   - IQR: Univariado, clásico pero complementario

6. **Explica el sistema de votación de 4 métodos. ¿Por qué el criterio es vote ≥ 3 y no ≥ 1?**
   - Criterio conservador: preserva variabilidad biológica
   - Evita sobre-eliminación de datos legítimos

7. **¿Qué es el Isolation Forest? ¿Cómo "aísla" observaciones anómalas?**
   - Particiones aleatorias, anomalías se aíslan más rápido
   - Multivariado, no paramétrico

8. **¿Cuál sería el impacto de tener un criterio de eliminación más agresivo (vote ≥ 1)?**
   - Menos datos, pero posiblemente más sesgado (perdería variabilidad real)
   - Trade-off: limpieza vs representatividad

---

## SECCIÓN 3: INTERVALOS DE CONFIANZA

### Preguntas sobre IC

9. **¿Qué es un intervalo de confianza del 95%? ¿Qué significa interpretarlo correctamente?**
   - Rango probable del parámetro poblacional con 95% confianza
   - IMPORTANTE: No es "95% de los datos está aquí", sino "95% de confianza que μ está aquí"

10. **¿Por qué se cambió de usar submuestras aleatorias a la muestra completa para calcular IC?**
    - Submuestreo: introduce variabilidad artificial, afecta reproducibilidad
    - Muestra completa: estimaciones más robustas

11. **¿Cuál es la diferencia entre IC paramétricos e IC percentílicos?**
    - Paramétricos: asumen distribución (t de Student), requieren normalidad
    - Percentílicos: basados en bootstrap, robustos sin asumir distribución

12. **¿Cómo se interpreta que el IC de una diferencia de medias NO incluya el cero?**
    - Evidencia de diferencia estadísticamente significativa entre grupos

13. **¿Por qué usaste distribución t de Student y no normal (z) para calcular IC?**
    - Muestra finita, desviación estándar estimada de muestra (no poblacional)

---

## SECCIÓN 4: PRUEBAS DE HIPÓTESIS

### Preguntas sobre Normalidad y Supuestos

14. **Describir el árbol de decisión para seleccionar la prueba de hipótesis correcta.**
    - Primero: ¿Normalidad? (Shapiro-Wilk)
    - Segundo (si normal): ¿Homocedasticidad? (Levene)
    - Tercero: seleccionar t-test, Welch, o Mann-Whitney según resultados

15. **¿Qué es la prueba de Shapiro-Wilk? ¿Qué hipótesis nula contrasta?**
    - H₀: Los datos provienen de distribución normal
    - Si p < 0.05: rechazar normalidad

16. **¿Qué es la prueba de Levene? ¿Por qué es importante antes de un t-test?**
    - Prueba homocedasticidad (igualdad de varianzas)
    - Importante: determina si usar t-test clásico o Welch

17. **¿Qué hallazgo sorpresivo se tuvo sobre normalidad? ¿Cómo se abordó?**
    - La mayoría de variables NO eran normales
    - Mitigación: usar Mann-Whitney U, IC percentílicos, verificar supuestos

### Preguntas sobre Pruebas de Hipótesis Específicas

18. **¿Cuándo se usa Mann-Whitney U en lugar de t-test? ¿Cuáles son sus características?**
    - Cuando falla normalidad
    - No paramétrica, basada en rangos, robusta

19. **¿Cuál es la diferencia entre t-test de Student y Welch t-test?**
    - Student: requiere homocedasticidad
    - Welch: robusto con varianzas desiguales

20. **¿Cómo se interpretan proporcionalmente el p-valor y α = 0.05?**
    - p < 0.05: rechazar H₀ (diferencia significativa)
    - p ≥ 0.05: no rechazar H₀ (insuficiente evidencia)
    - Nota: no significa H₀ es verdadera

21. **¿Por qué se utilizó prueba de Chi-cuadrado vs Fisher exacto para proporciones?**
    - Chi-cuadrado: si todos los valores esperados ≥ 5
    - Fisher: si algún valor esperado < 5

22. **¿Qué es ANOVA y cuándo se usa? ¿Cuál es su alternativa?**
    - ANOVA: compara medias de k > 2 grupos
    - Alternativa: Kruskal-Wallis si no normalidad

### Preguntas sobre Interpretación de Resultados

23. **¿Qué variables mostraron diferencias significativas entre GDM+ y GDM-?**
    - IMC, FPG, HOMA-IR, edad, presión sistólica
    - (Completar con p-valores y magnitud de diferencias del informe)

24. **¿Cuáles fueron los hallazgos sobre proporciones? (familiares, GDM previa, PCOS, tabaco)**
    - GDM previa: muy significativa (factor de riesgo fuerte)
    - PCOS y tabaco: también significativos
    - Familiares: no significativo en este dataset

---

## SECCIÓN 5: ANÁLISIS BIVARIADO

### Preguntas sobre Correlaciones

25. **¿Cuál es la diferencia entre correlación de Pearson y Spearman?**
    - Pearson: asociación lineal, paramétrica
    - Spearman: asociación monotónica, no paramétrica (basada en rangos)

26. **¿Por qué se usaron ambas correlaciones (Pearson y Spearman) si no normalidad?**
    - Complementariedad: Spearman es más robusta
    - Confirmación: si ambas coinciden, mayor confianza

27. **¿Qué correlación fuerte se encontró entre Insulina y HOMA-IR? ¿Era esperada?**
    - r ≈ 0.85 (correlación muy fuerte)
    - Esperada: HOMA-IR se calcula directamente con insulina
    - Implicación: no son independientes, solo incluir una en modelos multivariados

28. **¿Qué es la colinealidad? ¿Dónde se identificó en el análisis?**
    - Dos variables altamente correlacionadas (r > 0.7)
    - Problemas: multicolinealidad en modelos, estimación inestable de efectos
    - Ejemplos: Insulina-HOMA-IR, PAD-PAM

29. **¿Se encontraron diferencias en estructura de correlación entre GDM+ y GDM-?**
    - No (diferencias máximas < 0.16)
    - Implicación: mecanismos fisiológicos similares en ambos grupos

### Preguntas sobre Visualizaciones

30. **¿Qué información proporciona un heatmap de correlación que los números solos no dan?**
    - Visualización rápida de patrones
    - Identificación de clusters de variables correlacionadas

31. **¿Cómo se interpreta un pairplot? ¿Qué revela sobre separabilidad de grupos?**
    - Diagonal: distribuciones marginales
    - Off-diagonal: relaciones bivariadas
    - Separabilidad: limitada en la mayoría de combinaciones (necesita multivariado)

---

## SECCIÓN 6: DECISIONES METODOLÓGICAS

### Preguntas sobre Justificación de Métodos

32. **¿Cuál fue la principal decisión metodológica sobre manejo de outliers?**
    - Votación de 4 métodos con umbral ≥ 3
    - Justificación: conservador, preserva datos legítimos

33. **¿Por qué se eliminaron outliers ANTES de hacer pruebas de hipótesis?**
    - Mejora estabilidad de estimadores
    - Valores extremos pueden sesgar resultados

34. **¿Cómo se evitó el sesgo de submuestreo en el cálculo de IC?**
    - Se usó muestra completa en lugar de submuestras aleatorias
    - Decisión: tras identificar que repetido submuestreo introduce variabilidad artificial

35. **Explicar la frase "se decidió evitar sesgo usando el grupo completo en vez de secciones"**
    - Submuestreo aleatorio repetido: introduce sesgos metodológicos
    - Muestra completa: estimaciones más robustas y reproducibles

---

## SECCIÓN 7: CONCLUSIONES Y LIMITACIONES

### Preguntas sobre Interpretación Global

36. **¿Cuál fue el principal hallazgo sobre variables diferenciadores entre GDM+ y GDM-?**
    - Variables metabólicas (IMC, FPG, HOMA-IR) muestran diferencias significativas
    - Consistente con literatura científica

37. **¿Qué limitación crítica tiene este estudio para establecer causalidad?**
    - Diseño transversal (no longitudinal)
    - No se puede determinar si variables causan GDM o son consecuencia

38. **¿Por qué fue importante utilizar métodos no paramétricos?**
    - Mayoría de variables no eran normales
    - Robustez: métodos no paramétricos menos sensibles a violaciones de supuestos

39. **¿Qué análisis aún falta para construir un modelo predictivo?**
    - Regresión logística (multivariada)
    - Validación cruzada
    - Evaluación con métricas (AUC-ROC, sensibilidad, especificidad)

40. **¿Cuál sería el siguiente paso lógico en la investigación?**
    - Validación en cohorte independiente
    - Estudios longitudinales prospectivos
    - Análisis multivariado para identificar predictores independientes

---

## SECCIÓN 8: TÉCNICAS Y HERRAMIENTAS

### Preguntas sobre Implementación

41. **¿Qué librerías Python se utilizaron y para qué?**
    - Pandas: manipulación de datos
    - SciPy: pruebas estadísticas
    - Scikit-learn: Isolation Forest
    - Matplotlib/Seaborn: visualizaciones

42. **¿Cuál fue el propósito de las funciones auxiliares personalizadas?**
    - Reutilizable en múltiples variables
    - Evita duplicación de código
    - Centraliza lógica de cálculo (ej: IC, outliers)

43. **¿Cómo se garantizó la validación de transformaciones de datos?**
    - Exploración iterativa: después de cada operación, verificación
    - Ejemplo: df_filter dimensiones, valores faltantes, distribuciones

---

## SECCIÓN 9: INTERPRETACIÓN CLÍNICA

### Preguntas sobre Relevancia Médica

44. **¿Por qué el IMC pregestacional es un marcador importante de riesgo de GDM?**
    - Adiposidad aumentada → resistencia a insulina
    - Conocido factor de riesgo en literatura clínica

45. **¿Qué significa que FPG sea 0.3 mmol/L mayor en grupo GDM+?**
    - Pequeño en magnitud absoluta pero significativo estadísticamente
    - Refleja estado de hiperglucemia incipiente característico de GDM

46. **¿Cuál fue el factor de riesgo más fuerte identificado?**
    - GDM previa (proporción mucho mayor en grupo GDM+)
    - Justificación: recurrencia de GDM es conocida en medicina

47. **¿Por qué PCOS está asociado con GDM según la fisiopatología?**
    - Ambos comparten mecanismo: resistencia a la insulina
    - Hiperandrogenismo puede afectar metabolismo glucídico

48. **¿Qué implicaciones clínicas tiene que tabaquismo sea más frecuente en GDM+?**
    - Factor de riesgo posiblemente modificable
    - Consejería de cesación debería ser prioridad en cuidado prenatal

---

## PREGUNTAS INTEGRADORAS (SÍNTESIS)

### Preguntas que Requieren Conexión entre Conceptos

49. **Describe el flujo completo desde detección de outliers hasta pruebas de hipótesis. ¿Por qué cada paso?**
    - Outliers → df_filter limpio
    - Normalidad/homocedasticidad → seleccionar prueba
    - Prueba aplicada → p-valor → decisión

50. **¿Cómo se relaciona la falta de normalidad encontrada con la selección de métodos estadísticos?**
    - No normalidad → rechazar métodos paramétricos asimétricos
    - Adoptar no paramétricos y IC percentílicos
    - Transparencia: reportar supuestos junto con prueba

51. **¿Por qué se complementaron IC paramétricos con percentílicos?**
    - Redundancia estadística: confirmar hallazgos de formas distintas
    - Robustez ante violaciones de normalidad
    - Confianza aumentada si ambos coinciden

52. **Si tuvieras que defender este análisis ante un comité académico, ¿cuál sería tu argumento principal?**
    - Rigor metodológico: verificación de supuestos antes de pruebas
    - Conservadurismo en decisiones: eliminación conservadora de outliers, múltiples métodos
    - Transparencia: reporteo completo de decisiones y justificaciones
    - Complementariedad: uso de métodos paramétricos y no paramétricos

53. **¿Cómo cambiaría tu análisis si el dataset tuviera 100% normalidad?**
    - Podrías usar t-test, ANOVA directamente sin verificar alternativas
    - IC basadas en distribución t sin complementar con percentílicos
    - Menos necesidad de Mann-Whitney U

54. **¿Qué hubieras hecho diferente si el balance de clases fuera 50-50 en lugar de 17-83%**
    - Menos necesidad de estratificación
    - Pruebas de proporciones serían menos afectadas
    - Pero comparación de grupos seguiría requiriendo verificación de supuestos

---

## NOTAS PARA LA PREPARACIÓN

### Estructura Sugerida para Respuestas

1. **Define el concepto** (qué es)
2. **Explica por qué se utilizó** (justificación, supuestos)
3. **Describe cómo se implementó** (en tu caso específico del informe)
4. **Interpreta los resultados** (qué significa, implicaciones clínicas)
5. **Reconoce limitaciones** (cuándo falla, alternativas consideradas)

### Expresiones Clave para Usar

- "Se verificaron los supuestos antes de..."
- "Debido a que la mayoría de variables no cumplían normalidad..."
- "Para evitar sesgos de..."
- "El sistema de votación proporcionó robustez al..."
- "Esto es consistente con la literatura científica que muestra..."
- "La implicación clínica es que..."
- "Como limitación, este es un dataset sintético..."
- "Para validar estos hallazgos, sería necesario..."

### Errores Comunes a Evitar

- ❌ Confundir IC 95% con "95% de los datos está aquí"
- ❌ Afirmar causalidad en un estudio transversal
- ❌ No reportar supuestos junto con prueba utilizada
- ❌ Decir "no hay diferencia" si p ≥ 0.05 (debería ser "insuficiente evidencia")
- ❌ Ignorar que mayoría de variables no eran normales
- ❌ Asumir que correlación = causalidad

---

**Recomendación Final:** Practica conectando conceptos. Los examinadores buscán comprensión profunda, no solo memorización. Sé capaz de explicar NO solo el "qué" sino el "por qué" de cada decisión metodológica.
