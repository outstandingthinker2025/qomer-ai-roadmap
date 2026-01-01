import pandas as pd


def load_clean_data():
    return pd.read_csv("data/guinea_pigs_clean.csv")


def add_features(df):
    # Clasificación por peso
    df["weight_category"] = pd.cut(
        df["weight_kg"],
        bins=[0, 0.7, 0.9, 1.5],
        labels=["light", "medium", "heavy"],
    )

    # Edad en meses
    df["age_months"] = df["age_days"] / 30

    return df


def main():
    df = load_clean_data()
    df = add_features(df)
    print(df)
    save_features(df)

def save_features(df):
    df.to_csv("data/guinea_pigs_features.csv", index=False)


if __name__ == "__main__":
    main()
