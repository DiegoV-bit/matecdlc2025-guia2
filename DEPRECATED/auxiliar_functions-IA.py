import pandas as pd
import numpy as np
from scipy import stats
from math import sqrt

def get_range_outlier(
        q1:float, 
        q3:float, 
        IQR:float, 
        factor_value:float=1.5):

    min_value = q1 - IQR*factor_value
    max_value = q3 + IQR*factor_value

    return min_value, max_value

def check_is_outlier(value, min_value, max_value):
    
    if value > max_value or value < min_value:
        return True
    else:
        return False

def generate_df_counts(df_values, columns_name, verbose:bool=False):
    data_rows = []

    for column in df_values.columns:
        counts = df_values[column].value_counts()

        row = [column, 0, 0] # generamos una fila

        if 1 in counts.index: # preguntamos si se identificaron nulos
            row[1] = counts[1] # lo asignamos al espacio del nulos en la fila
        if 0 in counts.index: # preguntamos si se identificaron no nulos
            row[2] = counts[0] # lo asignamos al espacio de no nulos
        
        if verbose:
            print(row)
        data_rows.append(row) # la fila la agregamos a la matriz

    # usamos la matriz para generar un data frame.
    df_counts = pd.DataFrame(data=data_rows, columns=columns_name)
    return df_counts

def categorize_iqr(value):
    if value >0:
        return 1
    else:
        return 0
        
def calculate_ic_known_std(muestral_mean, population_std, n, trust_level=0.95):
    z_crit = stats.norm.ppf((1+trust_level)/2)
    min = muestral_mean - z_crit * (population_std/sqrt(n))
    max = muestral_mean + z_crit * (population_std/sqrt(n))
    return (min, max)

def calculate_ic_unknown_std(muestral_mean, muestral_std, n, trust_level=0.95):
    freedom_degrees = n-1
    t_crit = stats.t.ppf((1+trust_level)/2, freedom_degrees)
    min = muestral_mean - t_crit * (muestral_std/sqrt(n))
    max = muestral_mean + t_crit * (muestral_std/sqrt(n))
    return (min, max)

def calculate_ic_mean(mean, std, n, trust_level=0.95, known_std=False):
    if known_std:
        crit = stats.norm.ppf((1 + trust_level) / 2)
    else:
        crit = stats.t.ppf((1 + trust_level) / 2, df=n - 1)

    margin_error = crit * (std / sqrt(n))
    min = mean - margin_error
    max = mean + margin_error
    return (min, max)

def calculate_ic_variance(muestral_std, n, trust_level=0.95):
    freedom_degrees = n - 1
    alpha = 1 - trust_level

    chi2_low = stats.chi2.ppf(alpha / 2, df=freedom_degrees)
    chi2_high = stats.chi2.ppf(1 - alpha / 2, df=freedom_degrees)

    s2 = muestral_std ** 2
    var_min = (freedom_degrees * s2) / chi2_high
    var_max = (freedom_degrees * s2) / chi2_low

    return (var_min, var_max)

def calculate_ic_std(muestral_std, n, trust_level=0.95):
    min, max = calculate_ic_variance(muestral_std, n, trust_level)
    std_min = sqrt(min)
    std_max = sqrt(max)
    return (std_min, std_max)

# ----------------------------------------------
# Nuevas funciones para diferencias y métodos no paramétricos
# Estas funciones extienden los IC tradicionales para cubrir
# diferencias de medias y proporciones, así como métodos
# percentílicos y bootstrap. Están pensadas para análisis
# bivariado y comparación entre grupos.

