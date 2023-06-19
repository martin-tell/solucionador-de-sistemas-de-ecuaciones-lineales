from numpy import copy, argmax, abs, zeros, dot, round, max, empty, array

def redondea_matriz(matriz):
    return round(matriz, 5)

def eliminacion_gaussiana(n, a):
    proceso = []
    matriz = copy(a)
    for i in range(n):
        matriz = redondea_matriz(matriz)
        proceso.append(array(matriz))
        columna = matriz[i:, i]
        p = argmax(abs(columna))
        if columna[p] == 0:
            return empty((0, 0)), proceso
        if p != 0:
            matriz[[i, p], :] = matriz[[p, i], :]
        for j in range(i + 1, n):
            m = matriz[j, i] / matriz[i, i]
            matriz[j, :] -= m * matriz[i, :]
    x = zeros(n)
    x[n - 1] = matriz[n - 1, n] / matriz[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        s = dot(matriz[i, i + 1:n], x[i + 1:n])
        x[i] = (matriz[i, n] - s) / matriz[i, i]
    x = round(x, 5)
    return x, proceso


def pivoteo_maximo_columnas(n, a):
    proceso = []
    matriz = copy(a)
    for i in range(n):
        matriz = redondea_matriz(matriz)
        proceso.append(array(matriz))
        columna = matriz[i:, i]
        p = argmax(abs(columna))
        if columna[p] == 0:
            return empty((0, 0)), proceso
        if p != 0:
            matriz[[i, p], :] = matriz[[p, i], :]
        for j in range(i + 1, n):
            m = matriz[j, i] / matriz[i, i]
            matriz[j, :] -= m * matriz[i, :]
    x = zeros(n)
    x[n - 1] = matriz[n - 1, n] / matriz[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        s = dot(matriz[i, i + 1:n], x[i + 1:n])
        x[i] = (matriz[i, n] - s) / matriz[i, i]
    x = round(x, 5)
    return x, proceso

def pivoteo_escalado_columna(n, a):
    proceso = []
    matriz = copy(a)
    for i in range(n):
        matriz = redondea_matriz(matriz)
        proceso.append(array(matriz))
        submatriz = matriz[i:, :]
        max_abs_filas = max(abs(submatriz), axis=1)
        p = argmax(abs(submatriz[:, i] / max_abs_filas))
        if submatriz[p, i] == 0:
            return empty((0, 0)), proceso
        if p != 0:
            matriz[[i, i + p], :] = matriz[[i + p, i], :]
        for j in range(i + 1, n):
            m = matriz[j, i] / matriz[i, i]
            matriz[j, :] -= m * matriz[i, :]
    x = zeros(n)
    x[n - 1] = matriz[n - 1, n] / matriz[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        s = dot(matriz[i, i + 1:n], x[i + 1:n])
        x[i] = (matriz[i, n] - s) / matriz[i, i]
    x = round(x, 5)
    return x, proceso

def matriz_a_cadena(matriz):
        return '│' + '     │\n│'.join(['  '.join(['{:12}'.format(columna) for columna in fila]) for fila in matriz]) + '     │\n\n'