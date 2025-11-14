# 📚 GUÍA INTEGRAL DE PREPARACIÓN PARA EXAMEN ORAL

## Informe: Análisis Exploratorio de Datos de Diabetes Gestacional

**Equipo:** Alma de Litio  
**Integrantes:** Pablo Gómez (Líder), Emmanuel Velásquez, Diego Vidal  
**Asignatura:** Matemática para Ciencias de la Computación  
**Universidad:** Universidad de Magallanes  
**Fecha:** Noviembre 2025

---

## ¿QUÉ ES ESTA GUÍA?

Esta carpeta contiene una **suite completa de documentos de referencia** diseñados específicamente para preparación del examen oral sobre el Informe de Análisis de GDM.

**NO es un duplicado del informe.** Es un conjunto de herramientas complementarias que te ayuda a:
- 🎯 Entender el "por qué" de cada decisión metodológica
- 📖 Localizar rápidamente cualquier concepto
- 🎤 Practicar respuestas a preguntas potenciales
- ⚡ Recordar frases clave durante el examen
- 🗺️ Ver la estructura completa del análisis de un vistazo

---

## 📄 DOCUMENTOS INCLUIDOS

### 1️⃣ **INDICE_MAESTRO.md** ← COMIENZA AQUÍ
**El mapa de todos los documentos**
- Índice de contenidos de cada documento
- Cómo usar la guía según tu necesidad
- Estrategia de preparación por semana
- Checklist pre-oral

**👉 Lectura recomendada:** 5 minutos PRIMERO

---

### 2️⃣ **INDICE_VISUAL.md**
**Diagramas y estructura visual del análisis**
- Árbol jerárquico de todas las fases
- Matrices de métodos aplicados
- Diagramas de flujo de toma de decisiones
- Mapas de variables
- Visualización del big picture

**👉 Cuándo usar:** Cuando quieres ver la estructura general
**👉 Formato:** Árboles ASCII, tablas, diagramas

---

### 3️⃣ **CONCEPTOS.md**
**Glosario y explicación detallada de todos los métodos**
- Definiciones formales de cada técnica
- Explicación del por qué se utilizó cada método
- Detalle de variables clínicas
- Limitaciones reconocidas de cada enfoque

**👉 Cuándo usar:** Necesitas definición formal o entender a fondo una técnica
**👉 Extensión:** ~7,500 palabras (lectura completa)

---

### 4️⃣ **RESUMEN_EJECUTIVO.md**
**Referencia rápida: decisiones clave y frases para memorizar**
- Tabla de decisiones clave con justificaciones
- Frases exactas para usar en la oral
- Árbol de decisión simplificado
- Puntos fuertes del análisis
- Respuestas a críticas potenciales

**👉 Cuándo usar:** Necesitas recordar rápidamente respuesta durante la oral
**👉 Extensión:** ~4,000 palabras (lectura ágil)

---

### 5️⃣ **PREGUNTAS_ORAL.md**
**Banco de 54 preguntas potenciales del examen + respuestas esperadas**
- Dataset y EDA (4 preguntas)
- Outliers (5 preguntas)
- Intervalos de confianza (5 preguntas)
- Pruebas de hipótesis (15 preguntas)
- Análisis bivariado (5 preguntas)
- Decisiones metodológicas (3 preguntas)
- Conclusiones (5 preguntas)
- Técnicas (3 preguntas)
- Interpretación clínica (5 preguntas)
- Integradoras (6 preguntas)

**👉 Cuándo usar:** Para practicar antes de la oral
**👉 Cómo usar:** Lee pregunta, intenta responder, compara con esperado

---

### 6️⃣ **REFERENCIAS_CRUZADAS.md**
**Localizador rápido: dónde encontrar cada concepto en el informe**
- Busca por concepto → ubicación en notebook
- Busca por variable clínica → dónde analizada
- Busca por función → ubicación y definición
- Tabla de celdas críticas
- Explicación de cambios clave

**👉 Cuándo usar:** Necesitas localizar algo específico en el informe

---

## 🚀 CÓMO COMENZAR

