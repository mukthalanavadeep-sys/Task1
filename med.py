import pandas as pd

df = pd.read_csv("medical.csv", encoding="latin1")


print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

df["gender"] = df["gender"].str.strip().str.upper()
df["neighbourhood"] = df["neighbourhood"].str.strip().str.upper()
df["no_show"] = df["no_show"].str.strip().str.title()

df["scheduledday"] = pd.to_datetime(df["scheduledday"])
df["appointmentday"] = pd.to_datetime(df["appointmentday"])

df["age"] = df["age"].astype(int)

print("\nData Types:")
print(df.dtypes)
df.to_csv("cleaned_dataset.csv", index=False)
print("\nDataset cleaned successfully!")
