import pandas as pd
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
def cargar_y_limpiar_datos(ruta_archivo):
    # 1. Leemos el archivo usando el parámetro que ingresó el usuario
    df = pd.read_csv(ruta_archivo, skiprows=9)
    # 2. Mapeamos los nombres de las columnas de inglés a español
    columnas_nuevas = {
        'Date': 'fecha',
        'Page Type': 'plataforma',
        'Sentiment': 'sentimiento',
        'Snippet': 'texto_mencion'
    }

    # 3. Aplicamos el cambio al DataFrame
    df = df.rename(columns=columnas_nuevas)

    # 4. Devolvemos el DataFrame listo y traducido
    return df
def obtener_top_plataformas(df):
        # 1. Contamos cuántas veces se repite cada plataforma
        plataformas = df['plataforma'].value_counts().reset_index()

        # 2. Renombramos las columnas del nuevo mini-DataFrame
        plataformas.columns = ['plataforma', 'cantidad']

        # 3. Devolvemos el resultado procesado
        return plataformas
# 1. Creamos el analizador
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # 2. Definimos qué argumento debe buscar (Primero se añade)
    parser.add_argument('ruta_data', help='Ruta del archivo CSV de menciones')
    # 3. Procesamos la terminal para guardar los datos (Luego se lee)
    args = parser.parse_args()
    # 4. Usamos la variable dinámica sin comillas
    nuevo_df = cargar_y_limpiar_datos(args.ruta_data)
    menciones_por_dia = nuevo_df.groupby('fecha').size().reset_index(name='cantidad')
    sns.barplot(x='fecha', y='cantidad', data=menciones_por_dia)
    plt.title('Comportamiento por día')
    plt.xlabel('Fecha')
    plt.ylabel('Menciones')
    plt.savefig('menciones_por_dia.png') # Guardamos el primero
    plt.close() # Limpiamos el lienzo para el segundo gráfico
    #Creamos el DataFrame para las barras

    plataformas = obtener_top_plataformas(nuevo_df)
    sns.barplot(x='plataforma', y='cantidad', data=plataformas)
    plt.title('Top Plataformas')
    plt.xlabel('Red social')
    plt.ylabel('Menciones')
    plt.savefig('menciones_por_plataforma.png') # Guardamos el segundo
    plt.close() # Limpiamos el lienzo para el tercer gráfico
    sentimiento = nuevo_df['sentimiento'].value_counts().reset_index()
    sentimiento.columns = ['sentimiento', 'cantidad']
    plt.title('Sentimiento Total')
    plt.pie(sentimiento['cantidad'], labels=sentimiento['sentimiento'])
    plt.savefig('menciones_por_sentimiento.png')
    plt.close()
    evolucion = nuevo_df.groupby(['fecha', 'sentimiento']).size().reset_index(name='cantidad')
    sns.lineplot(x='fecha', y='cantidad', data=evolucion, hue='sentimiento')
    plt.title('Sentimiento por día')
    plt.xlabel('Fecha')
    plt.ylabel('Sentimiento')
    plt.savefig('Sentimiento_por_dia.png')
    from wordcloud import STOPWORDS, WordCloud
    nuevo_df.columns
    texto_completo = " ".join(nuevo_df['texto_mencion'].astype(str))
    nube = WordCloud().generate(texto_completo)
    plt.imshow(nube)
    plt.axis('off')
    plt.savefig('nube_de_palabras.png')
    plt.close()