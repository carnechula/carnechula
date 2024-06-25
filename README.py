- 👋 Hi, I’m @carnechula
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
carnechula/carnechula is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Función para guardar datos en Excel
def save_to_excel(data, filename, sheet_name):
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Función para registrar la entrada de carne
def registrar_entrada():
    data = {
        'Fecha Compra': [entry_fecha_compra.get()],
        'Kilos Media Res 1': [entry_kilos_1.get()],
        'Kilos Media Res 2': [entry_kilos_2.get()],
        'Kilos Media Res 3': [entry_kilos_3.get()],
        'Kilos Totales': [entry_kilos_totales.get()]
    }
    save_to_excel(data, 'control_de_ventas_carniceria.xlsx', 'Entradas de Carne')
    limpiar_campos_entrada()

# Función para registrar las ventas diarias
def registrar_venta():
    data = {
        'Fecha': [entry_fecha_venta.get()],
        'Producto': [entry_producto.get()],
        'Cantidad Vendida': [entry_cantidad_vendida.get()],
        'Precio Unitario': [entry_precio_unitario.get()],
        'Total Efectivo': [entry_efectivo.get()],
        'Cuenta DNI': [entry_cuenta_dni.get()],
        'Mercado Pago': [entry_mercado_pago.get()],
        'Tarjeta Crédito': [entry_tarjeta_credito.get()],
        'Tarjeta Débito': [entry_tarjeta_debito.get()],
        'Total Venta': [entry_total_venta.get()]
    }
    save_to_excel(data, 'control_de_ventas_carniceria.xlsx', 'Ventas Diarias')
    limpiar_campos_venta()

# Función para registrar los gastos
def registrar_gasto():
    data = {
        'Fecha': [entry_fecha_gasto.get()],
        'Descripción': [entry_descripcion.get()],
        'Pago a Proveedores': [entry_pago_proveedores.get()],
        'Deuda a Proveedores': [entry_deuda_proveedores.get()],
        'Artículos de Limpieza': [entry_limpieza.get()],
        'Insumos de Carnicería': [entry_insumos.get()],
        'Gastos Varios': [entry_gastos_varios.get()],
        'Total Gastos': [entry_total_gastos.get()]
    }
    save_to_excel(data, 'control_de_ventas_carniceria.xlsx', 'Gastos')
    limpiar_campos_gasto()

# Función para registrar los cortes de carne
def registrar_cortes():
    data = {}
    for corte in cortes:
        data[f'Peso {corte}'] = [entry_pesos[corte].get()]
        data[f'Precio {corte}'] = [entry_precios[corte].get()]
        data[f'Total {corte}'] = [float(entry_pesos[corte].get()) * float(entry_precios[corte].get()) * (1 + float(entry_porcentaje.get()) / 100)]
    save_to_excel(data, 'control_de_ventas_carniceria.xlsx', 'Cortes de Carne')
    limpiar_campos_cortes()

# Función para ajustar precios
def ajustar_precios():
    porcentaje = float(entry_porcentaje.get())
    for corte in cortes:
        precio_original = float(entry_precios[corte].get())
        entry_precios[corte].delete(0, tk.END)
        entry_precios[corte].insert(0, round(precio_original * (1 + porcentaje / 100), 2))

# Funciones para limpiar campos
def limpiar_campos_entrada():
    entry_fecha_compra.delete(0, tk.END)
    entry_kilos_1.delete(0, tk.END)
    entry_kilos_2.delete(0, tk.END)
    entry_kilos_3.delete(0, tk.END)
    entry_kilos_totales.delete(0, tk.END)

def limpiar_campos_venta():
    entry_fecha_venta.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_cantidad_vendida.delete(0, tk.END)
    entry_precio_unitario.delete(0, tk.END)
    entry_efectivo.delete(0, tk.END)
    entry_cuenta_dni.delete(0, tk.END)
    entry_mercado_pago.delete(0, tk.END)
    entry_tarjeta_credito.delete(0, tk.END)
    entry_tarjeta_debito.delete(0, tk.END)
    entry_total_venta.delete(0, tk.END)

def limpiar_campos_gasto():
    entry_fecha_gasto.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)
    entry_pago_proveedores.delete(0, tk.END)
    entry_deuda_proveedores.delete(0, tk.END)
    entry_limpieza.delete(0, tk.END)
    entry_insumos.delete(0, tk.END)
    entry_gastos_varios.delete(0, tk.END)
    entry_total_gastos.delete(0, tk.END)

def limpiar_campos_cortes():
    for corte in cortes:
        entry_pesos[corte].delete(0, tk.END)
        entry_precios[corte].delete(0, tk.END)
    entry_porcentaje.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Frigorífico los Centuriones")

# Crear pestañas
tab_control = ttk.Notebook(root)
tab_entrada = ttk.Frame(tab_control)
tab_venta = ttk.Frame(tab_control)
tab_gasto = ttk.Frame(tab_control)
tab_cortes = ttk.Frame(tab_control)
tab_control.add(tab_entrada, text='Entradas de Carne')
tab_control.add(tab_venta, text='Ventas Diarias')
tab_control.add(tab_gasto, text='Gastos')
tab_control.add(tab_cortes, text='Cortes de Carne')
tab_control.pack(expand=1, fill='both')

# Entradas de Carne
ttk.Label(tab_entrada, text="Fecha Compra:").grid(column=0, row=0, padx=10, pady=10)
entry_fecha_compra = ttk.Entry(tab_entrada)
entry_fecha_compra.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(tab_entrada, text="Kilos Media Res 1:").grid(column=0, row=1, padx=10, pady=10)
entry_kilos_1 = ttk.Entry(tab_entrada)
entry_kilos_1.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(tab_entrada, text="Kilos Media Res 2:").grid(column=0, row=2, padx=10, pady=10)
entry_kilos_2 = ttk.Entry(tab_entrada)
entry_kilos_2.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(tab_entrada, text="Kilos Media Res 3:").grid(column=0, row=3, padx=10, pady=10)
entry_kilos_3 = ttk.Entry(tab_entrada)
entry_kilos_3.grid(column=1, row=3, padx=10, pady=10)

ttk.Label(tab_entrada, text="Kilos Totales:").grid(column=0, row=4, padx=10, pady=10)
entry_kilos_totales = ttk.Entry(tab_entrada)
entry_kilos_totales.grid(column=1, row=4, padx=10, pady=10)

ttk.Button(tab_entrada, text="Registrar", command=registrar_entrada).grid(column=1, row=5, padx=10, pady=10)

# Ventas Diarias
ttk.Label(tab_venta, text="Fecha:").grid(column=0, row=0, padx=10, pady=10)
entry_fecha_venta = ttk.Entry(tab_venta)
entry_fecha_venta.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(tab_venta, text="Producto:").grid(column=
