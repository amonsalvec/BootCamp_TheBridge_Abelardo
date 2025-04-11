def auditoria_precios(df, imprimir=True):
    """
    Realiza una auditoría de precios por producto en un DataFrame con columnas:
    'id_pedido', 'nombre_producto', 'precio_producto'.

    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con información de pedidos.
    imprimir : bool
        Si True, imprime el reporte. Si False, solo retorna los objetos.

    Retorna:
    --------
    dict con:
        - precios_por_producto: pd.Series con precios únicos por producto
        - productos_con_precios_variados: pd.Series con productos con >1 precio
        - variaciones_precio: pd.DataFrame con detalle de precios por pedido
        - precio_mas_frecuente: pd.Series con precio modal por producto
    """
    import pandas as pd

    # 1. Precios distintos por producto
    precios_por_producto = df.groupby('nombre_producto')['precio_producto'].unique()

    # 2. Productos con múltiples precios
    conteo_precios = df.groupby('nombre_producto')['precio_producto'].nunique()
    productos_con_precios_variados = conteo_precios[conteo_precios > 1]

    # 3. Variaciones de precio por pedido
    variaciones_precio = (
        df[['id_pedido', 'nombre_producto', 'precio_producto']]
        .drop_duplicates()
        .sort_values(['nombre_producto', 'precio_producto'])
        .reset_index(drop=True)
    )

    # 4. Precio más frecuente (modal)
    precio_mas_frecuente = df.groupby('nombre_producto')['precio_producto']\
                             .agg(lambda x: x.value_counts().idxmax())

    if imprimir:
        print("🔍 AUDITORÍA DE PRECIOS POR PRODUCTO\n")

        print("1️⃣ Precios distintos por producto:\n")
        for producto, precios in precios_por_producto.items():
            print(f"   - {producto}: {list(precios)}")

        print("\n" + "-"*50)

        print("2️⃣ Productos con múltiples precios:\n")
        if not productos_con_precios_variados.empty:
            for producto, n in productos_con_precios_variados.items():
                print(f"   ⚠️ {producto} aparece con {n} precios distintos.")
        else:
            print("   ✅ No se detectaron productos con múltiples precios.")

        print("\n" + "-"*50)

        print("3️⃣ Variaciones de precio por producto y pedido:\n")
        print(variaciones_precio.to_string(index=False))

        print("\n" + "-"*50)

        print("4️⃣ Precio más frecuente por producto:\n")
        for producto, precio in precio_mas_frecuente.items():
            print(f"   - {producto}: {precio}")

        print("\n✅ Auditoría completada.")

    # Retornar resultados para su reutilización
    return {
        'precios_por_producto': precios_por_producto,
        'productos_con_precios_variados': productos_con_precios_variados,
        'variaciones_precio': variaciones_precio,
        'precio_mas_frecuente': precio_mas_frecuente
    }

resultados = auditoria_precios(df, imprimir=True)

# Acceder a resultados si los necesitas para análisis posterior:
precios_unicos = resultados['precios_por_producto']
productos_inconsistentes = resultados['productos_con_precios_variados']
detalle_precios = resultados['variaciones_precio']
precios_modales = resultados['precio_mas_frecuente']