def calculate_ic_diff_means(mean1, var1, n1, mean0, var0, n0, trust_level=0.95, equal_var=True):
    """
    Calcula el intervalo de confianza para la diferencia de medias (mean1 - mean0).
    Si equal_var es True usa el método clásico con varianza combinada,
    de lo contrario aplica la aproximación de Welch.

    Parámetros:
        mean1, var1, n1: media, varianza y tamaño de muestra para grupo 1.
        mean0, var0, n0: media, varianza y tamaño de muestra para grupo 0.
        trust_level: nivel de confianza (default 0.95).
        equal_var: bool indicando si se asume igualdad de varianzas.

    Devuelve:
        (ic_min, ic_max) para la diferencia de medias.
    """
    # Aseguramos que las varianzas sean flotantes
    var1 = float(var1)
    var0 = float(var0)
    n1 = int(n1)
    n0 = int(n0)
    diff = mean1 - mean0
    alpha = 1 - trust_level
    if equal_var:
        # Varianza combinada
        pooled_var = ((n1 - 1) * var1 + (n0 - 1) * var0) / (n1 + n0 - 2)
        se = sqrt(pooled_var * (1.0 / n1 + 1.0 / n0))
        df = n1 + n0 - 2
    else:
        # Welch
        se = sqrt(var1 / n1 + var0 / n0)
        df_num = (var1 / n1 + var0 / n0) ** 2
        df_den = (var1 ** 2) / (n1 ** 2 * (n1 - 1)) + (var0 ** 2) / (n0 ** 2 * (n0 - 1))
        df = df_num / df_den if df_den != 0 else n1 + n0 - 2
    # Puntillo crítico
    tcrit = stats.t.ppf(1 - alpha / 2, df)
    margin = tcrit * se
    return (diff - margin, diff + margin)

def calculate_ic_diff_proportions(x1, n1, x0, n0, trust_level=0.95):
    """
    Calcula el intervalo de confianza para la diferencia de proporciones (p1 - p0)
    utilizando la aproximación de Newcombe basada en Wilson (sin corrección de continuidad).

    Parámetros:
        x1, n1: número de éxitos y tamaño de muestra para grupo 1
        x0, n0: número de éxitos y tamaño de muestra para grupo 0
        trust_level: nivel de confianza (default 0.95)
    Devuelve:
        (ic_min, ic_max) para la diferencia de proporciones
    """
    z = stats.norm.ppf((1 + trust_level) / 2)
    p1, p0 = x1 / n1, x0 / n0
    # Wilson interval para cada proporción
    def wilson(p, n):
        denom = 1 + z ** 2 / n
        center = (p + z ** 2 / (2 * n)) / denom
        half = z * sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / denom
        return center - half, center + half
    l1, u1 = wilson(p1, n1)
    l0, u0 = wilson(p0, n0)
    # Newcombe interval
    return (p1 - p0 - sqrt((p1 - l1) ** 2 + (u0 - p0) ** 2),
            p1 - p0 + sqrt((u1 - p1) ** 2 + (p0 - l0) ** 2))

def calculate_ic_percentile(data, trust_level=0.95):
    """
    Calcula un intervalo de confianza basada en percentiles (sin suposiciones paramétricas).

    Parámetros:
        data: array o lista de valores numéricos
        trust_level: nivel de confianza (default 0.95)

    Devuelve:
        (ic_min, ic_max) correspondiente a los percentiles inferior y superior.
    """
    data = np.asarray(data)
    lower = np.percentile(data, (1 - trust_level) / 2 * 100)
    upper = np.percentile(data, (1 + trust_level) / 2 * 100)
    return (lower, upper)

def calculate_ic_bootstrap_mean(data, trust_level=0.95, n_boot=1000):
    """
    Calcula el intervalo de confianza para la media utilizando bootstrap.

    Parámetros:
        data: array o lista de valores numéricos
        trust_level: nivel de confianza (default 0.95)
        n_boot: número de remuestreos

    Devuelve:
        (ic_min, ic_max) del bootstrap para la media.
    """
    data = np.asarray(data)
    n = len(data)
    if n == 0:
        return (np.nan, np.nan)
    boot_means = []
    for _ in range(n_boot):
        sample = np.random.choice(data, size=n, replace=True)
        boot_means.append(np.mean(sample))
    lower = np.percentile(boot_means, (1 - trust_level) / 2 * 100)
    upper = np.percentile(boot_means, (1 + trust_level) / 2 * 100)
    return (lower, upper)