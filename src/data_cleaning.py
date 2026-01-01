import pandas as pd
import numpy as np


def load_raw_data():
    data = {
        "animal": ["guinea_pig", "guinea_pig", None, "guinea_pig"],
        "weight_grams": [850, -20, 900, None],
        "age_days": [90, 95, None, 2000],  # 2000 días es inválido
    }
    return pd.DataFrame(data)


def clean_data(df):
    # eliminar filas sin animal
    df = df.dropna(subset=["animal"])

    # corregir pesos inválidos
    df = df[df["weight_grams"] > 0]

    # eliminar edades fuera de rango lógico (0–365 días)
    df = df[(df["age_days"] >= 0) & (df["age_days"] <= 365)]

    # convertir a kg
    df["weight_kg"] = df["weight_grams"] / 1000

    return df


def main():
    df_raw = load_raw_data()
    print("Raw data:")
    print(df_raw)

    df_clean = clean_data(df_raw)
    print("\nClean data:")
    print(df_clean)
    save_clean_data(df_clean)


def save_clean_data(df):
    df.to_csv("data/guinea_pigs_clean.csv", index=False)

if __name__ == "__main__":
    main()
