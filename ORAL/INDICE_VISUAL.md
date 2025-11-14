# Índice Visual - Mapa Conceptual del Análisis

Estructura visual para navegar rápidamente el análisis completo. Útil como referencia rápida durante la preparación.

---

## ESTRUCTURA JERÁRQUICA DEL ANÁLISIS

```
ANÁLISIS EXPLORATORIO DE GDM
│
├─ FASE 1: PREPARACIÓN DE DATOS
│  ├─ Dataset Sintético (1500 registros, 17% GDM+)
│  ├─ Exploración Inicial
│  │  ├─ Dimensiones
│  │  ├─ Tipos de datos
│  │  └─ Distribución de clases
│  ├─ Análisis de Faltantes (MCAR/MAR)
│  └─ Estadística Descriptiva
│     └─ Media, mediana, IQR, min, max
│
├─ FASE 2: DETECCIÓN Y LIMPIEZA DE OUTLIERS
│  ├─ Método 1: IQR (univariado)
│  ├─ Método 2: Isolation Forest Categóricas (multivariado)
│  ├─ Método 3: Isolation Forest Continuas (multivariado)
│  ├─ Método 4: Isolation Forest Todas (multivariado integral)
│  ├─ Sistema de Votación
│  │  └─ Decisión: Eliminar si vote ≥ 3
│  └─ Resultado: df_filter (dataset limpio)
│
├─ FASE 3: INTERVALOS DE CONFIANZA
│  ├─ Cambio Metodológico
│  │  ├─ Antes: Submuestras aleatorias (sesgos)
│  │  └─ Después: Muestra completa (robustez)
│  ├─ IC para Media (95%)
│  │  ├─ Paramétrico: Distribución t
│  │  └─ Percentílico: Bootstrap
│  ├─ IC para Varianza
│  │  └─ Distribución chi-cuadrado
│  └─ Variables Clave: IMC, FPG, HbA1c
│
├─ FASE 4: PRUEBAS DE HIPÓTESIS
│  ├─ Verificación de Supuestos
│  │  ├─ Normalidad (Shapiro-Wilk)
│  │  │  └─ Hallazgo: Mayoría NO normales
│  │  └─ Homocedasticidad (Levene)
│  │
│  ├─ Comparación Dos Grupos (Continuas)
│  │  ├─ Si Normal + Homogéneo → t-test Student
│  │  ├─ Si Normal + Heterogéneo → Welch t-test
│  │  └─ Si No Normal → Mann-Whitney U (usado aquí)
│  │
│  ├─ Comparación Proporciones (Binarias)
│  │  ├─ Si valores esperados ≥ 5 → Chi-cuadrado
│  │  └─ Si valores esperados < 5 → Fisher exacto
│  │
│  ├─ Comparación k Grupos
│  │  ├─ Si Normal + Homogéneo → ANOVA
│  │  └─ Si No Normal → Kruskal-Wallis
│  │
│  └─ Resultados Significativos (p < 0.05)
│     ├─ Variables continuas: IMC, FPG, edad, HOMA-IR
│     └─ Variables binarias: GDM previa, PCOS, tabaco
│
├─ FASE 5: ANÁLISIS BIVARIADO
│  ├─ Correlación de Pearson (lineal)
│  ├─ Correlación de Spearman (monotónica)
│  ├─ Matrices por Grupo
│  │  ├─ GDM+ (positivos)
│  │  ├─ GDM- (negativos)
│  │  └─ Diferencia (GDM- - GDM+)
│  ├─ Identificación de Colinealidad
│  │  ├─ Insulina-HOMA (r = 0.85, esperada por cálculo)
│  │  ├─ PAD-PAM (r = 0.82, esperada fisiológicamente)
│  │  └─ FPG-HOMA (r = 0.72, ambas metabólicas)
│  └─ Visualizaciones
│     ├─ Heatmaps (Pearson, Spearman, diferencias)
│     └─ Pairplot (todas relaciones bivariadas)
│
└─ FASE 6: SÍNTESIS E INTERPRETACIÓN
   ├─ Hallazgos Principales
   │  ├─ Diferencias en variables metabólicas
   │  ├─ Factores de riesgo reproductivos relevantes
   │  └─ Estructura de correlación similar entre grupos
   ├─ Interpretación Clínica
   │  ├─ IMC: Factor de riesgo metabólico
   │  ├─ FPG: Indicador de hiperglucemia incipiente
   │  ├─ HOMA-IR: Resistencia a insulina
   │  ├─ GDM previa: Factor de riesgo más fuerte
   │  └─ PCOS: Comparte fisiopatología (resistencia a insulina)
   ├─ Limitaciones
   │  ├─ Dataset sintético (no generalizable directamente)
   │  ├─ Diseño transversal (sin causalidad)
   │  ├─ Análisis univariado/bivariado (sin control de confusoras)
   │  └─ Exclusión por lista (posibles sesgos)
   └─ Próximos Pasos
      ├─ Validación en cohortes reales
      ├─ Análisis multivariado (regresión logística)
      └─ Modelos predictivos (machine learning)
```

