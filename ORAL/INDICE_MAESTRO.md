# 📚 GUÍA DE ESTUDIO COMPLETA - ÍNDICE MAESTRO

**Generada:** 14 de Noviembre de 2025

Esta guía compiles todos los documentos de referencia para preparación del examen oral sobre el Informe de Análisis Exploratorio de GDM.

---

## 📄 DOCUMENTOS CREADOS

### 1. **CONCEPTOS.md** - Glosario Completo
- **Propósito:** Diccionario detallado de todos los métodos, técnicas y conceptos
- **Extensión:** ~7,500 palabras
- **Organización:** 14 secciones temáticas
- **Cuándo usar:** Cuando necesitas definición formal o explicación conceptual

**Contenido:**
- Conceptos fundamentales del dataset
- Estadística descriptiva
- Detección de outliers (4 métodos)
- Intervalos de confianza (tipos y métodos)
- Pruebas de hipótesis (árbol de decisión)
- Análisis bivariado (correlaciones)
- Decisiones sobre sesgos
- Variables clínicas explicadas
- Técnicas de visualización
- Librerías y funciones utilizadas

**Secciones clave:**
- 6.5: Árbol de decisión para seleccionar pruebas
- 7.1-7.7: Análisis bivariado en profundidad
- 8: Decisiones sobre sesgos

---

### 2. **PREGUNTAS_ORAL.md** - Banco de Preguntas y Respuestas
- **Propósito:** Preguntas potenciales del examen oral + respuestas esperadas
- **Cantidad:** 54 preguntas específicas
- **Organización:** 9 categorías temáticas
- **Cuándo usar:** Para practicar antes de la oral

**Preguntas por sección:**
- Dataset y EDA (4 preguntas)
- Métodos de outliers (5 preguntas)
- Intervalos de confianza (5 preguntas)
- Pruebas de hipótesis (15 preguntas)
- Análisis bivariado (5 preguntas)
- Decisiones metodológicas (3 preguntas)
- Conclusiones y limitaciones (5 preguntas)
- Técnicas y herramientas (3 preguntas)
- Interpretación clínica (5 preguntas)
- Preguntas integradoras (6 preguntas)

**Características especiales:**
- Errores comunes a evitar
- Expresiones clave para usar
- Estructura sugerida para respuestas

---

### 3. **RESUMEN_EJECUTIVO.md** - Referencia Rápida de Decisiones
- **Propósito:** Frases y respuestas rápidas para usar en la oral
- **Extensión:** ~4,000 palabras
- **Organización:** 12 secciones de referencia rápida
- **Cuándo usar:** Cuando necesitas recordar rápidamente el "por qué" de cada decisión

**Contenido:**
- Decisiones clave por sección (tablas)
- Frases clave para recordar y usar
- Árbol de decisiones (diagrama)
- Métricas reportadas
- Limitaciones reconocidas
- Resultados en una línea por variable
- Cronología de decisiones
- Puntos fuertes del análisis
- Respuestas a críticas potenciales
- Los 3 pilares metodológicos

**Tablas especiales:**
- Métodos de outliers con justificación
- Cambios metodológicos
- Decisiones elegidas vs rechazadas
- Resultados significativos por variable

---

### 4. **INDICE_VISUAL.md** - Mapas Mentales y Flujos
- **Propósito:** Visualización de la estructura completa del análisis
- **Formato:** Diagramas ASCII, árboles de decisión, flujos
- **Cuándo usar:** Para ver la "big picture" y entender flujo general

**Contenido:**
- Estructura jerárquica completa (árbol visual)
- Matriz de métodos estadísticos aplicados
- Decisiones y justificaciones (árbol visual)
- Flujo de toma de decisiones completo
- Mapa de variables (dónde encontrar cada análisis)
- Resultados resumidos
- Librerías y funciones (localización rápida)
- Checklist de verificación
- Navegación por documentos

**Diagramas:**
- Flujo completo: ANÁLISIS INICIADO → Conclusiones
- Árbol de decisión para seleccionar pruebas
- Búsqueda rápida de variables

---

### 5. **REFERENCIAS_CRUZADAS.md** - Navegación del Informe
- **Propósito:** Localizar cualquier concepto en el notebook
- **Extensión:** ~3,500 palabras
- **Cuándo usar:** Para encontrar dónde exactamente está cada cosa en el informe

