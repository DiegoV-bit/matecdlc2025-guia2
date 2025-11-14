# Preguntas de Interrogación basadas en `Entregable.ipynb`

1) ¿Cuál es la motivación y el objetivo general del estudio con respecto a la detección temprana de riesgo de GDM en el primer trimestre?
Respuesta: Caracterizar estadísticamente el dataset del primer trimestre y comprender las relaciones entre variables clínicas y el riesgo de GDM para apoyar la detección temprana (Sección 1.4: Objetivo general).
2) ¿Qué características tiene el dataset utilizado (tamaño muestral, tipo de datos, número de variables) y por qué es relevante que sea sintético?
Respuesta: Aproximadamente 1500 registros, 20 variables (continuas, discretas y categóricas), con valores faltantes y outliers simulados. Es sintético para reflejar escenarios clínicos realistas preservando control sobre patrones de datos (Sección 1.2 y 1.3).
3) ¿Cómo se caracterizan los patrones de datos faltantes (MCAR vs MAR) en el dataset y qué implicancias tienen para el análisis?
Respuesta: Se reportan patrones MCAR y MAR; esto exige cuantificación y manejo previo a análisis inferenciales, dado que los faltantes pueden sesgar estimaciones si no se abordan (Sección 1.3 y 2.1.3).
4) Explique el cálculo del IQR y cómo se obtienen los umbrales para identificar outliers en una variable continua.
Respuesta: IQR = Q3 − Q1. Los umbrales se calculan con `get_range_outlier(Q1, Q3, IQR)` y se evalúa cada valor con `check_is_outlier` para marcar outliers (Sección 2.1.4–2.1.5 y código correspondiente).
5) ¿Por qué se decidió usar múltiples métodos de detección de outliers (IQR e Isolation Forest en tres configuraciones) y cómo se complementan entre sí?
Respuesta: Para robustez y menor tasa de falsos positivos: IQR capta extremos univariados y Isolation Forest detecta anomalías multivariadas (categóricas, continuas y combinadas). Se integran vía sistema de votación (Sección 2.1.5 y justificación).
6) Describa el sistema de votación para outliers: ¿qué significa obtener 0, 1–2, 3 o 4 votos y cuál fue el criterio de filtrado aplicado?
Respuesta: 0 votos: normal; 1–2: outlier leve (se conserva); 3: moderado (se elimina); 4: extremo (se elimina). Se filtró con `vote_outlier < 3`, eliminando registros con ≥3 votos (Sección 2.1.5.3–2.1.5.4).
7) ¿Cómo se remapearon las salidas de Isolation Forest (1 y -1) y por qué fue necesario hacerlo antes de sumar los votos?
Respuesta: Se remapeó 1→0 (no outlier) y −1→1 (outlier) para homogenizar las señales de los cuatro métodos antes de sumarlas en `vote_outlier` (Sección 2.1.5 y código de remapeo).
8) ¿Cuántos registros se eliminaron tras aplicar el filtro `vote_outlier < 3` y qué riesgos de sesgo introduce esta decisión?
Respuesta: El documento muestra la impresión de la cantidad eliminada, pero no reporta un número específico en el texto. Riesgos: posible sesgo si los casos extremos tienen significado clínico; se adoptó criterio conservador para reducir ese riesgo (Sección 2.1.5.4).
9) ¿Qué diferencias visuales destacaría entre los grupos GDM+ y GDM- en histogramas, boxplots y violinplots para variables como IMC, FPG o HbA1c?
Respuesta: Se generan las visualizaciones comparativas por grupo, pero el informe no sintetiza diferencias específicas en texto. La comparación se plantea para IMC, FPG y HbA1c (Sección 2.1.6). Sin ejecutar las celdas no se listan patrones concretos.
10) ¿Qué variables categóricas/binarias se excluyeron de los análisis de estadística descriptiva de continuas y de correlaciones, y cuál es la justificación?
Respuesta: `parity`, `family_history_t2d`, `previous_gdm`, `pcos`, `smoking_first_trimester`, `label_gdm`, `physical_activity_level`. Justificación: no son continuas para estadística descriptiva de continuas/correlación Pearson-Spearman (Sección 2.1.4 y 2.5.1).
11) En los intervalos de confianza, ¿por qué se utiliza t de Student para la media y chi-cuadrado para la varianza? Ilustre cómo cambia la amplitud del IC al variar n.
Respuesta: t de Student modela la incertidumbre de la media con σ desconocida; chi-cuadrado se usa para la varianza. La amplitud disminuye al aumentar n (se evalúa n=10…100). El notebook imprime resultados por variable clave, sin tabla resumen (Sección 2.2 y 2.2.1).
12) Plantee H0 y H1 para comparar la media de presión arterial (sistólica o diastólica) entre GDM+ y GDM-. ¿Qué pruebas consideraría según normalidad y homocedasticidad?
Respuesta: H0: μ|GDM=0 = μ|GDM=1; H1: μ|GDM=0 ≠ μ|GDM=1. Si hay normalidad y varianzas iguales: t clásico; normalidad sin homocedasticidad: Welch; sin normalidad: Mann–Whitney U (Sección 2.3 y 2.3.1).
13) Explique el flujo de decisión implementado para seleccionar entre t-test clásico, Welch y Mann–Whitney U. ¿Cómo influye la prueba de Levene en esta elección?
Respuesta: Se verifica Shapiro por grupo; si normal_ok, se usa t-test con `equal_var` decidido por Levene (p>α → varianzas iguales; p≤α → Welch). Si falla normalidad, se usa Mann–Whitney U (Sección 2.3.1, función `compare_two_groups_numeric`).
14) ¿Qué concluye de las pruebas de normalidad (Shapiro-Wilk y KS-Lilliefors) y cómo condicionan la elección de métodos paramétricos vs no paramétricos?
Respuesta: El notebook calcula ambas y reporta decisiones por variable (Normal/No normal), priorizando Shapiro. El texto no sintetiza resultados por variable; la elección de pruebas debe seguir p≥0.05 para paramétricas, p<0.05 para no paramétricas (Sección 2.4 y 2.4.1).
15) ¿Qué asociaciones bivariadas relevantes se observaron en las matrices de correlación (Pearson y Spearman) y cómo difieren entre GDM+ y GDM-?
Respuesta: Se generan matrices y heatmaps por grupo y la diferencia GDM−−GDM+. Se identifica automáticamente si hay |r|>0.7, con nota de que podría no haber correlaciones fuertes en datos sintéticos. El informe no lista pares específicos (Sección 2.5.1–2.5.2).
16) Analice el impacto del desbalance de clases (≈17% GDM+) en la interpretación de resultados y en futuros modelos predictivos.
Respuesta: El desbalance (17% positivos) refleja prevalencia real y puede afectar comparaciones y modelos (p. ej., métricas, umbrales). Se reconoce como consideración en el análisis (Sección 1.3: Desbalance de clases).
17) ¿Qué rol jugarían medidas de tamaño de efecto (p. ej., d de Cohen o r) en la interpretación clínica de diferencias entre grupos?
Respuesta: Complementan el p-valor con magnitud de diferencia para relevancia clínica. El notebook planifica reportarlas (tarea pendiente en 2.3) (Sección 2.3: tareas pendientes).
18) Señale limitaciones clave del estudio (naturaleza sintética del dataset, diseño transversal, desbalance de clases) y cómo podrían mitigarse.
Respuesta: Limitaciones: dataset sintético y representatividad; confusores no controlados; sesgos de selección; diseño transversal; desbalance de clases; alcance univariado/bivariado. Mitigación: validación externa, modelos multivariados, estudios longitudinales, balance de clases (Sección 2.6.4).
19) ¿Qué próximos pasos propondría (p. ej., regresión logística, validación cruzada, ROC) y qué variables anticipa con mayor poder discriminante?
Respuesta: Próximos pasos: regresión logística para GDM, validación cruzada, curvas ROC y umbrales, estudios longitudinales y validación externa. Se sugiere explorar variables metabólicas (IMC, FPG, HbA1c, HOMA-IR, insulina) según las tareas planificadas (Sección 2.6.5 y 2.3).
20) ¿Qué verificaciones adicionales haría sobre variables específicas (p. ej., paridad extrema, PCOS, antecedentes familiares) para asegurar calidad de datos y robustez de hallazgos?
Respuesta: El notebook incluye chequeos: distribución de categóricas/binarias, exploración de paridad extrema (p=5), y revisión de PCOS/antecedentes. Sin ejecución, no se listan cifras; la verificación apoya calidad y consistencia (Sección 2.1.2–2.1.5).

