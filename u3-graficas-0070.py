# Axel Guzman NC 0070
# UIII Act 2 Graficas VA
# Ejemplo 6: Peliculas Taquilleras

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# datos de peliculas
avt = ['Avatar', 2.9, False, 2009]
end = ['Avengers: Endgame', 2.7, False, 2019]
ttn = ['Titanic', 2.2, True, 1997]
sw7 = ['Star Wars VII', 2.0, False, 2015]
inf = ['Avengers: Infinity War', 2.0, False, 2018]

# crear dataframe
peliculas = pd.DataFrame(
    [avt, end, ttn, sw7, inf],
    columns=['Pelicula', 'Recaudacion', 'Oscar', 'Año']
)

print(peliculas)

# obtener datos para las graficas
nombres = peliculas['Pelicula']
recaudacion = peliculas['Recaudacion']
años = peliculas['Año']

# grafica 1: barras
plt.figure(figsize=(10, 5))
plt.bar(nombres, recaudacion, color='skyblue')
plt.title('Recaudacion de peliculas taquilleras')
plt.xlabel('Peliculas')
plt.ylabel('Billones de USD')
plt.xticks(rotation=45)
plt.show()

# grafica 2: pastel
oscar = peliculas['Oscar'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(oscar, labels=['No gano Oscar', 'Gano Oscar'],
        autopct='%1.1f%%')
plt.title('Peliculas ganadoras del Oscar')
plt.show()

# grafica 3: lineas
plt.figure(figsize=(8, 5))
plt.plot(años, recaudacion, marker='o', color='green')
plt.title('Año y recaudacion de peliculas')
plt.xlabel('Año')
plt.ylabel('Billones de USD')
plt.grid()
plt.show()

# grafica 4: dispersion
plt.figure(figsize=(8, 5))
plt.scatter(años, recaudacion, color='red')
plt.title('Comparacion de año y recaudacion')
plt.xlabel('Año')
plt.ylabel('Billones de USD')
plt.grid()
plt.show()

print("Axel Guzman NC 0070")