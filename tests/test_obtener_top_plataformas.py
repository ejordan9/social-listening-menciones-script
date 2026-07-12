import pandas as pd
from script_menciones import obtener_top_plataformas 

def test_obtener_top_plataformas():
    # 1. Creamos los datos ficticios de prueba
    datos_juguete = {
        'plataforma': ['Twitter', 'Twitter', 'Twitter', 'Facebook', 'Facebook']
    }
    df_prueba = pd.DataFrame(datos_juguete)
    
    # 2. Ejecutamos tu función
    resultado = obtener_top_plataformas(df_prueba)
    
    # 3. Verificamos los resultados
    assert resultado.loc[resultado['plataforma'] == 'Twitter', 'cantidad'].values[0] == 3
    assert resultado.loc[resultado['plataforma'] == 'Facebook', 'cantidad'].values[0] == 2