### Opción A: Preparación Completa (Recomendado)
```
Semana 1:
├─ Día 1: INDICE_MAESTRO.md (orientación)
├─ Día 2: INDICE_VISUAL.md (estructura)
├─ Día 3-4: CONCEPTOS.md (definiciones)
└─ Día 5-6: RESUMEN_EJECUTIVO.md (síntesis)

Semana 2:
├─ Día 7-10: PREGUNTAS_ORAL.md (práctica)
├─ Día 11-13: Preguntas integradoras
└─ Día 14: Revisión de frases clave
```

### Opción B: Preparación Rápida (1-2 días)
```
Día 1:
├─ Mañana: INDICE_VISUAL.md (30 min)
└─ Tarde: RESUMEN_EJECUTIVO.md (60 min)

Día 2:
├─ Mañana: PREGUNTAS_ORAL.md - 10 preguntas (60 min)
└─ Tarde: Revisar frases clave (30 min)
```

### Opción C: Consulta Rápida (Durante la oral)
```
Si te hacen pregunta:
├─ Paso 1: Localiza en INDICE_VISUAL.md (5 seg)
├─ Paso 2: Recuerda frase de RESUMEN_EJECUTIVO.md (5 seg)
└─ Paso 3: Estructura respuesta con PREGUNTAS_ORAL.md (10 seg)
```

---

## ⚡ LOS 3 PILARES METODOLÓGICOS

Estos son los conceptos más importantes. Memoriza bien:

### 1️⃣ VERIFICACIÓN DE SUPUESTOS
**"Antes de cada prueba estadística, verificamos supuestos"**
- Normalidad (Shapiro-Wilk) → Si falla, usar Mann-Whitney U
- Homocedasticidad (Levene) → Si falla, usar Welch t-test
- Resultado: Mayoría de variables no normales → Usamos métodos no paramétricos

### 2️⃣ MÉTODOS COMPLEMENTARIOS
**"No depender de un único enfoque, usar múltiples métodos"**
- Outliers: Votación de 4 métodos (IQR + 3 IF) → Consenso
- IC: Paramétricos + percentílicos → Robustez
- Correlaciones: Pearson + Spearman → Validación cruzada

### 3️⃣ TRANSPARENCIA TOTAL
**"Justificar cada decisión, reportar supuestos, reconocer limitaciones"**
- Documentar por qué se eligió cada método
- Reportar resultado de verificación de supuestos
- Reconocer limitaciones del estudio

---

## 🎯 DECISIONES CLAVE QUE DEBES MEMORIZAR

### Decisión 1: Eliminación de Outliers
**¿Por qué sistema de votación con umbral ≥ 3?**
- Equilibra limpieza de datos vs preservación de variabilidad
- Conservador: 98%+ de datos se mantienen
- Rubusta: 4 métodos independientes evitan sesgo

### Decisión 2: Intervalos de Confianza
**¿Por qué muestra completa en lugar de submuestras?**
- Submuestreo repetido introduce sesgos metodológicos
- Muestra completa produce estimaciones más robustas
- Lección: Cambio metodológico por pensamiento crítico

### Decisión 3: Selección de Pruebas
**¿Por qué árbol de decisión basado en supuestos?**
- Rigidez estadística: verificar supuestos primero
- Mayoría variables fallaron normalidad → Mann-Whitney U
- Transparencia: reportar supuestos junto con resultado

---

## 📊 LOS 3 HALLAZGOS PRINCIPALES

Estos son los resultados que debes poder explicar:

### Hallazgo 1: Diferencias en Variables Metabólicas
- **IMC, FPG, HOMA-IR** muestran diferencias significativas
- **Interpretación:** Grupo GDM+ tiene peor perfil metabólico
- **Clínica:** Consistente con literatura sobre factores de riesgo

### Hallazgo 2: Factores de Riesgo Obstétricos
- **GDM previa** es el factor de riesgo más fuerte
- **PCOS** también significativamente asociado
- **Clínica:** Comparten mecanismo de resistencia a insulina

### Hallazgo 3: No Normalidad Generalizada
- **Mayoría de variables** no cumplen normalidad
- **Consecuencia:** Requiere métodos robustos no paramétricos
- **Metodología:** Nuestro árbol de decisión lo contempló

---

## ✅ CHECKLIST ANTES DE ENTRAR AL EXAMEN

