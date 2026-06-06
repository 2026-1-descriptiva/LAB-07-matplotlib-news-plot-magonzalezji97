"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """
    # 1. Configurar y validar rutas de entrada y salida
    input_path = "files/input/news.csv"
    if not os.path.exists(input_path):
        # Fallback si está en la raíz de la carpeta de datos
        input_path = "news.csv"
        if not os.path.exists(input_path):
            input_path = os.path.join(os.path.dirname(__file__), "../files/input/news.csv")

    output_dir = "files/plots"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "news.png")

    # 2. Leer los datos
    df = pd.read_csv(input_path)
    
    # Renombrar la primera columna que contiene los años
    df = df.rename(columns={df.columns[0]: "Year"})

    # 3. Crear la visualización
    plt.figure(figsize=(10, 6))
    
    # Graficar cada medio de comunicación
    plt.plot(df["Year"], df["Television"], label="Television", marker="o", linewidth=2)
    plt.plot(df["Year"], df["Newspaper"], label="Newspaper", marker="s", linewidth=2)
    plt.plot(df["Year"], df["Internet"], label="Internet", marker="^", linewidth=2)
    plt.plot(df["Year"], df["Radio"], label="Radio", marker="d", linewidth=2)

    # Personalizar el gráfico
    plt.title("Evolución del Consumo de Medios de Comunicación (2001 - 2010)", fontsize=14, fontweight="bold")
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Porcentaje / Consumo", fontsize=12)
    plt.xticks(df["Year"])  # Asegurar que se muestren todos los años enteros
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="best", fontsize=11)
    plt.tight_layout()

    # 4. Guardar el archivo gráfico
    plt.savefig(output_path, dpi=300)
    plt.close()


if __name__ == "__main__":
    pregunta_01()
