
import pandas as pd

# Load original dataset
df = pd.read_csv("scholartrack_applications_raw.csv")

print("Original dataset shape:", df.shape)

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing state with Unknown
df["state"] = df["state"].fillna("Unknown")

# Fill missing family income with median income
df["annual_family_income_inr"] = (
    df["annual_family_income_inr"].fillna(
        df["annual_family_income_inr"].median()
    )
)

# Keep missing review dates as blank
# because some applications may not have been reviewed yet

# Save cleaned dataset
df.to_csv("scholartrack_applications_cleaned.csv", index=False)

print("Cleaned dataset shape:", df.shape)
print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nApplication status summary:")
print(df["application_status"].value_counts())

print("\nCleaned dataset saved successfully!")
