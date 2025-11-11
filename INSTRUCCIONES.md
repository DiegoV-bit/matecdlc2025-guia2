# Guía práctica: Análisis Exploratorio de Datos

**Universidad de Magallanes**  
**Facultad de Ingeniería, Departamento de Ingeniería en Computación**  
**Asignatura:** Matemática para Ciencias de la Computación  
**Profesor:** David Medina Ortiz  
**Fecha:** 1 de noviembre de 2025  

---

## Comentarios y observaciones

Esta guía se enfoca en el **análisis exploratorio estadístico de datos clínicos**. Reforzará el manejo de:

- Estadística descriptiva.  
- Visualización.  
- Test de hipótesis.  
- Intervalos de confianza.  
- Comparaciones entre grupos.  
- Evaluación de supuestos estadísticos.

**Plazos y entrega:**

1. **Fecha límite:** viernes 15/11 a las 13:00 hrs (SCL).  
2. **Entrega:** los *Jupyter Notebooks* desarrollados y un **reporte tipo resumen** del trabajo planteado.  
3. Si usa GPT u otra herramienta de IA, **debe indicarlo** dentro de las herramientas empleadas.  
4. Toda entrega se envía en un archivo comprimido `.tar.gz` o `.zip` al correo: **david.medina@umag.cl**  
5. Preguntas hasta el jueves **13/11 a las 12:00 hrs SCL**.

---

## 1. Descripción general

Se trabajará con un **dataset sintético** con información clínica del **primer trimestre del embarazo**.  
El objetivo es **caracterizar estadísticamente los datos** y **explorar asociaciones** entre variables clínicas y el **riesgo de desarrollar diabetes gestacional (GDM)**.

**Características del dataset:**

- N ≈ 1500 registros  
- Variables clínicas: edad, IMC pregestacional, presión arterial, etc.  
- Marcadores bioquímicos: FPG, HbA1c, insulina, lípidos, HOMA-IR.  
- Factores de riesgo: antecedentes familiares, GDM previa, PCOS, tabaquismo.  
- Estilo de vida: actividad física, dieta.  
- Etiqueta: `label_gdm`  
- Datos faltantes (MCAR y MAR).  
- Presencia de outliers.  
- Desbalance de clases (~17% positivos).

---

## 2. Actividades a desarrollar

### 2.1 Análisis exploratorio

1. Resumen de dimensiones, tipos de datos y valores faltantes.  
2. Estadística descriptiva (media, mediana, desviación estándar, IQR, percentiles).  
3. Identificación y análisis de *outliers*.  
4. Visualización básica:
   - Histogramas  
   - Boxplots  
   - Density plots  
   - Gráficos de barras (para variables categóricas)

---

### 2.2 Intervalos de confianza

1. Calcular intervalos de confianza para variables numéricas relevantes (por ejemplo: IMC, FPG, HbA1c).  
2. Interpretar los intervalos desde un punto de vista clínico.

---

### 2.3 Test de hipótesis

Formular y ejecutar pruebas adecuadas según el tipo de variable y la pregunta planteada.  
Ejemplos:

- Comparación de presión arterial entre grupos **GDM vs no GDM** (t-test, Mann–Whitney).  
- Evaluar diferencias en dieta por nivel de actividad física (ANOVA / Kruskal–Wallis).  
- Comparación de proporciones (antecedentes familiares vs GDM).

**Debe incluir:**

- Formulación de hipótesis (H₀ y H₁).  
- Verificación de supuestos.  
- Elección de la prueba adecuada.  
- Interpretación de los resultados.

---

### 2.4 Evaluación de normalidad

1. Evaluar la normalidad en variables de interés (Shapiro–Wilk, Kolmogorov–Smirnov).  
2. Comentar el impacto sobre las pruebas aplicadas.

---

### 2.5 Análisis bivariado

1. Matrices de correlación para variables numéricas.  
2. Gráficos bivariados (dispersión + regresión, boxplots comparativos).  
3. Discusión de asociaciones relevantes.

---

## 3. Entregables

Debe entregar un informe con formato libre que incluya:

- Descripción general del dataset.  
- Análisis exploratorio de datos (EDA).  
- Intervalos de confianza.  
- Test de hipótesis.  
- Bondad de ajuste.  
- Análisis bivariado.  
- Interpretación clínica.  
- Conclusiones.  

Además:

- Código empleado (en celdas o script).

---

**Archivo:** `INSTRUCCIONES.md`  
**Curso:** Matemática para Ciencias de la Computación  
**Universidad de Magallanes**