---

## MATRIZ DE MÉTODOS ESTADÍSTICOS APLICADOS

```
╔════════════════════════╦════════════════════╦════════════════════╗
║ Tipo de Comparación    ║ Supuesto Clave     ║ Prueba Utilizada   ║
╠════════════════════════╬════════════════════╬════════════════════╣
║ Dos grupos            ║ Normalidad         ║ Mann-Whitney U     ║
║ (variables continuas) ║ (mayoría falla)    ║ (no paramétrica)   ║
╠════════════════════════╬════════════════════╬════════════════════╣
║ Dos grupos            ║ Independencia      ║ Chi-cuadrado o     ║
║ (proporciones)        ║ (frecuencias)      ║ Fisher            ║
╠════════════════════════╬════════════════════╬════════════════════╣
║ k > 2 grupos          ║ Normalidad en todos║ Kruskal-Wallis     ║
║ (variables continuas) ║ (si falla)         ║ (no paramétrica)   ║
╠════════════════════════╬════════════════════╬════════════════════╣
║ Asociación lineal     ║ Linealidad         ║ Pearson            ║
║ (dos variables)       ║ (si no → Spearman) ║ + Spearman         ║
╚════════════════════════╩════════════════════╩════════════════════╝
```

---

## DECISIONES Y SUS JUSTIFICACIONES

```
DECISIÓN 1: ELIMINACIÓN DE OUTLIERS
├─ Opción A: IQR sólo          ❌ Limitado (univariado)
├─ Opción B: IF sólo           ❌ Riesgo de sobre-eliminación
├─ Opción C: Votación (4 mét.) ✅ ELEGIDA
│  └─ Umbral ≥ 3               ✅ ELEGIDO (conservador)
│     └─ Elimina 1-2% de datos
└─ Opción D: vote ≥ 1          ❌ Demasiado agresivo

DECISIÓN 2: INTERVALOS DE CONFIANZA
├─ Opción A: Submuestras aleatorias  ❌ Introduce sesgos
├─ Opción B: Muestra completa        ✅ ELEGIDA (robusta)
├─ Complemento: IC percentílicos     ✅ AGREGADO (robusto a no normalidad)
└─ Nivel: 95%                        ✅ Estándar en biomedicina

DECISIÓN 3: SELECCIÓN DE PRUEBAS
├─ Opción A: Siempre paramétrica     ❌ Viola supuestos
├─ Opción B: Árbol de decisión       ✅ ELEGIDA
│  ├─ Verificar normalidad primero
│  ├─ Verificar homocedasticidad si normal
│  └─ Seleccionar según resultado
└─ Opción C: Siempre no paramétrica  ❌ Pierde poder estadístico

DECISIÓN 4: ANÁLISIS DE CORRELACIONES
├─ Opción A: Pearson sólo           ❌ Sensible a no normalidad
├─ Opción B: Spearman sólo          ❌ Información incompleta
└─ Opción C: Ambas complementarias  ✅ ELEGIDA (robustez)
```

---

## FLUJO DE TOMA DE DECISIONES - ÁRBOL

```
                        ANÁLISIS INICIADO
                              |
                              v
                    ¿Hay outliers?
                        /    \
                      SÍ      NO
                      |        |
                      v        |
              Votación 4 métodos
                      |        |
           vote ≥ 3?  |        |
            /    \    |        |
           SÍ      NO  |        |
           |       |   |        |
           v       v   |        |
      Eliminar  Guardar|        |
           |       |   |        |
           └───┬───┴───┘        |
               v                |
          df_filter             |
               └────┬───────────┘
                    v
            Calcular IC (95%)
                    |
         Usar muestra completa
         + IC percentílicos
                    |
                    v
         ¿Comparar dos grupos?
              /    |    \
    Continuas|Binarias|k>2 grupos
            /      |      \
           v       v       v
    Shapiro-W Chi-sq  Normalidad
    Levene   Fisher    en todos?
       |       |        /  \
       v       v      SÍ    NO
    Seleccionar Seleccionar |     |
    prueba      prueba      v     v
  (t/MW/Welch) (χ²/Fisher) ANOVA Kruskal-W
       |         |          |     |
       └─────────┴──────────┴─────┘
              |
              v
         p-valor < 0.05?
            /        \
           SÍ        NO
           |          |
    Significativo  No significativo
```