**Búsquedas por:**
1. **Concepto** → Ubicación en informe (A-W)
2. **Variable Clínica** → Dónde aparece
3. **Función/Método** → Ubicación y definición
4. **Tema** → Secciones relevantes
5. **Tabla de celdas críticas** → Localización exacta
6. **Cambios clave** → Qué evolucionó y por qué

**Ejemplo de uso:**
- "¿Dónde está la prueba Mann-Whitney?" → Sección 2.3.1, celda a0967d3c
- "¿Dónde se explica Isolation Forest?" → Sección 2.1.5.2, celdas 65bbb1ff-96ead88e
- "¿Dónde está la interpretación clínica?" → Sección 3.1.2, markdown

---

## 📊 CÓMO USAR ESTA GUÍA

### Antes de la Oral (Preparación General)

**Semana 1:** Comprensión General
```
Día 1-2: Leer INDICE_VISUAL.md (comprende estructura)
Día 3-4: Leer CONCEPTOS.md (aprende definiciones)
Día 5-7: Leer RESUMEN_EJECUTIVO.md (memoriza frases clave)
```

**Semana 2:** Práctica de Preguntas
```
Día 8-10: Responder preguntas de PREGUNTAS_ORAL.md (grupo 1-3)
Día 11-13: Responder preguntas (grupo 4-6)
Día 14: Responder preguntas (grupo 7-9) + integradoras
```

**Día del Examen:** Referencias Rápidas
```
Mañana: Revisar RESUMEN_EJECUTIVO.md + frases clave
Antes: Tener INDICE_VISUAL.md disponible mentalmente
Durante: Aplicar estructura de respuestas de PREGUNTAS_ORAL.md
```

---

### Búsqueda Estratégica

**Si te preguntan sobre...**

🔍 **"¿Cómo detectaste outliers?"**
- Ir a: RESUMEN_EJECUTIVO.md → Sección "Decisiones Clave"
- Ir a: CONCEPTOS.md → Sección 3 (Detección de Outliers)
- Ir a: REFERENCIAS_CRUZADAS.md → Buscar "Detección de Outliers"

🔍 **"¿Por qué Mann-Whitney en lugar de t-test?"**
- Ir a: INDICE_VISUAL.md → "Árbol de Decisión"
- Ir a: CONCEPTOS.md → Sección 6.5 (Árbol de Decisión)
- Ir a: PREGUNTAS_ORAL.md → Preguntas 18-19

🔍 **"¿Qué es un intervalo de confianza?"**
- Ir a: CONCEPTOS.md → Sección 5
- Ir a: PREGUNTAS_ORAL.md → Preguntas 9-13

🔍 **"¿Dónde está el análisis bivariado?"**
- Ir a: REFERENCIAS_CRUZADAS.md → "Análisis Bivariado"
- Ir a: INDICE_VISUAL.md → "Mapa de Variables"

🔍 **"¿Cuáles fueron las limitaciones?"**
- Ir a: CONCEPTOS.md → Sección 14
- Ir a: RESUMEN_EJECUTIVO.md → "Limitaciones Reconocidas"
- Ir a: PREGUNTAS_ORAL.md → Preguntas 36-40

---

## 🎯 ESTRATEGIA DE RESPUESTA

Cuando te hagan una pregunta en la oral:

1. **Localiza** el tema en INDICE_VISUAL.md (5 segundos)
2. **Recuerda** la frase clave de RESUMEN_EJECUTIVO.md (5 segundos)
3. **Estructura** tu respuesta según PREGUNTAS_ORAL.md (10 segundos)
4. **Responde** con confianza (30-60 segundos)

**Estructura de Respuesta (siempre igual):**
```
1. DEFINE: "Esto es..."
2. JUSTIFICA: "Se utilizó porque..."
3. IMPLEMENTA: "En nuestro caso..."
4. RESULTADO: "Esto significó que..."
5. VALIDA: "La validez se asegura mediante..."
```

---

## ✅ CHECKLIST PRE-ORAL

Completa antes de entrar al examen:

- [ ] ¿Entiendo el árbol de decisión para pruebas? (INDICE_VISUAL.md)
- [ ] ¿Sé las 3 decisiones más importantes? (RESUMEN_EJECUTIVO.md)
- [ ] ¿Puedo mencionar 2-3 frases clave? (RESUMEN_EJECUTIVO.md)
- [ ] ¿Entiendo por qué mayoría de pruebas fueron no paramétricas? (CONCEPTOS.md)
- [ ] ¿Sé diferenciar entre IC paramétrico y percentílico? (CONCEPTOS.md)
- [ ] ¿Reconozco las limitaciones del estudio? (RESUMEN_EJECUTIVO.md)
- [ ] ¿Puedo explicar colinealidad y dónde aparece? (CONCEPTOS.md)
- [ ] ¿Sé qué significa p < 0.05 correctamente? (PREGUNTAS_ORAL.md)
- [ ] ¿Reconozco el cambio de metodología en IC? (RESUMEN_EJECUTIVO.md)
- [ ] ¿Puedo conectar hallazgos estadísticos con clínica? (PREGUNTAS_ORAL.md grupo 8)

Si respondiste NO a alguno: Vuelve a leer esa sección.

---

## 🚀 VENTAJAS DE USAR ESTA GUÍA

✅ **Organización:** Múltiples puntos de entrada según necesidad
✅ **Flexibilidad:** Puedes saltarte a la sección que necesites
✅ **Comprensión:** No solo respuestas, sino razonamiento detrás
✅ **Práctica:** 54 preguntas para entrenar
✅ **Referencia Rápida:** Frases clave y tablas para memorizar
✅ **Estructurado:** Flujo lógico desde conceptos a síntesis
✅ **Validez:** Todo basado en informe actual

---

## 📋 RESUMEN DE DECISIONES CLAVE (PARA MEMORIZAR)

**Los 3 Pilares:**
1. ✅ Verificar supuestos ANTES de pruebas
2. ✅ Usar métodos complementarios (paramétrico + no paramétrico)
3. ✅ Justificar cada decisión (transparencia)

**Las 3 Decisiones Más Importantes:**
1. Sistema de votación (4 métodos, umbral ≥ 3) → Preserva datos, elimina extremos
2. Muestra completa para IC → Evita sesgos de submuestreo
3. Árbol de decisión para pruebas → Rigor en selección según supuestos

**Los 3 Hallazgos Principales:**
1. Variables metabólicas diferencial: IMC, FPG, HOMA-IR
2. GDM previa es el factor de riesgo más fuerte
3. Mayoría de variables no normales → Requiere métodos robustos

---

## 🎓 ÚLTIMA RECOMENDACIÓN

**Lee estos documentos en este orden para máxima comprensión:**

```
SEMANA DE PREPARACIÓN:
│
├─ Día 1: INDICE_VISUAL.md (estructura general)
├─ Día 2-3: CONCEPTOS.md (definiciones)
├─ Día 4: RESUMEN_EJECUTIVO.md (síntesis)
├─ Día 5: REFERENCIAS_CRUZADAS.md (navegación)
├─ Día 6-7: PREGUNTAS_ORAL.md (práctica)
│
DÍA DEL EXAMEN:
├─ Mañana: Revisar RESUMEN_EJECUTIVO.md (frases clave)
└─ Antes: Respirar profundo y confiar en tu preparación
```

**Recuerda:** No es memorizar valores, es demostrar comprensión del "por qué" de cada decisión metodológica.

---

## 📞 SOPORTE RÁPIDO

**Si necesitas recuerda rápidamente...**

| Necesito... | Ir a... |
|-------------|---------|
| Definición de concepto | CONCEPTOS.md |
| Pregunta potencial + respuesta | PREGUNTAS_ORAL.md |
| Frase clave para decir | RESUMEN_EJECUTIVO.md |
| Ver estructura visual | INDICE_VISUAL.md |
| Ubicación exacta en informe | REFERENCIAS_CRUZADAS.md |
| Tabla resumen de decisiones | RESUMEN_EJECUTIVO.md |
| Árbol de decisión | INDICE_VISUAL.md o CONCEPTOS.md |
| Errores a evitar | PREGUNTAS_ORAL.md (al final) |

---

**Creado:** 14 de Noviembre de 2025
**Para:** Equipo Alma de Litio (Pablo, Emmanuel, Diego)
**Objetivo:** Examen Oral - Matemática para Ciencias de la Computación
**Universidad:** Universidad de Magallanes

---

## 🏆 ¡ÉXITO EN LA ORAL!

Tienen todo lo necesario para demostrar comprensión profunda del análisis. El rigor metodológico está presente en cada decisión. Solo recuerdan explicar el POR QUÉ.

**Frases finales para recordar:**
- "Se verificaron los supuestos antes de..."
- "Para evitar sesgos de..."
- "El sistema de votación proporcionó robustez al..."
- "Esto es consistente con la literatura científica..."
- "La implicación clínica es que..."

🎓📊✨