Verifica que ENTIENDES (no solo memorices):

- [ ] ¿Por qué se usa IQR + Isolation Forest juntos?
- [ ] ¿Por qué Mann-Whitney U es la prueba más utilizada?
- [ ] ¿Por qué IC paramétricos + percentílicos?
- [ ] ¿Qué significa normalidad y por qué falla aquí?
- [ ] ¿Cómo el cambio de metodología en IC evita sesgos?
- [ ] ¿Cuál es el factor de riesgo más fuerte?
- [ ] ¿Qué NO se realizó (análisis multivariado) y por qué?
- [ ] ¿Qué limitaciones tiene el dataset sintético?
- [ ] ¿Cómo se conectan hallazgos estadísticos con clínica?
- [ ] ¿Qué significa "significancia estadística" vs magnitud de efecto?

**Si respondiste SÍ a 8+ → Estás muy listo**

---

## 📱 REFERENCIAS RÁPIDAS (Para Usar en la Oral)

### Cuando te pregunten: "¿Qué es un outlier?"
→ Lee CONCEPTOS.md Sección 3

### Cuando te pregunten: "¿Por qué Mann-Whitney?"
→ Lee INDICE_VISUAL.md "Árbol de Decisión"

### Cuando te pregunten: "¿Diferencias entre grupos?"
→ Lee RESUMEN_EJECUTIVO.md "Resultados en una línea"

### Cuando te pregunten: "¿Cuáles son las limitaciones?"
→ Lee CONCEPTOS.md Sección 14

### Cuando no sepas responder
→ Usa estructura de PREGUNTAS_ORAL.md: Define → Justifica → Implementa → Resultado → Valida

---

## 🎓 ESTRUCTURA DE RESPUESTA (SIEMPRE IGUAL)

Cuando respondas cualquier pregunta, sigue este patrón:

```
1. DEFINE el concepto
   "Un intervalo de confianza es..."

2. JUSTIFICA por qué se utilizó
   "Se utilizó porque..."

3. DESCRIBE cómo se implementó en tu caso
   "En nuestro análisis..."

4. REPORTA el resultado
   "Esto significó que..."

5. VALIDA la solidez
   "La validez se asegura mediante..."
```

**Ejemplo completo:**

P: ¿Por qué Mann-Whitney U?

R: "**[1 DEFINE]** Mann-Whitney U es una prueba no paramétrica que compara dos grupos basada en rangos. **[2 JUSTIFICA]** Se utilizó porque la mayoría de variables no cumplían el supuesto de normalidad según Shapiro-Wilk. **[3 IMPLEMENTA]** En nuestro análisis, cuando detectábamos falta de normalidad, seleccionábamos Mann-Whitney en lugar de t-test. **[4 RESULTADO]** Esto permitió análisis robusto sin asumir distribuciones. **[5 VALIDA]** La validez se asegura por que Mann-Whitney no paramétrico, es decir, no requiere normalidad."

---

## 🚨 ERRORES COMUNES A EVITAR

❌ **NO dices:** "El IC 95% significa que 95% de los datos está en este rango"
✅ **DICES:** "Hay 95% de confianza que el parámetro poblacional está en este rango"

❌ **NO dices:** "Las variables causan GDM"
✅ **DICES:** "Las variables están asociadas con GDM (correlación ≠ causalidad)"

❌ **NO dices:** "No hay diferencia si p ≥ 0.05"
✅ **DICES:** "Insuficiente evidencia de diferencia"

❌ **NO ignoras:** Los supuestos al seleccionar prueba
✅ **SIEMPRE:** Reportas resultado de verificación de supuestos

❌ **NO olvidas:** Justificar decisiones metodológicas
✅ **SIEMPRE:** Das razón del por qué de cada elección

---

## 🏆 FRASES CLAVE PARA USAR

Memoriza estas 5 frases y úsalas frecuentemente:

1. **"Se verificaron los supuestos antes de..."**
2. **"El sistema de votación proporcionó robustez al..."**
3. **"Para evitar sesgos de submuestreo, utilizamos..."**
4. **"Esto es consistente con la literatura científica que muestra..."**
5. **"La implicación clínica es que..."**

---

## 📞 SOPORTE RÁPIDO DURANTE LA ORAL

