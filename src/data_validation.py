import pandas as pd


REQUIRED_COLUMNS = {
    "animal": str,
    "weight_grams": float,
    "age_days": float,
    "weight_kg": float,
    "weight_category": str,
    "age_months": float,
}


def validate_schema(df):
    for col, dtype in REQUIRED_COLUMNS.items():
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")
    print("Schema validation passed.")


def main():
    df = pd.read_csv("data/guinea_pigs_features.csv")
    validate_schema(df)


if __name__ == "__main__":
    main()
