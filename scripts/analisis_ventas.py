
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/MOCK_DATA.csv")

# Convertir fecha
df["sales_date"] = pd.to_datetime(df["sales_date"], format="%d.%m.%Y")

# Crear columna de mes
df["month"] = df["sales_date"].dt.month

# Ventas totales
ventas_totales = df["sales_amount"].sum()

print("Ventas totales:")
print(ventas_totales)

# Mayor venta registrada
mayor_venta = df["sales_amount"].max()

print("\nMayor venta registrada:")
print(mayor_venta)

# Ventas por mes
ventas_por_mes = df.groupby("month")["sales_amount"].sum()

print("\nVentas por mes:")
print(ventas_por_mes)

# Crear gráfico
ventas_por_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

# Guardar gráfico
plt.savefig("resultados/ventas_por_mes.png")

print("\nGráfico guardado en /resultados")