---

## MAPA DE VARIABLES - DÓNDE ENCONTRAR CADA ANÁLISIS

```
VARIABLES CONTINUAS:
├─ Demográficas
│  ├─ age_years                    → Pruebas hipótesis [6.5], IC [5.2], Correlaciones [7]
│  └─ gestational_weeks            → Descriptiva [2.2]
├─ Antropométricas
│  └─ bmi_prepreg_kg_m2           → IC [5.2], Pruebas [6.5] ⭐ DIFERENCIA SIGNIFICATIVA
├─ Hemodinámicas
│  ├─ systolic_bp_mmHg            → Pruebas [6.5], Correlaciones [7]
│  ├─ diastolic_bp_mmHg           → Pruebas [6.5], Sin diferencia significativa
│  └─ map_mmHg                    → Descriptiva, Correlaciones [7]
├─ Metabólicas
│  ├─ fpg_mmol_l                  → IC [5.2], Pruebas [6.5] ⭐ DIFERENCIA SIGNIFICATIVA
│  ├─ hba1c_percent               → IC [5.2], Pruebas [6.5] ⭐ PEQUEÑA DIFERENCIA
│  ├─ insulin_uIU_ml              → Pruebas [6.5], Sin diferencia significativa
│  └─ homa_ir                     → Pruebas [6.5] ⭐ DIFERENCIA SIGNIFICATIVA
├─ Perfil Lipídico
│  ├─ triglycerides_mmol_l        → Descriptiva, Correlaciones [7]
│  └─ hdl_mmol_l                  → Descriptiva, Correlaciones [7]
├─ Estilo de Vida
│  ├─ physical_activity_level     → ANOVA/Kruskal-W [6.7]
│  └─ diet_score_0_100            → Descriptiva, Correlaciones [7]

VARIABLES BINARIAS/CATEGÓRICAS:
├─ Antecedentes Obstétricos
│  ├─ parity                      → Exploración [2.1.5.2]
│  └─ previous_gdm                → Proporciones [6.6] ⭐ MUY SIGNIFICATIVA
├─ Comorbilidades
│  ├─ family_history_t2d          → Proporciones [6.6], No significativa
│  ├─ pcos                        → Proporciones [6.6] ⭐ SIGNIFICATIVA
│  └─ smoking_first_trimester     → Proporciones [6.6] ⭐ SIGNIFICATIVA

VARIABLE OBJETIVO:
└─ label_gdm (0/1)               → Usada en todas las comparaciones GDM+/GDM-
                                 → 17% positivos, 83% negativos
```

---

## RESULTADOS RESUMIDOS

```
┌─ VARIABLES CON DIFERENCIAS SIGNIFICATIVAS (p < 0.05)
│  Continuas: IMC, FPG, HbA1c, edad, presión sistólica, HOMA-IR
│  Binarias:  GDM previa, PCOS, tabaquismo
│
├─ VARIABLES SIN DIFERENCIAS SIGNIFICATIVAS
│  Continuas: Presión diastólica, insulina sérica
│  Binarias:  Antecedentes familiares
│
├─ COLINEALIDAD IDENTIFICADA (|r| > 0.7)
│  Esperada:  Insulina-HOMA-IR (0.85), PAD-PAM (0.82)
│  Relevante: FPG-HOMA-IR (0.72) - ambas metabólicas
│
└─ ESTRUCTURA DE CORRELACIÓN
   Similar entre GDM+ y GDM- (diff máx < 0.16)
   → Mecanismos fisiológicos similares
```

---

## LIBRERÍAS Y FUNCIONES - LOCALIZACIÓN RÁPIDA