| Situación | Acción |
|-----------|--------|
| No entiendes la pregunta | Pide que repita de forma diferente |
| No sabes responder | Toma 5 segundos, consulta RESUMEN_EJECUTIVO.md mentalmente |
| Comenzaste mal | Pausar, responder, luego corregir |
| Se te olvida | Menciona documento, di "está en CONCEPTOS.md" |
| Duda sobre datos | Cita si puedes, si no di "Está en sección 2.3" |

---

## 🎯 OBJETIVOS DE APRENDIZAJE

Después de usar esta guía, DEBES poder:

✅ Explicar por qué cada método fue elegido
✅ Entender árbol de decisión para pruebas
✅ Conectar hallazgos estadísticos con interpretación clínica
✅ Justificar cambios de metodología
✅ Reconocer y articular limitaciones
✅ Usar ejemplos específicos del informe
✅ Responder preguntas integradoras conectando conceptos
✅ Defender las decisiones metodológicas
✅ Explicar diferencias entre métodos paramétricos/no paramétricos
✅ Interpretar p-valores, IC y correlaciones correctamente

---

## ⏱️ TIEMPO ESTIMADO DE PREPARACIÓN

| Documentos | Lectura Profunda | Práctica | Total |
|-----------|-----------------|----------|-------|
| Solo RESUMEN_EJECUTIVO.md | 1 hora | - | 1 hora |
| Todos menos PREGUNTAS | 4 horas | - | 4 horas |
| Todos completo | 6 horas | 3 horas | 9 horas |

**Recomendado:** 6-7 horas distribuidas en 1-2 semanas

---

## 📞 ¿PREGUNTAS FRECUENTES?

**P: ¿Por dónde empiezo?**
R: Comienza con INDICE_MAESTRO.md (5 min), luego INDICE_VISUAL.md

**P: ¿Necesito memorizar valores específicos?**
R: NO. Memoriza conceptos y frases clave. Valores están en REFERENCIAS_CRUZADAS.md

**P: ¿Qué es lo más importante?**
R: Los 3 pilares metodológicos y las 3 decisiones clave (arriba en este documento)

**P: ¿Qué hago si me hacen pregunta no cubierta?**
R: Usa estructura de respuesta (Define-Justifica-Implementa-Resultado-Valida)

**P: ¿Puedo usar estos documentos durante el examen?**
R: Probablemente NO, pero puedes memorizar las frases clave de RESUMEN_EJECUTIVO.md

---

## 📚 ORDEN DE LECTURA RECOMENDADO

**Lectura 1 (Orientación):** Este README + INDICE_MAESTRO.md
**Lectura 2 (Estructura):** INDICE_VISUAL.md
**Lectura 3 (Conceptos):** CONCEPTOS.md (secciones principales)
**Lectura 4 (Síntesis):** RESUMEN_EJECUTIVO.md
**Lectura 5 (Práctica):** PREGUNTAS_ORAL.md
**Consulta):** REFERENCIAS_CRUZADAS.md según necesidad

---

## 🌟 ÚLTIMO CONSEJO

> "No se trata de memorizar valores o estadísticas. Se trata de demostrar que ENTIENDES por qué cada decisión metodológica se tomó, cómo se implementó, y qué permite inferir sobre la comprensión del fenómeno de GDM."

**El examinador quiere escuchar:**
- Pensamiento crítico (¿por qué ese método y no otro?)
- Rigor estadístico (verificación de supuestos)
- Robustez (métodos complementarios)
- Humildad (reconocer limitaciones)
- Conexión clínica (implicaciones médicas)

**Si logras esto, aprobado seguro.** ✅

---

## ✨ ¡ÉXITO EN LA ORAL!

Tienen las herramientas necesarias. Solo confíen en la preparación y recuerden los pilares.

**Frases finales:**
- "Se verificaron los supuestos antes de..."
- "Para evitar sesgos de..."
- "El sistema de votación proporcionó robustez..."
- "Esto es consistente con la literatura..."
- "La implicación clínica es..."

🎓📊💪

---

**Creado:** 14 de Noviembre de 2025  
**Para:** Equipo Alma de Litio  
**Con:** ❤️ y rigor estadístico
