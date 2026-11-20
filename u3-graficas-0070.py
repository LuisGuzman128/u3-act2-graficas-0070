
# Axel Guzman NC 0070
# UIII Act 2 Graficas VA
# Ejemplo 6: Peliculas Taquilleras

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. DATAFRAME O MARCO DE DATOS PANDAS
# ==========================================

# datos de redes sociales

fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['LinkedIn', 7277, False, 2012]

# crear lista de redes sociales
lista_redes_sociales = [fb, twt, ig, wsp, tel, lkn]

# crear dataframe
df_redes_sociales = pd.DataFrame(
    lista_redes_sociales,
    columns=['nombre', 'cantidad', 'Es_fb', 'año']
)

# mostrar tabla de redes sociales
print("\nTABLA DE REDES SOCIALES")
print(df_redes_sociales)

# guardar archivo CSV
df_redes_sociales.to_csv("redessociales.csv", index=False)


# ==========================================
# 2. GRAFICA DE LINEAS DE REDES SOCIALES
# ==========================================

plt.figure(figsize=(10, 5))
plt.plot(df_redes_sociales["nombre"],
         df_redes_sociales["cantidad"],
         marker='o')

plt.title("Grafica de redes sociales Axel Guzman 0070")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.xticks(rotation=45)
plt.grid()
plt.show()


# ==========================================
# 3. GRAFICA DE PUNTOS DE REDES SOCIALES
# ==========================================

plt.figure(figsize=(8, 5))
plt.scatter(df_redes_sociales["nombre"],
            df_redes_sociales["cantidad"],
            color='red')

plt.title("Puntos de redes sociales Axel Guzman 0070")
plt.xlabel("Redes sociales")
plt.ylabel("Cantidad de usuarios")
plt.xticks(rotation=45)
plt.grid()
plt.show()


# ==========================================
# 4. GRAFICA DE BARRAS DE REDES SOCIALES
# ==========================================

plt.figure(figsize=(10, 5))
plt.bar(df_redes_sociales["nombre"],
        df_redes_sociales["cantidad"])

plt.title("Barras de redes sociales Axel Guzman 0070")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuarios")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 5. GRAFICA DE BARRAS DE MAYOR A MENOR
# ==========================================

df_rs_ordenar = df_redes_sociales.sort_values(
    "cantidad", ascending=False
)

plt.figure(figsize=(10, 5))
plt.bar(df_rs_ordenar["nombre"],
        df_rs_ordenar["cantidad"])

plt.title("Redes sociales de mayor a menor Axel Guzman 0070")
plt.xlabel("Redes sociales")
plt.ylabel("Cantidad de usuarios")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 6. COLOREANDO LA GRAFICA
# ==========================================

plt.figure(figsize=(10, 5))
plt.bar(df_rs_ordenar["nombre"],
        df_rs_ordenar["cantidad"],
        color=["b", "g", "c", "m", "y", "r"])

plt.title("Redes sociales con colores Axel Guzman 0070")
plt.xlabel("Redes sociales")
plt.ylabel("Cantidad de usuarios")
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 7. GRAFICA DE PASTEL O PIE
# ==========================================

plt.figure(figsize=(7, 7))
plt.pie(
    df_redes_sociales["cantidad"],
    labels=df_redes_sociales["nombre"],
    autopct='%1.1f%%'
)

plt.title("Pastel de redes sociales Axel Guzman 0070")
plt.show()


# ==========================================
# 8. EJEMPLO 6: PELICULAS TAQUILLERAS
# ==========================================

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

print("\nTABLA DE PELICULAS TAQUILLERAS")
print(peliculas)

# obtener datos para las graficas

nombres = peliculas['Pelicula']
recaudacion = peliculas['Recaudacion']
años = peliculas['Año']


# ==========================================
# 9. GRAFICA 1: BARRAS
# ==========================================

plt.figure(figsize=(10, 5))
plt.bar(nombres, recaudacion, color='skyblue')

plt.title('Recaudacion de peliculas taquilleras Axel Guzman 0070')
plt.xlabel('Peliculas')
plt.ylabel('Billones de USD')
plt.xticks(rotation=45)
plt.show()


# ==========================================
# 10. GRAFICA 2: PASTEL
# ==========================================

oscar = peliculas['Oscar'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    oscar,
    labels=['No gano Oscar', 'Gano Oscar'],
    autopct='%1.1f%%'
)

plt.title('Peliculas ganadoras del Oscar Axel Guzman 0070')
plt.show()


# ==========================================
# 11. GRAFICA 3: LINEAS
# ==========================================

plt.figure(figsize=(8, 5))
plt.plot(años, recaudacion, marker='o', color='green')

plt.title('Año y recaudacion de peliculas Axel Guzman 0070')
plt.xlabel('Año')
plt.ylabel('Billones de USD')
plt.grid()
plt.show()


# ==========================================
# 12. GRAFICA 4: DISPERSION
# ==========================================

plt.figure(figsize=(8, 5))
plt.scatter(años, recaudacion, color='red')

plt.title('Comparacion de año y recaudacion Axel Guzman 0070')
plt.xlabel('Año')
plt.ylabel('Billones de USD')
plt.grid()
plt.show()


# ==========================================
# FINAL
# ==========================================

print("Axel Guzman NC 0070")