```
┌─ LIBRERÍAS IMPORTADAS (Celda 1)
│  ├─ pandas (df_data, manipulación)
│  ├─ numpy (operaciones numéricas)
│  ├─ scipy.stats (pruebas estadísticas)
│  ├─ sklearn.ensemble.IsolationForest (detección anomalías)
│  └─ matplotlib/seaborn (visualizaciones)
│
├─ FUNCIONES AUXILIARES (auxiliar_functions.py)
│  ├─ calculate_ic_mean()          → IC para media (dist. t)
│  ├─ calculate_ic_std()           → IC para varianza (dist. χ²)
│  ├─ get_range_outlier()          → Límites IQR
│  ├─ check_is_outlier()           → Clasificar valor atípico
│  ├─ categorize_iqr()             → Convertir conteo a binario
│  └─ generate_df_counts()         → Tabla resumen de conteos
│
├─ FUNCIONES PERSONALIZADAS (IN SCRIPT)
│  ├─ compare_two_groups_numeric() → Comparación bivariada continua
│  ├─ compare_proportions()        → Comparación bivariada binaria
│  └─ compare_k_groups()           → ANOVA/Kruskal-Wallis
│
└─ VISUALIZACIONES
   ├─ histplot + KDE              → Distribuciones por grupo
   ├─ boxplot                     → Variabilidad y outliers
   ├─ violinplot                  → Forma de distribuciones
   ├─ heatmap                     → Correlaciones
   └─ pairplot                    → Todas las relaciones bivariadas
```

---

## CHECKLIST DE VERIFICACIÓN - ¿LO CUBRISTE TODO?

Para prepararte para la oral:

- [ ] ¿Entiendo por qué se eliminaron outliers con criterio ≥ 3?
- [ ] ¿Puedo explicar la diferencia entre IQR e Isolation Forest?
- [ ] ¿Sé por qué se cambió de submuestras a muestra completa para IC?
- [ ] ¿Entiendo el árbol de decisión para seleccionar pruebas?
- [ ] ¿Reconozco que mayoría de variables NO son normales?
- [ ] ¿Sé qué significa p < 0.05 correctamente (y qué NO significa)?
- [ ] ¿Puedo justificar por qué se usaron pruebas no paramétricas?
- [ ] ¿Entiendo colinealidad y cuándo es problema?
- [ ] ¿Sé interpretar IC percentílicos en contexto de no normalidad?
- [ ] ¿Reconozco limitaciones de dataset sintético y diseño transversal?
- [ ] ¿Puedo conectar hallazgos estadísticos con interpretación clínica?
- [ ] ¿Sé qué falta (análisis multivariado) y por qué?

Si respondiste SÍ a todas → Estás listo para la oral

---

## NAVEGACIÓN POR DOCUMENTOS DE REFERENCIA

```
📄 CONCEPTOS.md
   ├─ Glosario completo de métodos
   ├─ Definiciones de técnicas utilizadas
   └─ Leer cuando: necesitas recordar qué es una técnica específica

📄 PREGUNTAS_ORAL.md
   ├─ 54 preguntas potenciales
   ├─ Respuestas esperadas
   └─ Leer cuando: quieres practicar respuestas

📄 RESUMEN_EJECUTIVO.md
   ├─ Frases clave para la oral
   ├─ Tablas resumen de decisiones
   └─ Leer cuando: necesitas respuesta rápida a decisiones

📄 INDICE_VISUAL.md (este documento)
   ├─ Mapas mentales y flujos
   ├─ Estructura jerárquica
   └─ Leer cuando: quieres ver "big picture" rápidamente
```

---

## INFORMACIÓN CRÍTICA PARA NO OLVIDAR

**En Rojo (CRÍTICO):**
1. ❌ **NO** dices "95% de los datos están en el IC" - eso es FALSO
2. ❌ **NO** afirmas causalidad (es diseño transversal)
3. ❌ **NO** olvides reportar supuestos junto con prueba usada
4. ❌ **NO** ignores que mayoría variables no son normales

**En Verde (FORTALEZA):**
1. ✅ Sistema de votación es conservador y bien justificado
2. ✅ Cambio de metodología en IC demuestra pensamiento crítico
3. ✅ Verificación de supuestos muestra rigor estadístico
4. ✅ Uso de métodos complementarios muestra robustez

---

**Última revisión:** Usa este documento como "índice visual" durante la oral. Si te hacen pregunta, localiza aquí la sección, lee en detalle el CONCEPTOS.md o RESUMEN_EJECUTIVO.md, y responde con confianza.

¡Éxito! 🎓
