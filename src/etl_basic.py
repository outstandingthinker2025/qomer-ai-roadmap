import pandas as pd


def extract():
    data = {
        "animal": ["guinea_pig", "guinea_pig", "guinea_pig"],
        "weight_grams": [850, 900, 780],
        "age_days": [90, 95, 85],
    }
    return pd.DataFrame(data)


def transform(df):
    df["weight_kg"] = df["weight_grams"] / 1000
    return df


def load(df):
    df.to_csv("data/guinea_pigs.csv", index=False)


def main():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL pipeline executed successfully.")


if __name__ == "__main__":
    main()
