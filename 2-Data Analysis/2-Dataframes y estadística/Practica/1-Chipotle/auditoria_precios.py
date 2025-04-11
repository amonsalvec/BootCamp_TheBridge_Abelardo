def auditoria_precios(df):
    print("🔍 AUDITORÍA DE PRECIOS POR PRODUCTO\n")

    # 1. Precios distintos por producto
    precios_por_producto = df.groupby('nombre_producto')['precio_producto'].unique()
    print("1️⃣ Precios distintos por producto:\n")
    for producto, precios in precios_por_producto.items():
        print(f"   - {producto}: {list(precios)}")
    
    print("\n" + "-"*50)

    # 2. Productos con múltiples precios
    conteo_precios = df.groupby('nombre_producto')['precio_producto'].nunique()
    productos_con_precios_variados = conteo_precios[conteo_precios > 1]

    print("2️⃣ Productos con múltiples precios:\n")
    if not productos_con_precios_variados.empty:
        for producto, n in productos_con_precios_variados.items():
            print(f"   ⚠️ {producto} aparece con {n} precios distintos.")
    else:
        print("   ✅ No se detectaron productos con múltiples precios.")
    
    print("\n" + "-"*50)

    # 3. Detalle por producto, precio y pedido
    variaciones_precio = (
        df[['id_pedido', 'nombre_producto', 'precio_producto']]
        .drop_duplicates()
        .sort_values(['nombre_producto', 'precio_producto'])
    )

    print("3️⃣ Variaciones de precio por producto y pedido:\n")
    print(variaciones_precio.to_string(index=False))

    print("\n" + "-"*50)

    # 4. Precio más frecuente por producto
    precio_mas_frecuente = df.groupby('nombre_producto')['precio_producto']\
                             .agg(lambda x: x.value_counts().idxmax())

    print("4️⃣ Precio más frecuente por producto:\n")
    for producto, precio in precio_mas_frecuente.items():
        print(f"   - {producto}: {precio}")

    print("\n✅ Auditoría completada.")

return {
    'precios_por_producto': precios_por_producto,
    'productos_con_precios_variados': productos_con_precios_variados,
    'variaciones_precio': variaciones_precio,
    'precio_mas_frecuente': precio_mas_frecuente
}

def auditoria_precios(df):
    """
    Auditoría de coherencia de precios por producto en un DataFrame de pedidos.
    Requiere columnas: 'id_pedido', 'nombre_producto', 'precio_producto'.
    
    Devuelve un diccionario con:
        - precios_por_producto: Series con precios únicos por producto
        - productos_con_precios_variados: Series con productos que tienen más de un precio
        - variaciones_precio: DataFrame con combinación (producto, precio, pedido)
        - precio_mas_frecuente: Series con el precio más común por producto
    """

    print("🔍 AUDITORÍA DE PRECIOS POR PRODUCTO\n")

    # 1. Precios distintos por producto
    precios_por_producto = df.groupby('nombre_producto')['precio_producto'].unique()
    print("1️⃣ Precios distintos por producto:\n")
    for producto, precios in precios_por_producto.items():
        print(f"   - {producto}: {list(precios)}")

    print("\n" + "-"*50)

    # 2. Productos con múltiples precios
    conteo_precios = df.groupby('nombre_producto')['precio_producto'].nunique()
    productos_con_precios_variados = conteo_precios[conteo_precios > 1]

    print("2️⃣ Productos con múltiples precios:\n")
    if not productos_con_precios_variados.empty:
        for producto, n in productos_con_precios_variados.items():
            print(f"   ⚠️ {producto} aparece con {n} precios distintos.")
    else:
        print("   ✅ No se detectaron productos con múltiples precios.")

    print("\n" + "-"*50)

    # 3. Detalle por producto, precio y pedido
    variaciones_precio = (
        df[['id_pedido', 'nombre_producto', 'precio_producto']]
        .drop_duplicates()
        .sort_values(['nombre_producto', 'precio_producto'])
        .reset_index(drop=True)
    )

    print("3️⃣ Variaciones de precio por producto y pedido:\n")
    print(variaciones_precio.to_string(index=False))

    print("\n" + "-"*50)

    # 4. Precio más frecuente por producto
    precio_mas_frecuente = df.groupby('nombre_producto')['precio_producto']\
                             .agg(lambda x: x.value_counts().idxmax())

    print("4️⃣ Precio más frecuente por producto:\n")
    for producto, precio in precio_mas_frecuente.items():
        print(f"   - {producto}: {precio}")

    print("\n✅ Auditoría completada.\n")

    # 🔁 Devolver resultados como objetos
    return {
        'precios_por_producto': precios_por_producto,
        'productos_con_precios_variados': productos_con_precios_variados,
        'variaciones_precio': variaciones_precio,
        'precio_mas_frecuente': precio_mas_frecuente
    }


resultados = auditoria_precios(df)

# Ejemplo: acceder a los productos con múltiples precios
print("\nProductos con inconsistencias de precio:\n")
print(resultados['productos_con_precios_variados'])
