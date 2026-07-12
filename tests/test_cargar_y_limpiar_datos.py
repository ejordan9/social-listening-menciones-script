from script_menciones import cargar_y_limpiar_datos

def test_cargar_y_limpiar_datos(tmp_path):
    # 1. Creamos un archivo CSV temporal de juguete
    archivo_temporal = tmp_path / "datos_prueba.csv"

    # 2. Le escribimos 9 líneas de relleno y los encabezados en inglés
    contenido = (
        "\n" * 9 +  # Las 9 líneas vacías que se salta el skiprows=9
        "Date,Page Type,Sentiment,Snippet\n"  # Encabezados originales
        "2026-01-01,Twitter,Positive,Hola mundo\n"  # Una fila de datos de ejemplo
    )
    archivo_temporal.write_text(contenido)

    # 3. Ejecutamos tu función pasando la ruta del archivo temporal
    df_resultado = cargar_y_limpiar_datos(str(archivo_temporal))

    # 4. Verificamos que las columnas ahora existan en español
    columnas_esperadas = ['fecha', 'plataforma', 'sentimiento', 'texto_mencion']

    # Comprobamos si las columnas del resultado son exactamente las que esperamos
    assert list(df_resultado.columns) == columnas_esperadas