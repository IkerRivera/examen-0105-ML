# Reporte de Análisis de Granjas - Pandas

`Eliseo Nava Machine Learning pandas, NC 0105`

## 1. DataFrame Convertido
```text
         Granja  Hectareas  Animales
0   El Porvenir         50       500
1  La Esperanza         80       800
2      San José         35       300
3     Los Pinos        120      1200
4    El Rosario         65       600
5   Santa María         45       400
```

## 2.1 Primeras Filas (head)
```text
         Granja  Hectareas  Animales
0   El Porvenir         50       500
1  La Esperanza         80       800
```

## 2.2 Últimas Filas (tail)
```text
        Granja  Hectareas  Animales
4   El Rosario         65       600
5  Santa María         45       400
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Granja         str
Hectareas    int64
Animales     int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Granja     6 non-null      str  
 1   Hectareas  6 non-null      int64
 2   Animales   6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas de Hectáreas
```text
count      6.000000
mean      65.833333
std       30.889588
min       35.000000
25%       46.250000
50%       57.500000
75%       76.250000
max      120.000000
Name: Hectareas, dtype: float64
```

## 4. Orden Ascendente por Hectáreas
```text
         Granja  Hectareas  Animales
2      San José         35       300
5   Santa María         45       400
0   El Porvenir         50       500
4    El Rosario         65       600
1  La Esperanza         80       800
3     Los Pinos        120      1200
```

## 5. Orden Descendente por Animales
```text
         Granja  Hectareas  Animales
3     Los Pinos        120      1200
1  La Esperanza         80       800
4    El Rosario         65       600
0   El Porvenir         50       500
5   Santa María         45       400
2      San José         35       300
```

## 6. Estadísticas de Animales
```text
count       6.000000
mean      633.333333
std       326.598632
min       300.000000
25%       425.000000
50%       550.000000
75%       750.000000
max      1200.000000
Name: Animales, dtype: float64
```


`Eliseo Nava Machine Learning pandas, NC 0105`